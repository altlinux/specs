%define _unpackaged_files_terminate_build 1
%define abiversion 1

Name: libulog_cpp
Version: 1.0.1
Release: alt1

Summary: Streamed C++ ULog reader and writer library
License: MIT
Group: Development/C++
URL: https://github.com/PX4/ulog_cpp
Vcs: https://github.com/PX4/ulog_cpp.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): cmake gcc-c++
BuildRequires(pre): doctest-devel
BuildRequires: /proc

%description
Streamed C++ ULog reader and writer library.

%package -n libulog_cpp-devel
Summary: Development files for ulog_cpp
Group: Development/C++

%description -n libulog_cpp-devel
Headers for ulog_cpp package.

%package -n libulog_cpp%abiversion
Summary: Libraries for ulog_cpp
Group: Development/C++

%description -n libulog_cpp%abiversion
Shared libraries for ulog_cpp.

%prep
%setup

%build
%cmake -Ddoctest_DIR=%_cmakedir/doctest \
       -DBUILD_SHARED_LIBS=ON \
       -DCMAKE_INSTALL_LIBDIR=%_libdir \
       -DCMAKE_INSTALL_INCLUDEDIR=%_includedir \
       #

%cmake_build

%check
%ifarch aarch64
%make -C "aarch64-alt-linux" run-unit-tests
%endif

%ifarch x86_64
%make -C "x86_64-alt-linux" run-unit-tests
%endif

%ifarch i586
%make -C "i586-alt-linux" run-unit-tests
%endif

%install
%cmake_install

%files -n libulog_cpp-devel
%_includedir/ulog_cpp
%_cmakedir/ulog_cpp
%_libdir/libulog_cpp.so

%files -n libulog_cpp%abiversion
%doc README.md
%_libdir/libulog_cpp.so.%abiversion
%_libdir/libulog_cpp.so.%abiversion.0.0

%changelog
* Tue Jan 13 2026 Ilya Muhamadeev <nicourced@altlinux.org> 1.0.1-alt1
- Initial build.
