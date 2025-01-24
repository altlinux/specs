%define _unpackaged_files_terminate_build 1

%define abiversion 2

%define libcpp_base64 libcpp-base64_%abiversion

Name: cpp-base64
Version: 2.rc.08
Release: alt1

Summary: Base64 encoding and decoding with c++
License: Zlib
Group: Text tools
Url: https://github.com/ReneNyffenegger/cpp-base64
VCS: https://github.com/ReneNyffenegger/cpp-base64.git

Source: %name-%version.tar

Patch1: cpp-base64-fork-cmake.patch
Patch2: cpp-base64-alt-cmake.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
%summary.

%package -n %libcpp_base64
Summary: %summary
Group: System/Libraries

%description -n %libcpp_base64
%summary.

%package -n libcpp-base64-devel
Summary: Development package for %name
Group: Development/C++

%description -n libcpp-base64-devel
Files for development with %name.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE

%files -n %libcpp_base64
%doc LICENSE README.md
%_libdir/libcpp-base64.so.*
%_libdir/libcpp-base64.so.%abiversion

%files -n libcpp-base64-devel
%_includedir/cpp-base64/
%_libdir/libcpp-base64.so

%changelog
* Mon Jan 20 2025 Constantin Sunzow <protvin@altlinux.org> 2.rc.08-alt1
- Initial build.
