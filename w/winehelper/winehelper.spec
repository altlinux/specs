Name: winehelper
Version: 0.3.2
Release: alt1

Summary: Program for easy installation of Windows applications.

License: LGPLv2+
Group: Emulators
Url: https://git.linux-gaming.ru/CastroFidel/winehelper

Source: %name-%version.tar

Requires: wine-full
Requires: ca-certificates
Requires: cups-pdf fonts-ttf-ms
Requires: p7zip

ExclusiveArch: x86_64

%description
Program for easy installation of Windows applications with the possibility
of automatic prefix tuning.

%prep
%setup

%build
%install
install -Dm755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name/{autoinstall,database,image}
install -m755 dependencies.sh %buildroot%_datadir/%name/
install -m644 sha256sum.list %buildroot%_datadir/%name/
install -m644 autoinstall/*  %buildroot%_datadir/%name/autoinstall/
install -m644 database/* %buildroot%_datadir/%name/database/
install -m644 image/* %buildroot%_datadir/%name/image/

%files
%doc LICENSE CHANGELOG COPYING THIRD-PARTY
%_bindir/%name
%_datadir/%name

%changelog
* Wed Mar 12 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.2-alt1
- initial build for ALT Sisyphus
