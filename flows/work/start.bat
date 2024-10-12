call conda activate tagui

python ./.py/ocr.py

java -jar ./.jar/access.jar

java -jar ./.jar/gen_json.jar

python ./.py/jpg_txt_gen.py.py

python ./.py/jpg_xlsx_gen.py

python ./.py/report_jpg_gen.py

python ./.py/report_txt_gen.py

python ./.py/report_xlsx_gen.py

7z a .\.7z\待人工审批发票.7z .\.jpg\待人工审批发票\

call tagui ./.tag/jpg_email_sending.tag

call tagui ./.tag/report_email_sending.tag