%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qmltermwidget

Name: qt5-qmltermwidget
Version: 0.2.0
Release: alt1

Group: System/Libraries
Summary: A port of QTermWidget to QML
Url: http://qt.io/
License: GPL-2.0-or-later

Source: %qt_module-%version.tar
# FC
Patch1: qtw-0.2.0--fix-missing-includes.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-tools

%description
This project is a QML port of QTermWidget. It is written
to be as close as possible to the upstream project in order
to make cooperation possible.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel rpm-build-qml
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-qmltermwidget
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
Requires: libqt5-core = %_qt5_version
%description -n libqt5-qmltermwidget
%summary

%prep
%setup -n %qt_module-%version
%patch1 -p1

%build
%qmake_qt5
%make_build

%install
%installqt5

%files common

%files
%_qt5_qmldir/QMLTermWidget/


%changelog
* Fri Jun 11 2021 Sergey V Turchin <zerg@altlinux.org> 0.2.0-alt1
- initial build
