%define _stripped_files_terminate_build 1
%def_disable testing

%define rname audex

Name: %rname
Version: 26.04.2
Release: alt2
%K6init

Summary: Tool for ripping compact discs
License: GPL-2.0-or-later
Group: Graphical desktop/KDE
Url: https://invent.kde.org/multimedia/audex

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules
BuildRequires: pkgconfig(Qt6) pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(libcdio) pkgconfig(libcdio_cdda)
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kcrash-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kcmutils-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-ktextwidgets-devel
BuildRequires: kde6-libkcddb-devel

%if_enabled testing
BuildRequires: ctest
BuildRequires: icon-theme-breeze
BuildRequires: xauth
BuildRequires: xvfb-run
%endif

Requires: plasma6-breeze
Requires: icon-theme-breeze

%description
Audex is a CD ripper application. It lets you extract the audio from your
CDs to let you listen to them on your computer and your other devices.
It includes CDDB and MusicBrainz integrations to fetch the metadata and
covers for your CDs if available.

%prep
%setup -n %rname-%version

%build
%K6build \
%if_enabled testing
   -DBUILD_TESTING=ON \
%else
   -DBUILD_TESTING=OFF \
%endif
    #

%install
%K6install

%find_lang %name --with-kde --all-name --with-man

%check
%if_enabled testing
xvfb-run -a --server-args="-screen 0 1024x768x24+32" %ctest -j1 -VV
%endif

%files -f %{name}.lang
%doc README.md
%_K6bin/audex
%_K6xdgapp/*audex*.desktop
%_K6data/audex/
%_K6icon/hicolor/*/apps/*audex*
%_K6data/metainfo/*audex*.xml
%_K6data/solid/actions/*audex*.desktop

%changelog
* Mon Jun 15 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt2
- update packaging

* Fri Jun 05 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.2-alt1
- New version 26.04.2.

* Thu May 07 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.1-alt1
- New version 26.04.1.

* Fri Apr 17 2026 Nikolay Strelkov <snk@altlinux.org> 26.04.0-alt1
- New version 26.04.0.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.3-alt1
- New version 25.12.3.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 25.12.2-alt1
- Initial build of kf6-based Audex for Sisyphus
