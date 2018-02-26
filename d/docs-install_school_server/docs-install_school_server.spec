%setup_docs_module install_school_server ru

Name: %packagename
Version: 4.1
Release: alt6

Summary: School Server Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке дистрибутива Школьный Сервер
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
School Server Installation Guide.

%description -l ru_RU.UTF-8
Руководство по установке дистрибутива Школьный Сервер.

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
* Tue Feb 17 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt6
- fix distro name

* Sat Jan 31 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt5
- add note about bios boot priority setting

* Wed Jan 28 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- more precise hd space requirements for manual partitioning

* Fri Jan 23 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- update screenshots (20090122.iso)
- add "install on raid" link
- remove user step / add ldap step

* Wed Dec 24 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1.2
- update screenshots (20081209.iso)

* Mon Dec 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1.1
- update screenshots (20081208.iso)

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- initial build for Sisyphus

