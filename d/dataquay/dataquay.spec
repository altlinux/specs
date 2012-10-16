Name: dataquay
Version: 0.9
Release: alt1
Summary: A free open source library that provides a friendly C++ API for an RDF data store using Qt4 classes and containers
License: BSD-style
Group: Development/C++
Url: http://breakfastquay.com/dataquay/

Source: %name-%version.tar
Patch0: no-tests.patch
Patch1: fix-installpath.patch
Patch2: fix-linking.patch

BuildRequires: libredland-devel
BuildRequires: raptor2-devel
BuildRequires: pkgconfig(QtCore)
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
%patch0 -p2
%patch1 -p2
%patch2 -p2

%build
cp deploy/%name.pc.in deploy/%name.pc
PATH=$PATH:%_qt4dir/bin qmake \
	PREFIX=/usr \
	target.path=%_libdir \
	pkgconfig.path=%_libdir/pkgconfig \
	dataquay.pro
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%_libdir/*.so.*
%doc README.txt

%files devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Oct 15 2012 Paul Wolneykien <manowar@altlinux.ru> 0.9-alt1
- Initial release for ALT Linux.
