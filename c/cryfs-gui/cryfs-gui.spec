Name: cryfs-gui
Version: 1.3.4
Release: alt1

Summary: Qt GUI front end to cryfs and encfs

License: GPL-2.0+
Group: File tools
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mhogomchungu/cryfs-gui/releases/download/%version/cryfs-gui-%version.tar.xz
Source: %name-%version.tar
Url: http://mhogomchungu.github.io/cryfs-gui

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glibc-devel-static
BuildRequires: libgcrypt-devel
BuildRequires: libsecret-devel

BuildRequires: qt5-base-devel

%description
cryfs-gui is a Qt/C++ front end to encfs and cryfs.

%prep
%setup

%build
%cmake -DQT5=true -DNOKDESUPPORT=true -DNOSECRETSUPPORT=false -DCMAKE_BUILD_TYPE=RELEASE
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%_bindir/cryfs_gui
%_desktopdir/cryfs-gui.desktop

%dir %_datadir/cryfs-gui/translations
%dir %_datadir/cryfs-gui

%_iconsdir/hicolor/48x48/apps/cryfs-gui.png
%_pixmapsdir/cryfs-gui.png
%_datadir/cryfs-gui/translations/en_US.qm
%_datadir/cryfs-gui/translations/fr_FR.qm

%changelog
* Thu Mar 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- initial build for ALT Linux Sisyphus
