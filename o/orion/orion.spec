%define _unpackaged_files_terminate_build 1

Name: orion
Version: 1.6.7
Release: alt1
Summary: Seek and watch streams on Twitch
License: GPLv3+
Group: Networking/Other
Url: https://alamminsalo.github.io/orion/

# https://github.com/alamminsalo/orion.git
Source: %name-%version.tar

Patch1: %name-%version-fix-crash-at-exit.patch
Patch2: %name-%version-simplify-and-uniformize-singleton-initialization.patch
Patch3: %name-%version-dont-use-broken-font.patch
Patch4: %name-%version-change-default-view.patch
Patch5: %name-%version-revert-topbar-hiding-at-screen-edge.patch
Patch6: %name-%version-hide-headers-only-in-player-view.patch
Patch7: %name-%version-dont-strip.patch

BuildRequires: qt5-base-devel >= 5.8 qt5-quickcontrols qt5-svg-devel qt5-quickcontrols2-devel qt5-multimedia-devel

Requires: qt5-quickcontrols qt5-quickcontrols2 icon-theme-hicolor qt5-multimedia qt5-graphicaleffects

%description
A desktop client for Twitch.tv. Features:

 - Login by twitch credentials
 - Desktop notifications
 - Integrated player
 - Chat support
 - Support for live streams and vods

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -name '*.cpp' -o -name '*.h' | xargs sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
%qmake_qt5 "CONFIG+=multimedia"
%make_build

%install
%installqt5

%files
%doc README.md COPYING LICENSE.txt
%_bindir/%name
%_desktopdir/Orion.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/metainfo/Orion.appdata.xml

%changelog
* Tue Jun 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.7-alt1
- Updated to upstream version 1.6.7.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt6
- NMU: remove rpm-build-ubt from BR:

* Tue Jun 18 2019 Michael Shigorin <mike@altlinux.org> 1.6.1-alt5
- E2K: strip UTF-8 BOM for lcc < 1.24

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt4
- NMU: remove %%ubt from release

* Fri Mar 16 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt3
- add qt5-graphicaleffects dependency

* Tue Feb 20 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt2
- add qt5-multimedia dependency

* Tue Feb 06 2018 Maxim Voronov <mvoronov@altlinux.org> 1.6.1-alt1
- new version

* Wed Jan 23 2018 Maxim Voronov <mvoronov@altlinux.org> 1.5.1-alt1
- initial build for ALT

