Name: repocop-unittest-vendor-tag
Version: 0.6
Release: alt1

Summary: vendor-tag intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: vendor-tag.sh
Source1: vendor-tag.pl

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop > 0.55

%description
vendor-tag intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/vendor-tag/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/vendor-tag/posttest

mkdir -p %buildroot%_datadir/repocop/fixscripts/
install -p -m 644 %SOURCE1 %buildroot%_datadir/repocop/fixscripts/


%files
%dir %_datadir/repocop/pkgtests/vendor-tag/
%_datadir/repocop/pkgtests/vendor-tag/posttest
%_datadir/repocop/fixscripts/*

%changelog
* Thu Jul 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- new R::S::E syntax

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- made posttest

* Wed Nov 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- adapted for new fixscript syntax

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt2
- add Url:

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- rebuild

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- added fixscript
- reduced status to warning

* Sun Jan 18 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus


