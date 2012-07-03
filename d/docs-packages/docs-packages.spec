%setup_docs_module packages ru

Name: %packagename
Version: 0.1
Release: alt1

Summary: Installing software packages
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses => 0.6

Source: %name-%version.tar

%description
Installing software packages.


%prep
%setup

%build
%make_build -f \
/usr/share/xml/docbook/xsl-stylesheets/tools/make/Makefile.DocBook  html \
SOURCE_FILES_DBK=doc/packages.xml HTML_OR_XHTML=xhtml
mv doc/packages.html doc/index.html
rm doc/packages.xml
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
* Tue Sep 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initail build for Sisyphus

