%setup_docs_module whatis_sb ru

Name: %packagename
Version: 4.1
Release: alt1

Summary: What is ALT Linux Small Business
Summary(ru_RU.UTF-8): Что такое ALT Linux Small Business
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Description of ALT Linux Small Business distribution for customers.
No technical details.

%description -l ru_RU.UTF-8
Описание дистрибутива ALT Linux Small Business.
Без технических подробностей, для пользователей/заказчиков.

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
* Sat Nov 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus
