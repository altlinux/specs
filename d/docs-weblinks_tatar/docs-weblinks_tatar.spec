%setup_docs_module weblinks_tatar ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Web links to Tatar Internet Resources
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Web links to Tatar Internet Resources

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
* Thu May 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus


