%define docbook_ver 1.75.2
%define docbook_path %_datadir/xml/docbook/xsl-stylesheets-%docbook_ver

Name: docbook-tldp-xsl
Version: 20050304
Release: alt2
Summary: Customization layer for the standard DocBook XSL style sheets
License: FDL
Group: Publishing
Url: http://www.happy-monkey.net/docbook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.happy-monkey.net/docbook/tldp/tldp-xsl-04MAR2005.tar.gz

BuildArch: noarch

Requires: docbook-style-xsl

%description
The TLDP-XSL package is a customization layer for the standard DocBook
XSL style sheets. The customizations include things like automatic
numbering for chapters and sections as well as controlling how documents
are broken into multiple HTML pages. For additional information about
these customizations, please refer to the comments within the XSL files
in the html and fo directories of the tldp-xsl package.

%prep
%setup

%install
install -d %buildroot%docbook_path/fo
install -d %buildroot%docbook_path/html

install -p -m644 fo/* %buildroot%docbook_path/fo
install -p -m644 html/* %buildroot%docbook_path/html

%files
%doc readme.txt doc
%docbook_path/fo/*
%docbook_path/html/*

%changelog
* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20050304-alt2
- Rebuilt with docbook-style-xsl 1.75.2

* Thu Feb 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20050304-alt1
- Initial build for Sisyphus

