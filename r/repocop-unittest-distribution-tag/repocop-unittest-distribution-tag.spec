Name: repocop-unittest-distribution-tag
Version: 0.4
Release: alt1

Summary: distribution-tag intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: distribution-tag.sh
Source1: distribution-tag.pl

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop > 0.55

%description
distribution-tag intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/distribution-tag/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/distribution-tag/posttest

mkdir -p %buildroot%_datadir/repocop/fixscripts/
install -p -m 644 %SOURCE1 %buildroot%_datadir/repocop/fixscripts/


%files
%dir %_datadir/repocop/pkgtests/distribution-tag/
%_datadir/repocop/pkgtests/distribution-tag/posttest
%_datadir/repocop/fixscripts/*

%changelog
* Wed Nov 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- adapted for new fixscript syntax

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4
- tests declared as posttests

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt2
- add Url:

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- rebuild

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- added fixscript
- reduced status to warning

* Sun Jan 18 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus


