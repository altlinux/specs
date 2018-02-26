%setup_docs_module backup_before_install ru

Name: %packagename
Version: 0.1.2
Release: alt1

Summary: Backup Before Linux Installation
Summary(ru_RU.KOI8-R): Сохранение данных и меры предосторожности перед установкой ALT Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6
BuildRequires: alt-entities >= 0.11

# replace docs-backup_before_install-kirill
Provides: docs-backup_before_install-kirill
Obsoletes: docs-backup_before_install-kirill

Source: %name-%version.tar

%description
Short recommendations on backup and other security measures that should be done before Linux installation.

%description -l ru_RU.KOI8-R
Краткие рекомендации по мерам предосторожности, которые следует предпринять перед установкой Linux.

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
* Wed Sep 03 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fixed three typos
- edited module passport / spec
  * edited Title: in docinfo / Summary in spec
  * removed trailing whitespaces in License file

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt2
- replaces docs-backup_before_install-kirill
  + added Provides/Obsoletes

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo fixes

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-backup_before_install-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050919-alt1.1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050919-alt1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050919-alt1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt2.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sat Jul 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt1
- initial build

