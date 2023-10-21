# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: lowdown
Version: 1.0.2
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
%makeinstall_std install

%check
%make_build regress

%files
%doc README.md LICENSE.md
%_bindir/%name
%_bindir/%name-diff
%_datadir/%name
%_man1dir/%{name}*
%_man5dir/%{name}*

%changelog
* Sat Oct 21 2023 Vitaly Chikunov <vt@altlinux.org> 1.0.2-alt1
- Update to VERSION_1_0_2-12-ge030fa6 (2023-09-16).

* Wed Sep 28 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.0-alt1
- First import VERSION_1_0_0 (2022-05-28). Which is never committed to
  Sisyphus.
