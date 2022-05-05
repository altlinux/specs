Name: ccls
Version: 0.20210330
Release: alt1

Summary: C/C++/Objective-C language server
License: Apache-2.0
Group: Development/C
Url: https://github.com/MaskRay/ccls

Source: %name-%version-%release.tar

BuildRequires: cmake clang-devel libstdc++-devel llvm-devel zlib-devel
BuildRequires: pkgconfig(RapidJSON)

%description
%summary

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang
export CXX=clang++
%cmake -DCCLS_VERSION=%version-%release
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE README.md
%_bindir/ccls

%changelog
* Thu May 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20210330-alt1
- initial
