# Generated File.
%setup_docs_module postfix ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: E-mail (Postfix)
Summary(ru_RU.KOI8-R): Электронная почта (Postfix)
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-postfix-kirill
Provides: docs-postfix-kirill = 060320-alt2
Obsoletes: docs-postfix-kirill <= 060320-alt2

Source: %name-%version.tar

%description
This document describes how to configure Internet or local email exchange
using Postfix email server.

%description -l ru_RU.KOI8-R
В данном документе описано, как организовать обмен электронной почтой с Интернет и внутри локальной сети при помощи сервера электронной почты Postfix.

%prep
%setup

%build
%docs_module_build "DocBook/XML (ALT)" "postfix.xml"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Mar 29 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-postfix-kirill
  + added Provides/Obsoletes

* Mon Jan 14 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-postfix-kirill package

* Fri May 18 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 060320-alt2
- New version from heap

* Mon Mar 20 2006 Kirill Maslinsky <kirill@altlinux.ru> 060320-alt1
- Auto rebuild with new version.

* Tue Mar 14 2006 Kirill Maslinsky <kirill@altlinux.ru> 060314-alt1
- Auto rebuild with new version.

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050304-alt6.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt6
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5.1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5.1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt5
- rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt4
- rebuilt with rpm-build-docs-0.4.2-alt2

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 050304-alt3
- Requires bugfix;

* Mon Jun 06 2005 Alexey Gladkov <legion@altlinux.ru> 050304-alt2
- rebuild with new rpm-build-docs.

* Mon Apr 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050304-alt1
- initial build
