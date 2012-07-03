# Generated File.
%setup_docs_module corpnet ru
Name: %packagename
Version: 0.1
Release: alt1

Summary: Corporative network organization
Summary(ru_RU.KOI8-R): Организация корпоративной сети
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-corpnet-kirill
Provides: docs-corpnet-kirill
Obsoletes: docs-corpnet-kirill

Source: %name-%version.tar

%description
recommandations for corporative network organization on Linux platform.

%description -l ru_RU.KOI8-R
Рекомендации по организации корпоративной сети на базе Linux

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "corpnet.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Thu May 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-corpnet-kirill -> docs-corpnet
- build with rpm-build-docs-experimental
- used macro for License tag  (rpm-build-licenses)

* Wed May 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060524-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051114-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051114-alt1
- Auto build with new version.

