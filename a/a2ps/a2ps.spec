%define _unpackaged_files_terminate_build 1

Name: a2ps
Version: 4.15.8
Release: alt1

# Brain damaged lib/program_name system...
%set_verify_elf_method unresolved=relaxed

Summary: Any to PostScript filter
License: GPL
Group: Publishing
Url: http://www.gnu.org/s/a2ps

Source0: %name-%version.tar
Source1: %name-reconfigure
Patch1:  %name-alt-koi8.edf.patch

Requires: fonts-type1-urw

# Automatically added by buildreq on Fri Jan 20 2012
# optimized out: ghostscript-common texlive-base-bin texlive-latex-base
BuildRequires: ImageMagick-tools chrpath flex ghostscript-utils gperf groff-base gv imake libX11-devel libpaper-devel xorg-cf-files libgc-devel texinfo

%description
GNU a2ps is an Any to PostScript filter.  Of course it processes plain
text files, but also pretty prints quite a few popular languages.

Its slogan is precisely `` Do The Right Thing '', which means that
though it is highly configurable, everything was made so that a novice
user can do complicated PostScript manipulations.  For instance, it
has the ability to delegate the processing of some files to other
filters (such as groff, texi2dvi, dvips, gzip etc.), what allows a
uniform treatment (n-up, page selection, duplex etc.) of heterogeneous
files.

%description -l ru_RU.UTF-8
GNU a2ps - это фильтр Any to PostScript.  Конечно, он обрабатывает
обычные текстовые файлы, но также неплохо печатает на многих популярных
языках.
Его девиз - "Делай правильные вещи", что означает, что несмотря на
высокую степень конфигурируемости, все сделано так, чтобы начинающий
пользователь смог выполнять сложные манипуляции с PostScript.
Например, есть возможность делегировать обработку некоторых файлов
другим фильтрам (таким как groff, texi2dvi, dvips, gzip и т. д.),
что позволяет единообразную обработку (n-up, page selection, duplex
и т. д.) разнородных файлов.

%prep
%setup -q
%patch1 -p1

%build
%configure --disable-rpath --sysconfdir=%_sysconfdir/%name
%make
chrpath -d ./src/a2ps

%install
%make DESTDIR=%buildroot install
install -d %buildroot%_sbindir
install -m 755 %SOURCE1 %buildroot%_sbindir

%find_lang %name

%post
# Adapt /usr/share/a2ps/afm/fonts.map to the current system environment
%_sbindir/%name-reconfigure > /dev/null 2>&1

%files -f %name.lang
%config(noreplace) %_sysconfdir/%name/*.cfg
%_bindir/*
%_sbindir/*
%_datadir/%name
%_datadir/ogonkify
%_infodir/*
%_man1dir/*
%doc AUTHORS FAQ NEWS README ChangeLog TODO THANKS
%_datadir/locale/*/LC_MESSAGES/a2ps-gnulib.mo
%_datadir/emacs/site-lisp/a2ps-print.el
%_datadir/emacs/site-lisp/a2ps.el

%changelog
* Thu Jun 02 2026 Petr Usoltsev <usoltsevpv@altlinux.org> 4.15.8-alt1
- Version up

* Mon Jun 30 2025 Petr Usoltsev <usoltsevpv@altlinux.org> 4.15.6-alt1
- Version up
- Update koi8 patch
- Removing outdated third-party patches
- Fix build
- Deleting libraries, because upstream remove libs(noinst_LTLIBRARIES = liba2ps.la) in commit 267dc6a67c361179ddb267ee75e9e11291b43c67

* Tue Jun  3 2025 Evgeniy Gorbanyov <esgor@altlinux.org> 4.14-alt5
- Fixed FTBFS with gcc-14.

* Wed Oct 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 4.14-alt4
- NMU: fixed FTBFS with glibc 2.38

* Fri Dec 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.14-alt3
- Applied security patches from Debian and Gentoo (Fixes: CVE-2014-0466, CVE-2015-8107).

* Thu Jan 19 2012 Fr. Br. George <george@altlinux.ru> 4.14-alt2
- Fix build

* Wed Sep 14 2011 Fr. Br. George <george@altlinux.ru> 4.14-alt1
- New old upstream
- Version up

* Mon Oct 09 2006 Fr. Br. George <george@altlinux.ru> 4.13-alt3
- Resurrect from orphaned.
- MDV patches are included.
- VERIFY_ELF_UNRESOLVED set to "relaxed" for ill-designed "program_name".
- Use fonts-type1-urw for koi8 encoding.

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt2
- Fixed compilation with gcc3.4.

* Sat Dec 25 2004 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt1
- Security fix: CAN-2004-1170 

* Thu Dec 11 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.4
- Fixed permissions on some sources.

* Sun Dec 07 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.3
- *.la files removed.

* Wed Sep 03 2003 Andrey Astafiev <andrei@altlinux.ru> 4.13-alt0.1
- First version of RPM package for Sisyphus.
