%def_without glibc_debuginfo
# turn on by:
# gear --commit -v --hasher -- hsh --build-args "--with glibc_debuginfo" -v ~/hasher 2>&1 | tee log

Name: ltrace
Version: 0.7.91.0.198.git82c6640
Release: alt1

Summary: Tracks runtime library calls from dynamically linked executables
License: GPLv2+
Group: Development/Debuggers
Url: http://ltrace.alioth.debian.org/

# git://anonscm.debian.org/collab-maint/ltrace.git
# https://github.com/dkogan/ltrace
Source: %name-%version.tar

Patch0: ltrace-0.7.91.0.198.git82c6640-fix_readdir_r_deprecated.patch
Patch1: ltrace-0.7.91.0.198.git82c6640-fix_attach_process.patch
Patch2: ltrace-0.7.91.0.198.git82c6640-fix_attach_process_dlopen.patch
Patch3: ltrace-0.7.91.0.198.git82c6640-disable_long_double_test_wchar.patch
# patch3 due Ltrace doesn't support long
# see: etc/libc.so-types.conf:# XXX ltrace misses long double and long long support
Patch4: ltrace-0.7.91.0.198.git82c6640-fix_errors_in_tests.patch
%{?_without_glibc_debuginfo:
Patch5: ltrace-0.7.91.0.198.git82c6640-disable_glibc_core_debuginfo_tests.patch}

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%{?_without_glibc_debuginfo:
%patch5 -p1}

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
[ -w /dev/ptmx -a -f /proc/self/maps ] || exit
LC_ALL=en_US.UTF-8 make check RUNTESTFLAGS="--tool_exec=%buildroot/usr/bin/ltrace CFLAGS_FOR_TARGET=" </dev/ptmx

%files
%_bindir/*
%_mandir/man?/*
%_datadir/%name
%doc COPYING CREDITS README TODO
%exclude %_docdir/%name

%changelog
* Fri Nov 24 2017 Grigory Ustinov <grenka@altlinux.org> 0.7.91.0.198.git82c6640-alt1
- Build new version.
   (Closes: #33470)

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
