# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: IMSProg
Version: 1.8.5
Release: alt1

Summary: I2C, SPI and MicroWire EEPROM/Flash chip programmer for CH341a devices
Summary(ru_RU.UTF-8): I2C, SPI and MicroWire EEPROM/Flash программатор для CH341a устройств
License: GPL-3.0-or-later
Group: Engineering

Url: https://github.com/bigbigmdm/IMSProg
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: libudev-devel

%description
IMSProg - Linux IMSProg - I2C, SPI and MicroWire EEPROM/Flash chip programmer
for CH341a devices. The IMSProm is a free I2C EEPROM programmer tool for
CH341A device based on QhexEdit2 and modify SNANDer programmer.

This is a GUI program used widget QhexEditor. For setting the SPI chip
parameters you can use the Detect button for reading chip parameters
(JEDEC information reading) or manually setting it. The I2C and MicroWire
EEPROM only manually selected.

The chip database format is clone with EZP2019, EZP2020, EZP2023, Minpro I,
XP866+ programmers. You can edit the database use the EZP Chip data Editor.

%description -l ru_RU.UTF-8
IMSProg - Linux IMSProg - I2C, SPI and MicroWire EEPROM/Flash программатор
для CH341a устройств. IMSProm является бесплатной утилитой для
использования CH341A устройств в качестве программатора микросхем. Основана на
QhexEdit2 и модифицированном программаторе SNANDer.

Графический интерфейс программы использует виджеты QhexEditor. Для настройки
параметров чипа SPI вы можете использовать кнопку «Поиск» для чтения параметров
чипа (считывание информации JEDEC) или настроить его вручную. I2C и MicroWire
EEPROM выбираются только вручную.

Формат базы данных чипов клонируется программаторами EZP2019, EZP2020, EZP2023,
Minpro I, XP866+. Вы можете редактировать базу данных с помощью редактора данных
EZP Chip.

%prep
%setup
%patch -p1

# update translations
lrelease-qt6 IMSProg_editor/language/*.ts
lrelease-qt6 IMSProg_programmer/language/*.ts
lrelease-qt6 IMSProg_database_update/language/*.ts

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir
%cmake_build

%install
%cmake_install

# remove extra appdata
rm %buildroot%_datadir/metainfo/io.github.bigbigmdm.imsprog_database_update.metainfo.xml
rm %buildroot%_datadir/metainfo/io.github.bigbigmdm.imsprog_editor.metainfo.xml

# rename README
cp IMSProg_editor/README.md IMSProg_editor.md
cp IMSProg_programmer/README.md IMSProg_programmer.md

%files
%doc README.md IMSProg_editor.md IMSProg_programmer.md ChangeLog
%_docdir/imsprog/
%_bindir/IMSProg
%_bindir/IMSProg_editor
%_bindir/IMSProg_database_update
%_datadir/imsprog
%_desktopdir/IMSProg.desktop
%_desktopdir/IMSProg_editor.desktop
%_desktopdir/IMSProg_database_update.desktop
%_datadir/metainfo/io.github.bigbigmdm.imsprog.metainfo.xml
%_udevrulesdir/71-CH341.rules
%_pixmapsdir/chipEdit64.png
%_pixmapsdir/IMSProg64.png
%_pixmapsdir/IMSProg_database_update.png
%_man1dir/*.1.*

%changelog
* Tue Jun 09 2026 Valery Zabrovsky <brow@altlinux.org> 1.8.5-alt1
- New version 1.8.5.

* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 1.8.4-alt1
- New version 1.8.4.

* Thu Apr 23 2026 Valery Zabrovsky <brow@altlinux.org> 1.8.3-alt1
- New version 1.8.3.
- Add Qt6 support for IMSProg_database_update.
- Fix programmer main window displaying issues.

* Wed Apr 08 2026 Valery Zabrovsky <brow@altlinux.org> 1.8.2-alt1
- New version 1.8.2.

* Sat Jan 24 2026 Anton Midyukov <antohami@altlinux.org> 1.7.2-alt2
- Rebuild with qt6.

* Tue Nov 25 2025 Anton Midyukov <antohami@altlinux.org> 1.7.2-alt1
- New version 1.7.2.

* Mon Nov 10 2025 Anton Midyukov <antohami@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Wed Jul 02 2025 Anton Midyukov <antohami@altlinux.org> 1.6.2-alt1
- New version 1.6.2.

* Tue May 20 2025 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt1
- New version 1.6.1.

* Tue May 06 2025 Anton Midyukov <antohami@altlinux.org> 1.5.3-alt1
- New version 1.5.3.

* Thu Mar 06 2025 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- New version 1.5.2.

* Thu Feb 27 2025 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- New version 1.5.1.

* Fri Jan 17 2025 Anton Midyukov <antohami@altlinux.org> 1.4.5-alt1
- New version 1.4.5.

* Mon Sep 23 2024 Anton Midyukov <antohami@altlinux.org> 1.4.4-alt1
- new version

* Fri Jul 26 2024 Anton Midyukov <antohami@altlinux.org> 1.4.3-alt1
- new version

* Thu Jul 11 2024 Anton Midyukov <antohami@altlinux.org> 1.4.2-alt1
- new version
- include IMSProg_database_update

* Mon May 27 2024 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- new version

* Mon May 13 2024 Anton Midyukov <antohami@altlinux.org> 1.3.9-alt1
- new version

* Wed May 08 2024 Anton Midyukov <antohami@altlinux.org> 1.3.8-alt1
- new version

* Sun Apr 28 2024 Anton Midyukov <antohami@altlinux.org> 1.3.7-alt1
- new version

* Thu Apr 18 2024 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt1
- new version

* Thu Apr 11 2024 Anton Midyukov <antohami@altlinux.org> 1.3.5-alt1
- new version

* Mon Apr 08 2024 Anton Midyukov <antohami@altlinux.org> 1.3.4-alt1
- new version

* Tue Mar 26 2024 Anton Midyukov <antohami@altlinux.org> 1.3.3-alt1
- new version

* Thu Feb 29 2024 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- new version
- fix comments in %%_udevrulesdir/99-CH341.rules

* Thu Feb 15 2024 Anton Midyukov <antohami@altlinux.org> 1.3.1-alt1
- new version

* Sat Feb 10 2024 Anton Midyukov <antohami@altlinux.org> 1.2.1-alt1
- new version

* Wed Feb 07 2024 Anton Midyukov <antohami@altlinux.org> 1.1.12-alt1
- new version
- 99-CH341.rules: change group uucp instead plugdev

* Sun Feb 04 2024 Anton Midyukov <antohami@altlinux.org> 1.1.11-alt1
- new version

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- new version

* Sun Jan 21 2024 Anton Midyukov <antohami@altlinux.org> 1.1.6-alt1
- new version (Closes: 49084)

* Mon Jan 08 2024 Anton Midyukov <antohami@altlinux.org> 1.1.4-alt1
- new version

* Wed Dec 06 2023 Anton Midyukov <antohami@altlinux.org> 1.1.2-alt1
- new version (Closes: 48694)

* Fri Oct 13 2023 Anton Midyukov <antohami@altlinux.org> 1.0.27-alt1
- initial build (Closes: 47993)
