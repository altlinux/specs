Name: I2P-Messenger
Version: 0.2.20
Release: alt1

Summary: I2P Instant Messaging Client
License: GPL
Group: Security/Networking

Url: http://echelon.i2p/qti2pmessenger/
Source: I2P-Messenger-%version.tar
Source1: I2P-Messenger.desktop
Source2: I2P-Messenger.xpm
Patch0: 0001-00-soundpath.patch
Patch1: 0002-typofix.patch
Patch2: 0003-homedconfigs.patch
Patch3: 0004-typo-fixes.patch

BuildRequires: gcc-c++ libqt4-devel libaudio-devel

%description
I2P-Messenger is an I2P-internal, serverless, anonymous and secure (end-to-end
encrypted) instant messaging client with support for file transfers that
connects via the SAM bridge.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
qmake-qt4 I2P-Messenger_release.pro
%make

%install
mv I2P-Messenger_release %name
install -d %buildroot%_bindir
install -m 755 %name -t %buildroot%_bindir
install -d %buildroot%_datadir/%name/sounds
install -m 644 sounds/* -t %buildroot%_datadir/%name/sounds
install -d %buildroot%_desktopdir
install -d %buildroot%_pixmapsdir
install -m 644 %SOURCE1 %buildroot%_desktopdir
install -m 644 %SOURCE2 %buildroot%_pixmapsdir

%files
%_bindir/%name
%_datadir/%name/sounds
%_pixmapsdir/%name.xpm
%_desktopdir/%name.desktop

%changelog
* Sat Mar 05 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 0.2.20-alt1
- initial build for ALT Linux Sisyphus (thanx Kill Your TV <killyourtv@i2pmail.org>)

