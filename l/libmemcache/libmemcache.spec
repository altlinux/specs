%def_disable static

Name: libmemcache
Version: 1.4.0.rc2
Release: alt3

Summary: A high performance C API for memcached
License: BSD
Group: System/Libraries
Url: http://people.freebsd.org/~seanc/libmemcache/

Source: %name-%version-%release.tar
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

BuildRequires: check

%description
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system.

%package devel
Summary: Development %name library, its header files and documentation
Group: Development/C
Provides: memcache-devel
Requires: %name = %version-%release

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system.

This package contains the header files and
development library for use in developing applications that use the
%name library.

%description devel-static
libmemcache is the C API for memcached(8), a high-performance,
distributed memory object caching system.

This package contains the static %name library.

%prep
%setup

%build
%configure %{subst_enable static}
%make_build CFLAGS="%optflags_shared"

%install
%makeinstall

%files
%doc ChangeLog INSTALL
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0.rc2-alt3
- Rebuilt for soname set-versions

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0.rc2-alt2
- obsolete by filetriggers macros removed

* Fri Dec 14 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0.rc2-alt1
- second build for ALTLinux

* Sun Oct 30 2005 LAKostis <lakostis at altlinux.ru> 1.4.0.b9-alt1
- first build for ALTLinux.

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3

* Sun Jan 23 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.2-1mdk
- initial Mandrakelinux package
