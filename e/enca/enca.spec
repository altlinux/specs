%def_disable static

Name: enca
Version: 1.18
Release: alt1

Summary: A program that guesses encoding of text files
License: GPL
Group: Text tools

Url: http://cihar.com/software/enca
Source: http://dl.cihar.com/enca/%name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

Requires: lib%name = %version-%release

# Automatically added by buildreq on Fri Mar 04 2011
BuildRequires: gtk-doc librecode-devel perl-Encode perl-Unicode-Map

Summary(ru_RU.UTF-8): Программа, "угадывающая" кодировку текстовых файлов
Summary(uk_UA.UTF-8): Програма, що "вгадує" кодування текстових файлів

%description
Enca (Extremely Naive Charset Analyser) is a simple utility
guessing encoding of text files and optionally converting them
to some other encoding using either a built-in convertor, a
system conversion library or an external conversion program.

Currently, it has support for Belarussian, Czech, Polish,
Russian, Slovak, Ukrainian, Bulgarian, Croatian, Estonian,
Hungarian, Latvian, Lithuanian, Slovene and some multibyte
encodings (mostly variants of Unicode) independent on language.

Install Enca if you need to cope with text files of dubious
origin and unknown encoding and convert them to some reasonable
encoding.

%description -l ru_RU.UTF-8
Enca (Extremely Naive Charset Analyser) - простая утилита,
которая позволяет "угадывать" кодировку текстового файла и,
возможно, конвертировать его в другую известную.

Сейчас поддерживаются белорусский, чешский, польский, русский,
словацкий, украинский, болгарский, хорватский, эстонский,
венгерский, латвийский, литовский, словацкий языки и несколько
мультибайтных кодировок вне зависимости от языка.

%description -l uk_UA.UTF-8
Enca (Extremely Naive Charset Analyser) - проста утиліта,
що надає можливість "вгадувати" кодування тектового файлу
та, можливо, конвертувати його у інше відоме.

На цей час підтримуються білоруська, чеська, польська, російська,
словацька, українська, болгарська, хорватська, естонська,
угорська, латвійська, литовська, словацька мови та декілька
мультибайтових кодувань незалежно від мови.

%package -n lib%name
Summary: Shared Enca library
Group: System/Libraries

%description -n lib%name
This package contains shared Enca library which other programs
may use.

%package -n lib%name-devel
Summary: Header files and libraries for Enca development
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the development library and header files
for writing programs using the Extremely Naive Charset Analyser
library, and its API documentation.

Install this package if you are going to create applications
using the Enca library.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for Enca development
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the static library for building statically
linked programs using the Extremely Naive Charset Analyser library.
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall HTML_DIR=%buildroot%_docdir/%name-%version/html

%files
%_bindir/enca
%_bindir/enconv
%_libexecdir/%name/
%doc %_man1dir/*
%doc AUTHORS COPYING ChangeLog ChangeLog.prelib NEWS README.md THANKS TODO

%files -n lib%name
%_libdir/libenca.so.*

%files -n lib%name-devel
%_includedir/enca.h
%_libdir/libenca.so
%_pkgconfigdir/enca.pc
%doc DEVELOP.md
%doc devel-docs/html

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

# TODO:
# - fix devel-docs/html/ build

%changelog
* Sun Jan 10 2016 Michael Shigorin <mike@altlinux.org> 1.18-alt1
- 1.18

* Wed Jan 06 2016 Michael Shigorin <mike@altlinux.org> 1.17-alt1
- 1.17

* Wed Dec 24 2014 Michael Shigorin <mike@altlinux.org> 1.16-alt1
- 1.16

* Wed Jun 18 2014 Michael Shigorin <mike@altlinux.org> 1.15-alt1
- 1.15

* Thu Dec 15 2011 Michael Shigorin <mike@altlinux.org> 1.13-alt3
- autoreconf against broken RPATH

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 1.13-alt2
- rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Tue Feb 09 2010 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- 1.13

* Sat Jan 02 2010 Michael Shigorin <mike@altlinux.org> 1.12-alt3
- enabled librecode
- minor spec cleanup

* Thu Oct 29 2009 Michael Shigorin <mike@altlinux.org> 1.12-alt2
- rebuild

* Thu Oct 29 2009 Michael Shigorin <mike@altlinux.org> 1.12-alt1
- 1.12

* Mon Sep 28 2009 Michael Shigorin <mike@altlinux.org> 1.11-alt1
- 1.11

* Tue Aug 25 2009 Michael Shigorin <mike@altlinux.org> 1.10-alt1
- 1.10: new upstream
- backdated changelog entry to mention that :)

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.9-alt4
- applied repocop patch
- added Packager:
- minor spec cleanup

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt3
- NMU: cleanup spec, update buildreq
- move libdir/%name to main package
- disable requires from external convertors
- strict entries in files sections
- really disabled build with librecode

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.9-alt2.0
- Automated rebuild.

* Mon Apr 24 2006 Michael Shigorin <mike@altlinux.org> 1.9-alt2
- fix for #9440 (reported/suggested by rider@), should build
  on x86_64 now

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 1.9-alt1
- 1.9

* Fri Nov 25 2005 Michael Shigorin <mike@altlinux.org> 1.8-alt1
- 1.8 (minor feature enhancements)

* Fri Apr 22 2005 Victor Forsyuk <force@altlinux.ru> 1.7-alt1
- 1.7
- Looks like SMP build now OK.

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 1.3-alt1
- 1.3

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 1.2-alt1
- 1.2
- removed *.la
- don't package static library by default
- added pkgconfig file

* Fri Aug 29 2003 Michael Shigorin <mike@altlinux.ru> 0.99.4-alt1
- 0.99.4

* Thu Jul 03 2003 Michael Shigorin <mike@altlinux.ru> 0.99.3-alt1
- 0.99.3

* Sat Jun 14 2003 Michael Shigorin <mike@altlinux.ru> 0.99.0-alt1
- 0.99.0 (major feature enchancements)

* Sat Feb 01 2003 Michael Shigorin <mike@altlinux.ru> 0.10.7-alt2
- added missing %_libdir/*.so to lib%name-devel

* Tue Jan 28 2003 Michael Shigorin <mike@altlinux.ru> 0.10.7-alt1
- 0.10.7

* Tue Nov 26 2002 Michael Shigorin <mike@altlinux.ru> 0.10.6-alt1
- 0.10.6
- URL changed

* Fri Oct 11 2002 Michael Shigorin <mike@altlinux.ru> 0.10.4-alt1
- 0.10.4 (minor bugfixes)

* Fri Aug 30 2002 Dmitry V. Levin <ldv@altlinux.org> 0.10.1-alt2
- Fixed SMP build.
- Fixed interpackage dependencies.
- Fixed %%post/%%postun scripts.
- Automatically added buildrequires.

* Thu Aug 29 2002 Michael Shigorin <mike@altlinux.ru> 0.10.1-alt1
- 0.10.1 (fixes broken vanilla 0.10.0)

* Tue Aug 27 2002 Michael Shigorin <mike@altlinux.ru> 0.10.0-alt1
- 0.10.0
- libification (following upstream)
- last-minute author's fix

* Sat Mar 30 2002 Michael Shigorin <mike@altlinux.ru> 0.9.3-alt1
- built for ALT Linux

* Tue Jul 10 2001 David Necas (Yeti) <yeti@physics.muni.cz>
- changed rpm macros in Source and URL to autoconf macros to ease debian/
  stuff generation

* Sun May 20 2001 David Necas (Yeti) <yeti@physics.muni.cz>
- added BuildPrereq: bzip2-devel

* Wed May  2 2001 David Necas (Yeti) <yeti@physics.muni.cz>
- changed group to standard (but much less appropriate) Applications/Text
- rpm macros are used instead of autoconf macros (after the first definition)

* Sun Mar 11 2001 David Necas (Yeti) <yeti@physics.muni.cz>
- added defattr, doc attributes
- uses global configure cache
- heavy use of predefined directories
- configure moved to build section as is usual

* Sun Feb 25 2001 David Necas (Yeti) <yeti@physics.muni.cz>
- updated to enca-0.9.0pre4 (including files and descriptions)
- added sed dependency

* Sun Oct 25 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- updated to enca-0.7.5

* Sun Oct 11 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- removed redundant Provides: enca

* Sun Oct  1 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- updated to enca-0.7.1
- man page forced to be intstalled to ${prefix}/share/man

* Tue Sep 26 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- updated to enca-0.7.0
- spec autogenerated by configure

* Tue Sep 19 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- fixed not installing bcstocs

* Wed Sep 13 2000 David Necas (Yeti) <yeti@physics.muni.cz>
- first packaged (0.6.2)
