# TODO: build with external lxqt_wallet, with kwallet support
Name: sirikali
Version: 1.3.3
Release: alt1

Summary: A Qt/C++ GUI front end to ecryptfs-simple,cryfs,gocryptfs,securefs and encfs

License: GPL-2.0+
Group: File tools
Url: http://mhogomchungu.github.io/sirikali

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mhogomchungu/sirikali/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: libgcrypt-devel
BuildRequires: libsecret-devel
BuildRequires: libpwquality-devel

BuildRequires: qt5-base-devel

Provides: cryfs-gui = %version-%release
Obsoletes: cryfs-gui

Requires: xdg-utils

%description
SiriKali is a Qt/C++ GUI application that manages ecryptfs,cryfs,encfs,gocryptfs and securefs based encrypted folders.
ecryptfs-simple binary application is required to be installed for SiriKali to gain support for ecryptfs volumes.

cryfs binary application is required to be installed for SiriKali to gain support for cryfs volumes.

gocryptfs binary application is required to be installed for SiriKali to gain support for gocryptfs volumes.

encfs binary application is required to be installed for SiriKali to gain support for encfs volumes.

securefs binary application is required to be installed for SiriKali to gain support for securefs volumes.

Encrypted container folders have an advantage over encrypted container files like the ones that are created
by zuluCrypt,TrueCrypt,VeraCrypt among other projects that use file based encrypted containers.

%prep
%setup

%build
%cmake -DQT5=true -DNOKDESUPPORT=true -DNOSECRETSUPPORT=false -DCMAKE_BUILD_TYPE=RELEASE
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

%files
%_bindir/%name
%_bindir/%{name}.pkexec
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/%name.png
%_pixmapsdir/%name.png
%_man1dir/%name.*
%_datadir/polkit-1/actions/org.sirikali.pkexec.policy
%_datadir/metainfo/sirikali.appdata.xml

%changelog
* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt1
- initial build for ALT Linux Sisyphus
