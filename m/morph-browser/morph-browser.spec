%define _unpackaged_files_terminate_build 1

%def_with check

Name: morph-browser
Version: 1.99.4
Release: alt1

Summary: Web Browser for Lomiri
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/morph-browser

Source: %name-%version.tar

ExcludeArch: loongarch64 riscv64

# sync with version 1.1.2+dfsg-3 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libapparmor)
BuildRequires: /usr/bin/xvfb-run
BuildRequires: qt5-webengine-devel
BuildRequires: pkgconfig(lomiri-action-qt-1)

%if_with check
BuildRequires: ctest
BuildRequires: python3(flake8)
BuildRequires: lomiri-ui-toolkit
BuildRequires: /proc
%endif

Requires: fonts-ttf-liberation
Requires: lomiri-ui-toolkit
Requires: lomiri-ui-extras
Requires: lomiri-content-hub
Requires: libqt5-qml
Requires: libqt5-quick
Requires: qt5-quickcontrols2
Requires: libqt5-qtsystems
Requires: libqt5-webengine
Requires: liblomiri-action-api-qt5

%description
Lightweight web browser tailored for Lomiri, based on the Qt WebEngine
and using the Lomiri UI components.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=off \
       -DCMAKE_INSTALL_PREFIX=%_prefix \
       -DCMAKE_INSTALL_LIBDIR=%_lib \
%if_with check
       -DBUILD_TESTING=on
%else
       -DBUILD_TESTING=off
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%check
%ctest -j1 -VV -E tst_QmlTests

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/morph-browser
%_bindir/morph-webapp-container
%_bindir/morph-webapp-container-hook
%_desktopdir/morph-browser.desktop
%dir %_datadir/morph-browser
%_datadir/morph-browser/*
%dir %_qt5_qmldir/Morph
%dir %_qt5_qmldir/Morph/Web
%_qt5_qmldir/Morph/Web/*
%_datadir/lomiri-content-hub/peers/morph-browser
%_datadir/lomiri-url-dispatcher/urls/morph-browser.url-dispatcher

%exclude %_datadir/click/hooks/morph-webapp-container.hook
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/morph-browser.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/morph-browser.mo

%changelog
* Thu Apr 09 2026 Nikolay Strelkov <snk@altlinux.org> 1.99.4-alt1
- New version 1.99.4.

* Thu Feb 05 2026 Nikolay Strelkov <snk@altlinux.org> 1.99.3-alt1
- New version 1.99.3.

* Fri Jan 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.99.2-alt2
- Exclude loongarch64 and riscv64 arches as not buildable.

* Fri Dec 26 2025 Nikolay Strelkov <snk@altlinux.org> 1.99.2-alt1
- New version 1.99.2.

* Sat Dec 20 2025 Nikolay Strelkov <snk@altlinux.org> 1.99.1-alt1
- New version 1.99.1.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
