Name: pgtcl
Version: 1.6.2
Release: alt3
Summary: Postgresql binding tcl lib
Group: Development/Tcl
License: BSD-like
Url: http://pgfoundry.org/projects/pgtclng/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name.tar

# Automatically added by buildreq on Mon Mar 12 2007
BuildRequires: postgresql-devel tcl-devel

%description
Library for access PostgreSQL database from Tcl

%prep
%setup -q -c

%build
%autoreconf -fisv
%configure
%make

%install
%makeinstall pkglibdir=%buildroot%_libdir/tcl
mkdir -p %buildroot%_datadir/tcl/pgtcl
mv %buildroot%_libdir/tcl/pkgIndex.tcl %buildroot%_datadir/tcl/pgtcl/
sed -i 's:\<lib\>:%_lib:g' %buildroot%_datadir/tcl/pgtcl/pkgIndex.tcl

%files
%_includedir/*.h
%_libdir/tcl/*.so
%_datadir/tcl/pgtcl

%changelog
* Mon Jan 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt3
- fix build

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt2
- rebuild

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.6.2-alt1
- update to 1.6.2
- cleanup spec

* Mon Apr 16 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt3
- fix x86_64 build (thanks to at@)

* Mon Mar 12 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt2
- fix x86_64 build

* Mon Mar 12 2007 Denis Smirnov <mithraen@altlinux.ru> 1.6-alt1
- first build for Sisyphus
