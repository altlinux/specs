%setup_docs_module internet_mobile ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Internet connection over cell phone
Summary(ru_RU.KOI8-R): Подключение к Интернет через мобильный телефон
License: %fdl
Url: http://www.freesource.info/wiki/Stat'i/NastrojjkaInterneta/Mobile
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-internet_mobile-lav
Provides: docs-internet_mobile-lav
Obsoletes: docs-internet_mobile-lav

Source: %name-%version.tar

%description
Short overview of different ways network connection over cell phone.

%description -l ru_RU.KOI8-R
Кратко рассмотрены различные способы выхода в Сеть через мобильный телефон.

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
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-internet_mobile-lav
  + added Provides/Obsoletes
- used macro for License tag (rpm-build-licenses)

* Mon Jul 30 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- intial build for Sisyphus
  + based on docs-internet_mobile-lav package

* Mon Apr 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 060331-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050923-alt1.1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050923-alt1.1
- Auto rebuild with new version.

* Fri Sep 23 2005 Kirill Maslinsky <kirill@altlinux.ru> 050923-alt1
- Auto build with new version.

