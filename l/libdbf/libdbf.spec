Name: libdbf
Version: 0.0.1
Release: alt4

Summary: Library for reading dbase files
License: GPL
Group: System/Libraries
Url: http://dbf.berlios.de/

Source0: %name-%version.tar.bz2

Patch0: libdbf-0.0.1-alt-fix-build-endian.patch

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: intltool glib2-devel

%description
This library allows to read dbase files.

%package devel
Summary: Libraries, includes, etc. to develop dbase applications
Group: Development/Databases
Requires: libdbf = %version-%release

%description devel
Libraries, include files, etc you can use to develop dbase applications.

%prep
%setup -q -n %name
%patch0 -p1

%build
%autoreconf
chmod +x configure
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

# clean
rm -f %buildroot%_libdir/%name.a

%find_lang %name

%files -f %name.lang
%doc ChangeLog README
%_libdir/%name.so.*

%files devel
%_libdir/%name.so
%dir %_includedir/%name/
%_includedir/%name/%name.h
%_pkgconfigdir/libdbf.pc

%changelog
* Wed Oct 10 2012 Igor Zubkov <icesik@altlinux.org> 0.0.1-alt4
- rebuilt for debuginfo
- fix FTBFS

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt3
- Rebuilt for soname set-versions

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 0.0.1-alt2
- apply patch from repocop

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 0.0.1-alt1
- build for Sisyphus

