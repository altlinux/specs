# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: minisign
Version: 0.10
Release: alt2
Summary: A dead simple tool to sign files and verify signatures
License: ISC
Group: File tools
Url: https://jedisct1.github.io/minisign/
Vcs: https://github.com/jedisct1/minisign

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: libsodium-devel
BuildRequires: cmake

%description
Minisign is a dead simple tool to sign files and verify signatures.

It is portable, lightweight, and uses the highly secure Ed25519 public-key
signature system.

%prep
%setup

%build
%cmake -DCMAKE_STRIP=0
%cmake_build

%install
%cmake_install

%check
PATH=%_cmake__builddir:$PATH
yes | minisign -G
yes | minisign -Sm README.md
minisign -Vm README.md
! minisign -Vm README.md -P RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3
echo -ne '\0' >> README.md
! minisign -Vm README.md

%files
%doc LICENSE README.md
%_bindir/minisign
%_man1dir/minisign.1*

%changelog
* Sun May 29 2022 Vitaly Chikunov <vt@altlinux.org> 0.10-alt2
- Increment release to override Autoimports.

* Thu May 26 2022 Vitaly Chikunov <vt@altlinux.org> 0.10-alt1
- First import 0.10-6-g4b2df2e (2022-02-20).
