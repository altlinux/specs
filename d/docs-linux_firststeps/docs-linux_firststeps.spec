# Generated File.
%setup_docs_module linux_firststeps ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: First steps in Linux
Summary(ru_RU.KOI8-R): Первые шаги в системе Linux
License: %gpl2plus
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace docs-linux_firststeps-kirill
Provides: docs-linux_firststeps-kirill
Obsoletes: docs-linux_firststeps-kirill

Source: %name-%version.tar

%description
Section from textbook on command line interface basics: changing directories, simple operatons with files (copy, move, delete).

%description -l ru_RU.KOI8-R
Раздел учебника по основам работы в командной строке: перемещение по каталогам и простейшие операции с файлами (копирование, перемещение, удаление).

%prep
%setup

%build
%docs_module_build "DocBook/XML" "firststeps.xml"

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
- package renamed: docs-linux_firststeps-kirill -> docs-linux_firststeps
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)
- replaced License file: fdl -> gpl

* Mon Feb 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060202-alt1
- Auto build with new version.

