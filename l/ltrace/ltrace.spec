%def_without glibc_debuginfo
# turn on by:
# gear --commit -v --hasher -- hsh --build-args "--with glibc_debuginfo" -v ~/hasher 2>&1 | tee log

# TODO: fix tests
%def_without check

Name: ltrace
Version: 0.7.91.0.198.git82c6640
Release: alt7

Summary: Tracks runtime library calls from dynamically linked executables
License: GPLv2+
Group: Development/Debuggers
Url: http://ltrace.alioth.debian.org/

# git://anonscm.debian.org/collab-maint/ltrace.git
# https://github.com/dkogan/ltrace
Source: %name-%version.tar

# ===== RH Patches go here vvv =====
# RH Patches1-25 are included in git repo https://github.com/dkogan/ltrace

# GCC now warns (errors) on "tautological compares", and readdir_r is deprecated
Patch26: ltrace-0.7.91-tautology.patch

# ARM code has unreachable code after switch statement, move initialization
Patch27: ltrace-rh1423913.patch

# Patch28 makes braces unbalanced

# GCC-9 fix. Avoid passing NULL as argument to %%s
Patch29: ltrace-0.7.91-null.patch

# Patch30 is strange and obscure to me

# Patch31 is included in git repo

# Testsuite: AARCH64 ifuncs not supported yet yet
Patch32: ltrace-rh1225568.patch

# Patches33-34 are included in git repo

# GCC erroneously warns about uninitialized values
Patch35: ltrace-0.7.91-rh1799619.patch

Patch37: ltrace-ppc64le-use-after-free.patch

# ===== ALT Patches goes here vvv =====
Patch1001: ltrace-0.7.91.0.198.git82c6640-fix_attach_process.patch
Patch1002: ltrace-0.7.91.0.198.git82c6640-fix_attach_process_dlopen.patch
# Patch1003 due Ltrace doesn't support long
# see: etc/libc.so-types.conf:# XXX ltrace misses long double and long long support
Patch1003: ltrace-0.7.91.0.198.git82c6640-disable_long_double_test_wchar.patch
Patch1004: ltrace-0.7.91.0.198.git82c6640-fix_errors_in_tests.patch
%{?_without_glibc_debuginfo:
Patch1005: ltrace-0.7.91.0.198.git82c6640-disable_glibc_core_debuginfo_tests.patch}
Patch1006: ltrace-0.7.91.0.198.git82c6640-fix_Wlto-type-mismatch.patch
Patch3500: ltrace-loongarch.patch

BuildRequires: libelf-devel elfutils-devel gcc-c++
%{?!_without_check:%{?!_disable_check:
BuildRequires: dejagnu /dev/pts /proc}}
%{?!_without_glibc_debuginfo:
BuildRequires: glibc-core-debuginfo}

Summary(ru_RU.UTF-8): Трассировщик библиотечных вызовов из динамически скомпонованных приложений

%description
Ltrace is a debugging program which runs a specified command until it
exits.  While the command is executing, ltrace intercepts and records
the dynamic library calls which are called by the executed process and
the signals received by that process.
It can also intercept and print the system calls executed by the program.

The program to be traced need not be recompiled for this, so you can
use it on binaries for which you don't have the source handy.

Optionally you can install glibc-core-debuginfo for obtaining extra
features of Ltrace.

%description -l ru_RU.UTF-8
Ltrace представляет из себя утилиту отладки, которая запускает указанную
пользователем команду и дожидается её завершения. Пока команда выполняется,
Ltrace перехватывает и выводит все выполняемые процессом вызовы подпрограмм
из динамических библиотек, все системные вызовы и все получаемые сигналы.

Трассируемую программу не требуется перекомпилировать, так что отлаживать
с помощью Ltrace можно даже те приложения, исходные тексты которых недоступны.

Опционально можно установить glibc-core-debuginfo для получения дополнительных
возможностей Ltrace.

%prep
%setup

%patch26 -p1
%patch27 -p1
%patch29 -p1
%patch32 -p1
%patch35 -p1
%patch37 -p1

%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%{?_without_glibc_debuginfo:
%patch1005 -p1}
%patch1006 -p1
%patch3500 -p1

%build
export CFLAGS="%optflags -Werror"
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
LC_ALL=en_US.UTF-8 make check RUNTESTFLAGS="--tool_exec=%buildroot/%_bindir/ltrace CFLAGS_FOR_TARGET=" </dev/ptmx

%files
%_bindir/*
%_mandir/man?/*
%_datadir/%name
%doc COPYING CREDITS README TODO
%exclude %_docdir/%name

%changelog
* Wed Oct 18 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.7.91.0.198.git82c6640-alt7
- Support LoongArch architecture.

* Tue Oct 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt6
- Fixed FTBFS.

* Mon Nov 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt5
- Fixed FTBFS.

* Tue Oct 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt4
- Make lav@ happy. (Closes: #39102)

* Sat Dec 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt3
- Fixed FTBFS for gcc9.

* Wed Nov 28 2018 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt2
- Temporary disabled tests, because of new gcc.

* Fri Nov 24 2017 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt1
- Build new version. (Closes: #33470)

* Wed Aug 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.6.0-alt1
- Updated to 0.6.0-10-g43d1de9.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5-alt1
- Updated to 0.5-3.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.4-alt3
- Build with -D_GNU_SOURCE to get off64_t definition
  which is necessary for libelf-0.130.

* Tue Mar 14 2006 Ilya Evseev <evseev@altlinux.ru> 0.4-alt2
- fixup and disable ExclusiveArch

* Sat Mar 11 2006 Ilya Evseev <evseev@altlinux.ru> 0.4-alt1
- updated to new version 0.4

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.36-alt2
- Applied fixes from Jakub Jelinek.
- Build for all platforms.

* Sat Jan  8 2005 Ilya Evseev <evseev@altlinux.ru> 0.3.36-alt1
- 0.3.36
- Specfile: added russian summary/description

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.26-alt2
- Rebuilt in new environment.

* Thu Jun 13 2002 Dmitry V. Levin <ldv@altlinux.org> 0.3.26-alt1
- 0.3.26
- Changed group tag to "Development/Debuggers".

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 0.3.16-alt1
- 0.3.16

* Mon Dec 03 2001 Stanislav Ievlev <inger@altlinux.ru> 0.3.15-alt1
- 0.3.15

* Wed Aug 30 2000 Dmitry V. Levin <ldv@fandra.org> 0.3.10-ipl3mdk
- RE adaptions.

* Mon Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.3.10-3mdk
- added more docs

* Tue Apr 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.3.10-2mdk
- Updated group

* Wed Apr  5 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.3.10-1mdk
- updated BuildRoot
- version 0.3.10
- removed necessity for patch simply to fixup manpage location

* Wed Dec  1 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- update to 0.3.8
- use of _tmppath and prefix
- patch to get man page in /usr/man

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Fri Mar 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.3.6.

* Mon Sep 21 1998 Preston Brown <pbrown@redhat.com>
- upgraded to 0.3.4
