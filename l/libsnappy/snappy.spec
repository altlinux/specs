Name: libsnappy
Version: 1.0.5
Release: alt1
Summary: Google fast compression/decompression library
Group: System/Libraries
License: BSD
Url: http://code.google.com/p/snappy/
Source: snappy-%version.tar.gz

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: gcc-c++ libgflags-devel libgtest-devel liblzo2-devel zlib-devel

%description
Snappy is a compression/decompression library. It does not aim for
maximum compression, or compatibility with any other compression
library; instead, it aims for very high speeds and reasonable
compression. For instance, compared to the fastest mode of zlib, Snappy
is an order of magnitude faster for most inputs, but the resulting
compressed files are anywhere from 20%% to 100%% bigger.

%package devel
Summary: Development environment for %name
Group: Development/C++
Requires: %name = %version
%description devel
Development environment for %name

%package devel-static
Summary: Static development environment for %name
Group: Development/C++
%description devel-static
Static development environment for %name

%prep
%setup -n snappy-%version

%build
%configure
%make_build CXXFLAGS="-DNDEBUG -O2"

%install
%makeinstall
rm -rf %buildroot/%_defaultdocdir/snappy

%check
%make check

%files
%doc NEWS README ChangeLog INSTALL
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue Mar 27 2012 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Fri Sep 16 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

