Name: irony-server
Version: 1.6.0
Release: alt1

Summary: Clang-based irony-mode companion server
License: GPLv3
Group: Development/C
Url: https://github.com/Sarcasm/irony-mode

Source: %name-%version-%release.tar

BuildRequires: cmake
BuildRequires: clang-devel llvm-devel
BuildRequires: libstdc++-devel zlib-devel

%description
irony-server provides the libclang interface to irony-mode,
featuring code completion and syntax checking in Emacs.

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
* Fri Sep 29 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Wed May 04 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt3
- unpin clang version

* Wed Apr 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt2
- pin clang-12 for build

* Thu Dec 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- initial
