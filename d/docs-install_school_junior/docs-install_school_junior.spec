%setup_docs_module install_school_junior ru

Name: docs-install_school_junior
Version: 4.0
Release: alt3

Summary: Linux Junior Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке Линукс Юниор
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Linux Junior Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке Линукс Юниор.

%prep
%setup

%build
%docs_module_build "m-k" "index.m-k"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Mar 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt3
- remove docs-install-school from Provides/Obsoletes
- use hardcoded Name: in spec for better gear utilities support

* Fri Mar 06 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- fix headings in netinstall section
- edited last step description
- add note to bootloader section
- some rephrasings
- replace 'ye' with 'yo' & typo fixes
- add bios boot priority settings note

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1.1
- replaced wrong add_disks/packages/x11 screenshots
- fixed Version: in docinfo

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- new version scheme: version = branch
- school-4.0.0r1-linux-junior-i586-disk1-cd.iso screenshots
- placed botloader section to proper place (after package install)
- rewritten network section
- removed basesystem warning

* Fri Jun 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.2-alt1
- fixes from bertis@:
  + minorly edited (style and structure)
  + one typo fixed

* Fri Mar 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- fixed directory tree description needed for netinstall

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- typo and punctuation fixes (thanks bertis@)
- removed one more smc(www) mention

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- moved bootloader section to its proper place

* Wed Mar 05 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- step names are links now 

* Mon Feb 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt2
- removed ALT Linux mention

* Thu Feb 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- package renamed: docs-install-school -> docs-install_school_junior
- more detailed netinstall description (#14250)

* Mon Jan 28 2008 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt2
- package rebuilt
  + fixed missing heading & screenshot


* Wed Dec 19 2007 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + synchronized with latest beta (2007.12.17)
  + based on docs-install-junior.spec


