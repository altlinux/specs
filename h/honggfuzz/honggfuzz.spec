# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: honggfuzz
Version: 2.6
Release: alt1
Summary: Security oriented software fuzzer
License: Apache-2.0
Group: Development/Tools
URL: https://honggfuzz.dev/
Vcs: https://github.com/google/honggfuzz.git

Source: %name-%version.tar
%define docdir %_docdir/%name-%version

BuildRequires: binutils-devel
BuildRequires: hardlink
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
%define optflags_lto %nil
%ifarch ppc64le armh
# https://github.com/google/honggfuzz/issues/376
%add_optflags -Wno-error=array-bounds
%endif
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot%docdir
cp -a CHANGELOG COPYING CONTRIBUTING.md README.md docs/* \
   %buildroot%docdir
hardlink -v %buildroot%_bindir

%check
PATH=%buildroot%_bindir:$PATH
honggfuzz --help 2>/dev/null
honggfuzz -v -i examples/openssl/corpus_client -N 1 --run_time 1 -n 1 -P -- /bin/ls
cat <<'EOF' > test.c
#include <stdio.h>
int main(void) { printf("OK\n"); return 0; }
EOF
hfuzz-gcc test.c -o t1
./t1
hfuzz-gcc test.c -o t2 -fsanitize=address
./t2

%files
%_bindir/hfuzz-*
%_bindir/honggfuzz
%_includedir/libhfcommon/
%_includedir/libhfuzz/
%_includedir/libhnetdriver/
%docdir

%changelog
* Fri Sep 22 2023 Vitaly Chikunov <vt@altlinux.org> 2.6-alt1
- Update to 2.6 (2023-09-21).

* Sun Jul 16 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.5-alt3
- Reverted the workaround introduced in the previous change, as long as the bug
  has been fixed in the binutils-devel 2.40-alt2 release.

* Sun Jul 16 2023 Vitaly Chikunov <vt@altlinux.org> 2.5-alt2
- Fix rebuild with binutils-devel-2.40-alt1.

* Sun Jan 02 2022 Vitaly Chikunov <vt@altlinux.org> 2.5-alt1
- Updated to 2.5 (2022-01-01).

* Fri Feb 26 2021 Vitaly Chikunov <vt@altlinux.org> 2.4-alt1
- Update to 2.4 (2021-02-24).

* Sun Jul 26 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.1-alt1
- Update to 2.3.1 (2020-07-22).

* Thu May 14 2020 Vitaly Chikunov <vt@altlinux.org> 2.2-alt1
- Initial import of 2.2
