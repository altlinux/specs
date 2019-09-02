%define _unpackaged_files_terminate_build 1

%define oname double-conversion

Name: lib%oname
Version: 3.0.0
Release: alt4

Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles
License: BSD
Group: System/Libraries

Url: https://github.com/floitsch/double-conversion
Source: %name-%version.tar

BuildRequires: cmake ctest
BuildRequires: gcc-c++

%description
Provides binary-decimal and decimal-binary routines for IEEE doubles.
The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been re-factored
and improved so that it can be used more easily in other projects.

%package devel
Summary: Library providing binary-decimal and decimal-binary routines for IEEE doubles
Group: Development/C
Requires: %name = %EVR

%description devel
Contains header files for developing applications that use the %name
library.

%prep
%setup
%ifarch %e2k
sed -i 's,defined(__riscv),& || defined(__e2k__),' double-conversion/utils.h
%endif

%build
%cmake_insource \
        -DBUILD_SHARED_LIBS=ON \
        -DBUILD_STATIC_LIBS=OFF \
        -DBUILD_TESTING:BOOL=ON

%make_build

%install
%makeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build test

%files
%doc LICENSE README.md AUTHORS Changelog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/cmake/%oname
%_includedir/%oname

%changelog
* Mon Sep 02 2019 Michael Shigorin <mike@altlinux.org> 3.0.0-alt4
- Added e2k support (patch suggested upstream)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2
- NMU: remove %ubt from release

* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1%ubt
- Updated to upstream version 3.0.0.

* Mon Feb 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- Initial build
- master snapshot d8d4e668ee1e6e10b728f0671a89b07d7c4d45be
