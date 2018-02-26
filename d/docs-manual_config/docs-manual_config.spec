%setup_docs_module manual_config ru

Name: %packagename
Version: 0.1.6
Release: alt1

Summary: : Configuring system: editing configuration files
Summary(ru_RU.UTF-8): Настройка системы: правка конфигурационных файлов
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-manual_config-azol = 0.1-alt1
Obsoletes: docs-manual_config-azol

Source: %name-%version.tar

%description
Configuring system: editing configuration files.

%description -l ru_RU.UTF-8
Настройка системы: правка конфигурационных файлов.

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
* Tue Sep 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.6-alt1
- fixed syntax & punctuation (thanks bertis@)

* Thu Aug 28 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.5-alt1
- changed URL in example (bertis@)
- replaced 'ie' with 'io'

* Sun Mar 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
-  typo and punctuation fixes (thanks bertis@)

* Sun Mar 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
fixes from cas@
  + removed smc(www) mention
  + fixed russian smc name

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- new version
  + changed title
  + fixed typos

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo and punctuation fixes
  + some rephrasings

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

