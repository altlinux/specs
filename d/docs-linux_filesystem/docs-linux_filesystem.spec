%setup_docs_module linux_filesystem ru

Name: %packagename
Version: 0.1.3
Release: alt2

Summary: Linux Filesystem Structure
Summary(ru_RU.KOI8-R): Структура файловой системы Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_filesystem-kirill
Provides: docs-linux_filesystem-kirill
Obsoletes: docs-linux_filesystem-kirill

Source: %name-%version.tar

%description
Main terms of Linux filesystem: file, directory, mount.

%description -l ru_RU.KOI8-R
Основные понятия файловой системы Linux: файл, каталог, монтирование.

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
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt2
- replaces docs-linux_filesystem-kirill
  + added Provides/Obsoletes

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- punctuation fixes (thanks bertis@)

* Mon Mar 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- replaced double quotes with <<>> ones (thanks cas@)
- added missing "." in %%description

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + tiny term fix

* Mon Jul 23 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_filesystem-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060313-alt2
- New version from heap

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Wed Jan 25 2006 Kirill Maslinsky <kirill@altlinux.ru> 060124-alt1
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

* Wed Jul 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050720-alt1
- broken links fixed

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050716-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sat Jul 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050716-alt1
- initial build

