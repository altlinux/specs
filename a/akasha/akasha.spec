Name: akasha
Version: 0.5.2
Release: alt1

Summary: Advanced Knowledge Architecture for Social Human Advocacy

License: Apache 2.0
Url: https://github.com/AkashaProject/node-app#readme
Group: Networking/Instant messaging

ExclusiveArch: x86_64
# Source-url: https://github.com/AkashaProject/Alpha/releases/download/%version/AKASHA-linux-x64-%version.deb
Source: %name-%version.tar

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

# electron based requiries
BuildRequires: libgtk+2 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf

%description
A Next-Generation Social Media Network.
Powered by the Ethereum world computer.
Embedded into the Inter-Planetary File System.

AETH is our test token on the private chain used for this pre-release.
As a test token it does not have any value outside the purpose of testing AKASHA.
At this point, you can obtain AETH tokens by creating an identity on AKASHA.

%prep
%setup
# replace strange missed functions with exit
sed -E -i -e "s@(_ZN10crash_keys17SetVari|_ZN15MersenneTwister12in|_ZN15MersenneTwister13ge|_ZN15MersenneTwisterC1Ev|_ZN15MersenneTwisterD1Ev)@exit\x0MersenneTwisterD1Ev@g" opt/AKASHA/akasha
%__subst "s|/opt/AKASHA/akasha|%_bindir/%name|g" usr/share/applications/akasha.desktop

%install
mkdir -p %buildroot%_libdir/%name/
cp -a opt/AKASHA/* %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/akasha %buildroot/%_bindir/%name

mkdir -p %buildroot%_iconsdir/
cp -a usr/share/icons/hicolor/ %buildroot%_iconsdir/
mkdir -p %buildroot%_desktopdir/
cp -a usr/share/applications/akasha.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/akasha
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- initial release for ALT Sisyphus
