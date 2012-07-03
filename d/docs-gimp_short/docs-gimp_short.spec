# Generated File.
%setup_docs_module gimp_short ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Bitmap graphics editor Gimp
Summary(ru_RU.KOI8-R): Редактор растровой графики Gimp
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-gimp_short-kirill
Provides: docs-gimp_short-kirill = 050315-alt2.1
Obsoletes: docs-gimp_short-kirill <= 050315-alt2.1

Source: %name-%version.tar

%description
Short description of the Gimp functionality. Was not updated after 2Gimp .0 release. Excerpt from Maxim Ostavnov's book ``Free software applications at school''.

%description -l ru_RU.KOI8-R
Краткое описание возможностей The Gimp. Не обновлялось после выходя Gimp 2.0. Представляет собой фрагмент из книжки Максима Отставнова ``Прикладные и свободные программы и системы в школе''.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "thegimp.xml"

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
- replaces docs-gimp_short-kirill
  + added Provides/Obsoletes

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-gimp_short-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050315-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Nov 15 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt2
- Auto rebuild with new version.

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050315-alt1
- Auto build with new version.

