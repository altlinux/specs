# Generated File.
%setup_docs_module print_cups ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Print subsystem (Cups)
Summary(ru_RU.KOI8-R): Подсистема печати (Cups)
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-print_cups-kirill
Provides: docs-print_cups-kirill
Obsoletes: docs-print_cups-kirill

Source: %name-%version.tar

%description
Description of Linux print subsystem: main printing concepts, printer
types, spoolers. Cups configuration with web interface and with foomatic.

%description -l ru_RU.KOI8-R
Описание подсистемы печати Linux: основные понятия печати, типы принтеров, спулеры. Настройка cups через web-интерфейс и через foomatic.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "print.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-print_cups-kirill
  + added Provides/Obsoletes

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-print_cups-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060307-alt2
- New version from heap

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Sat Jan 21 2006 Kirill Maslinsky <kirill@altlinux.ru> 060121-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051017-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Oct 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 051017-alt1
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt1
- fixes in text for prerelease

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050420-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050420-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050420-alt2
- rebuild with new rpm-build-docs.

* Wed Apr 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050420-alt1
- removed mention: obsolete package cups-drivers

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050328-alt1
- initial build
