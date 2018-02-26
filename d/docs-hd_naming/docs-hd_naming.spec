%setup_docs_module hd_naming ru

Name: %packagename
Version: 0.1.2
Release: alt1

Summary: Disk naming conventions in Linux
Summary(ru_RU.KOI8-R): Именование дисков и разделов в Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-hd_naming-kirill
Provides: docs-hd_naming-kirill
Obsoletes: docs-hd_naming-kirill

Source: %name-%version.tar

%description
Short description of hard disk and other storage devices naming conventions in Linux. General idea of device files.

%description -l ru_RU.KOI8-R
Краткое введение в схему именования жёстких дисков и прочих накопителей в Linux. Самое общее представление о файлах устройств.

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
* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- replaced 'e' with 'io'

* Tue Jun 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- cross-reference (hd_structure) fixed. (thanks bertis@)

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-hd_naming-kirill
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-hd_naming-kirill package

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

