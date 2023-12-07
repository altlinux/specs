# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ugrep-indexer
Version: 0.9.3
Release: alt1
Summary: A monotonic indexer to speed up grepping
License: BSD-3-Clause
Group: File tools
Url: https://github.com/Genivia/ugrep-indexer
Requires: ugrep >= 3.12.5

Source: %name-%version.tar
BuildRequires: bzlib-devel
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: libpcre2-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: ugrep
}}

%description
The ugrep-indexer utility recursively indexes files to speed up recursive
grepping.

Note: this is a 0.9 beta version of a new generation of "monotonic indexers".
This release is subject to change and improvements based on experiments and
user feedback. Regardless, this implementation has been extensively tested for
correctness. Additional features and performance improvements are planned.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
bin/ugrep-indexer -I -v
ugrep -r -I -l 'std::chrono' --stats
ugrep -r -I -l 'std::chrono' --stats --index
bin/ugrep-indexer -d

%files
%doc LICENSE.txt README.md
%_bindir/ugrep-indexer
%_man1dir/ugrep-indexer.1*

%changelog
* Thu Dec 07 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.3-alt1
- Update to v0.9.3 (2023-12-06).

* Mon Aug 21 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- First import v0.9.1-1-g480cd20 (2023-08-12).
