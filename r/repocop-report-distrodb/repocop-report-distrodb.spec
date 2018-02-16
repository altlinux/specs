Name: repocop-report-distrodb
Version: 0.40
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.73
Obsoletes: repocop-report-distromap-db < 0.12
Requires: repocop-collector-buildreqs-subst

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

%files
#doc README ChangeLog
%_bindir/repocop-report-distrodb
%_bindir/repocop-report-helper-distrodb-preprocess
#%_man1dir/repocop-report-*

%changelog
* Fri Feb 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- php fixes

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- fixed raw pythons

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- restored sourceurl.raw

* Mon Dec 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- added requires.raw and added raw version 0

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- added sourceurl.raw

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- added exception for libgdiplus

* Wed Jul 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- python fixes

* Sat Jul 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- added base python

* Thu Jul 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- added raw php

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- added DependencyAnalyzer python

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- clean plugins

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- added plugins

* Fri Jun 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- added fonts

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- added static libs and kde*/qt* bin

* Thu Jun 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- pyegg fixes

* Fri May 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- added pyegg

* Mon May 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- correction for python3 so

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- new python3 path

* Fri Apr 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- support for buildreqs-subst

* Fri Mar 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- new version - cmake support

* Fri Mar 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- shell code moved to repocop-report-helper-distromap-db-preprocess

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
