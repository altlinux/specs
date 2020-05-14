# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: honggfuzz
Version: 2.2
Release: alt1
Summary: Security oriented software fuzzer
License: Apache-2.0
Group: Development/Tools
URL: https://honggfuzz.dev/
Vcs: https://github.com/google/honggfuzz.git

Source: %name-%version.tar
%define docdir %_docdir/%name-%version

BuildRequires: binutils-devel
BuildRequires: libunwind-devel
BuildRequires: liblzma-devel
%ifarch %ix86 x86_64
BuildRequires: libipt-devel
%endif
BuildRequires: /proc

%description
A security oriented, feedback-driven, evolutionary, easy-to-use fuzzer with
interesting analysis options. Supports evolutionary, feedback-driven fuzzing
based on code coverage (SW and HW based).

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot%docdir
cp -a CHANGELOG COPYING CONTRIBUTING README.md docs/* \
   %buildroot%docdir

%check
PATH=%buildroot/%_bindir:$PATH
honggfuzz --help
honggfuzz -v -i examples/openssl/corpus_client -N 1 --run_time 1 -n 1 -P -- /bin/ls

%files
%_bindir/hfuzz-*
%_bindir/honggfuzz
%_includedir/libhfcommon/
%_includedir/libhfuzz/
%_includedir/libhnetdriver/
%docdir

%changelog
* Thu May 14 2020 Vitaly Chikunov <vt@altlinux.org> 2.2-alt1
- Initial import of 2.2
