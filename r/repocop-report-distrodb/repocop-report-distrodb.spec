Name: repocop-report-distrodb
Version: 0.415
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
* Tue Mar 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.415-alt1
- php.raw cleanup

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.414-alt1
- xorg modules support in plugins

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.413-alt1
- added java.raw

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.412-alt1
- texmf w/o doc

* Sun Mar 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.411-alt1
- bugfix release

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- texlive 2017 support

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
