%define _unpackaged_files_terminate_build 1

%def_without static

Name: qalculate
Version: 2.8.2
Release: alt1

Summary: A very versatile desktop calculator
Group: Office
License: GPL
Url: https://qalculate.github.io/

# https://github.com/Qalculate/libqalculate.git
Source: lib%name-%version.tar

BuildRequires: libcln-devel gcc-c++ glib2-devel libgmp-devel libstdc++-devel perl-XML-Parser pkgconfig zlib-devel intltool libtool libxml2-devel
BuildRequires: libcurl-devel libicu-devel libmpfr-devel doxygen

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux.
It is small and simple to use but with much power and versatility
underneath. Features include customizable functions, units, arbitrary
precision, plotting.

%package -n lib%name
Summary: libqalculate libraries
Group: System/Libraries
Requires: %name-common = %EVR
Requires: /usr/bin/gnuplot

%description -n lib%name
Qalculate libraries.

%package -n lib%name-devel
Summary: libqalculate development package
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
The libqalculate package contains the header files needed for developing
applications that use libqalculate. Install libqalculate-devel if
you want to develop applications using libqalculate.

%if_enabled static
%package -n %libname-devel-static
Summary: libqalculate static library
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
This package contains static version of libqalculate. Install
libqalculate-devel-static if you want to develop applications statically linked
with libqalculate.
%endif

%package common
Summary: qalculate common files
Group: Office

%description common
This package contains common files used by qalculate frontends.

%prep
%setup -q -n lib%name-%version

%build
%autoreconf

%configure \
	--enable-defs2doc

pushd docs/reference
doxygen
popd

%make_build

%install
%makeinstall_std

# remove non-packaged files
rm -f %buildroot%_libdir/*.la
%if_without static
rm -f %buildroot%_libdir/*.a
%endif

%find_lang --output=%name.lang lib%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/lib%name
%_libdir/*.so
%_libdir/pkgconfig/*
%_defaultdocdir/lib%name

%files
%_bindir/*

%files common -f %name.lang
%_datadir/qalculate

%if_with static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Jan 15 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.2-alt1
- Updated to upstream version 2.8.2.

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.1-alt1
- Updated to upstream version 2.6.1.

* Fri May 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.0-alt1
- Updated to upstream version 2.5.0.

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2
- Updated build dependencies.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.

* Sun Nov 08 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt2.2
- Rebuild for gcc5 C++11 ABI
- Package all lolalization files
- Spec cleanup

* Mon Feb 07 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.7-alt2.1
- rebuild

* Wed Feb 02 2011 Alexey Morsov <swi@altlinux.ru> 0.9.7-alt2
- rebuild

* Thu Apr 22 2010 Alexey Morsov <swi@altlinux.ru> 0.9.7-alt1
- new version

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

