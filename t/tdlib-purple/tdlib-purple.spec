Name:     tdlib-purple
Version:  0.7.2
Release:  alt1

Summary:  libpurple Telegram plugin using tdlib

License:  GPL-2.0
Group:    Other
Url:      https://github.com/ars3niy/tdlib-purple

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Mon Oct 12 2020
# optimized out: cmake-modules glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 libstdc++-devel pkg-config python2-base sh4 tdlib tdlib-devel zlib-devel
BuildRequires: cmake gcc-c++ libpng-devel libpurple-devel librlottie-devel libssl-devel libtgvoip-devel libwebp-devel tdlib-devel-static
BuildRequires: libpcre-devel

#FIXME: tdlib requires tdlib-devel-static to build with
#FIXME: system librlottie lacks some symbols so building with bundled Lottie

%description
%summary

%prep
%setup
#rm -rf rlottie

%build
# 	-DNoBundledLottie=True \
%cmake_insource \
	-Dtgvoip_INCLUDE_DIRS=`pkg-config --cflags tgvoip | sed "s/-I//"` \
	..
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_libdir/purple-2/libtelegram-tdlib.so
%_datadir/metainfo/tdlib-purple.metainfo.xml
%_pixmapsdir/pidgin/protocols/*/telegram.png
%doc *.md

%changelog
* Mon Oct 26 2020 Ildar Mulyukov <ildar@altlinux.ru> 0.7.2-alt1
- new version
- added "keep-inline-downloads" option

* Mon Sep 28 2020 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus (Closes: #39000).
