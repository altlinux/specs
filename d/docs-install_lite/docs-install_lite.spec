%setup_docs_module install_lite ru

Name: %packagename
Version: 4.0
Release: alt3

Summary: ALT Linux Lite Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке ALT Linux Lite
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# rename: docs-install-desktop_lite -> docs-install_lite
Provides: docs-install-desktop_lite = %version
Obsoletes: docs-install-desktop_lite < %version

Source: %name-%version.tar

%description
ALT Linux Lite Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке ALT Linux Lite.

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
* Sun Mar 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt3
- fix Provides/Obsoletes list

* Thu Mar 05 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- fix headings in netinstall section
- edited last step description
- add note to bootloader section
- some rephrasings
- replace 'ye' with 'yo' & typo fixes
- add bios boot priority settings note

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1.1
- replaced wrong add_disks/packages screenschots
- fixed Version in docinfo

* Sun Feb 08 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- new version scheme: version = branch
- altlinux-4.0.2-lite-i586-install-cd.iso screenshots
- rewritten network section
- removed basesystem warning

* Fri Jun 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.2-alt1
- fixes from bertis@:
  + minorly edited (style and structure)
  + one typo fixed

* Wed May 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt2
- fixed distro name in Summary and description

* Fri Mar 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- fixed directory tree description needed for netinstall

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- typo and punctuation fixes (thanks bertis@)
- removed one more smc(www) mention

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- moved bootloader section to its proper place

* Wed Mar 05 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- updated install description
  + conform to current installer (lite-i586-20080212)

* Tue Feb 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- package renamed: docs-install-desktop_lite -> docs-install_lite
- more detailed netinstall description

* Wed Dec 12 2007 Vladimir Zhukov <bertis@altlinux.ru> 0.1-alt2
  - package rebuilt
    + added screenshots from redesigned 20071205 beta               

* Fri Nov 23 2007 Vladimir Zhukov <bertis@altlinux.org> 0.1-alt1
  - initial build
    spec based on docs-install-desktop_personal by azol@

