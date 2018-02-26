Name: hiredis
Version: 0.10.1
Release: alt2
Summary: The official C client for Redis

Group: System/Libraries
License: BSD
Url: https://github.com/antirez/hiredis
Packager: Anatoly Lyutin <vostok@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ 

%description
Hiredis is a minimalistic C client library for the Redis database.

%package -n lib%name
Summary: The official C client for Redis
License: BSD
Group: System/Libraries

Provides: hiredis = %version-%release
Obsoletes: hiredis

%description -n lib%name
Hiredis is a minimalistic C client library for the Redis database.

%package -n lib%name-devel
Summary: Header files and libraries for hiredis C development
Group: Development/C
Requires: lib%name = %version-%release

Provides: hiredis-devel = %version-%release
Obsoletes: hiredis-devel

%description -n lib%name-devel
The %name-devel package contains the header files and
ibraries to develop applications using a Redis database.

%prep
%setup

%build
%make_build

%install
%make install PREFIX=%buildroot%_prefix  LIBRARY_PATH=%_lib

mkdir -p %buildroot%_bindir/
cp hiredis-example %buildroot%_bindir/
cp hiredis-test %buildroot%_bindir/

%files -n lib%name
%doc COPYING CHANGELOG.md
%_bindir/hiredis-example
%_bindir/hiredis-test
%_libdir/*.so.*

%files -n lib%name-devel
%doc README.md
%_includedir/%name
%_libdir/*.so

%changelog
* Fri May 18 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt2
- rename to libhiredis (closes: #27301)

* Thu Apr 19 2012 Anatoly Lyutin <vostok@altlinux.org> 0.10.1-alt1
- initial build for ALT Linux

