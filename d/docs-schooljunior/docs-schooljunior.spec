# Generated File.
%setup_docs_module schooljunior ru
Name: %packagename
Version: 0.1
Release: alt3

Summary: Open Systems and Free Software
Summary(ru_RU.KOI8-R): Открытые системы и свободные программы
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-schooljunior-kirill, alt-docs-extras-schooljunior
Provides: docs-schooljunior-kirill, alt-docs-extras-schooljunior
Obsoletes: docs-schooljunior-kirill, alt-docs-extras-schooljunior

Source: %name-%version.tar

%description
If you don't know what free software is, what is GNU, open source, open systems -- this book will help you in these basic terms for Linux community.

%description -l ru_RU.KOI8-R
Если вы не знаете, что такое свободное программное обеспечение, GNU, программы с открытым кодом, открытые системы, эта книга поможет вам разобраться в этих базовых понятиях и терминах, чрезвычайно важных для Linux-сообщества. В ней также освещаются основные идеи и технологии, легшие в основу архитектуры UNIX и прочих открытых систем (например, Linux). Кроме того, она будет полезна преподавателям информатики, поскольку здесь предложены некоторые идеи по построению курса информатики на основе свободного программного обеспечения на платформе Linux.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "schooljunior.xml" -- --stringparam tag-level1 book --stringparam tag-level2 chapter --stringparam tag-level3 section --stringparam toc.section.depth 1

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Thu Mar 12 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt3
- replaces alt-docs-extras-schooljunior
  + added Provides/Obsoletes

* Thu May 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-schooljunior-kirill
  + added Provides/Obsoletes

* Fri Jan 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-schooljunior-kirill package

* Mon Jul 16 2007 Kirill Maslinsky <kirill@altlinux.ru> 051028-alt2
- updated spec due to new rpm-build-docs

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051028-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Thu Nov 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051028-alt1
- rebuilt with correct parameters (now TOC looks fine)

* Thu Oct 27 2005 Kirill Maslinsky <kirill@altlinux.ru> 051021-alt2
- added parameters for correct toc generation

* Mon Oct 24 2005 Kirill Maslinsky <kirill@altlinux.ru> 051021-alt1
- Auto build with new version.

