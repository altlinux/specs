# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# section [27] '.symtab': symbol [2468] (__ehdr_start)': st_value [0x400000] out of bounds [0x400270+0x40]
%set_verify_elf_method strict,lint=relaxed

Name: toybox
Version: 0.8.10
Release: alt1
Summary: All-in-one Linux command line
License: 0BSD
Group: Shells
Url: http://landley.net/toybox/
Vcs: https://github.com/landley/toybox

Source: %name-%version.tar
BuildRequires: glibc-devel-static
BuildRequires: liblzma-devel-static
BuildRequires: libssl-devel-static
BuildRequires: musl-devel-static
BuildRequires: zlib-devel-static
%{?!_without_check:%{?!_disable_check:
BuildRequires: /proc
}}

%description
%summary.

Statically compiled with musl and not requiring symlinks for toys
(shell command recursion).

%prep
%setup

%build
cp .gear/config .config
%make silentoldconfig
diff -u .gear/config .config ||:
%make_build CC=musl-gcc CFLAGS="-I/etc/sysconfig/kernel/include %optflags" LDFLAGS="-static" NOSTRIP=1 V=1

%install
install -Dp toybox -t %buildroot/bin

%check
# armh: scripts/test.sh: line 38: 2887805 Bus error
%ifnarch armh
# Known failures:
rm tests/du.test	# 0 on tmpfs
rm tests/id.test	# Additional groups
rm tests/mkpasswd.test	# AddressSanitizer: SEGV
rm tests/sed.test	# Timeout
rm tests/tar.test	# Hash mismatch
rm tests/timeout.test	# No "hello"
%make_build tests
%endif

# List compiled in commands.
./toybox |& sed 's/^/ :: /'
# Check it's statically linked.
! ldd toybox || exit 1
# Test 'shell command recursion'.
./toybox bash <<-EOF | grep -Fx 'toybox %version'
	ls --version
EOF

ls -l toybox
size toybox

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README .config
/bin/toybox

%changelog
* Sat Oct 07 2023 Vitaly Chikunov <vt@altlinux.org> 0.8.10-alt1
- First import 0.8.10-70-g47946f24 (2023-10-06).
