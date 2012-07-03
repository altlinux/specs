Name: patchutils
Version: 0.3.2
Release: alt1

Summary: Patchutils is a small collection of programs that operate on patch files
License: GPLv2+
Group: Text tools
Url: http://cyberelk.net/tim/patchutils/

# git://git.altlinux.org/gears/p/patchutils.git
Source: %name-%version-%release.tar

Requires: patch, diffutils, mktemp >= 1:1.3.1
Provides: interdiff
Obsoletes: interdiff

BuildRequires: libzio-devel, xmlto

Summary(ru_RU.UTF-8): Набор программ для обработки патчей

%description
Patchutils is a small collection of programs that operate on patch files.
This version contains:
+ combinediff: creates a cumulative patch from two incremental patches;
+ dehtmldiff: gets usable diff from an HTML page;
+ filterdiff: extracts or excludes diffs from a diff file;
+ fixcvsdiff: fixes problematic cvs diff files;
+ flipdiff: exchanges the order of two incremental patches;
+ grepdiff: shows files modified by a diff containing a regex;
+ espdiff: applies the appropriate transformation to a set of patches;
+ interdiff: shows differences between two unified diff files;
+ lsdiff: shows which files are modified by a patch;
+ recountdiff: recomputes patch counts and offsets;
+ rediff: fixes offsets and counts of a hand-edited diff;
+ splitdiff: separates out incremental patches;
+ unwrapdiff: demangles word-wrapped patches.

%description -l ru_RU.UTF-8
Термином "патч" ("patch", "заплатка") обозначают список отличий
между двумя версиями или вариантами исходного текста, программного
кода или данных.  Патч может иметь как текстовую, так и двоичную форму.

Популярные базовые утилиты diff и patch предназначены для создания
и применения патчей текстового формата для текстовых данных,
в первую очередь - для исходных текстов и конфигурационных файлов,
используемых программистами и системными администраторами.

Данный пакет содержит ряд полезных вспомогательных утилит для работы с патчами:
+ combinediff: создаёт объединённый кумулятивный патч из двух последовательных;
+ dehtmldiff: извлекает текст патча из HTML-страницы;
+ filterdiff: извлекает или исключает diff-отчёты из diff-файла;
+ fixcvsdiff: исправляет возможные ошибки в diff-файлах CVS;
+ flipdiff: меняет порядок наложения двух последовательных патчей;
+ grepdiff: выводит список файлов, изменяемых патчем,
            содержащим указанное регулярное выражение;
+ interdiff: показывает список отличий между двумя патчами;
+ lsdiff: выводит список файлов, изменяемых патчем;
+ recountdiff: заново расчитывает координаты фрагментов патча в исходниках;
+ rediff: исправляет координаты фрагментов во вручную исправлявшемся патче;
+ splitdiff: разделяет последовательные инкрементальные патчи;
+ unwrapdiff: удаляет лишние переносы строк из патчей, выравненных
              в тектовом редакторе по правым границам слов.

%prep
%setup -n %name-%version-%release
bzip2 -9k ChangeLog

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%check
%make_build -k check

%files
%_bindir/*
%_mandir/man?/*
%doc AUTHORS BUGS ChangeLog.bz2 NEWS* TODO

%changelog
* Fri Feb 18 2011 Dmitry V. Levin <ldv@altlinux.org> 0.3.2-alt1
- Updated to 0.3.2.
- Enabled test suite.

* Sat May 16 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt3
- Remplemented -z option using libzio.

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt2
- Updated License tag.
- Updated build deps.

* Fri Feb 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 0.2.31-alt3
- Rebuilt.

* Tue Jun 06 2006 Dmitry V. Levin <ldv@altlinux.org> 0.2.31-alt2
- Imported temporary file handling fix from Owl.

* Wed Jan  4 2006 Ilya Evseev <evseev@altlinux.ru> 0.2.31-alt1
- Updated to 0.2.31
- Specfile: added russian summary/description

* Fri Nov 26 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.30-alt1
- Updated to 0.2.30:
  + some minor parsing bugs were fixed;
  + the documentation was clarified;
  + a new option was added to lsdiff/filterdiff for selecting
    patches based on the order in which they appear.

* Wed Apr 07 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.29-alt1
- Updated to 0.2.29 (bugfix release).

* Thu Mar 18 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.28-alt1
- Updated to 0.2.28 (bugfix release).

* Sun Feb 29 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.27-alt1
- Updated to 0.2.27:
  + An option was added to lsdiff to treating empty files as absent.
  + The filterdiff and interdiff utilities now handle patches
    containing embedded null characters.
  + The dehtmldiff utility was improved slightly.

* Sat Jan 17 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.26-alt1
- Updated to 0.2.26:
  + Some build fixes were made.

* Tue Dec 16 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.25-alt1
- Updated to 0.2.25:
  + New filterdiff option for displaying patch filenames.
  + New splitdiff option to make it behave more like diffsplit.
  + Other minor bugfixes.

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.24-alt1
- Updated to 0.2.24:
  + New filterdiff option for removing timestamps.
  + New grepdiff options: -E and -f.
  = Minor bugfixes.
- Added support for -H in lsdiff/grepdiff (from CVS).
- Fixed syntax error in dehtmldiff(1).

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.22-alt1
- Updated to 0.2.22:
  Several small bugs were fixed.  A new option was added to splitdiff
  to split out every file-level patch, and a new option was added to
  grepdiff to display matching hunks.  A new tools was added for
  applying the appropriate transformation to a set of patches.

* Sun Feb 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.21-alt1
- Updated to 0.2.21:
  Several bugs were fixed in flipdiff and dehtmldiff.

* Thu Feb 06 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.20-alt1
- Updated to 0.2.20:
  A new tool was added for exchanging the order of two patches.

* Fri Jan 24 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.19-alt1
- Updated to 0.2.19:
  Several bug fixes were made, and a new program was added for
  extracting a diff from an HTML page.

* Tue Dec 17 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.18-alt1
- Updated to 0.2.18

* Thu Sep 12 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.17-alt1
- 0.2.17

* Fri Sep 06 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.17-alt0.1pre4
- 0.2.17pre4
- Corrected description.

* Mon Aug 19 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.16-alt1
- 0.2.16

* Wed Jun 05 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.14-alt1
- 0.2.14

* Wed May 15 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.13-alt1
- 0.2.13

* Sat Apr 27 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.12-alt1
- 0.2.12

* Fri Mar 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.11-alt1
- 0.2.11

* Wed Mar 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.10-alt1
- 0.2.10

* Tue Feb 26 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.9-alt1
- 0.2.9

* Mon Feb 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.8-alt1
- 0.2.8

* Mon Jan 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2.7-alt1
- 0.2.7

* Mon Dec 03 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.5-alt1
- 0.2.5

* Thu Nov 29 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.4-alt1
- 0.2.4, updated description.

* Wed Nov 21 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.2-alt1
- 0.2.2

* Sun Nov 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.1-alt1
- 0.2.1

* Tue Nov 13 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.2.0-alt1
- 0.2.0

* Wed Oct 24 2001 Dmitry V. Levin <ldv@alt-linux.org> 0.1.5-alt1
- 0.1.5
- Updated descriptions.

* Thu Oct 18 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.4-alt0.1
- 0.1.4 pre.

* Wed Oct 17 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.3-alt1
- Adopted for ALT.
- Ported cleanup patches from interdiff

* Tue Oct 16 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.1.3-1mdk
- initial release
- obsoletes interdiff
- macroize
- more docs
