%setup_docs_module ooo_infra_calc_guide ru

Name: %packagename
Version: 0.1
Release: alt2

Summary: OpenOffice.org Calc Guide
License: %gpl2plus
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
OpenOffice.org Calc Guide.

%prep
%setup

%build
%docs_module_build "pdf" "0300CG-CalcGuide-Ru.pdf"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sat Jan 31 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt2
- more informative Title: in docinfo (#17592)

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

