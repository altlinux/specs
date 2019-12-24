Name: upplay
Version: 1.3.9
Release: alt1

Summary: UPnP/OpenHome audio Control Point
License: GPLv2
Group: Sound
Url: http://www.lesbonscomptes.com/upplay/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: jsoncpp-devel libcurl-devel libexpat-devel libupnpp-devel
BuildRequires: qt5-base-devel qt5-script-devel qt5-webkit-devel

%description
Upplay is a simple Qt-based UPnP/OpenHome audio Control Point.
It supports gapless transitions using either AVTransport _setNextUri_ or
OpenHome _Playlist_, depending on what the device supports (OpenHome is
chosen if available).

%prep
%setup

%build
%qmake_qt5
%make_build

%install
INSTALL_ROOT=%buildroot STRIP=: \
%makeinstall_std

%files
%_bindir/upplay
%_datadir/upplay
%_desktopdir/upplay.desktop
%_liconsdir/upplay.png
%_pixmapsdir/upplay.png

%changelog
* Wed Dec 25 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.9-alt1
- initial
