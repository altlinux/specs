Name: libcityhash
Version: 1.0.3
Release: alt1
Summary: A family of hash functions for strings
Group: Development/C++
Source: cityhash-%version.tar.gz
License: MIT
Url: http://code.google.com/p/cityhash/

# Automatically added by buildreq on Sat Jul 23 2011
# optimized out: libstdc++-devel
BuildRequires: gcc-c++

%description
CityHash provides hash functions for strings. The functions mix the
input bits thoroughly but are not suitable for cryptography.

The README contains a good explanation of the various CityHash functions.

%package devel
Group: Development/C++
Summary: Developmen environment for %name
Requires: %name = %version
%description devel
Development environment for %name, %summary

%package devel-static
Group: Development/C++
Summary: Static developmen environment for %name
Requires: %name-devel = %version
%description devel-static
Static development environment for %name, %summary

%prep
%setup -n cityhash-%version

%build
%autoreconf
%configure
%make

%install
%makeinstall

%check
%make check

%files
%doc README NEWS
%_libdir/*.so.*
%exclude %_defaultdocdir/cityhash

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Sat Jul 23 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

