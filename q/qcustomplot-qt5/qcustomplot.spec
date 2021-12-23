# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global so_ver 2.1.0

Name: qcustomplot-qt5
Version: 2.1.0
Release: alt1
Summary: Qt widget for plotting and data visualization

License: GPLv3+
Group: Development/C++
Url: http://www.qcustomplot.com/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: qcustomplot-%version.tar
# Source-url: http://www.qcustomplot.com/release/%{version}fixed/QCustomPlot.tar.gz
Source1: qcustomplot.pro

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt5 version.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation and examples for %name
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains the documentation and examples for
%name.

%prep
%setup -n qcustomplot-%version
cp -a %SOURCE1 .

%build
LDFLAGS="%optflags -Wl,--as-needed" %qmake_qt5 SOVERSION=%so_ver QTSUFFIX=qt5 LIBDIR=%_libdir .
%make_build

%install
make INSTALL_ROOT=%buildroot install

# pkg-config file
mkdir -p %buildroot%_pkgconfigdir
cat > %buildroot%_pkgconfigdir/%name.pc <<EOF
libdir=%_libdir
includedir=%_includedir

Name: %name-qt5
Description: %summary
Version: %version
Cflags: -I\${includedir}\qcustomplot-qt5
Libs: -L\${libdir} -lqcustomplot-qt5
EOF

%files
%doc changelog.txt
%_libdir/libqcustomplot-qt5.so.*

%files devel
%_includedir/qt5/qcustomplot.h
%_libdir/libqcustomplot-qt5.so
%_pkgconfigdir/%name.pc

%files doc
%doc documentation examples

%changelog
* Thu Dec 23 2021 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version (2.1.0) with rpmgs script
- rename srpm to qcustomplot-qt5
- replace header to %_includedir/qt5
- cleanup spec

* Mon Sep 17 2018 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus
