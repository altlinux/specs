Name: orion
Version: 1.5.1
Release: alt1%ubt

Summary: Seek and watch streams on Twitch

License: GPLv3+
Group: Networking/Other
Url: https://alamminsalo.github.io/orion/

Source: %name-%version.tar

Patch0: %name-%version-fix_prefix.patch
Patch1: %name-%version-fix_desktop.patch

Requires: qt5-quickcontrols qt5-quickcontrols2 icon-theme-hicolor

BuildRequires(pre): rpm-build-ubt
BuildRequires: qt5-base-devel >= 5.7 qt5-quickcontrols qt5-svg-devel qt5-quickcontrols2-devel qt5-multimedia-devel

%description
A desktop client for Twitch.tv. Features:

 - Login by twitch credentials
 - Desktop notifications
 - Integrated player
 - Chat support
 - Support for live streams and vods

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%qmake_qt5 "CONFIG+=multimedia"
%make_build

%install
%installqt5

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%doc README.md COPYING LICENSE.txt

%changelog
* Wed Jan 23 2018 Maxim Voronov <mvoronov@altlinux.org> 1.5.1-alt1%ubt
- initial build for ALT

