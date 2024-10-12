call conda activate tagui

python ./.py/ocr.py

java -jar ./.jar/access.jar

java -jar ./.jar/excel.jar

7z a .\.7z\待人工审批发票.7z .\.jpg\待人工审批发票\

tagui ./.tag/jpg_email_sending.tag

tagui ./.tag/report_email_sending.tag