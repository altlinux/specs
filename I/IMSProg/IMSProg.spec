# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: IMSProg
Version: 1.0.27
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
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools
BuildRequires: pkgconfig(libusb-1.0)

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
lrelease-qt5 IMSProg_editor/language/*.ts
lrelease-qt5 IMSProg_programmer/language/*.ts

%build
pushd IMSProg_editor
%cmake
%cmake_build
popd

pushd IMSProg_programmer
%cmake
%cmake_build
popd

%install
pushd IMSProg_editor
%cmake_install
popd

pushd IMSProg_programmer
%cmake_install
popd

# move udev rules to %_udevrulesdir
mkdir -p %buildroot%_udevrulesdir
mv %buildroot%_sysconfdir/udev/rules.d/99-CH341.rules \
   %buildroot%_udevrulesdir/99-CH341.rules

# rename README
cp IMSProg_editor/README.md IMSProg_editor.md
cp IMSProg_programmer/README.md IMSProg_programmer.md

%files
%doc README.md IMSProg_editor.md IMSProg_programmer.md
%_bindir/%name
%_bindir/%{name}_editor
%_datadir/%name
%_desktopdir/%name.desktop
%_desktopdir/%{name}_editor.desktop
%_udevrulesdir/99-CH341.rules
%_iconsdir/hicolor/64x64/apps/%{name}_editor.png
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Fri Oct 13 2023 Anton Midyukov <antohami@altlinux.org> 1.0.27-alt1
- initial build (Closes: 47993)
