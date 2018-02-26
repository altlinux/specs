# Generated File.
%setup_docs_module free_and_open_source ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Software: right and freedom
Summary(ru_RU.KOI8-R): Программное обеспечение: право и свобода
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-free_and_open_source-kirill
Provides: docs-free_and_open_source-kirill
Obsoletes: docs-free_and_open_source-kirill

Source: %name-%version.tar

%description
Explaining purpose of open systems and free software. Relevant aspects of copyright law highlighted.

%description -l ru_RU.KOI8-R
Объяснение смысла свободного ПО и открытых систем. Растолковывается в необходимом объёме смысл авторского права.

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
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-free_and_open_source-kirill
  + added Provides/Obsoletes

* Wed Jan 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-free_and_open_source-kirill package

* Fri Apr 07 2006 Kirill Maslinsky <kirill@altlinux.ru> 060407-alt1
- Auto rebuild with new version.

* Mon Mar 13 2006 Kirill Maslinsky <kirill@altlinux.ru> 060313-alt1
- Auto rebuild with new version.

* Thu Feb 09 2006 Kirill Maslinsky <kirill@altlinux.ru> 060208-alt1
- Auto build with new version.

