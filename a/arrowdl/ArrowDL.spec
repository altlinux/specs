%define oname ArrowDL
%define webname com.arrowdl.extension

Name: arrowdl
Version: 4.2.1
Release: alt2

Summary: ArrowDL (Arrow Downloader) is a download manager

License: LGPL-2.1-or-later
Group: Networking/File transfer

Url: https://www.arrow-dl.com
Vcs: https://github.com/setvisible/ArrowDL

Source: %name-%version.tar

Requires: yt-dlp
#libcrypto3 libssl3

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ qt6-base-devel qt6-tools-devel
BuildRequires: libtorrent-rasterbar-devel libssl-devel

%description
ArrowDL (Arrow Downloader) is a download manager for Windows, MacOS and Linux.

%package web-extension-firefox
Summary: Web-extension %oname for FireFox
Group: Networking/File transfer
Requires: %name = %EVR
%description web-extension-firefox
Web-extension %oname for FireFox.

%package web-extension-chrome
Summary: Web-extension %oname for Chrome
Group: Networking/File transfer
Requires: %name = %EVR
%description web-extension-chrome
Web-extension %oname for Chrome.

%prep
%setup
#set locale path
subst 's|"%0/locale"|"%_datadir/%name/locale"|' src/core/locale.cpp
#set path for web-extension
subst 's|/ABSOLUTE/PATH/TO/APP/DIRECTORY/launcher|%_bindir/launcher|' \
web-extension/launcher/unix/launcher-manifest-chrome.json 
subst 's|/ABSOLUTE/PATH/TO/APP/DIRECTORY/launcher|%_bindir/launcher|' \
web-extension/launcher/unix/launcher-manifest-firefox.json

%build
%cmake \
	-DCMAKE_SKIP_RPATH='YES' \
	-DBUILD_TESTS='OFF' \
	-DLibtorrentRasterbar_INCLUDE_DIRS='%_includedir/libtorrent' \
	-DLibtorrentRasterbar_LIBRARIES='%_libdir/libtorrent-rasterbar.so' \
	-DLibtorrentRasterbar_OPENSSL_ENABLED='YES' \
	-DOPENSSL_INCLUDE_DIRS='%_includedir/openssl' \
	-DOPENSSL_CRYPTO_LIBRARY='%_libdir/libcrypto.so' \
	-DOPENSSL_SSL_LIBRARY='%_libdir/libssl.so'
%cmake_build

%install
install -Dm755 %_arch-alt-linux/src/%oname %buildroot%_bindir/%oname
install -Dm755 %_arch-alt-linux/web-extension/launcher/launcher \
	%buildroot%_bindir/launcher
install -d %buildroot%_datadir/%name/locale
cp -a %_arch-alt-linux/src/*.qm %buildroot%_datadir/%name/locale/
install -Dm 644 installer/unix/appimage/%oname.desktop \
	%buildroot%_desktopdir/%oname.desktop
install -Dm 0644 installer/unix/appimage/%oname.svg \
	%buildroot%_pixmapsdir/%oname.svg
install -Dm644 web-extension/launcher/unix/launcher-manifest-chrome.json \
	%buildroot%_sysconfdir/chromium/native-messaging-hosts/%webname.json
install -Dm644 web-extension/launcher/unix/launcher-manifest-firefox.json \
	%buildroot%_libdir/mozilla/native-messaging-hosts/%webname.json

%files
%_bindir/*
%_datadir/%name/locale
%_desktopdir/%oname.desktop
%_pixmapsdir/%oname.svg
%doc *.md

%files web-extension-firefox
%_libdir/mozilla/native-messaging-hosts/%webname.json

%files web-extension-chrome
%_sysconfdir/chromium/native-messaging-hosts/%webname.json

%changelog
* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.2.1-alt2
- fixed path for FireFox web extension

* Sat Mar 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.2.1-alt1
- Initial build for ALT Linux.

