%setup_docs_module moodle ru

Name: %packagename
Version: 0.3
Release: alt1

Summary: Moodle guide
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires: asciidoc
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Source: %name-%version.tar

%description
Moodle guide

%prep
%setup

%build
asciidoc -b html4 -f doc/html4.conf doc/index.txt
rm -f doc/html4.conf doc/index.txt
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
* Wed Jan 21 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.3-alt1
- headings fixed with quotes (thx Vladimir Zhukov)
- typo and syntax fixes

* Sat Dec 06 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- add text from Valentina Manyachina
- add link targets for admin/user guide

* Thu Nov 20 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initial build for Sisyphus
