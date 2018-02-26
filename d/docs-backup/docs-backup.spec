# Generated File.
%setup_docs_module backup ru

Name: %packagename
Version: 0.3
Release: alt8

Summary: Information backup
Summary(ru_RU.KOI8-R): Резервное копирование информации
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-backup-alenitchev
Provides: docs-backup-alenitchev
Obsoletes: docs-backup-alenitchev

Source: %name-%version.tar

%description
This document is addressed to those users who want to make backup of their 
information.

%description -l ru_RU.KOI8-R
Этот документ предназначен для пользователей Linux, желающих научиться самостоятельно выполнять резервное копирование информации своего компьютера.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "backup.xml" 

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt8
- replaces docs-backup-alenitchev
  + added Provides/Obsoletes

* Tue Apr 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt7
- initial build for Sisyphus
  + based on docs-backup-alenitchev package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.3-alt6.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt6
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt5.1.1.1
- Auto rebuild with new version.

* Tue Sep 27 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 0.3-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 0.3-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 11 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt1
- initial build

