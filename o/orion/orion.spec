Name: orion
Version: 1.6.1
Release: alt3%ubt

Summary: Seek and watch streams on Twitch

License: GPLv3+
Group: Networking/Other
Url: https://alamminsalo.github.io/orion/

Source: %name-%version.tar

Patch0: orion-1.5.1-fix_prefix.patch
Patch1: orion-1.5.1-fix_desktop.patch

Requires: qt5-quickcontrols qt5-quickcontrols2 icon-theme-hicolor qt5-multimedia qt5-graphicaleffects

BuildRequires(pre): rpm-build-ubt
BuildRequires: qt5-base-devel >= 5.8 qt5-quickcontrols qt5-svg-devel qt5-quickcontrols2-devel qt5-multimedia-devel

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
* Fri Mar 16 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt3%ubt
- add qt5-graphicaleffects dependency

* Tue Feb 20 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt2%ubt
- add qt5-multimedia dependency

* Tue Feb 06 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt1%ubt
- new version

* Wed Jan 23 2018 Maxim Voronov <mvoronov@altlinux.org> 1.5.1-alt1%ubt
- initial build for ALT

