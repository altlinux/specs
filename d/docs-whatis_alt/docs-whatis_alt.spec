%setup_docs_module whatis_alt ru

Name: %packagename
Version: 0.1.3
Release: alt1

Summary: What is ALT Linux
Summary(ru_RU.KOI8-R): Что такое ALT Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replaces docs-whatis_alt-kirill
Provides: docs-whatis_alt-kirill
Obsoletes: docs-whatis_alt-kirill

Source: %name-%version.tar

%description
Very short description of ALT Linux: Team, Sisyphus project, distributions.

%description -l ru_RU.KOI8-R
Очень краткое описание ALT Linux: Team, проект Sisyphus, дистрибутивы.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "altlinux.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Mon Mar 02 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- fix web-links:
  + alt distros page: http://www.altlinux.ru/products/
  + join team page: http://www.altlinux.org/Join

* Fri Sep 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- replaced old freesource.info wiki links

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt2
- replaces docs-whatis_alt-kirill
  + added Provides/Obsoletes

* Sat Mar 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixes from cas@
  + removed alterator-packages & aptitude mention
  + replaced i18n with l10n
- added missing "." in %%description

* Sun Aug 12 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-whatis_alt-kirill package

* Fri Mar 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 060303-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051128-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Nov 29 2005 Kirill Maslinsky <kirill@altlinux.ru> 051128-alt1
- Auto rebuild with new version.

* Mon Oct 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 051017-alt1
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050901-alt1.1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050901-alt1.1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050901-alt1
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
