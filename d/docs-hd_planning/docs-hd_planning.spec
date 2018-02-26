%setup_docs_module hd_planning ru

Name: %packagename
Version: 0.1.5
Release: alt1

Summary: Hard disk planning
Summary(ru_RU.KOI8-R): Планирование диска
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-hd_planning-kirill
Provides: docs-hd_planning-kirill
Obsoletes: docs-hd_planning-kirill

Source: %name-%version.tar

%description
Basic information about Linux filesystem and working with hard disks in Linux, that is required to install Linux.

%description -l ru_RU.KOI8-R
Начальные сведения о планировании диска для Linux: размещение фрагментов файловой системы на разных разделах.

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
* Fri Jan 29 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.1.5-alt1
- remove noexec recommendation for /var (Closes #22184)

* Thu Sep 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
- updated for desktop systems (thanks bertis@)

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- fixed typos
- replaced 'e' with 'io'

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt2
- replaces docs-hd_planning-kirill
  + added Provides/Obsoletes

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- replaced "e" with "yo"

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo fixes

* Wed Jul 18 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-hd_planning-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060307-alt2
- New version from heap

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
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

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sat Jul 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt1
- initial build

