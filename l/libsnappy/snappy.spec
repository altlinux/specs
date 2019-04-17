Name: libsnappy
Version: 1.1.7
Release: alt1
Summary: Google fast compression/decompression library
Group: System/Libraries
License: BSD
Url: http://google.github.io/snappy/
Source: snappy-%version.tar.gz
Patch0: FC-gtest.patch
Patch1: FC-version-macros.patch

# Automatically added by buildreq on Wed Apr 17 2019
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 libstdc++-devel python-base sh4
BuildRequires: cmake gcc-c++ libgflags-devel libgtest-devel liblzo2-devel zlib-devel

BuildRequires: ctest

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
%patch0 -p1
%patch1 -p1

%build
%cmake_insource -DBUILD_SHARED_LIBS:BOOL=ON
%make_build CXXFLAGS="-DNDEBUG -O2"

# create pkgconfig file
cat << \EOF >snappy.pc
prefix=%prefix
exec_prefix=%_exec_prefix
includedir=%_includedir
libdir=%_libdir

Name: %name
Description: A fast compression/decompression library
Version: %version
Cflags: -I${includedir}
Libs: -L${libdir} -lsnappy
EOF

%install
%makeinstall DESTDIR=%buildroot
install -D snappy.pc %buildroot%_libdir/pkgconfig/snappy.pc

%check
LD_LIBRARY_PATH=`pwd` ctest -V %_smp_mflags

%files
%doc NEWS AUTHORS CONTRIBUTING.md README.md
%_libdir/*.so.*

%files devel
%doc format_description.txt framing_format.txt
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/snappy.pc
%_libdir/cmake/Snappy/

%changelog
* Wed Apr 17 2019 Fr. Br. George <george@altlinux.ru> 1.1.7-alt1
- Autobuild version bump to 1.1.7
- Fix build, apply Fedora patches

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 1.1.3-alt1
- Autobuild version bump to 1.1.3

* Tue Dec 1 2015 Vladimir Didenko <cow@altlinux.org> 1.1.1-alt2
- Rebuild with gcc5

* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

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
