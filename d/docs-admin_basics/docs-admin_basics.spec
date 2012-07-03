# Generated File.
%setup_docs_module admin_basics ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: System administration basics
Summary(ru_RU.KOI8-R): Основы администрирования
License: %gpl2plus

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace docs-admin_basics-kirill
Provides:  docs-admin_basics-kirill
Obsoletes:  docs-admin_basics-kirill

Source: %name-%version.tar

%description
This document describes basic Linux administration issues that every user 
should be aware of. In particular that you shouldn't perform dayly tasks 
as root, you may use sudo utility to get root permissions. Introduction 
to the Linux system logs is included.

%description -l ru_RU.KOI8-R
Текст содержит основные положения об администрировании Linux, которые должен знать каждый пользователь. В частности, что не нужно работать под root, описание sudo. Кроме того даётся представление о системных журналах (log).

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "admin-basics.xml"

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
- replaces  docs-admin_basics-kirill
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-admin_basics-kirill package

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051012-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Wed Oct 12 2005 Kirill Maslinsky <kirill@altlinux.ru> 051012-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050919-alt1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050919-alt1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt5.1
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
