Name: pgfouine
Version: 1.2
Release: alt2

Summary: PgFouine PostgreSQL log analyzer

BuildArch: noarch
License: GPL
Group: Development/Tools
Source0: %name-%version.tar
Source2: pgfouine-tutorial.txt
Url: http://pgfouine.projects.postgresql.org

Patch1: pgfouine-0.7-include_path.patch

%description
pgFouine is a PostgreSQL log analyzer. It generates text
or HTML reports from PostgreSQL log files. These reports
contain the list of the slowest queries, the queries that
take the most time and so on.

pgFouine can also:
- analyze VACUUM VERBOSE output to help you improve your
VACUUM strategy,
- generate Tsung sessions file to benchmark your
PostgreSQL server.

%prep
%setup -q
%patch1 -p0
sed -i 's!@INCLUDEPATH@!%_datadir/%name!' pgfouine_vacuum.php
sed -i 's!@INCLUDEPATH@!%_datadir/%name!' pgfouine.php

cp %SOURCE2 .

%build
%install

# creating required directories
install -m 755 -d %buildroot/%_datadir/%name
install -m 755 -d %buildroot/%_bindir

# installing pgFouine
for i in include version.php; do
	cp -rp $i %buildroot/%_datadir/%name/
done

install -m 755 pgfouine.php %buildroot/%_bindir/
install -m 755 pgfouine_vacuum.php %buildroot/%_bindir/

%files
%doc AUTHORS ChangeLog COPYING THANKS README pgfouine-tutorial.txt
%attr(0755, root, root) %_bindir/pgfouine.php
%attr(0755, root, root) %_bindir/pgfouine_vacuum.php
%_datadir/%name

%changelog
* Fri Aug 27 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2-alt2
- Real update to 1.2

* Tue Aug 10 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2-alt1
- 1.2

* Wed Nov 12 2008 Denis Klimov <zver@altlinux.ru> 1.0-alt1
- modify for ALT Linux

* Sat Mar 30 2007 Guillaume Smet <guillaume-pg@smet.org> - 1.0-1
- released 1.0
* Mon Dec 11 2006 Guillaume Smet <guillaume-pg@smet.org> - 0.7.2-1
- released 0.7.2
* Thu Nov 30 2006 Devrim Gunduz <devrim@CommandPrompt.com> - 0.7.1-2
- Added tutorial.txt per bugzilla review
* Sat Oct 28 2006 Guillaume Smet <guillaume-pg@smet.org> - 0.7.1-1
- released 0.7.1
* Sun Sep 3 2006 Guillaume Smet <guillaume-pg@smet.org> - 0.7-4
- fixed spec according to bugzilla #202901 comment #2
* Thu Aug 18 2006 Devrim Gunduz <devrim@CommandPrompt.com> - 0.7-3
- fixed spec, per bugzilla review
* Thu Aug 17 2006 Devrim Gunduz <devrim@CommandPrompt.com> - 0.7-2
- fixed rpmlint warnings, and made cosmetic changes
* Thu Aug 17 2006 Guillaume Smet <guillaume-pg@smet.org>
- released 0.7
* Thu Aug 10 2006 Guillaume Smet <guillaume-pg@smet.org>
- fixed RPM packaging for 0.7
* Wed Jul 19 2006 Guillaume Smet <guillaume-pg@smet.org>
- added pgfouine_vacuum.php
* Sun May 21 2006 Guillaume Smet <guillaume-pg@smet.org>
- released 0.6
* Sun Mar 26 2006 Guillaume Smet <guillaume-pg@smet.org>
- released 0.5
* Tue Jan 10 2006 Guillaume Smet <guillaume-pg@smet.org>
- released 0.2.1
* Sun Dec 4 2005 Guillaume Smet <guillaume-pg@smet.org>
- released 0.2
* Fri Nov 18 2005 Guillaume Smet <guillaume-pg@smet.org>
- initial RPM packaging
