Name:    freeoffice
Version: 1.0.0
Release: alt4

Summary: Free Office Application Suite
License: Proprietary
Group:   Office

Url:     http://www.altlinux.org/FreeOffice
Source:  %name-%version.tar

ExcludeArch: %ix86 armh ppc64le

Requires: libreoffice
Requires: libreoffice-gtk3
Requires: libreoffice-kde6
Requires: libreoffice-langpack-be
Requires: libreoffice-langpack-kk
Requires: libreoffice-langpack-ky
Requires: libreoffice-langpack-ru
Requires: libreoffice-langpack-uk
Requires: libreoffice-langpack-uz
Requires: thunderbird
Requires: davmail
Requires: surguch
Requires: chromium
Requires: ca-certificates-digital.gov.ru
Requires: zenity

Summary(ru_RU.UTF-8): Пакет офисных приложений Свободный офис

%description
"Free Office" is a modern software suite for working with documents, email, and
web resources. The product is designed for a wide range of users - from home
computer owners to corporate clients and government employees.

"Free Office" includes applications for creating and editing text documents,
spreadsheets, presentations, mathematical formulas, and vector graphics. The
"Surguch" tools and ALT CSP CryptoPro with the CryptoPro package allow signing
and verifying documents with qualified electronic signatures directly within
the office applications. The Chromium browser, supporting GOST encryption
algorithms and pre-installed with the Ministry of Digital Development of
Russia's root certificate, ensures secure access to government and corporate
web services. The built-in mail client with calendar and address book enables
sending and receiving emails, storing correspondence, scheduling meetings, and
managing contacts.

"Free Office" supports opening, editing, and saving documents in common
formats, including DOCX, XLSX, PPTX, ODF, and others, allowing seamless file
exchange with users of other office suites without data loss or formatting
issues.

%description -l ru_RU.UTF-8
«Свободный офис» — современный программный комплекс для работы с документами,
электронной почтой и веб-ресурсами. Продукт рассчитан на широкий круг
пользователей — от владельцев домашних компьютеров до корпоративных клиентов и
сотрудников государственных учреждений.

«Свободный офис» включает приложения для создания и редактирования текстовых
документов, электронных таблиц, презентаций, математических формул и векторной
графики. Инструменты «Сургуч» и ALT CSP КриптоПро с пакетом КриптоПро позволяют
подписывать и проверять документы квалифицированной электронной подписью прямо
в офисных приложениях. Браузер Chromium с поддержкой ГОСТ-алгоритмов шифрования
и предустановленным корневым сертификатом Минцифры России обеспечивает
безопасную работу с государственными и корпоративными веб-сервисами. Встроенный
почтовый клиент с календарём и адресной книгой позволяет отправлять и получать
письма, хранить переписку, планировать встречи и вести список контактов.

«Свободный офис» поддерживает открытие, редактирование и сохранение документов
в распространённых форматах, включая DOCX, XLSX, PPTX, ODF и другие, что
позволяет обмениваться файлами с пользователями других офисных пакетов без
потери данных и форматирования.

%prep
%setup

%install
install -Dpm0644 license-en.html %buildroot%_datadir/%name/license-en.html
install -Dpm0644 license-ru.html %buildroot%_datadir/%name/license-ru.html
install -Dpm0644 com.Basealt.FreeOffice.appdata.xml %buildroot%_datadir/metainfo/com.Basealt.FreeOffice.appdata.xml
install -Dpm0644 freeoffice.svg %buildroot%_pixmapsdir/freeoffice.svg
install -Dpm0644 freeoffice-symbolic.svg %buildroot%_pixmapsdir/freeoffice-symbolic.svg
install -Dpm0755 freeoffice-installed %buildroot%_bindir/freeoffice-installed
install -Dpm0644 com.Basealt.FreeOffice.desktop %buildroot%_desktopdir/com.Basealt.FreeOffice.desktop

%files
%_bindir/freeoffice-installed
%_datadir/%name
%_datadir/metainfo/*.xml
%_pixmapsdir/*.svg
%_desktopdir/*.desktop

%changelog
* Mon Mar 23 2026 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt4
- NMU: remove runtime dependency on obsoleted package alt-csp-cryptopro.

* Wed Nov 26 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt3
- Required libreoffice instead of LibreOffice-still.

* Thu Sep 18 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- Added information dialog to menu.

* Mon Aug 18 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
