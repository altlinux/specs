Name: repocop-unittest-missing-url
Version: 0.1.5
Release: alt4

Summary: missing-url intergration tests for repocop test platform
Group: Development/Other
License: GPLv2+
Url: http://www.altlinux.org/Repocop

Source0: missing-url.sh

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

Requires: repocop >= 0.09-alt1

%description
missing-url intergration tests for repocop test platform.

%prep

%build

%install
mkdir -p %buildroot%_datadir/repocop/pkgtests/missing-url/
install -p -m 755 %SOURCE0 %buildroot%_datadir/repocop/pkgtests/missing-url/posttest

%files
%dir %_datadir/repocop/pkgtests/missing-url/
%_datadir/repocop/pkgtests/missing-url/posttest

%changelog
* Tue Oct 20 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt4
- tests declared as posttests

* Mon Sep 21 2009 Igor Zubkov <icesik@altlinux.org> 0.1.5-alt1
- remove repocop-* from ignore list
- add Url:

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1.4-alt1
- ignore design-alterator-*
- ignore design-bootloader-*
- ignore design-bootsplash-*
- ignore design-graphics-*
- ignore mithraen-*
- ignore docs-*
- ignore kde-settings-*
- ignore kde-styles-splash-*
- ignore apt-conf-*
- ignore altlinux-release-*
- ignore alt-notes-*

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- ignore alt-license-*

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1.2-alt1
- ignore xfce-settings-*
- ignore rpm-macros-*
- ignore rpm-build-*
- ignore indexhtml-*

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 0.1.1-alt1
- ignore alterator-*
- ignore branding-*
- ignore repocop-*

* Sun Jan 18 2009 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus



