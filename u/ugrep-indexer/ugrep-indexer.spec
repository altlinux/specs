# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ugrep-indexer
Version: 1.0.0
Release: alt1
Summary: A monotonic indexer to speed up grepping
License: BSD-3-Clause
Group: File tools
Url: https://github.com/Genivia/ugrep-indexer
Requires: ugrep >= 3.12.5

%define valgrind_arches %ix86 x86_64

Source: %name-%version.tar
BuildRequires: bzlib-devel
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: libbzip3-devel
BuildRequires: liblz4-devel
BuildRequires: liblzma-devel
BuildRequires: libpcre2-devel
BuildRequires: libzstd-devel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: bzip3
BuildRequires: ugrep
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
The ugrep-indexer utility recursively indexes files to speed up recursive
grepping.

Note: this is a 0.9 beta version of a new generation of "monotonic
indexers". This release is subject to change and improvements based on
experiments and user feedback. Regardless, this implementation has been
extensively tested for correctness.

%prep
%setup

%build
%autoreconf
%configure --with-bzip3
%make_build

%install
%makeinstall_std

%check
# Smoke testing. Upstream does not provide test suite.
%ifarch %valgrind_arches
# Valgrind does not treat --track-fds reports as errors (and they are
# suppressed with -q). Grep logs for 'Open file descriptor'.
%define valgrind valgrind --error-exitcode=2 --track-fds=yes --trace-children=yes --track-origins=yes
%else
%define valgrind %nil
%endif
%valgrind bin/ugrep-indexer -I -v
bzip2 -k README.md
bzip3 -k README.md
gzip -k README.md
xz -k README.md
zstd -k README.md
%valgrind bin/ugrep-indexer -I -v -z | grep -w '5 new files indexed'
ugrep -r -z -I -l 'std::chrono' --stats
ugrep -r -z -I -l 'std::chrono' --stats --index | grep -w '6 matching'
%valgrind bin/ugrep-indexer -d

%files
%doc LICENSE.txt README.md
%_bindir/ugrep-indexer
%_man1dir/ugrep-indexer.1*

%changelog
* Fri Apr 19 2024 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- Update to v1.0.0 (2024-04-18). [Final release, the following releases will be
  in ugrep package.]

* Sat Mar 02 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.6-alt1
- Update to v0.9.6 (2024-02-29).
- spec: Improve smoke testing in %%check.

* Tue Jan 02 2024 Vitaly Chikunov <vt@altlinux.org> 0.9.5-alt1
- Update to v0.9.5 (2023-12-31).

* Thu Dec 07 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.3-alt1
- Update to v0.9.3 (2023-12-06).

* Mon Aug 21 2023 Vitaly Chikunov <vt@altlinux.org> 0.9.1-alt1
- First import v0.9.1-1-g480cd20 (2023-08-12).
