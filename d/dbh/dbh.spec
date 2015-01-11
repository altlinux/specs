Name: dbh
Version: 5.0.16
Release: alt1

Summary: Disk based hash library
License: GPL
Group: Databases
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://dbh.sourceforge.net

Source: libdbh2-%version.tar.gz
Patch0: %name-5.0.13-bigendian.patch

# Automatically added by buildreq on Tue Nov 07 2006
BuildRequires: gcc-c++ glib2-devel

%description
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of
electronic data, such as graphic information. With the multidimensional binary
tree it is possible to mathematically prove that access time to any
particular record is minimized (using the concept of critical points from
calculus), which provides the means to construct optimized databases for
particular applications.

%package -n lib%name
Summary: dbh shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library required for packaging
libdbh-based software.

%package -n lib%name-devel
Summary: Development files for libdbh
Group: Development/C
PreReq: lib%name = %version-%release

%description -n lib%name-devel
This package contains development files required for packaging
libdbh-based software.

%prep
%setup -n lib%{name}2-%version
%patch0 -p1 -b .bigendian

%build
#autoreconf -vifs
export LDFLAGS="$LDFLAGS -lm"
%configure \
	--enable-debug=no \
	--disable-rpath
%make_build

%install
%makeinstall
#mv %buildroot%_pkgconfigdir/%name.pc %buildroot%_pkgconfigdir/%name-1.0.pc

mv $RPM_BUILD_ROOT/usr/share/gtk-doc .
rm -rf $RPM_BUILD_ROOT/usr/share/dbh

%files -n lib%name
%doc AUTHORS COPYING ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%doc examples/*.c examples/Makefile* doc/html gtk-doc
%_libdir/lib*.so
%_libdir/pkgconfig/*
%_includedir/*
#%_mandir/man1/dbh*
%_man3dir/dbh*

%changelog
* Sun Jan 11 2015 Ilya Mashkin <oddity@altlinux.ru> 5.0.16-alt1
- 5.0.16

* Mon Apr 14 2014 Ilya Mashkin <oddity@altlinux.ru> 5.0.15-alt1
- 5.0.15

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.5.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 06 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Sun Jun 19 2005 Andrey Astafiev <andrei@altlinux.ru> 1.0.24-alt2
- Added -lm flag.

* Tue Mar 15 2005 Andrey Astafiev <andrei@altlinux.ru> 1.0.24-alt1
- 1.0.24

* Thu Nov 11 2004 Andrey Astafiev <andrei@altlinux.ru> 1.0.20-alt1
- 1.0.20

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.17-alt3
- *.la files removed.

* Mon Nov 03 2003 Andrey Astafiev <andrei@altlinux.ru> 1.0.17-alt2
- Fixed Buildrequires.

* Fri Oct 31 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Tue Apr 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- First version for AltLinux Team.
