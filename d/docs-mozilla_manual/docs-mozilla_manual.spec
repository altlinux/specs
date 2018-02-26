# Generated File.
%setup_docs_module mozilla_manual ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: Mozilla. User manual
Summary(ru_RU.KOI8-R): Mozilla. Руководство пользователя
License: %fdl
Url: http://heap.altlinux.ru/HeapLinks/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

# replace docs-mozilla_manual-kirill, alt-docs-extras-mozilla
Provides: docs-mozilla_manual-kirill, alt-docs-extras-mozilla
Obsoletes: docs-mozilla_manual-kirill, alt-docs-extras-mozilla

Source: %name-%version.tar

%description
User manual for  Mozilla 1.6. 

%description -l ru_RU.KOI8-R
Руководство пользователя по пакету Mozilla (1.6), включает пояснение основных понятий www, описание браузера и почтового клиента Мозилла со скриншотами а также описание установки под Win.

%prep
%setup

%build
%docs_module_build "OOo 1.1" "mozmanual1.6.sxw"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Wed Mar 18 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- replace alt-docs-extras-mozilla package (add Provides/Obsoletes)

* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- package renamed: docs-mozilla_manual-kirill -> docs-mozilla_manual
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 050318-alt1.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Nov 14 2005 Kirill Maslinsky <kirill@altlinux.ru> 050318-alt1
- Auto build with new version.

