# Generated File.
%setup_docs_module inkscape_intro ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Inkscape overview
Summary(ru_RU.KOI8-R): Inkscape
License: %fdl
Url: http://www.linuxgraphics.ru/wiki/doku.php?id=openoffice-ru-2-inkscape-about
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-inkscape_intro-kirill
Provides: docs-inkscape_intro-kirill = 060503-alt2
Obsoletes: docs-inkscape_intro-kirill <= 060503-alt2

Source: %name-%version.tar

%description
Introductory overview for Inkscape: functionality, installation, further information. 

%description -l ru_RU.KOI8-R
Вводный обзор Inkscape: возможности, установка, справочная информация

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
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-inkscape_intro-kirill
  + added Provides/Obsoletes

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-inkscape_intro-kirill package

* Tue Jun 19 2007 Kirill Maslinsky <kirill@altlinux.ru> 060503-alt2
- change format in spec to m-k (fixes #12069)
- update spec

* Sat May 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060503-alt1
- Auto rebuild with new version.

* Thu Apr 27 2006 Kirill Maslinsky <kirill@altlinux.ru> 060426-alt1
- Initial build for Sisyphus

