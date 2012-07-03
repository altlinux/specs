%setup_docs_module win_lin_soft ru

Name: %packagename
Version: 20050320
Release: alt1

Summary: The table of analogs of Windows software in Linux
License: %fdl
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Url: http://www.linuxrsp.ru/win-lin-soft/
Source: %name-%version.tar

%description
The table of equivalents / replacements / analogs of Windows software in Linux.

%prep
%setup

%build
%docs_module_build "html" "index.html"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Thu Dec 13 2007 Artem Zolochevskiy <azol@altlinux.ru> 20050320-alt1
- initial build for Sisyphus

