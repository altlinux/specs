# Generated File.
%setup_docs_module finding ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Finding
Summary(ru_RU.KOI8-R): Поиск
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-finding-boyarsh
Provides: docs-finding-boyarsh
Obsoletes: docs-finding-boyarsh

Source: %name-%version.tar

%description
in short about finding in filesystem as such and more detailed about find utility.

%description -l ru_RU.KOI8-R
Кратко о поиске в файловой системе как таковом и более подробно про использование find.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "finding.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-finding-boyarsh -> docs-finding
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050404-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050404-alt1
- Auto build with new version.

