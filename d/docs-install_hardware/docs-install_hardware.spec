%setup_docs_module install_hardware ru

Name: %packagename
Version: 0.1.2
Release: alt1

Summary: Install hardware under Linux
License: %fdl
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Install hardware under Linux.

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
* Tue Sep 02 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fixed module description (Title: in docinfo)

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- punctuation fixes and minor edition

* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

