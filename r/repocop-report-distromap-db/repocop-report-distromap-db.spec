Name: repocop-report-distromap-db
Version: 0.11
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop report script that dumps test results to prometeus format
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.54

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
%_bindir/repocop-report-distromap-db
#%_man1dir/repocop-report-prometeus-*

%changelog
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
