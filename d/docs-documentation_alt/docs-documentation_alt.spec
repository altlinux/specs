%setup_docs_module documentation_alt ru

Name: %packagename
Version: 0.1
Release: alt3

Summary: Documentation
Summary(ru_RU.KOI8-R): Документация
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-documentation_alt-kirill
Provides: docs-documentation_alt-kirill
Obsoletes: docs-documentation_alt-kirill

Source: %name-%version.tar

%description
Overview of documantation standard for Linux/UNIX and specific for ALT Linux.
Includes short list of recommended literature on Linux.

%description -l ru_RU.KOI8-R
Описание стандартной документации Linux/UNIX и специфической документации, доступной в дистрибутивах ALT. Содержит краткий рекомендательный список литературы по Linux.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "documentation.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt3
- replaces docs-documentation_alt-kirill
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- fixed previous %%changelog entry

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-documentation_alt-kirill package

* Tue Jun 19 2007 Kirill Maslinsky <kirill@altlinux.ru> 070619-alt1
- #12050 fixed (thanks azol@)
- spec updated

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051021-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 25 2005 Kirill Maslinsky <kirill@altlinux.ru> 051021-alt1
- Auto rebuild with new version.

* Tue Oct 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 051018-alt1
- Auto rebuild with new version.

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

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt1
- fixes in text for prerelease

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050316-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050316-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050316-alt1
- initial build
