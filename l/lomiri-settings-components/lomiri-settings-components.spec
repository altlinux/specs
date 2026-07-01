%define _unpackaged_files_terminate_build 1

%def_with check

Name: lomiri-settings-components
Version: 1.2.1
Release: alt1

Summary: Lomiri settings components
License: GPL-3.0 and LGPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-settings-components

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: ayatana-cmake-modules
BuildRequires: qt5-declarative-devel

Requires: suru-icon-theme

# qt5/qml/Biometryd/qmldir
Requires: biometryd
# qt5/qml/Lomiri/Components/ListItems/qmldir, qt5/qml/Lomiri/Components/Pickers/qmldir, qt5/qml/Lomiri/Components/Popups/qmldir, qt5/qml/Lomiri/Components/Styles/qmldir, qt5/qml/Lomiri/Components/qmldir
Requires: lomiri-ui-toolkit
# qt5/qml/Lomiri/Thumbnailer.0.1/qmldir
Requires: lomiri-thumbnailer
# qt5/qml/QtQuick/Layouts/qmldir
Requires: libqt5-qml
# qt5/qml/QtQuick.2/qmldir
Requires: libqt5-quick

%if_with check
BuildRequires: ctest
%endif

%description
Lomiri settings components for Lomiri Desktop Environment

This package contains miscellaneous settings-related components such as
fingerprint-related components, connecting to Biometryd, components of
menus used in settings and VPN-related components.

%prep
%setup

%build
%cmake \
       -W no-dev \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
       -Dqmltestrunner_exe=%_qt5_bindir/qmltestrunner \
       -Dqmlscene_exe=%_qt5_bindir/qmlscene

%cmake_build

%install
%cmake_install

%find_lang %name

%check
%ctest -V

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.GPL COPYING.LGPL TODO
%dir %_qt5_qmldir/Lomiri/Settings
%_qt5_qmldir/Lomiri/Settings/*
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-settings-components.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-settings-components.mo

%changelog
* Wed Jul 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- New version 1.2.1.

* Sat Apr 11 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.3-alt1
- New version 1.1.3.

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
