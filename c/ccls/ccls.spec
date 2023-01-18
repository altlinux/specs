Name: ccls
Version: 0.20220729
Release: alt2

Summary: C/C++/Objective-C language server
License: Apache-2.0
Group: Development/C
Url: https://github.com/MaskRay/ccls

Source: %name-%version-%release.tar

%define _llvm_version 13.0

BuildRequires: cmake libstdc++-devel zlib-devel
BuildRequires: pkgconfig(RapidJSON)
BuildRequires: clang%_llvm_version-devel
BuildRequires: llvm%_llvm_version-devel

%description
%summary

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang
export CXX=clang++
export ALTWRAP_LLVM_VERSION=%_llvm_version
%cmake -DCCLS_VERSION=%version-%release
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE README.md
%_bindir/ccls

%changelog
* Wed Jan 18 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20220729-alt2
- 0.20220729-4-g8bc39595

* Wed Aug 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20220729-alt1
- 0.20220729 released

* Thu May 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20210330-alt1
- initial
