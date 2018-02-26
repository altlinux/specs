%setup_docs_module coreutils ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Short description of coreutils
Summary(ru_RU.KOI8-R): Путеводитель по coreutils
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-coreutils-boyarsh
Provides: docs-coreutils-boyarsh = 050316-alt7
Obsoletes: docs-coreutils-boyarsh <= 050316-alt7

Source: %name-%version.tar

%description
Short description of utilities included in coreutils package with some 
examples of the effective usage.

%description -l ru_RU.KOI8-R
Краткое описание программ из пакета coreutils и возможных способов их
применения.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "coreutils.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-coreutils-boyarsh
  + added Provides/Obsoletes

* Tue Dec 25 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-coreutils-boyarsh package

* Wed Jun 06 2007 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt7
- small fixes (thanks php-coder@)
  + fixed typo in package description/docinfo (#11856)
  + spec updated according to new rpm-build-docs trends

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050316-alt6.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt6
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050316-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050316-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt1
- initial build
