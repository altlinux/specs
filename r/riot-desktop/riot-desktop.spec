Name: riot-desktop
Version: 0.10.1
Release: alt1

Summary: A glossy Matrix collaboration client

License: Apache 2.0
Url: https://riot.im/desktop.html
Group: Networking/Instant messaging

ExclusiveArch: x86_64
# Source-url: https://riot.im/packages/debian/pool/main/r/riot-web/riot-web_%{version}_amd64.deb
Source: %name-%version.tar

AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

# electron based requiries
BuildRequires: libgtk+2 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf

%description
Riot (formerly known as Vector) is a Matrix web client built using the Matrix React SDK.

%prep
%setup
# replace strange missed functions with exit function
sed -E -i -e "s@(_ZN10crash_keys17SetVari|_ZN15MersenneTwister12in|_ZN15MersenneTwister13ge|_ZN15MersenneTwisterC1Ev|_ZN15MersenneTwisterD1Ev)@exit\x0MersenneTwisterD1Ev@g" opt/Riot/riot-web

%__subst "s|/opt/Riot/riot-web|%_bindir/riot-desktop|g" usr/share/applications/riot-web.desktop

%install
mkdir -p %buildroot%_libdir/%name/
cp -a opt/Riot/* %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/riot-web %buildroot/%_bindir/riot
ln -rs %buildroot%_libdir/%name/riot-web %buildroot/%_bindir/riot-desktop
mkdir -p %buildroot%_iconsdir/
cp -a usr/share/icons/hicolor/ %buildroot%_iconsdir/
mkdir -p %buildroot%_desktopdir/
cp -a usr/share/applications/riot-web.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/riot
%_bindir/riot-desktop
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 0.10.1-alt1
- initial release for ALT Sisyphus
