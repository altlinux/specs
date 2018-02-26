Name: repocop-unittest-vendor-tag
Version: 0.4
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
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/vendor-tag/done

mkdir -p %buildroot%_datadir/repocop/fixscripts/
install -p -m 644 %SOURCE1 %buildroot%_datadir/repocop/fixscripts/


%files
%dir %_datadir/repocop/pkgtests/vendor-tag/
%_datadir/repocop/pkgtests/vendor-tag/done
%_datadir/repocop/fixscripts/*

%changelog
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


