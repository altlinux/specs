Name: repocop-report-distrodb
Version: 0.19
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.67
Obsoletes: repocop-report-distromap-db < 0.12

BuildRequires: perl-devel perldoc
BuildRequires: repocop

Source: %name-%version.tar

%description
Repocop is a repository unit tests platform.
%summary

%prep
%setup
rm -f *.spec

%build

%install
mkdir -p %buildroot/%_bindir
install -m 755 repocop-report-* %buildroot/%_bindir/
ln -s repocop-report-distrodb %buildroot/%_bindir/repocop-report-distromap-db

%files
#doc README ChangeLog
%_bindir/repocop-report-distromap-db
%_bindir/repocop-report-distrodb
#%_man1dir/repocop-report-prometeus-*

%changelog
* Sat Mar 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- libsocket-devel support

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt3
- bugfixes

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- Perinci-CmdLine-Any-Lumped provides nothing good

* Tue Oct 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- tex support

* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- no perl(CPANPLUS) in distrodb hack

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- support for repocop > 0.67

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added headers-rebased

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- bugfix release

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- extra db

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt4
- bugfix release

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt3
- bugfix release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt2
- bugfix release

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- internal version 5; added bin db

* Tue Jan 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- bugfix release

* Fri Jan 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- bugfix in path
- new python format

* Sat Dec 15 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- python db
- renamed to repocop-report-distrodb

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- perl provides support

* Fri May 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- gir format shortened

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- gir support; support for repo components

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt2
- bugfix release

* Sat Dec 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added srcname2binnames table

* Thu Dec 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- moved to distrodb

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- added /usr/share/pkgconfig to pkg-config db

* Mon Dec 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixed pkg-config db

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- bugfix

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added compactification

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added path db

* Fri Dec 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- fixed libs map

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added provides map

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- First build for Sisyphus.
