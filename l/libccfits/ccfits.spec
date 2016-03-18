%define _name CCfits

Name: libccfits
Version: 2.5
Release: alt1

Summary: A C++ interface for cfitsio
Group: System/Libraries
License: BSD
Url: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits

Source: http://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits/%_name-%version.tar.gz
# fc
Patch: CCfits-2.5-removerpath.patch

BuildRequires: gcc-c++ gcc-fortran libcfitsio-devel

%description
CCfits is an object oriented interface to the cfitsio library. It is
designed to make the capabilities of cfitsio available to programmers
working in C++.
It is written in ANSI C++ and implemented using the C++ Standard Library
with namespaces, exception handling, and member template functions.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
These are the header files and libraries needed to develop a %name
application.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains the full API documentation for %name.

%prep
%setup -c
%setup -DT -n %name-%version/%_name
%patch -p1
rm -rf html/*.pl

%build
%configure --disable-static \
	--with-cfitsio-include=%_includedir/cfitsio
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/doc/%name
cp -R html %buildroot%_datadir/doc/%name/

%files
%_libdir/*.so.*
%doc License.txt

%files devel
%exclude %_bindir/cookbook
%_libdir/*.so
%_pkgconfigdir/%_name.pc
%_includedir/%_name/
%doc CHANGES

%files devel-doc
%_datadir/doc/%name/

%changelog
* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- 2.5

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.4-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Apr 08 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt2
- fixed build with new libcfitsio-3.280-alt1

* Fri Jan 31 2014 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- fc package adapted for Sisyphus

