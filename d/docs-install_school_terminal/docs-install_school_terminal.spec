%setup_docs_module install_school_terminal ru

Name: docs-install_school_terminal
Version: 4.0
Release: alt1

Summary: Linux Terminal Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке Линукс Терминал
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Linux Terminal Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке Линукс Терминал.

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
* Fri Mar 06 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt1
- initial build for Sisyphus
  + based on docs-install_school_junior package
  
