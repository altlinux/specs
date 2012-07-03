%setup_docs_module linux_ha_openvz ru
Name: %packagename
Version: 0.1
Release: alt1
Summary: High availability cluster with OpenVZ
Summary(ru_RU.UTF-8): Кластер высокой готовности с использованием OpenVZ
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-linux_ha_openvz-enp
Obsoletes: docs-linux_ha_openvz-enp

Source: %name-%version.tar

%description
Building high availability cluster with OpenVZ

%description -l ru_RU.UTF-8
Построение кластера высокой готовности с использованием OpenVZ

%prep
%setup

%build
%docs_module_build "tex" "index.tex"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Jul 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-linux_ha_openvz-enp -> docs-linux_ha_openvz
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Tue Sep 18 2007 Eugene Prokopiev <enp@altlinux.ru> 180907-alt1
- new version

* Mon Sep 17 2007 Eugene Prokopiev <enp@altlinux.ru> 170907-alt1
- initial build for Sisyphus
