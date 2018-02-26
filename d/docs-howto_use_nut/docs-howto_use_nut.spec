# Generated File.
%setup_docs_module howto_use_nut ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Howto use UPS with nut
Summary(ru_RU.KOI8-R): Как использовать UPS с nut
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-howto_use_nut-kirill
Provides: docs-howto_use_nut-kirill
Obsoletes: docs-howto_use_nut-kirill

Source: %name-%version.tar

%description
Use of nut in ALT Linux Master 2.4.

%description -l ru_RU.KOI8-R
Использование nut в AltLinux Мастер 2.4

%prep
%setup

%build
%docs_module_build "html" "Howto_use_UPS_nut.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- reaplces docs-howto_use_nut-kirill
  + added Provides/Obsoletes

* Tue Apr 15 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
  + based on howto_use_nut-kirill package

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050604-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050604-alt1
- Auto build with new version.

