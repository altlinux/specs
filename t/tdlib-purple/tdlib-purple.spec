Name:     tdlib-purple
Version:  0.6.4
Release:  alt1

Summary:  libpurple Telegram plugin using tdlib

License:  GPL-2.0
Group:    Other
Url:      https://github.com/ars3niy/tdlib-purple

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake gcc-c++ tdlib-devel-static librlottie-devel libtgvoip-devel
BuildRequires: libpurple-devel libwebp-devel libpng-devel libssl-devel

ExcludeArch: %ix86

%description
%summary

%prep
%setup

%build
%cmake_insource -DNoLottie=TRUE \
       -Dtgvoip_INCLUDE_DIRS=`pkg-config --cflags tgvoip | sed "s/-I//"` \
       ..
%make_build

%install
%makeinstall_std

%files
%_libdir/purple-2/libtelegram-tdlib.so
%_datadir/locale/de/LC_MESSAGES/tdlib-purple.mo
%_datadir/metainfo/tdlib-purple.metainfo.xml
%_pixmapsdir/pidgin/protocols/16/telegram.png
%_pixmapsdir/pidgin/protocols/22/telegram.png
%_pixmapsdir/pidgin/protocols/48/telegram.png
%doc *.md

%changelog
* Mon Sep 28 2020 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus (Closes: #39000).
