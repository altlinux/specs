%setup_docs_module hd_structure ru

Name: %packagename
Version: 0.1.4
Release: alt1

Summary: Hard Disk Structure
Summary(ru_RU.KOI8-R): Структура жёсткого диска
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-hd_structure-kirill
Provides: docs-hd_structure-kirill
Obsoletes: docs-hd_structure-kirill

Source: %name-%version.tar

%description
Short description of hard disk structure: sertors, partitions, partition table.

%description -l ru_RU.KOI8-R
Краткое описание структуры жёсткого диска: сектора, разделы, таблица разделов.

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
* Wed Sep 03 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
- fixed NBER web link
- removed trailing whitespaces from License file

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- fixed typos
- replaced 'e' with 'io'

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt2
- replaces docs-hd_structure-kirill
  + added Provides/Obsoletes

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- replaced "e" with"yo"

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo fixes

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-hd_structure-kirill package

* Thu May 31 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 051012-alt3
- Rebuilt with new version from heap

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 051012-alt2
- New version from heap

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051012-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Wed Oct 12 2005 Kirill Maslinsky <kirill@altlinux.ru> 051012-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1
- Auto rebuild with new version.

* Wed Jul 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050720-alt1
- broken links fixed

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050716-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sat Jul 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050716-alt1
- initial build

