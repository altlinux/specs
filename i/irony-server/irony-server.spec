Name: irony-server
Version: 1.5.0
Release: alt1

Summary: Clang-based irony-mode companion server
License: GPLv3
Group: Development/C
Url: https://github.com/Sarcasm/irony-mode

Source: %name-%version-%release.tar

BuildRequires: cmake
BuildRequires: clang12.0 clang12.0-devel clang12.0-devel-static clang12.0-tools clangd12.0
BuildRequires: llvm12.0-devel llvm12.0-devel-static
BuildRequires: libstdc++-devel zlib-devel

%description
irony-server provides the libclang interface to irony-mode.
It uses a simple protocol based on S-expression.

%prep
%setup

%build
%define optflags_lto %nil
export CC=clang
export CXX=clang++
%cmake -S server
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md
%_bindir/irony-server

%changelog
* Thu Dec 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- initial
