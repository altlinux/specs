%setup_docs_module linux_apps ru

Name: %packagename
Version: 0.1.2
Release: alt2

Summary: Applications for Linux
Summary(ru_RU.KOI8-R): Прикладные программы для Linux
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_apps-kirill
Provides: docs-linux_apps-kirill
Obsoletes: docs-linux_apps-kirill

Source: %name-%version.tar

%description
This is a short survey of Linux applications. It is entirely not a complete list, just example and illustration of multiple possibilities.

%description -l ru_RU.KOI8-R
Этот документ посвящён краткому обзору прикладных программ для Linux, предназначенных для решения самых разных пользовательских задач. Материал, вошедший сюда, нужно воспринимать только как пример, демонстрацию, но вовсе не исчерпыывающий список.

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
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt2
- replaces docs-linux_apps-kirill
  + added Provides/Obsoletes

* Sun Oct 07 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- new version
  + added SeaMonkey mention
  + typo fixes

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo fixes

* Mon Jul 30 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_apps-kirill package

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Thu Feb 02 2006 Kirill Maslinsky <kirill@altlinux.ru> 060201-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051121-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 051121-alt1
- Auto rebuild with new version.

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 051114-alt1
- Auto build with new version.

