%def_enable check

Name: libsignal-protocol-c
Version: 2.3.3
Release: alt1

Summary: Signal Protocol C library
Group: System/Libraries
License: GPL-3.0
Url: https://github.com/signalapp/libsignal-protocol-c

Source: %url/archive/v%version/%name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libssl-devel
%{?_enable_check:BuildRequires: libcheck-devel ctest}

%description
This is a ratcheting forward secrecy protocol that works in synchronous
and asynchronous messaging environments.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
Development files for %name library.

%prep
%setup -n %name-%version

%build
%cmake -DBUILD_SHARED_LIBS=ON \
%{?_enable_check:-DBUILD_TESTING=1}
%nil
%cmake_build

%install
%cmakeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
pushd BUILD/tests
ctest -V
popd

%files
%_libdir/%name.so.*
%doc README.md

%files devel
%_includedir/signal
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Fri Jan 31 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- first build for Sisyphus

