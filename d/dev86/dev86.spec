Name: dev86
Version: 0.16.17
Release: alt5

Summary: A real mode 80x86 assembler and linker
License: GPL
Group: Development/Other
Url: http://www.cix.co.uk/~mayday
Packager: Dmitry V. Levin <ldv@altlinux.org>

# %url/dev86/Dev86src-%version.tar.gz
Source: Dev86src-%version.tar

Patch1: dev86-0.16.16-rh-alt-owl-kinclude.patch
Patch2: dev86-0.16.17-owl-warnings.patch
Patch3: dev86-0.16.17-owl-makefile.patch
Patch4: dev86-0.16.16-alt-optflags.patch
Patch5: dev86-0.16.17-alt-noelksemu.patch
Patch6: dev86-0.16.17-owl-tmp.patch
Patch7: dev86-0.16.17-alt-fixes.patch

ExclusiveArch: %ix86 x86_64
Provides: bin86
Obsoletes: bin86

Summary(ru_RU.KOI8-R): Ассемблер и компоновщик для реального режима Intel 80x86

%package devel
Summary: Development files for dev86
Group: Development/Other
Requires: %name = %version-%release

%description
dev86 provides an assembler and linker for real mode 80x86 instructions.
You'll need to have this package installed in order to build programs
that run in real mode, including LILO and the kernel's bootstrapping code,
from their sources.

%description -l ru_RU.KOI8-R

Пакет %name содержит транслятор языка Ассемблер и компоновщик, предназначенные
для компиляции программ под т.н. реальный режим процессоров Intel 80x86.
Установите его, если вы собираетесь собирать из исходников программы,
работающие в реальном режиме - такие, как LILO или загрузочный код ядра Linux.

%description devel
dev86 provides an assembler and linker for real mode 80x86 instructions.
You'll need to have this package installed in order to build programs
that run in real mode, including LILO and the kernel's bootstrapping code,
from their sources.

This package provides C headers need to use bcc, the C compiler for
real mode x86.

Note that you don't need this package in order to build a kernel.

%description -l ru_RU.KOI8-R devel

dev86 содержит транслятор языка Ассемблер и компоновщик, предназначенные
для написания программ под т.н. реальный режим процессоров Intel 80x86.
Установите его, если вы собираетесь компилировать из исходников программы,
работающие в реальном режиме - такие, как LILO или загрузочный код ядра Linux.

Этот пакет содержит заголовочные файлы и библиотеки языка Си, необходимые
для запуска Си-компилятора bcc, который генерирует код реального режима 80x86.

Примечание: для компиляции ядра Linux нужен пакет dev86, поскольку
загрузочная часть ядра целиком написана на Ассемблере.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

find -type f -print0 |
	xargs -r0 grep -FZl /usr/lib/liberror.txt -- |
	xargs -r0 %__subst 's,/usr/lib/liberror\.txt,/usr/lib/bcc/liberror.txt,g' --

mkdir -p lib/bcc
ln -s ../../include lib/bcc/include

%build
%add_optflags -fno-strict-aliasing -fno-builtin-exp2
make GCCFLAG="%optflags" <<!EOF!
5
quit
!EOF!

for f in `find -mindepth 2 -type f -name README\*`; do
	d="${f%%/*}"
	cp -p "$f" "${f##*/}.${d##*/}"
done

%install
%make_install DIST=%buildroot MANDIR=%_mandir install

for f in nm86 size86; do
	ln -sf objdump86 "%buildroot%_bindir/$f"
done

find %buildroot%_prefix/lib/bcc -type d |
	fgrep -v /include |
	sed -e "s|%buildroot|%%dir |g" >files.list

find %buildroot%_prefix/lib/bcc \! -type d |
	fgrep -v /include |
	sed -e "s|%buildroot||g" |
	fgrep -v 86/lib | fgrep -v \.a >>files.list

%files -f files.list
%_bindir/*
%_mandir/man?/*
%doc README* MAGIC Changes Contributors bin86

%files devel
%dir %_prefix/lib/bcc
%dir %_prefix/lib/bcc/i386
%_prefix/lib/bcc/i386/lib*.a
%_prefix/lib/bcc/lib*.a
%_prefix/lib/bcc/include

%changelog
* Tue Jul 17 2007 Dmitry V. Levin <ldv@altlinux.org> 0.16.17-alt5
- Fixed regression introduced in previous release (nidd, #12355).

* Sun Oct 15 2006 Dmitry V. Levin <ldv@altlinux.org> 0.16.17-alt4
- Synced with 0.16.17-owl3.
- Fixed bugs discovered by new toolchain.

* Mon Oct 10 2005 Ilya Evseev <evseev@altlinux.ru> 0.16.17-alt3
- fixed bug with URL macro case

* Mon Jun 13 2005 Ilya Evseev <evseev@altlinux.ru> 0.16.17-alt2
- disabled elksemu build on x86_64 fix, see here for details:
  https://bugzilla.altlinux.org/show_bug.cgi?id=7003

* Thu May 12 2005 Ilya Evseev <evseev@altlinux.ru> 0.16.17-alt1
- updated to version 0.16.17
- added russian summary/description

* Fri Sep 03 2004 Anton D. Kachalov <mouse@altlinux.org> 0.16.16-alt1
- 0.16.16

* Wed Apr 28 2004 Stanislav Ievlev <inger@altlinux.org> 0.16.3-alt3
- rebuild with glibc2.3

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 0.16.3-alt2
- rebuild

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.16.3-alt1
- 0.16.3, updated patches.
- Relocated /usr/lib/liberror.txt to /usr/lib/bcc/liberror.txt
- Additional convention enforcement on patch file names.

* Thu Jun 14 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.15.5-alt1
- 0.15.5
- Updated patches (rh).

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 0.15.4-ipl1mdk
- 0.15.4

* Mon Aug 18 2000 Dmitry V. Levin <ldv@fandra.org> 0.15.1-ipl1mdk
- 0.15.1

* Wed Aug 16 2000 Dmitry V. Levin <ldv@fandra.org> 0.15.0-ipl3mdk
- split out -devel package (needed only for elks developers).
- BM.

* Wed Jul 19 2000 Dmitry V. Levin <ldv@fandra.org> 0.15.0-ipl1mdk
- RE and Fandra adaptions.

* Wed Jun 14 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.15.0-1mdk
- First mandrake version from rh package.
