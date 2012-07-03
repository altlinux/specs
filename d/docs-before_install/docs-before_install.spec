%setup_docs_module before_install ru

Name: %packagename
Version: 0.3
Release: alt1

Summary: Recommendations before start installation
Summary(ru_RU.UTF-8): Рекомендации перед установкой системы
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Recommendations before start installation.

%description -l ru_RU.UTF-8
Рекомендации перед установкой системы.

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
* Wed Nov 26 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- new version (merged with docs-backup_before_install)

* Wed Sep 03 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- edited module passport
  * better Title: in docinfo
  * removed trailing whitespaces in License file

* Thu Aug 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- fixed typo / replaced 'ie' with 'io'
- fixed version in docinfo

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + typo fixes
  + links to external modules reordered

* Mon Jul 23 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus 

