%setup_docs_module install_desktop ru

Name: docs-install_desktop
Version: 4.1
Release: alt9

Summary: ALT Linux Desktop Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке ALT Linux Desktop
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace old docs-install[0-2]-desktop, docs-installer_intro-kirill  packages
# rename docs-install-desktop_personal -> docs-install_desktop
Provides: docs-install0-desktop = %version
Provides: docs-install2-desktop = %version
Provides: docs-installer_intro-kirill = %version
Provides: docs-install-desktop_personal = %version

Obsoletes: docs-install0-desktop < %version
Obsoletes: docs-install2-desktop < %version
Obsoletes: docs-installer_intro-kirill < %version
Obsoletes: docs-install-desktop_personal < %version

Source: %name-%version.tar

%description
ALT Linux Desktop Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке ALT Linux Desktop.

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
* Sat Mar 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt9
- add docs-installer_intro-kirill to Obsolete list
- update Version in docinfo file

* Sat Mar 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt8
- fix Provides/Obsoletes list
- use hardcoded Name: for better gear utilities support

* Sun Mar 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt7
- fix Provides/Obsoletes list
- remove docs-install-desktop from Provides/Obsoletes list

* Thu Mar 05 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt6
- typo fixes
- emphasize paragraph before disk partitioning step
- remove basesystem warning
- fix version in docinfo

* Sat Jan 31 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt5
- added note about bios boot priority setting (#17905)

* Sat Jan 31 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- added recovery note to bootloader section (#18223)

* Sat Nov 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- updated to conform installer interface

* Tue Oct 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- removed "gui mode" checkbox mention (#17470)

* Thu Sep 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- new version scheme:
  + version = branch

* Mon Sep 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5.2-alt1
- fixed last step (quit) description
- punctuation fixes (thanks bertis@)

* Sun Sep 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5.1-alt1
- removed add_disks section
- new screenshots (altlinux-4.1.0-beta-20080819-desktop-i586-ru-dvd.iso)

* Wed Aug 27 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5-alt1
- updated to 4.1.0 beta stage
  + new screenshots (altlinux-4.1.0-beta-20080809-desktop-i586-ru-dvd.iso)
  + small description fixes
- fixed typos
- replaced 'ie' with 'io'

* Fri Mar 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- fixed directory tree description needed for netinstall

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- typo and punctuation fixes (thanks bertis@)
- removed one more smc(www) mention

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- moved bootloader section to its proper place

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2.1-alt1
- new packages screenshot
  + from altlinux-4.0.3-desktop-i586-install_ru-dvd5.iso

* Wed Mar 05 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- step names are links now

* Sat Mar 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- updated install description
  + conform to current installer (4.0.3)
  + new screenshots

* Wed Feb 27 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- package renamed: docs-install-desktop_personal -> docs-install_desktop
- more detailed netinstall description

* Tue Sep 04 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- new version
  + added mention of F1 for step-related help

* Mon Aug 20 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- new version
  + typo fixes
  + changed headings level in x11 section

* Tue Aug 14 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + mkbootflash mention

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-install-desktop package
  + typo and punctuation fixes
  + some rephrasings
  + screenshots from RC-20070809

