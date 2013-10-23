
%define qt_module qtjsbackend

Name: qt5-jsbackend
Version: 5.1.1
Release: alt1

Group: System/Libraries
Summary: Qt5 - QtJSBackend component
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Wed Sep 25 2013 (-bi)
# optimized out: elfutils libstdc++-devel pkg-config python-base python-modules python3 python3-base ruby ruby-stdlibs
#BuildRequires: gcc-c++ glibc-devel-static python-module-distribute qt5-base-devel rpm-build-python3 rpm-build-ruby
BuildRequires: gcc-c++ glibc-devel qt5-base-devel python-devel

%description
%summary

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
#Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary

%package -n libqt5-v8
Summary: Qt5 library
Group: System/Libraries
#Requires: %name-common = %EVR
%description -n libqt5-v8
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
syncqt.pl-qt5 \
    -version %version \
    -private \
    -module QtV8

%build
%qmake_qt5
%make_build

%install
%install_qt5


%files -n libqt5-v8
%doc LGPL_EXCEPTION.txt
%_qt5_libdir/libQt5V8.so.*

%files devel
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt5*.so
%_qt5_libdir/libQt5*.prl
%_qt5_archdatadir/mkspecs/modules/*.pri
%_pkgconfigdir/Qt5*.pc

%changelog
* Wed Sep 25 2013 Sergey V Turchin <zerg@altlinux.org> 5.1.1-alt1
- initial build
