%define qdoc_found %{expand:%%(if [ -e %_qt5_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtfeedback

Name:    qt5-feedback
Version: 5.0.0
Release: alt1

Group: System/Libraries
Summary: Qt5 - tactile and audio feedback
# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Url:     http://www.qt.io

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): qt5-tools
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-xmlpatterns-devel qt5-multimedia-devel

%description
The C++ Feedback API enables a client to control and provide tactile and
audio feedback to the user.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt5-base-common
BuildArch: noarch
%description common
Common package for %name

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
#Requires: %name = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package doc
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-feedback
Group: System/Libraries
Summary: Qt5 - library
Requires: %name-common = %EVR
#Requires: libqt5-core = %_qt5_version
%description -n libqt5-feedback
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

sed -i 's|^MODULE_VERSION.*|MODULE_VERSION = %version|' .qmake.conf

%build
syncqt.pl-qt5 -version %version
%qmake_qt5
%make_build
sed -i '/_populate_Feedback_plugin_properties/d' lib*/cmake/Qt5Feedback/Qt5Feedback_.cmake
%if %qdoc_found
%make docs
%endif

%install
%install_qt5
%if %qdoc_found
%make INSTALL_ROOT=%buildroot install_docs ||:
%endif

# remove libtool files
rm -fr %buildroot%_qt5_libdir/*.la


%files common

%files
%doc LICENSE.*
%_qt5_plugindir/feedback/
%_qt5_qmldir/QtFeedback/

%files -n libqt5-feedback
%_qt5_libdir/libQt5Feedback.so.*

%files devel
%_qt5_headerdir/QtFeedback/
%_qt5_libdir/libQt?F*.prl
%_qt5_libdatadir/libQt?F*.prl
%_qt5_libdir/cmake/Qt5Feedback/
%_qt5_libdir/pkgconfig/Qt?F*.pc
%_qt5_archdatadir/mkspecs/modules/qt_lib_f*.pr*
%_qt5_libdir/libQt*.so
%_qt5_libdatadir/libQt*.so

%files doc
%if %qdoc_found
%_qt5_docdir/*
%endif
#%_qt5_examplesdir/*

%changelog
* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 5.0.0-alt1
- initial build of git-20180329
