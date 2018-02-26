%setup_docs_module whatis_desktop ru

Name: %packagename
Version: 4.1
Release: alt5

Summary: What is ALT Linux Desktop
Summary(ru_RU.UTF-8): Что такое ALT Linux Desktop
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-whatis_desktop4.0-azol = 0.1-alt1
Obsoletes: docs-whatis_desktop4.0-azol

Source: %name-%version.tar

%description
Description of ALT Linux Desktop distribution for customers.
No technical details.

%description -l ru_RU.UTF-8
Описание дистрибутива ALT Linux Desktop.
Без технических подробностей, для пользователей/заказчиков.

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
* Wed Mar 04 2009 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt5
- fix OpenOffice version
- fix dictionary list

* Sat Nov 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt4
- fixed typo

* Mon Oct 27 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt3
- fixed distro description and software names (thanks bertis@)

* Thu Sep 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt2
- added NetwokManager/dosemu/wine/qemu/virtualbox mention

* Wed Sep 24 2008 Artem Zolochevskiy <azol@altlinux.ru> 4.1-alt1
- removed "variants" section
- fixed typo in previous changelog entry
- new version scheme:
  + version = branch

* Mon Sep 22 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt1
- Desktop 4.1 adaptation
- removed distro version from spec (summary/description) and docinfo

* Sat Mar 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3.1-alt1
- fixed typo and punctuation (thanks bertis@)

* Sat Mar 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- fixes from cas@
  + fixed distro names
  + more precise hardware requirements
  + removed smc(www) mention
  + removed Corporate Desktop mention

* Wed Aug 29 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2.3-alt1
- new version
  + fixed distro names according to
  http://www.altlinux.ru/company_news/personal_desktop_4.html
- fixed Summary and %%description

* Mon Aug 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- new version
  + typo fixes

* Tue Aug 14 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- new version
  + typo fixes

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- new version
  + new disto names and descriptions in Desktop 4.0 series

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- intial build for Sisyphus

