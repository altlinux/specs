%setup_docs_module whatis_junior ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: What is ALT Linux 4.0 Junior
Summary(ru_RU.UTF-8): Что такое ALT Linux 4.0 Junior
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Description of ALT Linux 4.0 Junior distribution for customers.
No technical details.

%description -l ru_RU.UTF-8
Описание дистрибутива ALT Linux 4.0 Junior.
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
* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on http://www.altlinux.ru/company_news/junior_40_beta.html

