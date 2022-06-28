Name: whatsapp-for-linux
Version: 1.4.4
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
BuildRequires: pkgconfig(webkit2gtk-4.0)
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

%files
%doc README.md
%_bindir/whatsapp-for-linux
%_desktopdir/*.desktop
%_iconsdir/hicolor/*x*/apps/*.png

%changelog
* Tue Jun 28 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- new version 1.4.4 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Sisyphus

