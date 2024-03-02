# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: bzip3
Version: 1.4.0
Release: alt1
Summary: A better and stronger spiritual successor to BZip2.
# bzip3 as a whole is licensed under LGPLv3 only. It is not dual-licensed
# under LGPLv3 and Apache 2.0.
License: LGPL-3.0-only
Group: Archiving/Compression
Url: https://github.com/kspalaiologos/bzip3
Requires: libbzip3 = %EVR

%define valgrind_arches %ix86 x86_64 aarch64

Source: %name-%version.tar
%{?!_without_check:%{?!_disable_check:
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
A better, faster and stronger spiritual successor to BZip2. Features
higher compression ratios and better performance thanks to a order-0
context mixing entropy coder, a fast Burrows-Wheeler transform code
making use of suffix arrays and a RLE with Lempel Ziv+Prediction pass
based on LZ77-style string matching and PPM-style context modeling.

Like its ancestor, BZip3 excels at compressing text or code.

%package -n libbzip3
Summary: Shared library for %name
Group: System/Libraries

%description -n libbzip3
%summary.

%package -n libbzip3-devel
Summary: Developmend files for libbzip3
Group: Development/C
Requires: libbzip3 = %EVR

%description -n libbzip3-devel
%summary.

%prep
%setup
echo %version-%release > .tarball-version
rm .gitignore # For AX_SUBST_MAN_DATE

%build
%add_optflags %(getconf LFS_CFLAGS)
%ifarch x86_64
%add_optflags -Werror -fanalyzer -Wno-analyzer-malloc-leak -Wno-error=unused-function
%endif
%autoreconf
%configure --disable-static --disable-arch-native
%make_build

%install
%makeinstall_std
# We don't have the dependency.
rm %buildroot%_bindir/bz3most %buildroot%_man1dir/bz3most.1

%check
./bzip3 --version | grep -xF '%name %version-%release'
make roundtrip test
%ifarch %valgrind_arches
%define valgrind valgrind -q --error-exitcode=2 --track-origins=yes
%else
%define valgrind %nil
%endif
head -2333444c /dev/urandom > testfile
%valgrind .libs/lt-bzip3 -z < testfile > testfile.bz3
%valgrind .libs/lt-bzip3 -d < testfile.bz3 | cmp - testfile

%files
%doc NEWS README.md
%_bindir/bunzip3
%_bindir/bzip3
%_bindir/bz3*
%_man1dir/b*.1*

%files -n libbzip3
%doc LICENSE
%_libdir/libbzip3.so.0*

%files -n libbzip3-devel
%doc doc/*.md
%_includedir/libbz3.h
%_libdir/libbzip3.so
%_pkgconfigdir/bzip3.pc

%changelog
* Sat Mar 02 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.0-alt1
- First import 1.4.0-5-gf55631b (2024-01-14).
