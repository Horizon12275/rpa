call conda activate tagui

python ./.py/ocr.py

java -jar ./.jar/access.jar

python ./.py/report_gen.py

7z a .\.7z\待人工审批发票.7z .\.jpg\待人工审批发票\

call tagui ./.tag/jpg_email_sending.tag

call tagui ./.tag/report_email_sending.tag