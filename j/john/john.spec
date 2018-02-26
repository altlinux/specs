Name: john
Version: 1.7.6.1
Release: alt1
%define charsets_version 20051216

Summary: John the Ripper password cracker
License: GPL
Group: System/Base
Url: http://www.openwall.com/john/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.openwall.com/pub/projects/john/john-%version.tar
# git://git.altlinux.org/gears/j/john
Source0: %name-%version-%release.tar
# ftp://ftp.openwall.com/pub/projects/john/john-charsets-%charsets_version.tar.gz
Source1: john-charsets-%charsets_version.tar

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

%ifarch x86_64
%define cflags -c %optflags -Wall -DJOHN_SYSTEMWIDE=1
%else
%define cflags -c %optflags -finline-limit=2000 --param inline-unit-growth=2000 -Wall -DJOHN_SYSTEMWIDE=1
%endif
%define with_cpu_fallback 0

%build
cd src
%ifarch %ix86
%define john_execdir /usr/libexec/john
%define with_cpu_fallback 1
%ifarch athlon athlon_xp i786 i886 i986
make linux-x86-mmx CFLAGS='%cflags'
%else
make linux-x86-any CFLAGS='%cflags'
%{!?_without_check:%{!?_without_test:%__make check}}
mv ../run/john ../run/john-non-mmx
make clean
make linux-x86-mmx CFLAGS='%cflags -DCPU_FALLBACK=1'
%endif #athlon athlon_xp i786 i886 i986
%{!?_without_check:%{!?_without_test:%__make check}}
mv ../run/john ../run/john-non-sse
make clean
make linux-x86-sse2 CFLAGS='%cflags -DCPU_FALLBACK=1'
%endif #%ix86
%ifarch x86_64
make linux-x86-64 CFLAGS='%cflags'
%endif
%ifarch alpha alphaev5 alphaev56 alphapca56 alphaev6 alphaev67
make linux-alpha CFLAGS='%cflags'
%endif
%ifarch sparc sparcv9
make linux-sparc CFLAGS='%cflags'
%endif
%ifarch ppc
make linux-ppc32 CFLAGS='%cflags'
%endif
%{!?_without_check:%{!?_without_test:%__make check}}

%install
mkdir -p %buildroot{%_bindir,%_datadir/john}
install -m 700 run/john %buildroot%_bindir/
cp -a run/un* %buildroot%_bindir/
%if %with_cpu_fallback
mkdir -p %buildroot%john_execdir
install -m 700 run/john-* %buildroot%john_execdir/
%endif
install -m 644 -p run/{john.conf,password.lst} \
	john-charsets-%charsets_version/*.chr \
	%buildroot%_datadir/john/
install -m 644 -p run/mailer doc/

%files
%doc doc/*
%attr(750,root,wheel) %_bindir/john
%_bindir/un*
%if %with_cpu_fallback
%dir %john_execdir
%attr(750,root,wheel) %john_execdir/*
%endif
%dir %_datadir/john
%attr(640,root,wheel) %config(noreplace) %_datadir/john/john.conf
%attr(644,root,root) %_datadir/john/password.lst
%attr(644,root,root) %_datadir/john/*.chr

%changelog
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
