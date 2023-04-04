Name: bogofilter
Version: 1.2.5
Release: alt2

Summary: Fast anti-spam filtering by Bayesian statistical analysis
Summary(ru_RU.CP1251): Ѕыстра€ фильтраци€ спама на основе статистической формулы Ѕайеса
Group: Networking/Mail
License: GPL-2.0-or-later AND GPL-3.0-only
URL: http://bogofilter.sourceforge.net/

Packager: Ilya Mashkin <oddity@altlinux.ru>

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Source0: %name-%version.tar
Patch0001: 0001-ALT-Hide-qmail-inject-from-dependency-search-because.patch
Patch0002: 0002-DEBIAN-Make-bf_tar-use-tar-instead-of-pax-to-drop-de.patch

Requires: %name-bdb
Requires: %name-doc

BuildRequires(pre): rpm-macros-alternatives

BuildRequires: flex
BuildRequires: libgsl-devel >= 1.4
BuildRequires: libdb4.7-devel
BuildRequires: libsqlite3-devel
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

%package bdb
Summary: Fast anti-spam filtering by Bayesian statistical analysis with Berkeley DB backend
Group: Networking/Mail

Requires: %name-common = %EVR
Provides: %name-backend = %EVR

Provides: bogofilter-tuning
Obsoletes: bogofilter-tuning

Provides: bogofilter-utils = %EVR
Obsoletes: bogofilter-utils <= 1.2.5-alt1

%description bdb
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms  (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

This package contains %name build with the Berkeley DB backend.


%package sqlite
Summary: Fast anti-spam filtering by Bayesian statistical analysis with SQLite backend
Group: Networking/Mail

Provides: %name-backend = %EVR
Requires: %name-common = %EVR

%description sqlite
Bogofilter is a Bayesian spam filter.  In its normal mode of
operation, it takes an email message or other text on standard input,
does a statistical check against lists of "good" and "bad" words, and
returns a status code indicating whether or not the message is spam.
Bogofilter is designed with fast algorithms  (including Berkeley DB system),
coded directly in C, and tuned for speed, so it can be used for production
by sites that process a lot of mail.

This package contains %name build with the sqlite3 backend.


%package common
Summary: Common files for Bogofilter
Group: Networking/Mail
BuildArch: noarch

%description common
This package contains shared files for various %name backends


%package contrib
Summary: Scripts contributed to Bogofilter
Group: Networking/Mail
BuildArch: noarch
Requires: %name-backend = %version-%release

AutoReq: yes, noperl, noshell

%description contrib
Helpful scripts contributed to the bogofilter package.
Bogofilter is a Bayesian spam filter.


%package doc
Summary: Bogofilter documentation
Group: Networking/Mail
BuildArch: noarch

%description doc
This package contains the documentation of bogofilter.

%prep
%setup -q
%autopatch -p2

%build
%define _configure_script ../configure

build()
{
	local flavour=$1; shift

	mkdir -p build-$flavour
	cd build-$flavour

	%configure \
		--disable-dependency-tracking \
		--disable-rpath \
		"$@" ||
		return $?

	%make_build ||
		return $?
	cd -
}

mkdir -p build-common
cd build-common
%configure
cd -

build bdb    --program-suffix=-bdb    --with-database=db
build sqlite --program-suffix=-sqlite --with-database=sqlite

%install
%define _makeinstall_target install-exec-recursive

%makeinstall_std -C build-common/doc install

mkdir -p --  $RPM_BUILD_ROOT%_altdir
for o in bdb sqlite; do
	%makeinstall_std -C "build-$o" \
		mandir="/.ignore"
	{
		printf '%%s\t%%s\t1\n' "%_bindir/bogofilter" "%_bindir/bogofilter-$o"
		find "$RPM_BUILD_ROOT%_bindir" -type f \
			\( -name "*-$o" -a \! -name "bogofilter-$o" \) \
			-printf '%%f\n' | sort |
			sed -re 's|(.*)-([^-]+)$|%_bindir/\1\t%_bindir/&\t%_bindir/bogofilter-\2|'
	} > "$RPM_BUILD_ROOT%_altdir/%name-$o"
done
rm -rf -- "$RPM_BUILD_ROOT/.ignore"

mkdir -p -m755 -- $RPM_BUILD_ROOT%_datadir/%name/contrib
find contrib -type f \
	! \( -name 'Makefile*' -o -name '*.[co]' -o -name '*.Po' \) \
	-execdir cp -pt "$RPM_BUILD_ROOT%_datadir/%name/contrib" -- '{}' '+'

%check
%make -C build-bdb check
%make -C build-sqlite check

%files

%files common
%_sysconfdir/bogofilter.cf.example
%_man1dir/bogofilter.1*
%_man1dir/bf_*.1*
%_man1dir/bogolexer.1*
%_man1dir/bogotune.1*
%_man1dir/bogoupgrade.1*
%_man1dir/bogoutil.1*

%files bdb
%_altdir/bogofilter-bdb
%_bindir/bogofilter-bdb
%_bindir/bf_compact-bdb
%_bindir/bf_copy-bdb
%_bindir/bf_tar-bdb
%_bindir/bogolexer-bdb
%_bindir/bogotune-bdb
%_bindir/bogoupgrade-bdb
%_bindir/bogoutil-bdb

%files sqlite
%_altdir/bogofilter-sqlite
%_bindir/bogofilter-sqlite
%_bindir/bf_compact-sqlite
%_bindir/bf_copy-sqlite
%_bindir/bf_tar-sqlite
%_bindir/bogolexer-sqlite
%_bindir/bogotune-sqlite
%_bindir/bogoupgrade-sqlite
%_bindir/bogoutil-sqlite

%files contrib
%_datadir/%name

%files doc
%doc AUTHORS COPYING GETTING.STARTED NEWS README RELEASE.NOTES TODO
%doc doc/*.html doc/integrating-with-* doc/README.*

%changelog
* Sun Apr 02 2023 Alexey Gladkov <legion@altlinux.ru> 1.2.5-alt2
- Split package by database backends (Berkeley DB and SQLite).
- Put all utilites in the single package.
- Add alternative for utilities to be able to install them in parallel.
- Make bf_tar use tar instead of pax.
- Move contrib to _datadir.
- Move docs in to separate package.
- Fix License tag.

* Sun Mar 28 2021 Ilya Mashkin <oddity@altlinux.ru> 1.2.5-alt1
- 1.2.5

* Thu Aug 15 2013 Ilya Mashkin <oddity@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Sat Feb 09 2013 Ilya Mashkin <oddity@altlinux.ru> 1.2.3-alt1
- 1.2.3

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
