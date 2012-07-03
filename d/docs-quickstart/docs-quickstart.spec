%setup_docs_module quickstart ru

Name: %packagename
Version: 0.2.2
Release: alt1

Summary: Quickstart for beginners
Summary(ru_RU.UTF-8): Быстрый старт для начинающих
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-quickstart-azol = 4.0-alt1
Obsoletes: docs-quickstart-azol

Source: %name-%version.tar

%description
Quickstart for beginners.

%description -l ru_RU.UTF-8
Быстрый старт для начинающих.

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
* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- punctuation fixes
- removed smc(ww) mention

* Sun Mar 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- fixed synaptic name (as it appears in menu) (thanks cas@)
- fixed module passport
  + Title
  + Abstrac

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + typo and punctuation fixes
  + some rephrasings
  + added reference to ndiswrapper

* Sun Jul 29 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

