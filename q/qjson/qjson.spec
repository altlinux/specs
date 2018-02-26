Name: qjson
Version: 0.7.1
Release: alt2

Group: System/Libraries
Summary: Lightweight data-interchange format
Url: http://qjson.sourceforge.net
License: GPLv2+

Source: http://sourceforge.net/projects/qjson/files/%name/%version/%name-%version.tar.bz2
Packager: Sergey V Turchin <zerg@altlinux.org>

BuildRequires: kde-common-devel cmake gcc-c++ libqt4-devel

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances,
while JSON objects will be mapped to QVariantMap.

%package -n lib%name
Summary: Lightweight data-interchange format library
Group: System/Libraries
%description -n lib%name
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represents integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects: JSON arrays will be mapped to QVariantList instances,
while JSON objects will be mapped to QVariantMap.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%name = %version-%release
%description devel
Development files for %name


%prep
%setup -q


%build
%Kcmake \
    -DCMAKE_MODULES_INSTALL_DIR=%_datadir/CMake/Modules
%Kmake

%install
%Kinstall


%files -n lib%name
%doc README
%_libdir/lib*.so.*

%files devel
%doc README
%_libdir/lib*.so
%_includedir/%name
%_datadir/CMake/Modules/FindQJSON.cmake
%_pkgconfigdir/*

%changelog
* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt2
- fix to build

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.1
- Rebuilt for soname set-versions

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt0.M51.1
- built for M51

* Mon Aug 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.1-alt1
- initial specfile
