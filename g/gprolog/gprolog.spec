Name: gprolog
Version: 1.5.0
Release: alt1

Summary: GNU Prolog compiler
License: GPL-2.0-or-later or LGPL-3.0-or-later
Group: Development/Other
Url: http://www.gprolog.org
Vcs: https://git.code.sf.net/p/gprolog/code
Source: %name-%version-%release.tar
# x86 - unstable: something in the gplc chain segfaults from time to time.
# arm - broken: ma2asm aborts.
ExclusiveArch: x86_64 aarch64

%description
GNU Prolog is a free Prolog compiler with constraint solving over
finite domains (FD).  GNU Prolog is largely compliant with the ISO
standard and is part of the Prolog Commons initiative.

%prep
%setup -n %name-%version-%release

%build
#../BipsPl/error_supp.c: In function 'Pl_Remove_Predicate_2':
#src/EnginePl/wam_archi.h:62:21: error: global register variable follows a function definition
#   62 | register WamWord   *pl_reg_bank asm ("r12");
#      |                     ^
%define optflags_lto %nil
REGS=
%ifarch %ix86
# This not just disables pie but also somehow helps to avoid text relocations.
export CC='%__cc -no-pie'
# Without this pl2wam segfaults.
REGS='--disable-regs'
%endif
%ifarch %arm
%remove_optflags -mthumb
%endif
cd src
%configure \
	--with-install-dir=%_libdir/%name \
	--without-doc-dir \
	--without-examples-dir \
	--without-links-dir \
	--with-c-flags="%optflags $(getconf LFS_CFLAGS)" \
	$REGS \
	#
make -j1

%install
%make_install install-system -C src \
	DESTDIR=%buildroot \
	TXT_FILES= \
	#

mkdir -p %buildroot%_bindir
ln -rsnf %buildroot%_libdir/%name/bin/* \
	%buildroot%_bindir/

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
env PATH=%buildroot%_bindir:$PATH \
	make -j1 -k check -C src

%files
%_bindir/*
%_libdir/%name/
%doc README COPYING VERSION NEWS PROBLEMS ChangeLog gprolog.ico

%changelog
* Thu Jul 08 2021 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- v1.4.5-26-g0db40713 -> v1.5.0-1-g8a8220dc.

* Sat Apr 17 2021 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt0.1
- v1.4.5-26-g0db40713.
- Removed compilation date from packaged files (patch by Antoine Belvire).
