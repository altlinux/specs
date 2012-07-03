Name: repocop-unittest-invalid-url
Version: 0.3
Release: alt4

Summary: invalid-url intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: invalid-url.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.09-alt1

%description
invalid-url intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/invalid-url/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/invalid-url/posttest

%files
%dir %_datadir/repocop/pkgtests/invalid-url/
%_datadir/repocop/pkgtests/invalid-url/posttest

%changelog
* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.3-alt4
- tests declared as posttests

* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt2
- add Url:

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.3-alt1
- rebuild

* Sun Jan 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- reduced message level
- fixed bug

* Sun Jan 18 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus


