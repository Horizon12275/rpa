call conda activate tagui

python ./.py/ocr.py

java -jar ./.jar/access.jar

java -jar ./.jar/gen_json.jar

python ./.py/jpg_txt_gen.py

python ./.py/jpg_xlsx_gen.py

python ./.py/report_jpg_gen.py

python ./.py/report_txt_gen.py

python ./.py/report_xlsx_gen.py

7z a .\.7z\待人工审批发票.7z .\.jpg\待人工审批发票\

copy ".\.7z\待人工审批发票.7z" ".\.tag\"
copy ".\.xlsx\发票自动化处理统计报表.xlsx" ".\.tag\"
copy ".\.xlsx\转人工审批原因.xlsx" ".\.tag\"
copy ".\.jpg\买方开销分布.jpg" ".\.tag\"
copy ".\.jpg\卖方收入分布.jpg" ".\.tag\"
copy ".\.jpg\发票金额分布.jpg" ".\.tag\"

call tagui ./.tag/jpg_email_sending.tag

call tagui ./.tag/report_email_sending.tag

del .\.7z\待人工审批发票.7z
del .\.tag\待人工审批发票.7z
del .\.tag\发票自动化处理统计报表.xlsx
del .\.tag\转人工审批原因.xlsx
del .\.tag\买方开销分布.jpg
del .\.tag\卖方收入分布.jpg
del .\.tag\发票金额分布.jpg