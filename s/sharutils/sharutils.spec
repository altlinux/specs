Name: sharutils
Version: 4.6.3
Release: alt1.1.qa1

Summary: The GNU shar utilities for packaging and unpackaging shell archives
License: GPL
Group: Archiving/Backup

URL: ftp://ftp.gnu.org/gnu/%name/REL-%version
Source: %url/%name-%version.tar.bz2
Patch0: %name-4.3.78-alt-tmpfile.patch
Patch8: %name-4.3.77-alt-tmp.patch

BuildPreReq: help2man

Summary(ru_RU.KOI8-R): Утилиты GNU для создания и распаковки текстовых архивов

%package -n remsync
Summary: Remote synchronization of directories
Summary(ru_RU.KOI8-R): Утилита синхронизации двух каталогов
Group: Archiving/Backup
Requires: %name = %version-%release, perl-base, tar, findutils, gzip-utils

%description
The %name package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar).  This
format can be sent through email (which can be problematic for
regular binary files).  The shar utility supports a wide range of
capabilities (compressing, uuencoding, splitting long files for
multi-part mailings, providing checksums), which make it very flexible
at creating shar files.  After the files have been sent, the unshar
tool scans mail messages looking for shar files.  Unshar automatically
strips off mail headers and introductory text and then unpacks the shar
files.

%description -l ru_RU.KOI8-R
shar расшифровывается как shell archive, т.е. сценарий интерпретатора команд,
в текстовом виде хранящий в своём теле набор данных, которые он при запуске
распаковывает в файлы. Такие архивы имеют три достоинства:
 * благодаря полностью 7-битному содержимому их можно передавать
   любыми коммуникационными программами, включая mail, xmodem и т.д.;
 * формат архива и код самораспаковки являются полностью независимыми
   от операционной системы и аппаратной архитектуры;
 * на целевом компьютере нужен только интерпретатор команд, совместимый с sh.
Недостатками шелл-архивов являются большой размер и низкая скорость обработки.

Утилиты GNU в данном пакете предназначены для создания и управления
шелл-архивами, включая сжатие, нарезание на куски, подсчёт контрольной суммы,
автоматическое извлечение из почтовых сообщений и т.д.

%description -n remsync
The remsync program tries to maintain up-to-date copies of whole
hierarchy of files over many loosely connected sites,
provided there is at least some slow electronic mail between them.

It prepares and sends out specially packaged files called
"synchronization packages", and is able to processes them after reception.
There is no _master_ site, each site has an equal opportunity
to modify files, and modified files are propagated.

People deciding to cooperate in keeping a synchronized set of files
must have trust each other, as each participant has the power
of modifying the contents of files at other sites. 

%description -n remsync -l ru_RU.KOI8-R
Утилита Remsync служит для синхронизации содержимого каталогов
на разных компьютерах через почтовые сообщения.

С её помощью производится как подготовка т.н. пакетов синхронизации
на отправляющей почту стороне, так и их обработка на приёмной.
Отметки синхронизации сохраняются в служебных файлах с именем '.remsync'
внутри синхронизируемых каталогов.

Все узлы, обменивающиеся файлами посредством remsync,
являются равноправными и полноправными,
т.е. пользователь-получатель должен проверять полномочия отправителя вручную.
Вместе с тем, Remsync отслеживает конфликты, связанные с получением
нескольких независимо изменённых вариантов одного файла.

%prep
%setup -q
#patch0
%patch8 -p1

%build
export ac_cv_lib_intl_main=no
export ac_cv_path_MAILER=/bin/mail
%configure
%make_build

%install
%makeinstall install-man

# fix japanese catalog file

%define old_jpdir %buildroot%_datadir/locale/ja_JP.EUC/LC_MESSAGES
%define new_jpdir %buildroot%_datadir/locale/ja/LC_MESSAGES

if [ -d %old_jpdir ]; then
	%__mkdir_p %new_jpdir
	mv %old_jpdir/*.mo %new_jpdir
	rm -rf %old_jpdir
fi

%find_lang %name

# Manual page for remsync
cd %buildroot%_man1dir
help2man %buildroot%_bindir/remsync > remsync.1
subst 's,info remsync,info sharutils,' remsync.1

%files -f %name.lang
%exclude %_bindir/remsync*
%exclude %_mandir/man?/remsync*
%_bindir/*
%_infodir/*.info*
%_mandir/man?/*

%files -n remsync
%_bindir/remsync
%_mandir/man?/remsync*

%changelog
* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 4.6.3-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for sharutils
  * postclean-05-filetriggers for spec file

* Tue May 22 2007 ALT QA Team Robot <qa-robot@altlinux.org> 4.6.3-alt1.1
- Automated rebuild (#11785).

* Tue Jul 25 2006 Ilya Evseev <evseev@altlinux.ru> 4.6.3-alt1
- updated to new version 4.6.3

* Tue May  2 2006 Ilya Evseev <evseev@altlinux.ru> 4.6.2-alt1
- updated to new version 4.6.2

* Thu Jan 12 2006 Ilya Evseev <evseev@altlinux.ru> 4.6-alt1
- updated to new version 4.6

* Tue Aug 30 2005 Ilya Evseev <evseev@altlinux.ru> 4.5.1-alt1
- updated to new version 4.5.1

* Thu Jul 28 2005 Ilya Evseev <evseev@altlinux.ru> 4.4-alt1
- updated to new version 4.4
- bugfix #7264 (reported to upstream and fixed by him)
- specfile: restyle japanese fix

* Fri Jun  3 2005 Ilya Evseev <evseev@altlinux.ru> 4.3.80-alt1
- updated to new version 4.3.80
- patch #0 is no more needed

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.ru> 4.3.78-alt2
- added patch #0 for exploitable temporary file race in unshar,
  http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=302412

* Wed Jan 26 2005 Ilya Evseev <evseev@altlinux.ru> 4.3.78-alt1
- 4.3.78

* Sat Jan  8 2005 Ilya Evseev <evseev@altlinux.ru> 4.3.77-alt1
- 4.3.77
- all old patches except alt-tmp are no more needed
  because they are included to upstream;
  so, we don't need automake/autoconf at build stage.
- remsync is packaged separately for reducing requirements of base stuff

* Mon Oct 06 2003 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-ipl11mdk
- Updated package dependencies.
- Updated package build dependencies.

* Mon Nov 18 2002 Rider <rider@altlinux.ru> 4.2.1-ipl10mdk
- rebuild

* Tue May 14 2002 Dmitry V. Levin <ldv@altlinux.org> 4.2.1-ipl9mdk
- Really update to version 4.2.1
- Merged in RH and MDK patches (the code still have problems).
- Built without libintl (never used).

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 4.2.1-ipl8mdk
- rebuild

* Thu Dec 14 2000 Dmitry V. Levin <ldv@fandra.org> 4.2.1-ipl7mdk
- Fixed texinfo documentation.

* Thu Aug  3 2000 Dmitry V. Levin <ldv@fandra.org> 4.2.1-ipl6mdk
- RE adaptions.

* Fri Jul 28 2000 Francis Galiegue <fg@mandrakesoft.com> 4.2.1-6mdk
- More macros

* Fri Jul 21 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.2.1-5mdk
- use %%make for SMP build.
- corrected %%install_info and %%uninstall_info calls to expand correctly.

* Wed Jul 19 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 4.2.1-4mdk
- bugfix for uudecode and filenames with spaces on them
- BM

* Sun Jun 04 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 4.2.1-3mdk
- fixed the mess with the catalog files.

* Sat Mar 18 2000 Francis Galiegue <francis@mandrakesoft.com> 4.2.1-2mdk
- Let spec helper do its job
- Some spec file changes

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
_ SMP check/build
- 4.2.1

* Wed Aug 25 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Remove gzip -9nf stuff, so they info's aren't .gz.bz2
- add %%defattr, (builds as none root)

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 info

* Wed May 05 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 12)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat Apr 11 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- ALRIGHT!  Woo-hoo!  Erik already did the install-info stuff!
- added BuildRoot
- spec file cleanups

* Sun Sep 14 1997 Erik Troan <ewt@redhat.com>
- uses install-info

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc

