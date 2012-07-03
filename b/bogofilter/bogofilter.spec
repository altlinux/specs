Name: bogofilter
Version: 1.2.2
Release: alt1.2

Summary: Fast anti-spam filtering by Bayesian statistical analysis
Summary(ru_RU.CP1251): Ѕыстра€ фильтраци€ спама на основе статистической формулы Ѕайеса
Group: Networking/Mail
License: GPL
URL: http://bogofilter.sourceforge.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

%define gsl_ver 1.4

%define pkgdocdir %_docdir/%name-%version

Source: %name-%version.tar.bz2
Patch0: %name-0.96.4-alt-bogus-deps.patch

Requires: libgsl >= %gsl_ver

BuildRequires: OpenSP flex
BuildRequires: libgsl-devel >= %gsl_ver
BuildRequires: libdb4.7-devel 
BuildRequires: perl-Pod-Parser

%description
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms  (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

%description -l ru_RU.CP1251
Bogofilter Ч это фильтр дл€ спама на основе формулы Ѕайеса. ¬ обычном
режиме работы программа получает со стандартного ввода почтовое сообщение
или другой текст, выполн€ет статистическую проверку относительно списков
"хороших" и "плохих" слов, и возвращает код, показывающий €вл€етс€ ли
сообщение спамом или нет. Bogofilter спроектирован дл€ быстрой работы
(включа€ систему Berkeley DB), написан на C, и оптимизован дл€ скорости, так
что он может быть использован дл€ серверов, которые обрабатывают большое
количество почты.

%package utils
Summary: Bogofilter utilities
Group: Networking/Mail
Requires: %name = %version-%release pax
Provides: bogofilter-tuning
Obsoletes: bogofilter-tuning

%description utils
This package features various utilities to maintain bogofilter installations.
Bogofilter is a Bayesian spam filter using databases of "good" and "bad"
words for operation.

%package contrib
Summary: Scripts contributed to Bogofilter
Group: Networking/Mail
Requires: %name = %version-%release

AutoReq: yes, noperl

%description contrib
Helpful scripts contributed to the bogofilter package.
Bogofilter is a Bayesian spam filter.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-dependency-tracking \
    --with-database=db --disable-rpath
%make_build
%{?!_disable_check:%make check}

%install
%set_verify_info_method relaxed
%makeinstall
#cp $RPM_BUILD_ROOT%_sysconfdir/bogofilter.cf.example \
#   $RPM_BUILD_ROOT%_sysconfdir/bogofilter.cf

install -d -m755 $RPM_BUILD_ROOT%_libdir/%name
install -d -m755 $RPM_BUILD_ROOT%_libdir/%name/contrib
for f in $(find contrib -type f ! \( -name 'Makefile*' -o -name '*.c' -o -name '*.o' -o -name '*.Po' \)); do
    cp -p "$f" $RPM_BUILD_ROOT%_libdir/%name/contrib
done

install -d -m755 $RPM_BUILD_ROOT%pkgdocdir
ln -s %_licensedir/GPL-2 $RPM_BUILD_ROOT%pkgdocdir/COPYING
install -m644 AUTHORS GETTING.STARTED NEWS README RELEASE.NOTES TODO \
    $RPM_BUILD_ROOT%pkgdocdir/
install -m644 doc/*.html \
    $RPM_BUILD_ROOT%pkgdocdir/
install -m644 doc/integrating-with-* \
    $RPM_BUILD_ROOT%pkgdocdir/
install -m644 doc/README.db \
    $RPM_BUILD_ROOT%pkgdocdir/

%files
%dir %pkgdocdir
%pkgdocdir/COPYING
%pkgdocdir/AUTHORS
%pkgdocdir/GETTING.STARTED
%pkgdocdir/NEWS
%pkgdocdir/README*
%pkgdocdir/RELEASE.NOTES
%pkgdocdir/TODO
%pkgdocdir/*.html
%pkgdocdir/integrating-with-*
%_bindir/bogofilter
%_man1dir/bogofilter.1*
%_sysconfdir/bogofilter.cf.example
#%config(noreplace) %_sysconfdir/bogofilter.cf

%files utils
%_bindir/bf_*
%_bindir/bogolexer
%_bindir/bogotune
%_bindir/bogoupgrade
%_bindir/bogoutil
%_man1dir/bf_*
%_man1dir/bogolexer.1*
%_man1dir/bogotune.1*
%_man1dir/bogoupgrade.1*
%_man1dir/bogoutil.1*

%files contrib
%dir %_libdir/%name
%_libdir/%name/contrib

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.2
- Removed bad RPATH

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.2-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sun Feb 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Apr 05 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Nov 30 2008 Ilya Mashkin <oddity@altlinux.ru> 1.1.7-alt2
- rebuild with libdb-4.7

* Fri Aug 29 2008 Ilya Mashkin <oddity@altlinux.ru> 1.1.7-alt1
- new version: 1.1.7

* Mon Nov 19 2007 Ilya Mashkin <oddity@altlinux.ru> 1.1.5-alt1
- New stable version 1.1.5

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 1.1.3-alt1
- New version 1.1.3

* Sun Mar 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.2-alt1
- Release 1.0.2

* Sun Jan 22 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Thu Dec 01 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sun Nov 13 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.96.6-alt1
- 0.96.6

* Tue Nov 01 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.96.4-alt1
- 0.96.4
- Patch0 is obsolete

* Wed Oct 26 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.96.3-alt1
- 0.96.3

* Thu Oct 06 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.96.2-alt1
- 0.96.2
- Patch1 has gone upstream

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.95.2-alt2
- Correct unwrapping order for MIME encoded message parts [Patch1]

* Sat Jul 09 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.95.2-alt1
- New stable upstream release

* Tue Jun 21 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.94.14-alt1
- Updated to 0.94.14
- Patch1 is obsolete

* Fri Feb 11 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.92.8-alt2
- Build against libdb4.3 [Patch1]

* Tue Oct 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.92.8-alt1
- New stable upstream release

* Sat Aug 28 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.92.6-alt1
- New stable upstream release

* Sat Jul 03 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.92.0-alt1
- New stable upstream release

* Fri Apr 09 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.17.5-alt1
- New stable upstream release

* Fri Mar 05 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.16.4-alt3
- Requires libgsl >= 1.4, kudos to Egor Orlov at avalon.ru

* Fri Feb 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.16.4-alt2
- Rebuild against libdb4.2

* Sat Jan 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.16.4-alt1
- New stable upstream release

* Thu Jan 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.13.2-alt2
- Updated patch0 to prevent one more false dependency (bug #3562)
- Build contrib requires fully automatically
- tuning does not require procmail for operation

* Tue Jan 13 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.13.2-alt1
- New stable upstream release

* Wed Jan 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.13.1-alt1
- New stable upstream release

* Thu Jan 01 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.13-alt1
- New stable upstream release

* Thu Oct 23 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.15.7-alt1
- New stable upstream release

* Fri Sep 05 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.14.5.4-alt1
- New version

* Sun Aug 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.14.5.2-alt1
- New version

* Sun Jul 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.13.7.2-alt2
- Disabled perl dependencies for the contrib package

* Thu Jul 03 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.13.7.2-alt1
- New version
- Subpackaged tuning

* Fri Jun 06 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.13.6.2-alt1
- New version (see the release notes)
- Symlinked the license
- Do not install the default config file

* Sat Apr 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.2-alt1
- New version
- Descriptions from Alex Ott's bogofilter-0.11.1.5-alt1 package

* Wed Mar 26 2003 Mikhail Zabaluev <mhz@altlinux.ru> 0.11.1.3-alt1
- New version
- Doc list expansion
- Relocated contrib under /usr/lib, because it includes binaries nowadays
- Indirect invocation of qmail-inject for AutoReq to skip it [Patch0]

* Sat Dec 07 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.1.2-alt1
- Initial release based on the package from SourceForge
- Patch0: patch the lexer to exclude more random tokens, parse
  boundaries in conformance to RFC 2046
