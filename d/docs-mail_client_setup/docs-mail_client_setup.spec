# Generated File.
%setup_docs_module mail_client_setup ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Mail client setup
Summary(ru_RU.KOI8-R): Настройка почтового клиента
License: %fdl
Url: http://heap.altlinux.ru/kirill/mail_client_setup/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-mail_client_setup-kirill
Provides: docs-mail_client_setup-kirill
Obsoletes: docs-mail_client_setup-kirill

Source: %name-%version.tar

%description
Short instruction on mail account setup in Mozilla Thunderbird and Sypheed=Claws mail clients.

%description -l ru_RU.KOI8-R
Краткая инструкция по настройке учётных записей в почтовых клиентах Mozilla Thunderbird и Sylpheed-Claws.

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
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-mail_client_setup-kirill
  + added Provides/Obsoletes

* Mon Apr 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-mail_client_setup-kirill package

* Fri Mar 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 060303-alt1
- First build for Sisyphus.

