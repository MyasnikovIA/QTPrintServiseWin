
@echo off
call :isAdmin

if %errorlevel% == 0 (
    goto :run
) else (
    echo Error: Run as administrator.
)
pause
exit /b

:isAdmin
fsutil dirty query %systemdrive% >nul
exit /b

:run
"%~dp0QTPrintService.exe" install

pause