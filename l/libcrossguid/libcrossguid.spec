Name: libcrossguid
Version: 20150803
Release: alt1

Summary: C++ GUID library
License: MIT
Group: System/Libraries

Source: %name-%version.tar

BuildRequires: gcc-c++ libuuid-devel

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.

%package devel
Summary: C++ GUID library
Group: Development/C++

%description devel
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.
This package contains development part of %name

%prep
%setup

%build
c++ -shared %optflags %optflags_shared -std=c++11 -Wl,-soname,libcrossguid.so.0 \
	-DGUID_LIBUUID -I/usr/include/uuid  guid.cpp -o libcrossguid.so.0.0.0 -luuid

%install
install -pm0644 -D guid.h %buildroot%_includedir/guid.h
install -pm0644 -D libcrossguid.so.0.0.0 %buildroot%_libdir/libcrossguid.so.0.0.0
ln -s libcrossguid.so.0.0.0 %buildroot%_libdir/libcrossguid.so

%files
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/guid.h

%changelog
* Tue Mar 08 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 20150803-alt1
- initial
