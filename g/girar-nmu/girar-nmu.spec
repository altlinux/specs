Name: girar-nmu
Version: 1.37
Release: alt1

Summary: git.alt client utilities for NMU automation
License: GPL
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
Url: http://www.altlinux.org/Git.alt/girar-nmu
#BuildArch: noarch

Source: %name-%version.tar

#BuildRequires: help2man
BuildRequires: perl-devel perl-podlators perl(RPM/Header.pm) perl-RPM-Source-Editor perl-RPM-Source-Convert perl(Pod/Usage.pm) perl(Date/Parse.pm) /usr/bin/pod2man perl-Gear-Rules
Requires: gear
Requires: perl-RPM-Source-Editor >= 0.894

%description
This package contains client utilities for git.alt
for NMU automation.

%prep
%setup
rm *.spec

%build
gcc -O2 %optflags -o girar-nmu-helper-pos-sort pos-sort.c

%install
#make_install install DESTDIR=%buildroot

mkdir -p %buildroot%perl_vendor_privlib/RPM/Source/Tools
install -m 644 GirarWriterPrototype.pm %buildroot%perl_vendor_privlib/RPM/Source/Tools/

mkdir -p %buildroot%_bindir
install -m 755 girar-* rpm-sign-* srpmlschangelog %buildroot%_bindir/

for i in girar-* srpmlschangelog; do
    pod2man  --name $i --center 'girar-nmu utils' --section 1 --release %version $i > $i.1 ||:
done
find . -name '*.1' -size 0 -print -delete
mkdir -p %buildroot%_man1dir
install -m 644 girar-*.1 %buildroot%_man1dir/

%files
%doc README
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/RPM*

%changelog
* Mon Jan 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- use new R::S::E interface

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- use RPM::Header

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- updated BR:

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- rest of fixes for interface changes in R::S::E Transform 16

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- fixes for interface changes in R::S::E Transform 16

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- more verbose debug for marked files

* Wed Jan 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- added buildfrom-rpm-marked opt to girar-nmu-sort-transaction

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- added girar-nmu-helper-task-add-rebuild

* Sun Nov 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- <before_subtask_id> support in girar-nmu-helper-git-push-build

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- improved debug output in girar-nmu-sort-transaction

* Fri Nov 13 2015 Ivan Zakharyaschev <imz@altlinux.org> 1.27-alt2
- girar-nmu-helper-clone-and-setup-build-commit: configure the remote
  in a standard way (like "git remote add" does; ALT#31482).
- minor tweaks in the code:
  - factored out git://git.altlinux.org/gears and
    git://git.altlinux.org/srpms as variables (to become environment
    parameters in future).
  - typo in documentation.

* Thu Oct 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- <before_subtask_id> support in girar-nmu-helper-task-add-srpm

* Tue Oct 13 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.26-alt1
- girar-nmu-helper-task-add-git: fixed typo.

* Sat Aug 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- support for girar and gitery

* Sun Dec 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- new version

* Thu Dec 11 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- new version

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- new version

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- new version

* Wed Nov 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- bugfix release

* Sun Oct 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- bugfix release thanks to glebfm@ (closes: #30371)

* Fri Sep 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- new version

* Sat Jun 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- use Gear::Rules library

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- new version

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- new utility girar-backport-prepare

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt3
- bugfix release

* Sun May 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt2
- bugfix release

* Sun May 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- new version

* Wed Apr 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- stable release

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- fixes in cycle detection

* Thu Mar 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- ported --buildreq for new relations set

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- another bugfix in sort-transaction (thanks to aris@)

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- bugfix in sort-transaction (thanks to aris@)

* Sat Dec 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- better python sypport

* Sat Dec 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- new version, requires new RPM-Source-Editor

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- maintainance release

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- new version thanks to mithraen@

* Mon Jun 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- new version thanks to mithraen@

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- new version

* Mon Jan 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- new version

* Fri Dec 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- new version

* Thu Nov 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- new utils:
	girar-print-build-commit
	girar-nmu-filter-name

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- new version

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt6
- girar-nmu-sort-transaction: updated man page (thanks to aris@).

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt5
- bugfix release

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt4
- bugfix release

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt3
- fixes in girar-nmu-helper-push-build

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt2
- bugfix release

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt0.M51.1
- backport

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- new version

* Fri Jan 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.95-alt0.M51.1
- M51 backport

* Fri Jan 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- bugfix release

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt0.M51.1
- M51 backport

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- Release Candidate 4

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.93-alt0.M51.1
- M51 backport

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- Release Candidate 3

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.92-alt0.M51.1
- M51 backport

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- Release Candidate 2

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.91-alt0.M51.1
- M51 backport

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- girar-nmu-local-build: added -f option.
- safe girar-clone-build-commit.

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 0.90-alt0.M51.1
- M51 backport

* Sat Nov 20 2010 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- RC1

* Thu Nov 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- girar-fetch-build-commit, man pages, etc.

* Tue Nov 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- use remote git clone when possible; new options, etc.

* Mon Nov 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- refined documentation

* Fri Nov 12 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- implemented cycle breaking

* Tue Nov 09 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- sort: preliminary support of breaking cycles

* Fri Nov 05 2010 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- sort: support of transaction subset

* Thu Nov 04 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- print separate cycle components

* Thu Nov 04 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- bugfix release

* Thu Nov 04 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- bugfix release

* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix release

* Wed Nov 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added bunch of helper utilities

* Tue Nov 02 2010 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- fix in sort utility

* Mon Oct 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix (thanks to @mithraen)

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added --ignore-extra-rpms option

* Sat Oct 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added rpm-sign-no-passphrase

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fix in rpm-sign-gpg-agent

* Tue Sep 14 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added rpm-sign-gpg-agent

* Mon Sep 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- girar-nmu -> girar-nmu-prepare

* Mon Sep 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added utilities to sort packages in transaction

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added girar-nmu-git-commit-push-build utility

* Wed Jun 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first prerelease w/o documentation

