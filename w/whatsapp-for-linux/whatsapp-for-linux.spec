Name: whatsapp-for-linux
Version: 1.6.5
Release: alt1

Summary: An unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2

License: GPL-3.0
Group: Networking/Instant messaging
Url: https://github.com/eneshecan/whatsapp-for-linux

# Source-url: https://github.com/eneshecan/whatsapp-for-linux/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
#BuildRequires: pkgconfig(appindicator3-0.1)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(webkit2gtk-4.0) >= 2.34
#BuildRequires: pkgconfig(webkit2gtk-4.1) >= 2.34
BuildRequires: pkgconfig(gtkmm-3.0)
BuildRequires: pkgconfig(libcanberra)

# just to hide Package libpcre was not found in the pkg-config search path.
BuildRequires: libpcre2-devel

%description
Whatsapp-for-linux is an unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.

%prep
%setup
# disable hw-accel by default (ALT bug 43906)
#subst 's|"hw-accel", 1|"hw-accel", 0|' src/ui/WebView.cpp

%build
%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install
%find_lang %name
# FIXME:
rm -rv %buildroot%_datadir/locale/pt-br/
rm -rv %buildroot%_datadir/locale/zh-Hans/

%files -f %name.lang
%doc README.md
%_bindir/whatsapp-for-linux
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/*x*/status/*.png
/usr/share/metainfo/com.github.eneshecan.WhatsAppForLinux.appdata.xml

%changelog
* Fri May 31 2024 Roman Alifanov <ximper@altlinux.org> 1.6.5-alt1
- new version 1.6.5 (with rpmrb script)

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- new version 1.6.4 (with rpmrb script)

* Tue May 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- new version 1.6.3 (with rpmrb script)

* Fri Apr 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)
- disable hw-accel by default (ALT bug 43906)

* Wed Mar 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- new version 1.6.1 (with rpmrb script) (ALT bug 45056)

* Thu Dec 29 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script) (ALT bug 44739)

* Wed Nov 02 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)

* Sun Aug 28 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- new version 1.4.6 (with rpmrb script)

* Tue Jul 19 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- new version 1.4.5 (with rpmrb script)

* Tue Jun 28 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Sisyphus

