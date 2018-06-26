Name: repocop-unittest-uncompressed-manpages
Version: 0.2
Release: alt1

Summary: uncompressed-manpages intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: uncompressed-manpages.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.73

%description
uncompressed-manpages intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/uncompressed-manpages/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/uncompressed-manpages/posttest

%files
%dir %_datadir/repocop/pkgtests/uncompressed-manpages/
%_datadir/repocop/pkgtests/uncompressed-manpages/posttest

%changelog
* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- changed to posttest

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt2
- add Url:

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus



