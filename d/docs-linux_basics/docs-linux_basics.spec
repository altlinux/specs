%setup_docs_module linux_basics ru

Name: %packagename
Version: 0.2.5
Release: alt1

Summary: Basics for Work in Linux
Summary(ru_RU.KOI8-R): Основы работы в ALT Linux
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-linux_basics-kirill
Provides: docs-linux_basics-kirill
Obsoletes: docs-linux_basics-kirill

Source: %name-%version.tar

%description
This document is written for those users who are not yet acquanted with Linux. 
Short overview of Linux features that every user will meet: how to begin and finish work, virtual consoles and graphical environment, command line, permissions. The way to find an answer to your question is drawn: documentation, Internet resources, support service.

%description -l ru_RU.KOI8-R
Документ ориентирован на пользователя, ещё не знакомого с Linux. Даётся краткий обзор таких особенностей работы в Linux, с которыми придётся столкнуться каждому пользователю: начало и завершение сеанса, виртуальные консоли и графическая среда, командная строка, права доступа. Описан путь поиска ответов на вопросы: документация, ресурсы Интернет и служба поддержки.

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
* Mon Sep 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.5-alt1
- fixed shortcut (#17374)

* Tue Jun 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.4-alt1
- typo fixes (thanks bertis@)

* Mon Jun 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.3-alt1
- updated date command example

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt2
- replaces docs-linux_basics-kirill
  + added Provides/Obsoletes

* Mon Mar 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.2-alt1
- punctuation fixes (thanks bertis@)
- fixed link to mailing lists
- fixed System Management center name

* Wed Mar 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2.1-alt1
- fixed "internet" declension

* Thu Jan 31 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- added description of copying text from command line (thanks bertis@)
  (# 14200)

* Mon Aug 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- new version
  + typo fixes

* Fri Jul 27 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-linux_basics-kirill package

* Thu May 31 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060307-alt2
- Rebuilt with new version from heap

* Mon Mar 06 2006 Kirill Maslinsky <kirill@altlinux.ru> 060307-alt1
- Auto rebuild with new version.

* Sat Jan 14 2006 Kirill Maslinsky <kirill@altlinux.ru> 060113-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051021-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 25 2005 Kirill Maslinsky <kirill@altlinux.ru> 051021-alt1
- Auto rebuild with new version.

* Tue Oct 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 051018-alt1
- Auto rebuild with new version.

* Mon Oct 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 051017-alt1
- Auto rebuild with new version.

* Mon Oct 10 2005 Kirill Maslinsky <kirill@altlinux.ru> 051010-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1.1
- Auto rebuild with new version.

* Tue Sep 20 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1.1
- Auto rebuild with new version.

* Fri Sep 16 2005 Kirill Maslinsky <kirill@altlinux.ru> 050905-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050718-alt1
- fixes in text for prerelease

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050712-alt1
- initial build

