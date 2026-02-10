%def_with check

%global descr Snappy is a compression/decompression library. It does not aim for\
maximum compression, or compatibility with any other compression\
library; instead, it aims for very high speeds and reasonable\
compression. For instance, compared to the fastest mode of zlib, Snappy\
is an order of magnitude faster for most inputs, but the resulting\
compressed files are anywhere from 20 - 100 percent bigger.

%global oname snappy

%global soversion 1

Name: libsnappy
Version: 1.2.2
Release: alt2

Summary: Google fast compression/decompression library
Group: System/Libraries
License: BSD
Url: https://google.github.io/snappy/
Vcs: https://github.com/google/snappy.git

Source0: %name-%version.tar
Source1: %oname.pc
Patch: fix-libsnappy-FEDORA-snappy-thirdparty-cmake.patch

BuildRequires(Pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgflags-devel
BuildRequires: libgtest-devel
BuildRequires: liblzo2-devel
BuildRequires: zlib-devel

%if_with check
BuildRequires: ctest
%endif

%description
%descr

%package -n %name%soversion
Summary: %summary
Group: System/Libraries
Obsoletes: libsnappy < %EVR

%description -n %name%soversion
%descr

%package devel
Summary: Development environment for %name
Group: Development/C++
Requires: %name%soversion

%description devel
Development environment for %name.
%descr

%prep
%setup
%autopatch -p1
cp %SOURCE1 %oname.pc
sed -i -e 's|@prefix@|%prefix|g' \
	-e 's|@_exec_prefix@|%_exec_prefix|g' \
	-e 's|@_includedir@|%_includedir|g' \
	-e 's|@_libdir@|%_libdir|g' \
	-e 's|@version@|%version|g' %oname.pc

%build
%cmake -DCMAKE_CXX_STANDARD=17 -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
install -Dpm 0644 %oname.pc %buildroot%_pkgconfigdir/%oname.pc

%check
%ctest

%files -n %name%soversion
%_libdir/%name.so.%{soversion}*

%files devel
%doc NEWS AUTHORS CONTRIBUTING.md README.md
%doc format_description.txt framing_format.txt
%_libdir/%name.so
%_includedir/%{oname}*.h
%_pkgconfigdir/%oname.pc
%_libdir/cmake/Snappy/

%changelog
* Tue Feb 10 2026 Ulysses Apokin <ulysses@altlinux.org> 1.2.2-alt2
- Fixed conflicts with file from package libsnappy-1.1.7 (ALT #57822).

* Fri Feb 06 2026 Ulysses Apokin <ulysses@altlinux.org> 1.2.2-alt1
- New version.
- Corrected as per shared libs policy.

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
