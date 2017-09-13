%define sover 0.12
%define oname hiredis

%def_without devel

%if_with devel
Name: %oname
%else
Name: %oname%sover
%endif
Version: 0.12.1
Release: alt1
Summary: The official C client for Redis

Group: System/Libraries
License: BSD
Url: https://github.com/redis/hiredis

# https://github.com/redis/hiredis.git
Source: %oname-%version.tar
Patch1: hiredis-0.13.3-alt-makefile.patch

BuildRequires: gcc-c++ libevent-devel libev-devel glib2-devel

%description
Hiredis is a minimalistic C client library for the Redis database.

%package -n lib%oname%sover
Summary: The official C client for Redis
License: BSD
Group: System/Libraries

%description -n lib%oname%sover
Hiredis is a minimalistic C client library for the Redis database.

%if_with devel
%package -n lib%oname-devel
Summary: Header files and libraries for hiredis C development
Group: Development/C
Requires: lib%oname%sover = %version-%release

Provides: hiredis-devel = %version-%release
Obsoletes: hiredis-devel

%description -n lib%oname-devel
The %oname-devel package contains the header files and
ibraries to develop applications using a Redis database.
%endif

%prep
%setup -n %oname-%version
%patch1 -p2

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

%files -n lib%oname%sover
%doc COPYING CHANGELOG.md
%_bindir/hiredis-example*
%_bindir/hiredis-test
%_libdir/*.so.*

%if_with devel
%files -n lib%oname-devel
%doc README.md
%_includedir/%oname
%_libdir/*.so
%endif

%changelog
* Wed Sep 13 2017 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20140529
- Version 0.11.0

* Fri May 18 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt2
- rename to libhiredis (closes: #27301)

* Thu Apr 19 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt1
- initial build for ALT Linux

