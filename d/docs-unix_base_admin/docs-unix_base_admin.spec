# Generated File.
%setup_docs_module unix_base_admin ru

Name: %packagename
Version: 0.8
Release: alt2

Summary: Linux Administration Intro 
Summary(ru_RU.KOI8-R): Введение в администрирование UNIX
License: %fdl
Url: http://lug.mstu.ru/doc-admin/
Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6
BuildRequires: inkscape

# replace docs-unix_base_admin-dralex
Provides: docs-unix_base_admin-dralex
Obsoletes: docs-unix_base_admin-dralex

Source: %name-%version.tar

%description
Introduction into Linux administration of UNIX-like operating systems -- course of lectures with a practical part.

%description -l ru_RU.KOI8-R
Введение в администрирование UNIX-подобных систем в виде набора лекций и практических занятий.

%prep
%setup

%build
cd doc/
make 
cd ../
%docs_module_build "DocBook/XML" "unix-base-admin.docbook" -- "--stringparam chunker.output.indent yes --stringparam html.stylesheet 'general.css'"

%install
%docs_module_install

%post
%docs_module_postin

%postun
%docs_module_postun

%files
%docs_module_files

%changelog
* Sun Jun 01 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.8-alt2
- package renamed: docs-unix_base_admin-dralex -> docs-unix_base_admin
- build with rpm-build-docs-experimental
- used macro for License tag (rpm-build-licenses)

* Fri Mar 03 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.8-alt1
- Initial build for Sisyphus

