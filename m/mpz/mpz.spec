Name: mpz
Version: 1.0.23
Release: alt1

Summary: Music player for the large local collections

License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/olegantonyan/mpz

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/olegantonyan/mpz/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-x11extras-devel

%description
Music player for big local collections. Treats your folders with music as a library.
Features 3-column UI: directory tree viewer, playlists list and tracks from current playlist.
Similar to "album list" in Foobar2000.

%prep
%setup

%build
mkdir build
cd build
qmake-qt5 CONFIG+=release CONFIG+=force_debug_info ..
%make_build

%install
cd build
%make_install install INSTALL_ROOT=%buildroot

%files
%doc license.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.23-alt1
- new version 1.0.23 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1.0.20-alt1
- new version 1.0.20 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.19-alt1
- new version 1.0.19 (with rpmrb script)

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.15-alt1
- new version 1.0.15 (with rpmrb script)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.14-alt1
- new version 1.0.14 (with rpmrb script)

* Mon Dec 14 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt1
- new version 1.0.11 (with rpmrb script)

* Sat Oct 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.8-alt1
- new version 1.0.8 (with rpmrb script)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.7-alt1
- new version 1.0.7 (with rpmrb script)

* Tue Oct 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- new version 1.0.5 (with rpmrb script)

* Fri Oct 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus

* Sun Aug 9 2020 Oleg Antonyan <oleg.b.antonyan@gmail.com>
- First public release
