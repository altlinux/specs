%define _unpackaged_files_terminate_build 1

Name: wifi-qr
Version: 0.4
Release: alt1

Summary: Wi-Fi password share via QR codes
License: GPL-3.0-or-later AND CC0-1.0
Group: System/Configuration/Networking
Url: https://github.com/kokoye2007/wifi-qr

Source: %name-%version.tar

BuildArch: noarch

%description
Shares Wi-Fi SSID and password via a QR code.
Generate a QR code of a Wi-Fi network with its password.
Scan QR codes and easily connect to Wi-Fi Networks.

For Android, OS version 10 and above is supported.

For iOS, the Shortcut app supports generating Wi-Fi QR codes.

%prep
%setup
sed -i "s|--icon=wifi-qr|--icon=%_iconsdir/hicolor/scalable/apps/wifi-qr.svg|" wifi-qr
sed -i "s|/usr/share/doc/wifi-qr/copyright|/usr/share/doc/wifi-qr-%version/COPYING|" wifi-qr

%build
%make_build

%install
mkdir -pv %buildroot%_bindir
install -m 755 wifi-qr %buildroot%_bindir/

mkdir -pv %buildroot%_desktopdir
install -m 644 wifi-qr.desktop %buildroot%_desktopdir/

mkdir -pv %buildroot%_datadir/metainfo
install -m 644 wifi-qr.metainfo.xml %buildroot%_datadir/metainfo/

mkdir -pv %buildroot%_iconsdir/hicolor/scalable/apps
install -m 644 wifi-qr.svg %buildroot%_iconsdir/hicolor/scalable/apps/

mkdir -pv %buildroot%_man1dir
install -m 644 wifi-qr.1 %buildroot%_man1dir/

%files
%doc COPYING LICENSE README.KDE.md README.md screenshots
%_bindir/wifi-qr
%_desktopdir/wifi-qr.desktop
%_iconsdir/hicolor/scalable/apps/wifi-qr.svg
%_man1dir/wifi-qr.1*
%_datadir/metainfo/wifi-qr.metainfo.xml

%changelog
* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 0.4-alt1
- Initial build for Sisyphus
