Name:		DeroGUIWallet
Version:	0.0.1
Release:	alt1
Summary:	GUI Wallet for Dero
Url:		https://github.com/drigler/DeroGUIWallet/
Group:		Office
License:	MIT
Source0:	%name.tar.xz
Source1:	%name.desktop
Source2:	%name

BuildArch:	noarch

BuildRequires:	python-dev rpm-build-gir /usr/bin/convert

Requires:	dero python-module-psutil python-module-requests python-module-PySide

Provides:	deroguiwallet

%description
DERO GUI Wallet

This is a fork of the Sumokoin GUI Wallet:
https://github.com/sumoprojects/SumoGUIWallet adopted to work with Dero binaries.

%prep
%setup -n %name

%install
mkdir -p %buildroot/usr/libexec/%name
cp -a * %buildroot/usr/libexec/%name/
chmod +x %buildroot/usr/libexec/%name/wallet.py

install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dp -m 0755 %SOURCE2 %buildroot%_bindir/%name

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 Resources/icons/dero_icon.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 Resources/icons/dero_icon.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 Resources/icons/dero_icon.png %buildroot%_miconsdir/%name.png

%files
%dir /usr/libexec/%name
%_bindir/%name
/usr/libexec/%name/*
%_desktopdir/*.desktop
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%changelog
* Tue Feb 06 2018 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux
