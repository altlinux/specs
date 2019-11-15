Summary: Simple scripts for encrypt and digest files with openssl and caja
Name: mate-file-manager-actions-gost
Version: 1
Release: alt1
Group: Graphical desktop/MATE
License: GPL-3.0+

Url: https://git.altlinux.org/people/lvol/packages/mate-file-manager-actions-gost

Packager: Leontiy Volodin <lvol@altlinux.org>

BuildRequires: mate-file-manager-actions gnome-icon-theme
Requires: mate-file-manager-actions gnome-icon-theme

BuildArch: noarch

Source: %name-%version.tar
Source1: caja-gost-encrypt
Source2: caja-gost-decrypt
Source3: caja-gost-digest

%description
The package adds gost-grasshopper encryption and digest for Caja, the MATE file manager

%prep
%setup

%build
%install
mkdir -p %buildroot%_bindir
cp -a %SOURCE1 %buildroot%_bindir/
cp -a %SOURCE2 %buildroot%_bindir/
cp -a %SOURCE3 %buildroot%_bindir/

mkdir -p %buildroot%_iconsdir/gnome/48x48/status
ln -s %_iconsdir/gnome/48x48/status/changes-prevent.png %buildroot%_iconsdir/gnome/48x48/status/changes-prevent.png
ln -s %_iconsdir/gnome/48x48/status/changes-allow.png %buildroot%_iconsdir/gnome/48x48/status/changes-allow.png
ln -s %_iconsdir/gnome/48x48/status/dialog-information.png %buildroot%_iconsdir/gnome/48x48/status/dialog-information.png

mkdir -p %buildroot%_datadir/file-manager/actions/

#---
# Create context menu for encrypt script
#---
touch %buildroot%_datadir/file-manager/actions/caja-gost-encrypt.desktop

echo "[Desktop Entry]
Type=Action
ToolbarLabel[ru_RU]=Зашифровать по ГОСТ
ToolbarLabel[ru]=Зашифровать по ГОСТ
Name[ru_RU]=Зашифровать по ГОСТ
Name[ru]=Зашифровать по ГОСТ
Profiles=profile-zero;


Icon[ru_RU]=/usr/share/icons/gnome/48x48/status/changes-prevent.png
Icon[ru]=/usr/share/icons/gnome/48x48/status/changes-prevent.png
Tooltip[ru_RU]=Зашифровать файл или папку по ГОСТ, используя алгоритм "Кузнечик"
Tooltip[ru]=Зашифровать файл или папку по ГОСТ, используя алгоритм "Кузнечик"

[X-Action-Profile profile-zero]
Exec=/usr/bin/caja-gost-encrypt %B
Name[ru_RU]=Зашифровать по ГОСТ
Name[ru]=Зашифровать по ГОСТ" >> %buildroot%_datadir/file-manager/actions/caja-gost-encrypt.desktop

#---
# Create context menu for decrypt script
#---
touch %buildroot%_datadir/file-manager/actions/caja-gost-decrypt.desktop

echo "[Desktop Entry]
Type=Action
ToolbarLabel[ru_RU]=Расшифровать по ГОСТ
ToolbarLabel[ru]=Расшифровать по ГОСТ
Name[ru_RU]=Расшифровать по ГОСТ
Name[ru]=Расшифровать по ГОСТ
Profiles=profile-zero;


Icon[ru_RU]=/usr/share/icons/gnome/48x48/status/changes-allow.png
Icon[ru]=/usr/share/icons/gnome/48x48/status/changes-allow.png
Tooltip[ru_RU]=Расшифровать файл или папку по ГОСТ, используя алгоритм "Кузнечик"
Tooltip[ru]=Расшифровать файл или папку по ГОСТ, используя алгоритм "Кузнечик"

[X-Action-Profile profile-zero]
Exec=/usr/bin/caja-gost-decrypt %B
Name[ru_RU]=Расшифровать по ГОСТ
Name[ru]=Расшифровать по ГОСТ" >> %buildroot%_datadir/file-manager/actions/caja-gost-decrypt.desktop

#---
# Create context menu for digest script
#---
touch %buildroot%_datadir/file-manager/actions/caja-gost-digest.desktop

echo "[Desktop Entry]
Type=Action
ToolbarLabel[ru_RU]=Подсчитать контрольную сумму по ГОСТ
ToolbarLabel[ru]=Подсчитать контрольную сумму по ГОСТ
Name[ru_RU]=Подсчитать контрольную сумму по ГОСТ
Name[ru]=Подсчитать контрольную сумму по ГОСТ
Profiles=profile-zero;


Icon[ru_RU]=/usr/share/icons/gnome/48x48/status/dialog-information.png
Icon[ru]=/usr/share/icons/gnome/48x48/status/dialog-information.png
Tooltip[ru_RU]=Вычислить контрольную сумму ГОСТ
Tooltip[ru]=Вычислить контрольную сумму ГОСТ

[X-Action-Profile profile-zero]
Exec=/usr/bin/caja-gost-digest %B
Name[ru_RU]=Подсчитать контрольную сумму по ГОСТ
Name[ru]=Подсчитать контрольную сумму по ГОСТ" >> %buildroot%_datadir/file-manager/actions/caja-gost-digest.desktop


%files
%_bindir/*
%dir %_datadir/file-manager/actions
%_datadir/file-manager/actions/caja-gost-encrypt.desktop
%_datadir/file-manager/actions/caja-gost-decrypt.desktop
%_datadir/file-manager/actions/caja-gost-digest.desktop
%exclude %_iconsdir/gnome/48x48/status/changes-prevent.png
%exclude %_iconsdir/gnome/48x48/status/changes-allow.png
%exclude %_iconsdir/gnome/48x48/status/dialog-information.png

%changelog
* Fri Nov 15 2019 Leontiy Volodin <lvol@altlinux.org> 1-alt1
- Initial build for ALT Sisyphus.
