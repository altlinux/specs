# Stolen from docs-alterator_apt.spec
%setup_docs_module init_d ru

Name: %packagename
Version: 0.2
Release: alt2

Summary: Initscripts
Summary(ru_RU.KOI8-R): Стартовые сценарии
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-init_d-kirill
Provides: docs-init_d-kirill = 1.0-alt1
Obsoletes: docs-init_d-kirill <= 1.0-alt1

Source: %name-%version.tar

%description
Description of principles of service management using start acripts, recommendations for their creation and edition.

%description -l ru_RU.KOI8-R
Описание принципов управления службами при помощи стартовых сценариев, рекомендации по их созданию и редактированию.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "init.d.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt2
- replaces docs-init_d-kirill
  + added Provides/Obsoletes

* Thu Jan 31 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- added short decription of: (thanks bertis@) (#14192)
  + system services
  + chkconfig and service commands
- added missing "." in %%description tag

* Sun Jan 13 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-init_d-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 1.0-alt1
- First build for Sisyphus
