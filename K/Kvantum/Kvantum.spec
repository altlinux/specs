%def_without clang
%def_disable qt4
%def_enable qt5
%def_with kf6

Name: Kvantum
Version: 1.1.2
Release: alt1

Summary: SVG-based theme engine for Qt6, KDE and LXQt
License: GPL-3.0-or-later
Group: Graphical desktop/Other

Url: https://github.com/tsujan/Kvantum
# Source-url: https://github.com/tsujan/Kvantum/archive/V%%version.tar.gz
Source: %name-%version.tar.gz
Packager: Leontiy Volodin <lvol@altlinux.org>

BuildPreReq: rpm-build-ninja desktop-file-utils rpm-macros-qt6
BuildRequires: cmake qt6-svg-devel qt6-tools-devel

%if_with clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%if_enabled qt4
BuildPreReq: rpm-macros-qt4
BuildRequires: libqt4-devel
%endif

%if_enabled qt5
BuildPreReq: rpm-macros-qt5
BuildRequires: qt5-svg-devel qt5-x11extras-devel kf5-kwindowsystem-devel
Requires: %name-qt5
%endif

%if_with kf6
BuildRequires: kf6-kwindowsystem-devel
%endif

Requires: %name-data %name-qt6

%description
Kvantum is an SVG-based theme engine for Qt6, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme of
Enlightenment. Creation of realistic themes like that for KDE was the first
reason to make Kvantum but it goes far beyond its default theme: you could
make themes with very different looks and feels for it, whether they be
photorealistic or cartoonish, 3D or flat, embellished or minimalistic, or
something in between, and Kvantum will let you control almost every aspect of
Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt6
installation and can be selected and activated by using Kvantum Manager.

%package data
Summary: SVG-based theme engine for Qt6, KDE and LXQt
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Kvantum is an SVG-based theme engine for Qt6, KDE and LXQt, with an emphasis
on elegance, usability and practicality.

This package contains the data needed for Kvantum.

%if_enabled qt4
%package qt4
Summary: Qt4 plugins for %name
Group: Graphical desktop/Other

%description qt4
This packages provides qt4 plugins for %name.
%endif

%if_enabled qt5
%package qt5
Summary: Qt5 plugins for %name
Group: Graphical desktop/Other

%description qt5
This packages provides qt5 plugins for %name.
%endif

%package qt6
Summary: Qt6 plugins for %name
Group: Graphical desktop/Other

%description qt6
This packages provides qt6 plugins for %name.

%prep
%setup

%build
%if_with clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif

%if_enabled qt4
%cmake -B build4 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DENABLE_QT4=ON \
#
cmake --build "build4" -j%__nprocs
%endif

%if_enabled qt5
%cmake -B build5 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DENABLE_QT5=ON \
#
cmake --build "build5" -j%__nprocs
%endif

%cmake -B build6 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_without kf6
 -DWITHOUT_KF=ON \
%endif
#
cmake --build "build6" -j%__nprocs

%install
export DESTDIR="%buildroot"
%if_enabled qt4
cmake --install "build4/style" --verbose
%endif
%if_enabled qt5
cmake --install "build5/style" --verbose
%endif
cmake --install "build6" --verbose

# desktop-file-validate doesn't recognize LXQt
sed -i "s|LXQt|X-LXQt|" %buildroot%_desktopdir/kvantummanager.desktop
desktop-file-validate %buildroot%_desktopdir/kvantummanager.desktop

%find_lang %name --all-name --with-qt

%files
%doc COPYING
%doc ChangeLog NEWS README.md
%_bindir/kvantummanager
%_bindir/kvantumpreview

%files data -f %name.lang
%_datadir/Kvantum
%_desktopdir/kvantummanager.desktop
%dir %_datadir/kvantummanager
%dir %_datadir/kvantummanager/translations
%_datadir/kvantummanager/translations/kvantummanager_zh_Hant.qm
%dir %_datadir/kvantumpreview
%dir %_datadir/kvantumpreview/translations
%_datadir/kvantumpreview/translations/kvantumpreview_zh_Hant.qm
%dir %_datadir/color-schemes
%_datadir/color-schemes/Kv*
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/kvantum.svg

%if_enabled qt4
%files qt4
%_qt4dir/plugins/styles/libkvantum.so
%endif

%if_enabled qt5
%files qt5
%_qt5_plugindir/styles/libkvantum.so
%endif

%files qt6
%_qt6_plugindir/styles/libkvantum.so

%changelog
* Thu Jul 04 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.2-alt1
- New version 1.1.2.
- Built with kf6 support.

* Mon May 13 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- New version 1.1.1.
- Disabled qt4 module (task 272104).

* Thu Mar 21 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt2
- Fixed application startup without qt6 module.

* Tue Mar 19 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- 1.1.0.
- Switched to qt6 by upstream.

* Tue Apr 11 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.10-alt1
- 1.0.10.

* Mon Feb 13 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.9-alt1
- 1.0.9.

* Mon Dec 05 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt1
- 1.0.7.

* Thu Oct 27 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.6-alt1
- 1.0.6.

* Mon Oct 03 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.5-alt1
- 1.0.5.

* Tue Aug 02 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.4-alt1
- 1.0.4.

* Mon Jul 11 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.3-alt1
- 1.0.3.

* Fri May 20 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.2-alt1
- 1.0.2.

* Fri Feb 18 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.1-alt1
- 1.0.1.

* Mon Jan 10 2022 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- 1.0.0.

* Thu Sep 16 2021 Leontiy Volodin <lvol@altlinux.org> 0.20.2-alt1
- 0.20.2.

* Thu Jul 22 2021 Leontiy Volodin <lvol@altlinux.org> 0.20.1-alt1
- 0.20.1.

* Mon May 31 2021 Leontiy Volodin <lvol@altlinux.org> 0.20.0-alt1
- 0.20.0
- NMU: spec: adapted to new cmake macros (altlinux.org/CMakeMigration2021)

* Sat Mar 13 2021 Leontiy Volodin <lvol@altlinux.org> 0.19.0-alt1
- 0.19.0

* Wed Jan 06 2021 Leontiy Volodin <lvol@altlinux.org> 0.18.0-alt1
- 0.18.0

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 0.17.0-alt1
- 0.17.0
- Built with ninja instead make

* Tue Aug 11 2020 Leontiy Volodin <lvol@altlinux.org> 0.16.1-alt1
- 0.16.1

* Thu Jun 25 2020 Leontiy Volodin <lvol@altlinux.org> 0.16.0-alt1
- 0.16.0
- fully translated in russian (thanks Dmitry Astankov)

* Wed May 06 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.3-alt1
- 0.15.3

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.2-alt1
- 0.15.2

* Wed Mar 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.1-alt1
- 0.15.1

* Thu Mar 12 2020 Leontiy Volodin <lvol@altlinux.org> 0.15.0-alt1
- 0.15.0

* Thu Jan 09 2020 Leontiy Volodin <lvol@altlinux.org> 0.14.1-alt1
- 0.14.1

* Mon Dec 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.14.0-alt1
- 0.14.0

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Oct 14 2019 Leontiy Volodin <lvol@altlinux.org> 0.12.1-alt1
- 0.12.1

* Wed Oct 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.12.0-alt1
- 0.12.0

* Tue Jul 30 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.2-alt1
- 0.11.2

* Tue Jul 02 2019 Michael Shigorin <mike@altlinux.org> 0.11.1-alt2
- E2K: explicit -std=c++11
- minor spec cleanup

* Mon May 13 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Mar 25 2019 Leontiy Volodin <lvol@altlinux.org> 0.11.0-alt1
- New release 0.11.0

* Wed Feb 06 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt3
- 0.10.9 (final release)

* Fri Jan 11 2019 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt2.gitefca972
- Update from git (commit: efca972)
- Fixed post-install files

* Thu Nov 08 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.9-alt1
- New release 0.10.9
- Changed spec for update from git

* Wed Nov 07 2018 Leontiy Volodin <lvol@altlinux.org> 0.10.8-alt1
- Initial release for Sisyphus

