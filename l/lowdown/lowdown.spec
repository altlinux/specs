# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lowdown
Version: 1.1.1
Release: alt1
Summary: A simple markdown translator
License: ISC
Group: Development/Documentation
Url: https://kristaps.bsd.lv/lowdown/
Vcs: https://github.com/kristapsdz/lowdown

Source: %name-%version.tar

BuildRequires: libmd-devel

%description
lowdown is a Markdown translator producing HTML5, roff documents in the
ms and man formats, LaTeX, gemini, OpenDocument, and terminal output.

lowdown is a fork of hoedown, although the parser and front-ends have
changed significantly.

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Requires: lib%name = %EVR
Group: Development/C

%description -n lib%name-devel
%summary.

%prep
%setup

%build
# Default MAKEFLAGS will cause garbage written to Makefile.configure.
unset MAKEFLAGS
%add_optflags %(getconf LFS_CFLAGS)
CFLAGS="%optflags" \
./configure \
	LDFLAGS="-lm" \
	PREFIX=%_prefix \
	LIBDIR=%_libdir \
	MANDIR=%_mandir

%make_build

%install
%makeinstall_std install_lib_common install_shared

%check
%make_build regress

%files
%doc README.md LICENSE.md
%_bindir/%name
%_bindir/%name-diff
%_datadir/%name
%_man1dir/%{name}*
%_man5dir/%{name}*

%files -n lib%name-devel
%_includedir/lowdown.h
%_pkgconfigdir/lowdown.pc
%_libdir/liblowdown.so
%_man3dir/%{name}*

%files -n lib%name
%_libdir/liblowdown.so.*

%changelog
* Wed Sep 25 2024 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt1
- Update to VERSION_1_1_1 (2024-09-24).

* Wed Jun 19 2024 Boris Yumankulov <boria138@altlinux.org> 1.1.0-alt1.1
- NMU: add devel subpackage (ALT bug: 50681)

* Wed Nov 08 2023 Vitaly Chikunov <vt@altlinux.org> 1.1.0-alt1
- Update to VERSION_1_1_0 (2023-11-07).

* Sat Oct 21 2023 Vitaly Chikunov <vt@altlinux.org> 1.0.2-alt1
- Update to VERSION_1_0_2-12-ge030fa6 (2023-09-16).

* Wed Sep 28 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- First import VERSION_1_0_0 (2022-05-28). Which is never committed to
  Sisyphus.
