%setup_docs_module rescue ru

Name: %packagename
Version: 0.4.6
Release: alt1

Summary: First aid
Summary(ru_RU.KOI8-R): Первая помощь
License: %gpl2plus

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-rescue-kirill
Provides: docs-rescue-kirill
Obsoletes: docs-rescue-kirill

Source: %name-%version.tar

%description
Some hints on solving problems during installation of ALT Linux and 
operation in rescue mode.

%description -l ru_RU.KOI8-R
Рекомендации по решению проблем, возникших при установке и загрузке ALT Linux и использование восстановительного режима.

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
* Thu Mar 05 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.4.6-alt1
- fix new 'rescue system' boot item name in 4.1
- fix module version in docinfo file

* Wed Mar 04 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.4.5-alt1
- add boot loader recovery procedure with separate /boot partition
  (thx Anton Nikolaevich Paramonov)

* Mon Sep 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.4-alt1
- fixed mount dir (#14079)

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.3-alt1
- more typos fixed

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.2-alt2
- replaces docs-rescue-kirill
  + added Provides/Obsoletes

* Sun Mar 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.2-alt1
- fixed typos and punctuation (thanks bertis@)

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4.1-alt1
- /sys also schould be mounted for lilo reinstall

* Wed Jan 30 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- better paraphrasing (thanks bertis@)

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- added xdriver and instdebug parameters description (#14191)

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + new bootloader restore algorithm

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-rescue-kirill package

* Fri Apr 07 2006 Kirill Maslinsky <kirill@altlinux.ru> 060407-alt1
- Auto rebuild with new version.

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050921-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt2
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- initial build
