Summary: Simple scripts for encrypt and digest files with openssl and caja
Name: mate-file-manager-actions-gost
Version: 3
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
Source11: caja-gost-encrypt.desktop
Source12: caja-gost-decrypt.desktop
Source13: caja-gost-digest.desktop

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
cp -a %SOURCE11 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE12 %buildroot%_datadir/file-manager/actions/
cp -a %SOURCE13 %buildroot%_datadir/file-manager/actions/

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
* Wed Nov 20 2019 Leontiy Volodin <lvol@altlinux.org> 3-alt1
- Fixed checksum calculation for files with spaces in names.

* Tue Nov 19 2019 Leontiy Volodin <lvol@altlinux.org> 2-alt1
- Fixed encryption of files with spaces in names.
- The spec was simplified.

* Fri Nov 15 2019 Leontiy Volodin <lvol@altlinux.org> 1-alt1
- Initial build for ALT Sisyphus.
