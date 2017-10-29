%define sover 0.12

%def_without devel

%if_with devel
Name: hiredis
%else
Name: hiredis%sover
%endif
Version: 0.12.1
Release: alt2
Summary: The official C client for Redis

Group: System/Libraries
License: BSD
Url: https://github.com/redis/hiredis

# https://github.com/redis/hiredis.git
Source: hiredis-%version.tar
Patch1: hiredis-0.13.3-alt-makefile.patch

BuildRequires: gcc-c++ libevent-devel libev-devel glib2-devel

%description
Hiredis is a minimalistic C client library for the Redis database.

%package -n libhiredis%sover
Summary: The official C client for Redis
License: BSD
Group: System/Libraries

%description -n libhiredis%sover
Hiredis is a minimalistic C client library for the Redis database.

%if_with devel
%package -n libhiredis-devel
Summary: Header files and libraries for hiredis C development
Group: Development/C
Requires: libhiredis%sover = %version-%release

Provides: hiredis-devel = %version-%release
Obsoletes: hiredis-devel

%description -n libhiredis-devel
The hiredis-devel package contains the header files and
ibraries to develop applications using a Redis database.
%endif

%prep
%setup -n hiredis-%version
%patch1 -p1

%build
%make_build
%make examples
%make hiredis-test

%install
%if %_lib == lib64
LIB_SUFFIX=64
%endif
%make install PREFIX=%buildroot%_prefix  LIBRARY_PATH=%_lib \
	LIB_SUFFIX=$LIB_SUFFIX

mkdir -p %buildroot%_bindir/
cp examples/hiredis-example* %buildroot%_bindir/
cp hiredis-test %buildroot%_bindir/

%files -n libhiredis%sover
%doc COPYING CHANGELOG.md
%_libdir/*.so.%{sover}*

%if_with devel
%files -n libhiredis-devel
%doc README.md
%_bindir/hiredis-example*
%_bindir/hiredis-test
%_includedir/hiredis
%_libdir/*.so
%_libdir/pkgconfig/hiredis.pc
%endif

%changelog
* Sun Oct 29 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.12.1-alt2
- Do not package example and test executables in the compat library package
  (ALT #34016)

* Mon Oct 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.3-alt2
- (ALT #34016) Move example files to devel package

* Tue Sep 19 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Wed Sep 13 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.3-alt1
- Version 0.13.3

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20140529
- Version 0.11.0

* Fri May 18 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt2
- rename to libhiredis (closes: #27301)

* Thu Apr 19 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt1
- initial build for ALT Linux

