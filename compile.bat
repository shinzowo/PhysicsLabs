pyinstaller -F main.py --optimize 2 -w --disable-windowed-traceback --workpath "./.build/build" --specpath "./.build" --distpath "./.build/dist" --icon "../icons/icon.png"
xcopy /e /k /h /i /y .\otchot .\.build\dist\otchot
xcopy /e /k /h /i /y .\data .\.build\dist\data
xcopy /e /k /h /i /y .\images .\.build\dist\images