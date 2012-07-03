# Generated File.
%setup_docs_module zsh_intro ru

Name: %packagename
Version: 0.1.1
Release: alt1

Summary: Zsh command processor
Summary(ru_RU.KOI8-R): Командный процессор Zsh
License: distributable
Url: http://xtalk.msk.su/~ott/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3

# replace docs-ZshIntro-kirill
Provides: docs-ZshIntro-kirill = 050407-alt1.1
Obsoletes: docs-ZshIntro-kirill <= 050407-alt1.1

Source: %name-%version.tar

%description
Concise survey of Zsh.

%description -l ru_RU.KOI8-R
небольшой обзор командного процессора Zsh

%prep
%setup

%build
%docs_module_build "DocBook/XML" "zsh_intro.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Sep 02 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- fixed module description (Abstract: in docinfo)

* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-ZshIntro-kirill
  + added Provides/Obsoletes

* Wed Feb 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-ZshIntro-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050407-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050407-alt1
- Auto build with new version.

