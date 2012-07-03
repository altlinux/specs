%setup_docs_module filesystems_use ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Filesystems in use
Summary(ru_RU.KOI8-R): Работа с файловыми системами
License: %gpl2plus
Url: http://www.logic.ru/Russian/soft/ligs/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-filesystems_use-kirill
Provides: docs-filesystems_use-kirill
Obsoletes: docs-filesystems_use-kirill

Source: %name-%version.tar

%description
This document describes basic filesystem operations in Linux: mount/unmount
and consistency check (fsck). Sample fstab included. This document 
represents a part of ``Linux Installation and Getting Started'' by 
Matt Welsh et al. (in russian translation) with some additions and 
corrections from ALT specific documentation. 

%description -l ru_RU.KOI8-R
В документе описаны базовые операции с файловыми системами в Linux: монтирование и проверка целостности (fsck). Дан пример fstab. Документ представляет собой фрагмент из книги ``Руководство по установке и использованию системы Linux'' с некоторыми дополнениями из документации ALT Docs.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "filesystems.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-filesystems_use-kirill -> docs-filesystems_use
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050304-alt6.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt6
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050304-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050304-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt1
- initial build
