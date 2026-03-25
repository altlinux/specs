# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: busybox
Version: 1.37.0
Release: alt2
Summary: Statically linked binary providing simplified versions of system commands
License: GPL-2.0-only
Group: Shells
Url: https://busybox.net/
Vcs: https://git.busybox.net/busybox

Source: %name-%version.tar
BuildRequires: musl-devel-static >= 1.2.5-alt7
BuildRequires: perl-podlators
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
BuildRequires: /usr/bin/zip
}}

%description
BusyBox combines tiny versions of many common UNIX utilities into a single
small executable. BusyBox provides a fairly complete POSIX environment
for any small system, both embedded environments and more full featured
systems concerned about space.

This package can be useful in various system recovering or boot scenarios.

Statically compiled with musl. CONFIG_FEATURE_SH_STANDALONE is enabled
to not require symlinking.

%prep
%setup
# Relocation problem on x86.
sed -Ei 's/(CONFIG_SHA.*_HWACCEL)=y/# \1 is not set/' config
cp config .config
sed -i '/^CFLAGS_busybox/s/-static/-static-pie/' Makefile.flags

%build
%add_optflags -DBB_EXTRA_VERSION='\" (%release%{?disttag::%disttag})\"'
export KCONFIG_NOTIMESTAMP=1
make oldconfig
diff -u config .config
export SKIP_STRIP=y
%make_build V=1 CC=musl-gcc EXTRA_CFLAGS="%optflags"

%install
install -Dp busybox_unstripped -T %buildroot/bin/busybox
install -Dpm644 docs/busybox.1 -t %buildroot%_man1dir

%check
timeout 1 ./busybox
set -o pipefail
export SKIP_KNOWN_BUGS=1
export SKIP_INTERNET_TESTS=1
# Note: Base build options should not change or it will rebuild.
if %make_build test V=1 CC=musl-gcc EXTRA_CFLAGS="%optflags" &> test.log
then
	grep -E 'PASS:|FAIL:|SKIPPED:' test.log
else
	awk "/FAIL:/" RS======================= ORS='\n' test.log
	exit 1
fi
# date tests fail but they do not return exit failure.
file busybox_unstripped | grep 'pie executable,.*, static-pie linked,'
ldd busybox_unstripped | grep 'statically linked'
# Verify standalone mode.
./busybox sh <<-EOF |& grep -Fw 'BusyBox v%version'
	! ls --version
EOF
ls -l busybox busybox_unstripped
size busybox

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README AUTHORS .config
/bin/busybox
%_man1dir/busybox.1*

%changelog
* Fri Mar 20 2026 Vitaly Chikunov <vt@altlinux.org> 1.37.0-alt2
- tc: Fix CBQ FTBFS on newer kernels/glibc-kernheaders.
- Build static PIE executable (with ASLR).

* Sat Mar 01 2025 Vitaly Chikunov <vt@altlinux.org> 1.37.0-alt1
- Update to 1_37_0 (2024-09-26). (Fixes: CVE-2023-42363, CVE-2023-42366).

* Sun Oct 08 2023 Vitaly Chikunov <vt@altlinux.org> 1.36.1-alt1
- First import 1_36_1 (2023-05-19).
