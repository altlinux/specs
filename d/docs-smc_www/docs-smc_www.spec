%setup_docs_module smc_www ru

Name: %packagename
Version: 0.2
Release: alt2

Summary: Short description of System management center (www)
Summary(ru_RU.UTF-8): Краткое описание Центра управления системой (www)
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-smc_web-azol = 0.1-alt1
Obsoletes: docs-smc_web-azol

Source: %name-%version.tar

%description
Short description of System management center (www) functionality and usage.

%description -l ru_RU.UTF-8
Краткое описание возможностей и использования Центра управления системой (www).

%prep
%setup

%build
asciidoc -b html4 -f doc/html4.conf doc/index.txt
rm -f doc/html4.conf doc/index.txt
%docs_module_build "html" "index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Feb 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt2
- proofreading (thx Vladimir Zhukov)
- small rephrasing, typo fixes, browser warning

* Wed Nov 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- updated version

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo and punctuation fixes

* Thu Jul 26 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus 

