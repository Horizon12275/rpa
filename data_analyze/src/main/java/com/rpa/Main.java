package com.rpa;

import org.apache.commons.compress.utils.IOUtils;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.InputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Image Example");

        // 使用类加载器获取资源文件
        String imagePath = "/.jpg/b0.jpg"; // 假设图片在 src/main/resources/.jpg/ 目录下
        try (InputStream fis = Main.class.getResourceAsStream(imagePath)) {
            if (fis == null) {
                System.err.println("Image not found!");
                return;
            }
            // 将图片转换为字节数组
            byte[] imageBytes = IOUtils.toByteArray(fis);
            // 添加图片到工作簿
            int pictureIndex = workbook.addPicture(imageBytes, Workbook.PICTURE_TYPE_PNG);
            // 创建一个绘图对象
            CreationHelper helper = workbook.getCreationHelper();
            Drawing<?> drawing = sheet.createDrawingPatriarch();
            // 创建一个锚点，定义图片的位置
            ClientAnchor anchor = helper.createClientAnchor();
            anchor.setCol1(0); // 设置列索引
            anchor.setRow1(0); // 设置行索引
            anchor.setCol2(10); // 设置列索引（高度）
            anchor.setRow2(50); // 设置行索引（宽度）

            // 插入图片
            drawing.createPicture(anchor, pictureIndex);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 写入到文件
        try (FileOutputStream fileOut = new FileOutputStream("image_example.xlsx")) {
            workbook.write(fileOut);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                workbook.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
