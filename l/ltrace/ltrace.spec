Name: ltrace
Version: 0.6.0
Release: alt1

Summary: Tracks runtime library calls from dynamically linked executables
License: GPLv2+
Group: Development/Debuggers
Url: http://ltrace.alioth.debian.org/

# git://anonscm.debian.org/collab-maint/ltrace.git
# git://git.altlinux.org/gears/l/ltrace.git
Source: %name-%version-%release.tar

BuildRequires: libelf-devel

Summary(ru_RU.UTF-8): Трассировщик библиотечных вызовов из динамически скомпонованных приложений

%description
Ltrace is a debugging program which runs a specified command until it
exits.  While the command is executing, ltrace intercepts and records
the dynamic library calls which are called by the executed process and
the signals received by that process.
It can also intercept and print the system calls executed by the program.

The program to be traced need not be recompiled for this, so you can
use it on binaries for which you don't have the source handy.

%description -l ru_RU.UTF-8
Ltrace представляет из себя утилиту отладки, которая запускает указанную
пользователем команду и дожидается её завершения. Пока команда выполняется,
Ltrace перехватывает и выводит все выполняемые процессом вызовы подпрограмм
из динамических библиотек, все системные вызовы и все получаемые сигналы.

Трассируемую программу не требуется перекомпилировать, так что отлаживать
с помощью Ltrace можно даже те приложения, исходные тексты которых недоступны.

%prep
%setup -n %name-%version-%release
bzip -9k ChangeLog

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_mandir/man?/*
%config(noreplace) %_sysconfdir/*
%doc BUGS ChangeLog.bz2 README TODO
%exclude %_docdir/%name

%changelog
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

* Wed Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 0.3.10-3mdk
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
