package org.example.rpa;


import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONObject;
import org.example.rpa.entity.Customer;
import org.example.rpa.entity.Invoice;
import org.example.rpa.entity.NonInvoice;
import org.example.rpa.entity.Supplier;
import org.example.rpa.repo.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.mock.web.MockMultipartFile;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

@SpringBootApplication
public class RpaApplication implements CommandLineRunner {
    @Value("${file.path}")
    private String filePath = "/data.json";
    private final List<JSONObject> data = new ArrayList<>();
    private final List<Customer> customers=new ArrayList<>();
    private final List<Supplier> suppliers=new ArrayList<>();
    private final List<Invoice> invoices=new ArrayList<>();
    private final List<NonInvoice> nonInvoices=new ArrayList<>();
    private final int[] nonInvoiceTypes = {20,22,26,27,35,31,83,39,37,33,38};
    private final UploadRepo uploadRepo;
    private final CustomerRepo customerRepo;
    private final SupplierRepo supplierRepo;
    private final InvoiceRepo invoiceRepo;
    private final NonInvoiceRepo nonInvoiceRepo;

    public RpaApplication(UploadRepo uploadRepo, CustomerRepo customerRepo, SupplierRepo supplierRepo, InvoiceRepo invoiceRepo, NonInvoiceRepo nonInvoiceRepo) {
        this.uploadRepo = uploadRepo;
        this.customerRepo = customerRepo;
        this.supplierRepo = supplierRepo;
        this.invoiceRepo = invoiceRepo;
        this.nonInvoiceRepo = nonInvoiceRepo;
    }

    public static void main(String[] args) {
        SpringApplication.run(RpaApplication.class, args);


    }
    @Override
    public void run(String... args) throws Exception {
        data.addAll(readData());
        parseData();
    }

    private List<JSONObject> readData() {
        System.out.println("Reading data from file: " + filePath);
        try (InputStream inputStream = getClass().getResourceAsStream(filePath)){
            if (inputStream == null) {
                System.out.println("File not found");
            }
            String json = new String(inputStream.readAllBytes(), StandardCharsets.UTF_8);
            return JSON.parseArray(json, JSONObject.class);
        } catch (Exception e) {
            System.out.println("Error reading file");
        }
        return null;
    }
    // 将file转换为multipartFile并上传 返回url
    private String uploadFile(String filePath) throws IOException {
        filePath="src/main/resources/"+filePath; // 修正路径
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IOException("File not found: " + filePath);
        }
        FileInputStream fileInputStream = new FileInputStream(file);
        MultipartFile multipartFile = new MockMultipartFile(file.getName(), file.getName(), "image/jpeg", fileInputStream);
        return uploadRepo.uploadFile(multipartFile, "image");
    }
    private void parseData() throws IOException{
        for (JSONObject json : data) {
            int code = json.getJSONObject("header").getIntValue("code");
            if (code != 0){ // 有错误码
                Invoice invoice = new Invoice();
                invoice.setStatus(3); // 人工审批
                invoice.setRemark("无法识别发票 错误码：{" + code + "}");
                invoice.setImageUri(uploadFile(json.getString("file_name")));
                invoiceRepo.save(invoice);
                continue;
            }
            // 获取base64编码的结果
            String base64 = json.getJSONObject("payload").getJSONObject("output_text_result").getString("text");
            JSONObject result = JSON.parseArray(new String(java.util.Base64.getDecoder().decode(base64))).getJSONObject(0);
            System.out.println(result.toJSONString());
            int type = result.getIntValue("invoiceType");
            if (Arrays.stream(nonInvoiceTypes).anyMatch(i -> i == type)) { // 非发票
                NonInvoice nonInvoice = new NonInvoice();
                nonInvoice.setImageUri(uploadFile(json.getString("file_name")));
                nonInvoiceRepo.save(nonInvoice);
            } else { // 发票
                if (result.containsKey("invoice")){
                    result=result.getJSONObject("invoice"); // 有invoice字段
                }
                Invoice invoice = new Invoice();
                String number = result.getString("invoiceNumber");//发票号码
                if (number != null && invoiceRepo.getInvoiceByNumber(number) != null) { // 重复发票 不再处理
                    continue;
                }
                String dateStr = result.getString("billingDate");
                if (dateStr != null) {
                    LocalDate date = LocalDate.parse(result.getString("billingDate"));//开票日期
                    invoice.setDate(date);
                }
                String supplierName = result.getString("salesName");//供应商名称
                String customerName = result.getString("purchaserName");//客户名称
                Integer amount = result.getInteger("amountTax");//金额
                invoice.setNumber(number);
                invoice.setAmount(amount);
                if (supplierName != null) {
                    Supplier supplier = supplierRepo.getSupplierByName(supplierName);
                    if (supplier == null) {
                        supplier = new Supplier();
                        supplier.setName(supplierName);
                        supplier.setAmount(0);
                        supplier.setCount(0);
                    }
                    supplier.setAmount(supplier.getAmount() + amount);
                    supplier.setCount(supplier.getCount() + 1);
                    supplierRepo.save(supplier);
                    invoice.setSupplier(supplier);
                }
                if (customerName != null) {
                    Customer customer = customerRepo.getCustomerByName(customerName);
                    if (customer == null) {
                        customer = new Customer();
                        customer.setName(customerName);
                        customer.setAmount(0);
                        customer.setCount(0);
                    }
                    customer.setAmount(customer.getAmount() + amount);
                    customer.setCount(customer.getCount() + 1);
                    customerRepo.save(customer);
                    invoice.setCustomer(customer);
                }
                //进行审批
                int dataSet = json.getIntValue("data_set");
                approve(dataSet,invoice);
                invoice.setImageUri(uploadFile(json.getString("file_name")));
                invoiceRepo.save(invoice);
            }
        }
    }
    // 审批 type是数据集类型
    private void approve(int dataSet,Invoice invoice){
        if (dataSet == 1) {
            Customer customer = invoice.getCustomer();
            if (customer == null) {
                invoice.setStatus(2);
                invoice.setRemark("无法识别付款方");
                return;
            }
            String customerName = customer.getName();
            if (!Objects.equals(customerName, "浙江大学")) {
                int same=customerName.contains("浙")?1:0;
                same+=customerName.contains("江")?1:0;
                same+=customerName.contains("大")?1:0;
                same+=customerName.contains("学")?1:0;
                if (same<3) { // 名字至少包含3个字
                    invoice.setStatus(2);
                    invoice.setRemark("付款方不是浙江大学");
                }
                else {
                    invoice.setStatus(3);
                    invoice.setRemark("付款方疑似识别不清 人工审批");
                }
                return;
            }
            LocalDate date = invoice.getDate();
            if (date == null) {
                invoice.setStatus(2);
                invoice.setRemark("无法识别开票日期");
                return;
            }
            if (date.getYear()!=2015){
                invoice.setStatus(2);
                invoice.setRemark("开票日期不是2015年");
                return;
            }
            Integer amount = invoice.getAmount();
            if (amount == null) {
                invoice.setStatus(2);
                invoice.setRemark("无法识别金额");
                return;
            }
            if (invoice.getAmount() > 1600) {
                invoice.setStatus(2);
                invoice.setRemark("金额超过1600元");
                return;
            }
            invoice.setStatus(1);
        }
    }
}
