%setup_docs_module mediawiki ru

Name: %packagename
Version: 0.2
Release: alt2

Summary: Mediawiki guide
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Mediawiki guide

%prep
%setup

%build
make -C doc/
rm -f doc/html4.conf doc/index.txt doc/Makefile doc/link-examples.html
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
* Mon Dec 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt2
- fix docinfo: Author section

* Sat Dec 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- add link targets for admin/user guide

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
