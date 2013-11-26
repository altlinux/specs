%global qt_module qtquickcontrols

Name: qt5-quickcontrols
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - module with set of QtQuick controls
License: LGPLv2 / GPLv3
Url: http://qt-project.org/

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Tue Nov 26 2013 (-bi)
# optimized out: elfutils libGL-devel libqt5-clucene libqt5-core libqt5-gui libqt5-help libqt5-network libqt5-qml libqt5-quick libqt5-sql libqt5-v8 libqt5-widgets libqt5-xml libstdc++-devel python-base python3 python3-base qt5-base-devel qt5-declarative-devel qt5-tools ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static python-module-distribute qt5-jsbackend-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-gir rpm-build-python3 rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel
BuildRequires: qt5-jsbackend-devel qt5-script-devel qt5-declarative-devel qt5-tools

%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common qt5-declarative-common
%description common
Common package for %name

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%prep
%setup -qn %qt_module-opensource-src-%version
#syncqt.pl-qt5 \
#    -version %version \
#    -private \
#    -module QtQuickControls \
#    #

%build
%qmake_qt5
%make_build
%make docs

%install
%install_qt5
%make INSTALL_ROOT=%buildroot install_docs ||:

%files common
%files
%_qt5_archdatadir/qml/QtQuick/
%doc LGPL_EXCEPTION.txt header.BSD

%files doc
%_qt5_docdir/qtquick*.qch
%_qt5_docdir/qtquick*s/

%changelog
* Tue Nov 26 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
