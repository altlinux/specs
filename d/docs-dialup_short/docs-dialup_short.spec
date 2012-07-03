# Generated File.
%setup_docs_module dialup_short ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Dialup connection to the Internet
Summary(ru_RU.KOI8-R): Удалённое подключение к Интернет по модему
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-dialup_short-kirill
Provides: docs-dialup_short-kirill
Obsoletes: docs-dialup_short-kirill

Source: %name-%version.tar

%description
Very short description of dialup configuration

%description -l ru_RU.KOI8-R
Очень краткое описание, как настроить dialup

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "dialup.xml"

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
- replaces docs-dialup_short-kirill
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-dialup_short-kirill package

* Fri Apr 07 2006 Kirill Maslinsky <kirill@altlinux.ru> 060407-alt1
- Auto rebuild with new version.

* Fri Mar 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 060303-alt1
- Auto rebuild with new version.

* Wed Jan 25 2006 Kirill Maslinsky <kirill@altlinux.ru> 060124-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050321-alt6.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt6
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050321-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- initial build
