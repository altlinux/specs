%setup_docs_module install_school ru

Name: %packagename
Version: 0.6.2
Release: alt1

Summary: School Linux Installation Guide
Summary(ru_RU.UTF-8): Руководство по установке дистрибутивов школьного комплекта
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
School Linux Installation Guide:
Linux Lite, Linux Junior, Linux Master, Linux Terminal.

%description -l ru_RU.UTF-8
Руководство по установке дистрибутивов школьного комплекта:
Лёгкий Линукс, Линукс Юниор, Линукс Мастер, Линукс Терминал.

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
* Thu Jun 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.6.2-alt1
- use Russian spelling for Linux

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.6.1-alt1
- fixed two typos

* Sun Jun 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.6-alt1
- renamed distro pack
- more verbose language step description
- updated disk space requirements
- more typos fixed

* Sat Jun 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5.1-alt1
- changes from bertis@
  + typo fixes
  + added distro specific notes
  + better paraphrasings

* Sun Jun 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5-alt1
- initial build for Sisyphus
  + based on school-20080529-linux installers

