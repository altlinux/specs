%setup_docs_module quickstart_desktop_sb ru

Name: %packagename
Version: 0.2
Release: alt1

Summary: Quickstart for beginners
Summary(ru_RU.UTF-8): Быстрый старт для начинающих
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# rename: docs-quickstart-desktop_sb -> docs-quickstart_desktop_sb
Provides: docs-quickstart-desktop_sb = 0.1-alt1
Obsoletes: docs-quickstart-desktop_sb <= 0.1-alt1

Source: %name-%version.tar

%description
Quickstart for beginners.

%description -l ru_RU.UTF-8
Быстрый старт для начинающих.

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
* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- punctuation fixes
- removed smc(www) mention

* Sun Mar 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- package renamed: docs-quickstart-desktop_sb -> docs-quickstart_desktop_sb
- fixed synaptic name (as it appears in menu) (thanks cas@)
- fixed module passport
  + Title
  + Abstract

* Wed Aug 22 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-quickstart package
  + added link to WINE@Etersoft Local documentation

