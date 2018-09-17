# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global so_ver 2.0.0

Name: qcustomplot
Version: 2.0.1
Release: alt1
Summary: Qt widget for plotting and data visualization

License: GPLv3+
Group: Development/C++
Url: http://www.qcustomplot.com/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# http://www.qcustomplot.com/release/%version/QCustomPlot.tar.gz
Source1: %name.pro

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

%package qt5
Summary: Qt widget for plotting and data visualization
Group: Development/C++
Requires: %name-qt5 = %EVR

%description qt5
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication quality 2D
plots, graphs and charts, as well as offering high performance for realtime
visualization applications.

This package contains the Qt5 version.

%package qt5-devel
Summary: Development files for %name (Qt5)
Group: Development/C++
Requires: %name-qt5 = %EVR

%description qt5-devel
The %name-devel package contains libraries and header files for
developing applications that use %name (Qt5).

%package doc
Summary: Documentation and examples for %name
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains the documentation and examples for
%name.

%prep
%setup
cp -a %SOURCE1 .

%build
LDFLAGS="%optflags -Wl,--as-needed" %qmake_qt5 SOVERSION=%so_ver QTSUFFIX=-qt5 LIBDIR=%_libdir .
%make_build

%install
make INSTALL_ROOT=%buildroot install

# pkg-config file
install -d %buildroot%_pkgconfigdir/
cat > %buildroot%_pkgconfigdir/%name-qt5.pc <<EOF
libdir=%_libdir
includedir=%_includedir

Name: %name-qt5
Description: %summary
Version: %version
Cflags: -I\${includedir}
Libs: -L\${libdir} -lqcustomplot-qt5
EOF

%files qt5
%doc changelog.txt GPL.txt
%_libdir/libqcustomplot-qt5.so.*

%files qt5-devel
%_includedir/qcustomplot.h
%_libdir/libqcustomplot-qt5.so
%_pkgconfigdir/%name-qt5.pc

%files doc
%doc documentation examples

%changelog
* Mon Sep 17 2018 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build for ALT Sisyphus
