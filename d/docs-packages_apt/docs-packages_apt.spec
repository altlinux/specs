%setup_docs_module packages_apt ru

Name: %packagename
Version: 0.3
Release: alt1

Summary: Install and remove programs (packages)
Summary(ru_RU.KOI8-R): Установка и удаление программ (пакетов)
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-packages_apt-kirill
Provides: docs-packages_apt-kirill
Obsoletes: docs-packages_apt-kirill

Source: %name-%version.tar

%description
This is a guide for package management with APT/RPM. Term `package' is 
explained and some instructions on APT configuration are given. Here you 
will not find description of graphical frontends for APT.

%description -l ru_RU.KOI8-R
Руководство по работе с пакетами при помощи apt/rpm, содержит пояснения, что такое пакет, не содержит описания графических надстроек над apt. Приводятся некоторые инструкции по настройке apt.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "packages.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Mon Jan 25 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- add more ALT Linux repo information (Closes: #14032)

* Mon Sep 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- fixed backports footnote link (#17374)

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt2
- replaces docs-packages_apt-kirill
  + added Provides/Obsoletes

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- punctuation fixes (thanks bertis@)

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + removed Server specific apt-get/cache examples

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- inital build for Sisyphus
  + based on docs-packages_apt-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060313-alt2
- New version from heap

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Tue Dec 13 2005 Kirill Maslinsky <kirill@altlinux.ru> 051212-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051010-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt2
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050315-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050315-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt1
- initial build
