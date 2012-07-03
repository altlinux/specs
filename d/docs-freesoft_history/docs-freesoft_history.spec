# Generated File.
%setup_docs_module freesoft_history ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Free Software History
Summary(ru_RU.KOI8-R): История возникновения свободного ПО
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-freesoft_history-kirill
Provides: docs-freesoft_history-kirill
Obsoletes: docs-freesoft_history-kirill

Source: %name-%version.tar

%description
History of the `free software' notion and phenomenon, development of
free licenses.

%description -l ru_RU.KOI8-R
Изложена история появления понятия ``свободное программное обеспечение'' и свободных лицензий.

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
* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replaces docs-freesoft_history-kirill
  + added Provides/Obsoletes

* Sat Apr 12 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on docs-freesoft_history-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 051012-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Wed Oct 12 2005 Kirill Maslinsky <kirill@altlinux.ru> 051012-alt1
- Auto rebuild with new version.

* Tue Oct 04 2005 Kirill Maslinsky <kirill@altlinux.ru> 050830-alt1.1
- Auto rebuild with new version.

* Wed Sep 21 2005 Kirill Maslinsky <kirill@altlinux.ru> 050830-alt1
- Auto rebuild with new version.

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 050717-alt2
-rebuilt with rpm-build-docs-0.4.2-alt3

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 050717-alt1
- initial build

