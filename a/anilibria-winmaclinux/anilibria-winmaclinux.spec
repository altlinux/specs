Name: anilibria-winmaclinux
Version: 1.2.11
Release: alt2

Summary: AniLibria online video player for desktop platforms
Summary(ru_RU.UTF-8): Онлайн-видеоплеер AniLibria для настольных платформ
License: GPL-3.0-only
Group: Video
Url: http://anilibriadesktop.reformal.ru

Requires: qt5-graphicaleffects
Requires: libqt5-multimedia
Requires: qt5-quickcontrols2
Requires: qt5-quickcontrols
Requires: libqt5-quickparticles
Requires: libqt5-svg

# Source-url: https://github.com/anilibria/anilibria-winmaclinux/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch: %name-1.2.4-alt-config.patch
Patch1: %name-1.2.4-alt-fix_prefix.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-graphicaleffects
BuildRequires: qt5-svg-devel
BuildRequires: qt5-websockets-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: gstreamer1.0-devel

BuildRequires(pre): rpm-macros-qt5 

%description
Linux\Windows\Mac client for online viewing of cartoons and animated films
from a group of well-known fandabers AniLibria.

%description -l ru_RU.UTF-8
Linux\Windows\Mac клиент для онлайн просмотра мультфильмов и анимационных
фильмов от группы известных фандаберов AniLibria.

%prep
%setup
%autopatch -p1

%build
pushd src
%qmake_qt5 CONFIG+=debug
%make_build
popd

%install
pushd src
INSTALL_ROOT=%buildroot %makeinstall_std
mv %buildroot%_desktopdir/anilibria.desktop %buildroot%_desktopdir/tv.anilibria.AniLibria.desktop
popd

%files
%doc *.md
%_bindir/AniLibria
%_desktopdir/tv.anilibria.AniLibria.desktop
%_iconsdir/hicolor/*/apps/anilibria.png

%changelog
* Thu Nov 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.2.11-alt2
- NMU: removed qt5-webengine from (build) requirements since this package
  does not use webengine/webview (see src/AniLibria.pro and dependencies
  of the binary package). Build on more architectures (including LoongArch).

* Tue Nov 28 2023 Roman Alifanov <ximper@altlinux.org> 1.2.11-alt1
- new version 1.2.11 (with rpmrb script) (ALT Bug 48603)

* Mon Oct 02 2023 Roman Alifanov <ximper@altlinux.org> 1.2.10-alt1
- new version 1.2.10 (with rpmrb script)

* Wed Aug 30 2023 Roman Alifanov <ximper@altlinux.org> 1.2.9-alt1
- new version (1.2.9) with rpmgs script
- rename anilibria.desktop to tv.anilibria.AniLibria.desktop for wayland support

* Fri Aug 04 2023 Roman Alifanov <ximper@altlinux.org> 1.2.8-alt1
- new version (1.2.8) with rpmgs script (ALT Bug #45956)

* Wed Apr 19 2023 Evgeny Chuck <koi@altlinux.org> 1.2.5-alt1
- new version (1.2.5) with rpmgs script (Closes: 45781)

* Wed Feb 08 2023 Evgeny Chuck <koi@altlinux.org> 1.2.4-alt1
- new version (1.2.4) with rpmgs script

* Fri Dec 16 2022 Evgeny Chuck <koi@altlinux.org> 1.2.3-alt1
- new version (1.2.3) with rpmgs script

* Thu Dec 15 2022 Evgeny Chuck <koi@altlinux.org> 1.2.2-alt2
- Fixed a crash when clicking on the random release button (Closes: 44597)
- Fixed bug in index values on page Theme Editor
- Added QuickParticles to support the snow effect in the application window

* Sun Nov 27 2022 Evgeny Chuck <koi@altlinux.org> 1.2.2-alt1
- new version (1.2.2) with rpmgs script

* Mon Nov 07 2022 Evgeny Chuck <koi@altlinux.org> 1.2.1-alt3
- Fixed saving window size when exiting full screen mode

* Sat Nov 05 2022 Evgeny Chuck <koi@altlinux.org> 1.2.1-alt2
- Fix window right alignment (Closes: 44087)

* Fri Nov 04 2022 Evgeny Chuck <koi@altlinux.org> 1.2.1-alt1
- new version (1.2.1) with rpmgs scrip
- Remove unused toggle from settings menu (Closes: 44086)

* Thu Nov 03 2022 Evgeny Chuck <koi@altlinux.org> 1.2.0-alt2
- Fixed application minimization from full window mode (Closes: 44088)
- Fixed transition to standby mode when playing a video

* Sun Oct 09 2022 Evgeny Chuck <koi@altlinux.org> 1.2.0-alt1
- new version (1.2.0) with rpmgs script
- create debug package

* Sat Sep 10 2022 Evgeny Chuck <koi@altlinux.org> 1.1.12-alt1
- new version (1.1.12) with rpmgs script

* Fri Aug 19 2022 Evgeny Chuck <koi@altlinux.org> 1.1.11-alt1
- new version (1.1.11) with rpmgs script
- Changed the description of the "Summary" tag to be more accurate

* Mon Aug 15 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt3
- Added dependencies that fix errors when running the QML interface

* Mon Aug 01 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt2
- Added dependency libqt5-multimedia to fix media playback

* Mon Jul 25 2022 Evgeny Chuck <koi@altlinux.org> 1.1.10-alt1
- new version (1.1.10) with rpmgs script

* Sat Jun 18 2022 Evgeny Chuck <koi@altlinux.org> 1.1.9-alt1
- initial build for ALT Linux Sisyphus
