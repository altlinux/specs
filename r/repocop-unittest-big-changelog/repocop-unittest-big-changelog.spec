Name: repocop-unittest-big-changelog
Version: 0.2
Release: alt4

Summary: big-changelog intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: big-changelog.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.09-alt1

%description
big-changelog intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/big-changelog/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/big-changelog/posttest

%files
%dir %_datadir/repocop/pkgtests/big-changelog/
%_datadir/repocop/pkgtests/big-changelog/posttest

%changelog
* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt4
- tests declared as posttests

* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt3
- tests declared as posttests

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.2-alt2
- add Url:

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.2-alt1
- fix #18605

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus
