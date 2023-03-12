# TODO: build with external lxqt_wallet, with kwallet support
Name: sirikali
Version: 1.5.0
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
SiriKali is a Qt/C++ GUI application that manages ecryptfs, cryfs,
encfs, gocryptfs and securefs based encrypted folders.

ecryptfs-simple binary application is required to be installed for
SiriKali to gain support for ecryptfs volumes.

cryfs binary application is required to be installed for SiriKali
to gain support for cryfs volumes.

gocryptfs binary application is required to be installed for SiriKali
to gain support for gocryptfs volumes.

encfs binary application is required to be installed for SiriKali
to gain support for encfs volumes.

securefs binary application is required to be installed for SiriKali
to gain support for securefs volumes.

Encrypted container folders have an advantage over encrypted
container files like the ones that are created by zuluCrypt,
TrueCrypt, VeraCrypt among other projects that use file based
encrypted containers.

%prep
%setup
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%cmake \
	-DQT5=true \
	-DNOKDESUPPORT=true \
	-DNOSECRETSUPPORT=false \
	-DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_bindir/%{name}.pkexec
%_datadir/%name/
%_desktopdir/io.github.mhogomchungu.sirikali.desktop
%_iconsdir/hicolor/48x48/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/%name.png
%_pixmapsdir/%name.png
%_man1dir/%name.*
%_datadir/polkit-1/actions/org.sirikali.pkexec.policy
%_datadir/metainfo/sirikali.appdata.xml

%changelog
* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.4.8-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- new version 1.4.8 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- new version 1.4.7 (with rpmrb script)

* Fri Aug 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- new version 1.4.6 (with rpmrb script)

* Fri Jun 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Wed May 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- new version 1.4.3 (with rpmrb script)

* Tue Jan 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Mon Oct 14 2019 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- minor spec cleanup

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.9-alt1
- new version 1.3.9 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.8-alt1
- new version 1.3.8 (with rpmrb script)

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.7-alt1
- new version 1.3.7 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.6-alt1
- new version 1.3.6 (with rpmrb script)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- new version 1.3.5 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version 1.3.4 (with rpmrb script)

* Sun Feb 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- new version 1.3.3 (with rpmrb script)

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)

* Sat Jun 17 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.7-alt1
- initial build for ALT Linux Sisyphus
