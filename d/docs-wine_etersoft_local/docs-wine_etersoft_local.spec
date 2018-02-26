%setup_docs_module wine_etersoft_local ru

Name: %packagename
Version: 1.0.8.1
Release: alt1

Summary: WINE@Etersoft Local documentation
Summary(ru_RU.UTF-8): Документация WINE@Etersoft Local
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
WINE@Etersoft Local documentation.

%description -l ru_RU.UTF-8
Документация WINE@Etersoft Local.

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
* Sun May 04 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.0.8.1-alt1
- punctuation and typos fixes
- text adapted to alt linux reality

* Fri Mar 21 2008 Artem Zolochevskiy <azol@altlinux.ru> 1.0.8-alt1
- updated to 1.0.8

* Thu Aug 16 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  based on:
  + http://www.etersoft.ru/content/view/85
  + http://etersoft.ru/content/view/56

