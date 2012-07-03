%setup_docs_module install_school_master ru

Name: %packagename
Version: 4.0
Release: alt2

Summary: Linux Master Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке Линукс Мастер
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Linux Master Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке Линукс Мастер.

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
* Fri Mar 06 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.0-alt2
- initial build for Sisyphus
  + based on docs-install_school_junior package
  
