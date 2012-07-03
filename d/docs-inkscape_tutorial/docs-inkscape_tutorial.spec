# Generated File.
%setup_docs_module inkscape_tutorial ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Inkscape tutorials (russian translation)
Summary(ru_RU.KOI8-R): Уроки по Inkscape
License: %fdl
Url: http://inkscape.org/doc/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-inkscape_tutorial-kirill
Provides: docs-inkscape_tutorial-kirill = 060517-alt1
Obsoletes: docs-inkscape_tutorial-kirill <= 060517-alt1

Source: %name-%version.tar

%description
Russian translation of several Inkscape tutorials. Originals are included with the program asregular Inkscape documents.

%description -l ru_RU.KOI8-R
Перевод нескольких уроков по Inkscape. Оригиналы (на английском языке) включены в саму программу и доступны в качестве обычных документов Inkscape.

%prep
%setup

%build
%docs_module_build "DocBook/XML" "tutorial.xml" -- --stringparam chunk.section.depth 2 --stringparam generate.section.toc.level 2 --stringparam chunk.first.sections 1


%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-inkscape_tutorial-kirill
  + added Provides/Obsoletes

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-inkscape_tutorial-kirill package

* Wed May 17 2006 Kirill Maslinsky <kirill@altlinux.ru> 060517-alt1
- Initial build for Sisyphus

