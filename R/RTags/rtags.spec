Name: RTags
Version: 2.41
Release: alt2

Summary: Cross-reference client/server tool for C/C++
License: GPLv3
Group: Development/Other
Url: https://github.com/Andersbakken/rtags

Source: %name-%version-%release.tar

BuildRequires: cmake libstdc++-devel clang12.0-devel llvm12.0-devel zlib-devel

%description
RTags is a client/server application that indexes C/C++ code and keeps
a persistent file-based database of references, declarations, definitions,
symbolnames etc. There is also limited support for ObjC/ObjC++. It allows
to find symbols by name, including nested class and namespace scope.

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang-12
export CXX=clang++-12
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/rc
%_bindir/rdm
%_bindir/rp
%_man7dir/rc.7*
%_man7dir/rdm.7*

%changelog
* Wed Apr 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.41-alt2
- pin clang-12 for build

* Fri Dec 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.41-alt1
- initial
