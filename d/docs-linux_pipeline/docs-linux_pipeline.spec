# Generated File.
%setup_docs_module linux_pipeline ru

Name: %packagename
Version: 0.1
Release: alt3

Summary: Input, output and pipeline
Summary(ru_RU.KOI8-R): Ввод, вывод и конвейер
License: %gpl2plus
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses

# replace docs-linux_pipeline-kirill
Provides: docs-linux_pipeline-kirill
Obsoletes: docs-linux_pipeline-kirill

Source: %name-%version.tar

%description
Section from Matt Welsh and others' book on Linux concerning inpput, output and pipeline in shell. Modularized.

%description -l ru_RU.KOI8-R
Раздел из книжки Уэлша и др. про перенаправление ввода/вывода в командной строке.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "pipeline.xml"

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
- fixed License:
  + FDL -> GPL

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-linux_pipeline-kirill
  + added Provides/Obsoletes

* Thu Jan 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_pipeline-kirill package

* Fri Mar 24 2006 Kirill Maslinsky <kirill@altlinux.ru> 060324-alt1
- Auto rebuild with new version.

* Tue Mar 14 2006 Kirill Maslinsky <kirill@altlinux.ru> 060314-alt1
- Auto rebuild with new version.

* Fri Mar 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 060302-alt1
- Initial build for Sisyphus.

