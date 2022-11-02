Name: whatsapp-for-linux
Version: 1.5.0
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
BuildRequires: pkgconfig(gtkmm-3.0)

# just to hide Package libpcre was not found in the pkg-config search path.
BuildRequires: libpcre2-devel

%description
Whatsapp-for-linux is an unofficial WhatsApp linux client written in C++ with the help of gtkmm-3.0 and webkit2.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/whatsapp-for-linux
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/*x*/status/*.png
/usr/share/metainfo/com.github.eneshecan.WhatsAppForLinux.appdata.xml

%changelog
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

