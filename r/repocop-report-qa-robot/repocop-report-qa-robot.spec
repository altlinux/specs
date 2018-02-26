Name: repocop-report-qa-robot
Version: 0.34
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Repocop qa-robot mail reports.
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Source: %name-%version.tar

Conflicts: repocop < 0.34
Requires: repocop > 0.34
BuildRequires: repocop > 0.34

%description
Repocop is a repository unit tests platform.
This package provides tools for repocop mail reports.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_datadir/repocop-report-email/bin}
install -m755 qa-robot-repocop repocop-report-email repocop-report-qa-robot-* $RPM_BUILD_ROOT%_bindir/
install -m755 bin/* $RPM_BUILD_ROOT%_datadir/repocop-report-email/bin/

%files
%_bindir/repocop-report-qa-robot-*
%_bindir/repocop-report-email
%_bindir/qa-robot-repocop
%_datadir/repocop-report-email

%changelog
* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt3
- bugfix

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt2
- bugfix

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- added repocop-report-email

* Sun Jan 03 2010 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- split from main repocop package
