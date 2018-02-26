%setup_docs_module install_ltsp ru

Name: %packagename
Version: 0.1.4
Release: alt1

Summary: Linux Terminal Server Installation Guide
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Linux Terminal Server Installation Guide.

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
* Wed Jun 25 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.4-alt1
- fixed default interface name (eth0)

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.3-alt1
- use Russian spelling for Linux

* Mon Jun 23 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.2-alt1
- fixed one typo

* Mon Jun 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1.1-alt1
- changes from bertis@
  + text expanded to become more understandable
- removed ALT Linux mention from spec (Summary, description) and docinfo

* Wed Jan 30 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- inital build for Sisyphus

