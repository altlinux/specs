%setup_docs_module network ru

Name: %packagename
Version: 0.2
Release: alt1

Summary: Network setup
License: %fdl

Buildarch: noarch
Requires: docs-utils
BuildRequires(pre): rpm-build-docs-experimental >= 0.3
BuildRequires(pre): rpm-build-licenses >= 0.6

Provides: docs-network_setup = %version, docs-network_setup-kirill
Obsoletes: docs-network_setup < %version, docs-network_setup-kirill

Source: %name-%version.tar

%description
Network setup.

%prep
%setup

%build
%make_build -f \
/usr/share/xml/docbook/xsl-stylesheets/tools/make/Makefile.DocBook  html \
SOURCE_FILES_DBK=doc/network.xml HTML_OR_XHTML=xhtml
mv doc/network.html doc/index.html
rm doc/network.xml
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
* Wed Feb 25 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1
- docs-network obsoletes old packages:
  + docs-network_setup
  + docs-network_setup-kirill

* Wed Sep 24 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.1-alt1
- initail build for Sisyphus


