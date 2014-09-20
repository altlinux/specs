%define oname dataquay
Name: %oname-minefeld
Version: 0.9
Release: alt1.hg20140617
Summary: A free open source library that provides a friendly C++ API for an RDF data store using Qt4 classes and containers
License: BSD-style
Group: Development/C++
Url: http://breakfastquay.com/dataquay/

Source: %name-%version.tar

BuildRequires: libredland-devel
BuildRequires: raptor2-devel
BuildRequires: qt5-base-devel
BuildRequires: gcc-c++

%description
Dataquay is simple to use and easy to integrate. It is principally
intended for use in Qt-based applications that would like to use an
RDF datastore as backing for in-memory project data, to avoid having
to provide application data-specific file formats and to make it easy
to augment the data with descriptive metadata pulled in from external
sources. Dataquay is also intended to be useful for applications whose
primary purpose is not related to RDF but that have ad-hoc RDF needs
for metadata management.

%package devel
Summary: A free open source library that provides a friendly C++ API for an RDF data store using Qt4 classes and containers
Group: Development/C++
Conflicts: %oname-devel

%description devel
Dataquay is simple to use and easy to integrate. It is principally
intended for use in Qt-based applications that would like to use an
RDF datastore as backing for in-memory project data, to avoid having
to provide application data-specific file formats and to make it easy
to augment the data with descriptive metadata pulled in from external
sources. Dataquay is also intended to be useful for applications whose
primary purpose is not related to RDF but that have ad-hoc RDF needs
for metadata management.

This package contains the development files.

%prep
%setup

%build
cp deploy/%oname.pc.in deploy/%oname.pc
PATH=$PATH:%_qt5_bindir qmake \
	PREFIX=/usr \
	LIBDIR=%_libdir \
	target.path=%_libdir \
	pkgconfig.path=%_libdir/pkgconfig \
	QMAKE_CXXFLAGS="%optflags" \
	dataquay.pro
%make_build

%install
sed -i 's|\(^STRIP\)|\1 = echo|' Makefile.lib
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_libdir/*.so.*
%doc README.txt

%files devel
%_includedir/%oname
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Sat Sep 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.hg20140617
- Minefeld

* Mon Oct 15 2012 Paul Wolneykien <manowar@altlinux.ru> 0.9-alt1
- Initial release for ALT Linux.
