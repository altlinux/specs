# Generated File.
%setup_docs_module console_setup  ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Console setup
Summary(ru_RU.KOI8-R): Настройка консоли
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-console_setup-kirill
Provides: docs-console_setup-kirill
Obsoletes: docs-console_setup-kirill

Source: %name-%version.tar

%description
Console setup in Linux: fonts, keyboard layouts, russification.

%description -l ru_RU.KOI8-R
Настройка консоли в Linux: шрифты, раскладки клавиатуры, русификация.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "console.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-console_setup-kirill
  + added Provides/Obsoletes

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-console_setup-kirill package

* Wed Jun 06 2007 Kirill Maslinsky <kirill@altlinux.ru> 070606-alt1
- small fixes (thanks php-coder@)
  + fix typo in package description/docinfo (#11857)
  + update spec due to new rpm-build-docs

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050321-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050321-alt1
- Auto build with new version.

