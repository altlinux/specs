Name: repocop-report-distrodb
Version: 0.433
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPLv2+ or Artistic-2.0
Url: http://repocop.altlinux.org

Requires: repocop > 0.76
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
* Sat Nov 04 2023 Igor Vlasenko <viy@altlinux.org> 0.433-alt1
- new version

* Mon May 02 2022 Igor Vlasenko <viy@altlinux.org> 0.432-alt1
- new version

* Thu Dec 16 2021 Igor Vlasenko <viy@altlinux.org> 0.431-alt1
- new version

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 0.430-alt1
- added typelib db

* Thu Apr 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.429-alt1
- new version

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.428-alt1
- new version (unified subcomponent style in pkg-config)

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.427-alt1
- added vala vapi

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.426-alt1
- new version

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.425-alt1
- use repocop 0.77 api

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.424-alt1
- added themes

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.423-alt1
- docuwiki support

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.422-alt1
- added ocaml,nodejs

* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.421-alt1
- added golang

* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.420-alt1
- added gimp and cups support

* Sat Mar 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.419-alt1
- added aspell.raw

* Fri Mar 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.418-alt1
- added mono.raw and /usr/share/gnome-shell

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.417-alt1
- shared-share.raw -> shared-data.raw

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.416-alt1
- added shared-share.raw

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
