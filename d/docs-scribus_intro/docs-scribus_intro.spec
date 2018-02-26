# Generated File.
%setup_docs_module scribus_intro ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Scribus
Summary(ru_RU.KOI8-R): Scribus
License: %fdl
Url: http://www.linuxgraphics.ru/wiki/doku.php?id=openoffice-ru-2-scribus-about
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-scribus_intro-kirill
Provides: docs-scribus_intro-kirill
Obsoletes: docs-scribus_intro-kirill

Source: %name-%version.tar

%description
Introductory overview for Scribus publishing system: functionality, installation, usage.

%description -l ru_RU.KOI8-R
Вводный обзор Scribus: функциональность и использование.

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
* Tue Jun 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- typos and punctuation fixes from bertis@

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-scribus_intro-kirill
  + added Provides/Obsoletes

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-scribus_intro-kirill package

* Tue Jun 19 2007 Kirill Maslinsky <kirill@altlinux.ru> 060503-alt2
- change build format to m-k (closes #12070)
- spec updated

* Sat May 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060503-alt1
- Auto rebuild with new version.

* Thu Apr 27 2006 Kirill Maslinsky <kirill@altlinux.ru> 060426-alt1
- Initial build for Sisyphus

