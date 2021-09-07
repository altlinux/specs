Name: john
Version: 1.9
Release: alt2
%define charsets_version 20130529

Summary: John the Ripper password cracker
License: GPL-2.0-or-later
Group: System/Base
Url: https://www.openwall.com/john/

# ftp://ftp.openwall.com/pub/projects/john/john-%version.tar
# git://git.altlinux.org/gears/j/john
Source0: %name-%version-%release.tar
# ftp://ftp.openwall.com/pub/projects/john/john-charsets-%charsets_version.tar.gz
Source1: john-charsets-%charsets_version.tar
Patch2000: %name-e2k.patch

ExclusiveArch: x86_64 %ix86 aarch64 %arm ppc64le %e2k

%def_enable avx
%def_enable xop
%def_enable omp

%if_enabled omp
BuildRequires: libgomp-devel
%endif

Summary(ru_RU.UTF-8): Взломщик шифрованных паролей путём перебора

%description
John the Ripper is a fast password cracker (password security auditing
tool).  Its primary purpose is to detect weak Unix passwords, but a number
of other hash types are supported as well.

%description -l ru_RU.UTF-8
Высокопроизводительный взломщик паролей, используемый для аудита защищённости.
Основное его назначение состоит в выявлении простых паролей в Юниксе,
хотя поддерживаются и некоторые другие алгоритмы хэширования паролей.

%prep
%setup -n %name-%version-%release -a1
%ifarch %e2k
%patch2000 -p1
%endif

# -flto fix
sed -i "s|\$(JOHN_OBJS) \$(LDFLAGS)|\$(filter-out -c,\$(CFLAGS)) &|" src/Makefile

%define arg_cc CC='%__cc'
%ifarch %ix86
# non-pic asm code
%define arg_cc CC='%__cc -no-pie'
%endif
%define cflags -c %optflags -DJOHN_SYSTEMWIDE=1 $(getconf LFS_CFLAGS)
%define _make_bin %__make
%define john_execdir /usr/libexec/john

%build
cd src

make() {
	%make_build %arg_cc "$@"
	%{!?_without_check:%{!?_without_test:%__make check}}
}

CPU_FALLBACK=
mv_john() {
	mv ../run/john ../run/john-$1
	%__make clean
	CPU_FALLBACK="\\\"john-$1\\\""
}

%ifarch %ix86
# non-OpenMP builds
make linux-x86-any CFLAGS="%cflags"
mv_john %_target_cpu
make linux-x86-mmx CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
mv_john mmx
make linux-x86-sse2 CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
%define john_last sse2
%if_enabled avx
mv_john sse2
make linux-x86-avx CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
%define john_last avx
%endif #avx
%if_enabled xop
mv_john avx
make linux-x86-xop CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
%define john_last xop
%endif #xop
# OpenMP builds
%if_enabled omp
mv_john %john_last
OMP_FALLBACK='\"john-%_target_cpu\"'
make linux-x86-any CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
mv_john omp-%_target_cpu
eval CPU_FALLBACK="$CPU_FALLBACK"
OMP_FALLBACK='"john-mmx"'
make linux-x86-mmx CFLAGS="%cflags -fopenmp -mmmx" CFLAGS_MAIN="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK' -DHAVE_CRYPT" OMPFLAGS='-fopenmp -mmmx'
mv_john omp-mmx
eval CPU_FALLBACK="$CPU_FALLBACK"
OMP_FALLBACK='"john-sse2"'
make linux-x86-sse2 CFLAGS="%cflags -fopenmp -msse2" CFLAGS_MAIN="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK' -DHAVE_CRYPT" OMPFLAGS='-fopenmp -msse2'
%if_enabled avx
mv_john omp-sse2
OMP_FALLBACK='\"john-avx\"'
make linux-x86-avx CFLAGS="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%if_enabled xop
mv_john omp-avx
OMP_FALLBACK='\"john-xop\"'
make linux-x86-xop CFLAGS="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #xop
%endif #avx
%endif #omp
%endif #%ix86

%ifarch x86_64
# non-OpenMP builds
make linux-x86-64 CFLAGS="%cflags"
%define john_last sse2
%if_enabled avx
mv_john sse2
make linux-x86-64-avx CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
%define john_last avx
%if_enabled xop
mv_john avx
make linux-x86-64-xop CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
%define john_last xop
%endif #xop
%endif #avx
# OpenMP builds
%if_enabled omp
mv_john %john_last
OMP_FALLBACK='\"john-sse2\"'
make linux-x86-64 CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%if_enabled avx
mv_john omp-sse2
OMP_FALLBACK='\"john-avx\"'
make linux-x86-64-avx CFLAGS="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%if_enabled xop
mv_john omp-avx
OMP_FALLBACK='\"john-xop\"'
make linux-x86-64-xop CFLAGS="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #xop
%endif #avx
%endif #omp
%endif #x86_64

%ifarch aarch64
# non-OpenMP builds
make linux-arm64le CFLAGS="%cflags"
# OpenMP builds
%if_enabled omp
mv_john arm64le
OMP_FALLBACK='\"john-arm64le\"'
make linux-arm64le CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #omp
%endif #aarch64

%ifarch %arm
# non-OpenMP builds
make linux-arm32le CFLAGS="%cflags"
mv_john arm32le
make linux-arm32le-neon CFLAGS="%cflags -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK'"
# OpenMP builds
%if_enabled omp
mv_john arm32le-neon
OMP_FALLBACK='\"john-arm32le\"'
make linux-arm32le CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
mv_john omp-arm32le
OMP_FALLBACK='\"john-arm32le-neon\"'
make linux-arm32le-neon CFLAGS="%cflags -fopenmp -DCPU_FALLBACK=1 -DCPU_FALLBACK_BINARY='$CPU_FALLBACK' -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #omp
%endif #arm

%ifarch ppc64 ppc64le
# non-OpenMP builds
make linux-ppc64 CFLAGS="%cflags"
# OpenMP builds
%if_enabled omp
mv_john ppc64
OMP_FALLBACK='\"john-ppc64\"'
make linux-ppc64 CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #omp
%endif #ppc64

%ifarch %e2k
# non-OpenMP builds
make linux-e2k CFLAGS="%cflags"
# OpenMP builds
%if_enabled omp
mv_john e2k
OMP_FALLBACK='\"john-e2k\"'
make linux-e2k CFLAGS="%cflags -fopenmp -DOMP_FALLBACK=1 -DOMP_FALLBACK_BINARY='$OMP_FALLBACK'" OMPFLAGS=-fopenmp
%endif #omp
%endif #e2k

%install
mkdir -p %buildroot{%_bindir,%john_execdir,{/etc,%_datadir}/john}
install -pm755 run/john{,-*} %buildroot%john_execdir/
ln -r -s %buildroot%john_execdir/john %buildroot%_bindir/
cp -a run/un* %buildroot%_bindir/
install -pm644 run/john.conf %buildroot/etc/john/
install -pm644 run/password.lst \
	john-charsets-%charsets_version/*.chr \
	%buildroot%_datadir/john/
ln -r -s %buildroot/etc/john/john.conf %buildroot%_datadir/john/
install -pm644 run/{mailer,makechr,relbench} doc/

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files
%doc doc/*
%attr(750,root,wheel) %dir /etc/john/
%attr(750,root,wheel) %dir %john_execdir/
%config(noreplace) /etc/john/*
%_bindir/*
%john_execdir/*
%_datadir/john/

%changelog
* Tue Sep 07 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.9-alt2
- Added Elbrus support.
- Fixed OpenMP build target for aarch64 and ppc64.
- Fixed -flto.

* Thu Apr 22 2021 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt1
- Synced with 1.9-owl1.
- Fixed build on x86 when gcc produces pie executables by default.
- Added build rules for aarch64, arm, and ppc64le.

* Sun Sep 22 2013 Dmitry V. Levin <ldv@altlinux.org> 1.8.0.2-alt1
- Synced with 1.8.0.2-owl1.

* Thu Apr 18 2013 Dmitry V. Levin <ldv@altlinux.org> 1.7.9.7-alt1
- Synced with 1.7.9.7-owl1.

* Fri Jul 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.6.1-alt1
- Synced with 1.7.6.1-owl1.

* Tue Mar 23 2010 Dmitry V. Levin <ldv@altlinux.org> 1.7.5-alt1
- Updated to 1.7.5.

* Sun Oct 25 2009 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.4-alt1
- Updated to 1.7.3.4-owl1
- Fixed x86-specific john exec directory location (closes: #22052).

* Thu Jul 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.1-alt2
- src/charset.c (charset_generate_all): Fixed off-by-one
  header->version overflow.  The overflow itself is harmless but
  fortified gcc complains.

* Mon Jul 13 2009 Dmitry V. Levin <ldv@altlinux.org> 1.7.3.1-alt1
- Updated to 1.7.3.1-owl1

* Thu Oct 05 2006 Dmitry V. Levin <ldv@altlinux.org> 1.7.2.1-alt1
- Updated to 1.7.2.1-owl1

* Tue Feb 14 2006 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt1
- Updated to 1.7-owl2

* Mon Jan 10 2005 Dmitry V. Levin <ldv@altlinux.org> 1.6.37.3-alt1
- Updated to 1.6.37.3

* Sun Jan  9 2005 Ilya Evseev <evseev@altlinux.ru> 1.6.37-alt1
- 1.6.37
- specfile: added URL, added russian summary and description

* Wed Feb 05 2003 Dmitry V. Levin <ldv@altlinux.org> 1.6.33-alt1
- ALT adaptions.

* Fri Jan 24 2003 Solar Designer <solar@owl.openwall.com>
- Added a 64-bit Solaris SPARC make target (recent gcc only for now).

* Wed Jan 15 2003 Solar Designer <solar@owl.openwall.com>
- Split the 64-bit MIPS target into two such that it is possible to have
64-bit builds which do or don't require at least an R10K CPU.

* Tue Nov 05 2002 Solar Designer <solar@owl.openwall.com>
- Workaround a Solaris stdio bug triggered by code in "unique".

* Fri Nov 01 2002 Solar Designer <solar@owl.openwall.com>
- Fixed a bug in "unique" which caused it to fail on big-endian boxes
on files bigger than a single buffer, thanks to Corey Becker.

* Sat Oct 19 2002 Solar Designer <solar@owl.openwall.com>
- Simplified DES_bs_get_binary_raw().

* Thu Oct 03 2002 Solar Designer <solar@owl.openwall.com>
- Never point cfg_name to path_expand()'s result buffer, make a copy.

* Thu Sep 05 2002 Solar Designer <solar@owl.openwall.com>
- Never put dupes in crk_guesses, that could overflow it and would be
inefficient anyway.

* Fri Apr 26 2002 Solar Designer <solar@owl.openwall.com>
- Check for with_cpu_fallback correctly (unbreak builds on non-x86).

* Thu Apr 11 2002 Solar Designer <solar@owl.openwall.com>
- On x86, always build the MMX binary, with a run-time fallback to the
non-MMX one if necessary.

* Wed Apr 10 2002 Solar Designer <solar@owl.openwall.com>
- Packaged 1.6.31-dev for Owl, with minor modifications.
