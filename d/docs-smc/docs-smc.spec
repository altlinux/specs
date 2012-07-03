%setup_docs_module smc ru

Name: %packagename
Version: 0.4
Release: alt1

Summary: Short description of System management center
Summary(ru_RU.UTF-8): Краткое описание Центра управления системой
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-smc-azol = 0.1-alt1
Obsoletes: docs-smc-azol
# obsolete old docs-alterator packages
Provides: docs-acc-kirill, docs-alterator_apt-kirill, docs-alterator_timezone-kirill, docs-alterator_x11-kirill, docs-alterator_packages-kirill, docs-alterator_network-kirill, docs-alterator_printers-kirill, docs-alterator_users-kirill
Obsoletes: docs-acc-kirill, docs-alterator_apt-kirill, docs-alterator_timezone-kirill, docs-alterator_x11-kirill, docs-alterator_packages-kirill, docs-alterator_network-kirill, docs-alterator_printers-kirill, docs-alterator_users-kirill

Source: %name-%version.tar

%description
Short description of System management center functionality and usage.

%description -l ru_RU.UTF-8
Краткое описание возможностей и использования Центра управления системой.

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
* Fri Sep 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- removed smc module description

* Thu Aug 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3.2-alt1
- fixed smc name in module passport

* Thu Aug 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3.1-alt1
- couple of text fixes (bertis@)
- fixed typos / replaced 'ie' with 'io'

* Tue Aug 19 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt2
- added missing Provides (#16653)
  + docs-acc-kirill
  + docs-alterator_apt-kirill
  + docs-alterator_timezone-kirill
  + docs-alterator_x11-kirill
  + docs-alterator_packages-kirill
  + docs-alterator_network-kirill
  + docs-alterator_printers-kirill
  + docs-alterator_users-kirill

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- updated and reordered module description
- fixed russian smc name in module info (docinfo)

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt3
- fixed Obsolete list
  + added docs-acc-kirill

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt2
- obsolete old docs-alterator packages:
  + docs-alterator_apt-kirill
  + docs-alterator_timezone-kirill
  + docs-alterator_x11-kirill
  + docs-alterator_packages-kirill
  + docs-alterator_network-kirill
  + docs-alterator_printers-kirill
  + docs-alterator_users-kirill

* Mon Mar 03 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- fixed russian smc name
- fixed command name: acc instead of alterator-standalone

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + added module description

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo and punctuation fixes

* Thu Jul 26 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

