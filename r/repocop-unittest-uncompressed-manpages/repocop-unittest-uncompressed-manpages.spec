Name: repocop-unittest-uncompressed-manpages
Version: 0.1
Release: alt2

Summary: uncompressed-manpages intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: uncompressed-manpages.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.09-alt1

%description
uncompressed-manpages intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/uncompressed-manpages/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/uncompressed-manpages/done

%files
%dir %_datadir/repocop/pkgtests/uncompressed-manpages/
%_datadir/repocop/pkgtests/uncompressed-manpages/done

%changelog
* Tue Sep 22 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt2
- add Url:

* Mon Jan 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus



