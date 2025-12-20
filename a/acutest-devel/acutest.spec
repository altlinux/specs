# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: acutest-devel
Version: 20240124
Release: alt1
Summary: Simple header-only C/C++ unit testing facility
License: MIT
Group: Development/C
Url: https://github.com/mity/acutest
BuildArch: noarch

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
BuildRequires: gcc-c++
}}

%description
Acutest is C/C++ unit testing facility aiming to be as simple as
possible, not to stand in the developer's way and to minimize any
external dependencies.

To achieve that, the complete implementation resides in a single C header
file, and its core depends only on few standard C library functions.

%prep
%setup

%install
install -Dpm644 include/acutest.h -t %buildroot%_includedir

%check
gcc -I include -o c-example examples/c-example.c
./c-example   | grep -Fx 'FAILED: 4 of 6 unit tests have failed.'
g++ -I include -o cpp-example examples/cpp-example.cc
./cpp-example | grep -Fx 'FAILED: 3 of 4 unit tests have failed.'

%files
%define _customdocdir %_docdir/acutest
%doc LICENSE.md README.md examples/*.c*
%_includedir/acutest.h

%changelog
* Sat Dec 20 2025 Vitaly Chikunov <vt@altlinux.org> 20240124-alt1
- First import 31751b4 (2024-01-24).
