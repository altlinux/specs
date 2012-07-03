%setup_docs_issue insideout

Name: %packagename
Version: 0.10
Release: alt1
Group: Books/Other

Summary: ALT Linux outside and inside
Summary(ru_RU.KOI8-R): ALT Linux снаружи и изнутри
License: %fdl

Buildarch: noarch
BuildRequires(pre): rpm-build-docs-experimental >= 0.4
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-issue-compactbook = %version
Obsoletes: docs-issue-compactbook < %version

Source: %name-%version.tar

%docs_issue_requires

%description
This package encloses documents which constitute "ALT Linux outside and inside" book.
Some of the sections may contain more recent versions of the documents than those printed.

%description -l ru_RU.KOI8-R
Этот пакет объединяет документы, составившие книгу "ALT Linux снаружи и изнутри".
Некоторые разделы могут содержать более новые версии документов по сравнению 
с напечатанной версией.

%prep
%setup

%build
%docs_issue_build

%install
%docs_issue_install

%files
%docs_issue_files

%post
%docs_issue_postin

%postun
%docs_issue_postun

%changelog
* Wed Apr 09 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.10-alt1
- package renamed: docs-issue-compactbook -> docs-issue-insideout
- changed Packager: kirill@ -> ALT Docs Team
- replaced/removed obsoleted modules
- used modules without commiter_id
- fixed link to wine and openoffice modules

* Thu May 31 2007 Kirill Maslinsky <kirill@altlinux.ru> 0.9-alt1
- included (almost) all book contents
  + install chapter updated for 4.0 installer
  + minimum about text, no authors list, license notes etc. yet

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Tue Dec 06 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial draft


