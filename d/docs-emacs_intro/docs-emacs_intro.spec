# Generated File.
%setup_docs_module emacs_intro ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Emacs for beginners
Summary(ru_RU.KOI8-R): Emacs для начинающих
License: %fdl
Url: http://xtalk.msk.su/~ott/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-emacs-intro-kirill
Provides: docs-emacs-intro-kirill = 051010-alt2.1
Obsoletes: docs-emacs-intro-kirill <= 051010-alt2.1

Source: %name-%version.tar

%description
Short introduction into Emacs possibilities and conviniencies.

%description -l ru_RU.KOI8-R
Краткое введение в возможности и удобства Emacs.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "emacs.xml"

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
- replaces docs-emacs-intro-kirill
  + added Provides/Obsoletes

* Mon Jan 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-emacs-intro-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051010-alt2.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Nov 15 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt2
- Auto rebuild with new version.

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto build with new version.

