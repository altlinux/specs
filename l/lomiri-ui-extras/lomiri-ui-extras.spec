%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-ui-extras
Version: 0.8.2
Release: alt1

Summary: Lomiri UI Extra Components (Qt5)
License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-ui-extras

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(cups)
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(pam)

%if_with check
BuildRequires: ctest
BuildRequires: /usr/bin/xvfb-run
BuildRequires: lomiri-ui-toolkit
%endif

# qt5/qml/QtQml/Models.2/qmldir
Requires: libqt5-qml
# qt5/qml/QtQuick/Window.2/qmldir, qt5/qml/QtQuick.2/qmldir
Requires: libqt5-quick

%description
A collection of UI components that for various reasons can't be included
in the main Lomiri UI toolkit - mostly because of the level of quality,
lack of documentation and/or lack of automated tests.

This package contains the Qt5 QML module.

%prep
%setup

%build
%cmake \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
%if_with check
       -DQMLTESTRUNNER_BIN=%_qt5_bindir/qmltestrunner \
       -DENABLE_TESTS=ON
%else
       -DENABLE_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%dir %_qt5_qmldir/Lomiri/Components/Extras
%_qt5_qmldir/Lomiri/Components/Extras/*
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-ui-extras.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-ui-extras.mo

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Sun Apr 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.8.1-alt1
- New version 0.8.1.

* Thu Dec 04 2025 Nikolay Strelkov <snk@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus
