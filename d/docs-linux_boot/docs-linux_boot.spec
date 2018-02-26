%setup_docs_module linux_boot ru

Name: %packagename
Version: 0.2
Release: alt1

Summary: Boot Setup
Summary(ru_RU.KOI8-R): Настройка загрузки
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace  docs-linux_boot-kirill
Provides:  docs-linux_boot-kirill
Obsoletes:  docs-linux_boot-kirill

Source: %name-%version.tar

%description
Linux boot process is described, also how to configure Linux bootloader for several operationg systems boot.

%description -l ru_RU.KOI8-R
Описан процесс загрузки Linux, настройка загрузчика Linux, в том числе для загрузки нескольких операционных систем.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "boot.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Fri Dec 05 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- made text distro neutral

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-linux_boot-kirill
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Wed Jul 25 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_boot-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060307-alt2
- New version from heap

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051017-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051017-alt2
- Auto rebuild with new version.

* Mon Oct 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 051017-alt1
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050921-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- initial build

