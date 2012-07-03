%setup_docs_module install_school_lite ru

Name: %packagename
Version: 4.0
Release: alt2

Summary: Linux Lite Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке дистрибутива Лёгкий Линукс
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Linux Lite Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке дистрибутива Лёгкий Линукс.

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
* Fri Mar 06 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- fix headings in netinstall section
- edited last step description
- add note to bootloader section
- some rephrasings
- replace 'ye' with 'yo' & typo fixes
- add bios boot priority settings note

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1.2
- added better x11 screenshot

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1.1
- replaced wrong packages screenshot
- fixed Version in docinfo

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- new version scheme: version = branch
- school-4.0.0-linux-lite-i586-disk1-cd.iso screenshots
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
- updated install description
  + conform to current installer (lite-school-20080212)
  + new screenshots

* Tue Feb 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- initial build for Sisyphus
  + based on docs-install_lite package

