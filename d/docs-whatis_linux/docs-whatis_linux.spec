%setup_docs_module whatis_linux ru

Name: %packagename
Version: 0.1.5
Release: alt1

Summary: What is Linux
Summary(ru_RU.KOI8-R): Что такое Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-whatis_linux-kirill
Provides: docs-whatis_linux-kirill = 051017-alt1.1
Obsoletes: docs-whatis_linux-kirill <= 051017-alt1.1

Source: %name-%version.tar

%description
The shortest introduction in Linux, some basic terms: free software, 
distribution, open source development model in a few paragraphs.

%description -l ru_RU.KOI8-R
Кратчайшее введение в Linux: понятие свободного ПО, дистрибутива, модели разработки в нескольких абзацах.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "linux.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Fri Sep 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.5-alt1
- typo and style fixes from bertis@ 

* Wed Sep 03 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
- fixed two typos

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- used russian gnu.org homepage link

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt2
- replaces docs-whatis_linux-kirill
  + added Provides/Obsoletes

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fixed punctuation (thanks bertis@)

* Sat Mar 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed product names (thanks cas@)

* Sun Aug 12 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-whatis_linux-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051017-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

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
