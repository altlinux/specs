%setup_docs_module packages_synaptic ru

Name: %packagename
Version: 0.2.2
Release: alt1

Summary: Short description of synaptic usage
Summary(ru_RU.UTF-8): Краткое описание использования программы synaptic
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Short description of synaptic usage.

%description -l ru_RU.UTF-8
Краткое описание использования программы synaptic.

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
- punctuation fixes (thanks bertis@)
- replaced "e" with "yo"

* Sun Mar 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- fixed synaptic name (as it appears in menu) (thanks cas@)

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + synaptic description shortened
  + syntax and typos fixed

* Sat Jul 28 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

