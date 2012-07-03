%setup_docs_module alterator_vm ru

Name: %packagename
Version: 0.1.6
Release: alt1

Summary: Disk partitions management by alterator
Summary(ru_RU.KOI8-R): Разбиение диска средствами программы установки
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-alterator_vm-kirill
Provides: docs-alterator_vm-kirill = 1.0-alt2
Obsoletes: docs-alterator_vm-kirill <= 1.0-alt2

Source: %name-%version.tar

%description
Description of disk partitioning module for alterator.

%description -l ru_RU.KOI8-R
Описание модуля разбиения жёсткого диска для alterator.

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
* Wed Nov 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.6-alt1
- distro neutral text

* Tue Sep 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.5-alt1
- replaced ie with io

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
- fixed typos

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt2
- replaces docs-alterator_vm-kirill
  + added Provides/Obsoletes
- added missing changelog entry: docs-alterator_vm-kirill 1.0-alt2

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- punctuation fixes (thanks bertis@)
- replaced "e" with "yo"

* Sat Mar 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fixed russian trackbar name (thanks cas@)
- added missing "." in %%description

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo and punctuation fixes

* Mon Jul 23 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1.1
- fixed link to hd_naming documentation module

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-alterator_vm-kirill package

* Thu May 31 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt2
- Rebuilt with new version from heap

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
