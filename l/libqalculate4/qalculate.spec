%def_without static

Name: libqalculate4
Version: 0.9.6
Release: alt3.1

Summary: libqalculate compat libraries
Group: System/Libraries
License: GPL
Url: http://qalculate.sourceforge.net

Source: libqalculate-%version.tar
Patch1: libqalculate-gcc43-cln1.2.2.alt.patch
Packager: Alexey Morsov <swi@altlinux.ru>

BuildRequires: libcln-devel gcc4.3-c++ glib2-devel libg2c-devel libgmp-devel libstdc++-devel perl-XML-Parser pkgconfig zlib-devel intltool libtool_1.5 libxml2-devel

%description
Qalculate libraries.

%package -n %name-devel
Summary: libqalculate compat development package
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
The libqalculate package contains the header files needed for developing
applications that use libqalculate. Install libqalculate-devel if
you want to develop applications using libqalculate.

%if_enabled static
%package -n %name-devel-static
Summary: libqalculate static library
Group: Development/C
Requires: %name-devel = %version-%release

%description -n %name-devel-static
This package contains static version of libqalculate. Install
libqalculate-devel-static if you want to develop applications statically linked
with libqalculate.
%endif

%prep
%setup -q -n libqalculate-%version
%patch1 -p1

%build
%autoreconf

%configure --enable-shared --disable-textport

%make_build

%install
%make_install DESTDIR=%buildroot install

# remove non-packaged files
%__rm -f %buildroot%_libdir/*.la
%if_without static
%__rm -f %buildroot%_libdir/*.a
%endif

%files
%_libdir/*.so.*

%files -n %name-devel
%_includedir/libqalculate
%_libdir/*.so
%_libdir/pkgconfig/*

%if_with static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Dec 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt3.1
- Rebuilt with libcln6

* Thu Apr 22 2010 Nick S. Grechukh <gns@altlinux.ru> 0.9.6-alt3
- compat library

* Sat Feb 07 2009 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt2.2
- fix patch

* Fri Nov 07 2008 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt2.1
- rebuild with libcln 1.2.2
- fix spec
  + remove deprecated cal in post/postun

* Thu Nov 06 2008 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt2
- fix build with gcc4.3

* Mon Jun 18 2007 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1
- 0.9.6 release
- put api documentation in -devel package

* Tue Dec 19 2006 Alexey Morsov <swi@altlinux.ru> 0.9.5-alt1
- 0.9.5 release.

* Sat Jan 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9.2-alt1
- 0.9.2 release.

* Mon Dec 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.9.0-alt1
- 0.9.0 release.

* Fri Oct 07 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1.2-alt1
- Upstream bugfix release.

* Tue Oct 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1.1-alt2
- Fixed lt error.

* Sat Aug 27 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.8.1.1-alt1
- Initial build.

