Name: girar-nmu
Version: 1.03
Release: alt1
#Release: alt0.M51.1

Summary: git.alt client utilities for NMU automation
License: GPL
Group: Development/Other
Packager: Igor Vlasenko <viy@altlinux.org>
Url: http://www.altlinux.org/Git.alt/girar-nmu
#BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: gear, help2man
BuildRequires: perl-RPM perl-RPM-Source-Editor perl(Pod/Usage.pm) /usr/bin/pod2man
Requires: perl-RPM-Source-Editor >= 0.777

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
mkdir -p %buildroot%_bindir
install -m 755 girar-* rpm-sign-* %buildroot%_bindir/

for i in girar-*; do
    pod2man  --name $i --center 'girar-nmu utils' --section 1 --release %version $i > $i.1
done
mkdir -p %buildroot%_man1dir
install -m 644 girar-*.1 %buildroot%_man1dir/

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
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

