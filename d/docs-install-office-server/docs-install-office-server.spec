%setup_docs_module install-office-server ru

Name: docs-install-office-server
Version: 5.0
Release: alt2

Summary: ALT Linux Server Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке Альт Линукс Сервер
License: %fdl

# rename docs-install_office_server -> docs-install-office-server
Provides: docs-install_office_server = %version
Obsoletes: docs-install_office_server < %version

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
ALT Linux Server Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке Альт Линукс Сервер.

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
* Sat Mar 21 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt2
- fix install path

* Fri Mar 20 2009 Artem Zolochevskiy <azol@altlinux.ru> 5.0-alt1
- package renamed:
  + docs-install_office_server -> docs-install-office-server
- fix distro name: spec, docinfo

* Sat Jan 31 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt5
- add note about bios boot priority setting

* Thu Jan 29 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- edit hd space requirements for manual partitioning

* Fri Jan 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- remove user / add ldap screenshot
- add "install on raid" link
- remove user step / add ldap step

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus

