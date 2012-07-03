%define tarname pisa
Name: python-module-pisa
Version: 3.0.33
Release: alt1.1

Summary: PDF generator using HTML and CSS

Group: Development/Python
License: GPLv2
Url: http://www.xhtml2pdf.com/

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: http://pypi.python.org/packages/source/p/pisa/%tarname-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%description
pisa is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and pyPdf.
It supports HTML 5 and CSS 2.1 (and some of CSS 3). It is completely written in pure Python 
so it is platform independent. The main benefit of this tool that a user with
Web skills like HTML and CSS is able to generate PDF templates very quickly
without learning new technologies. Easy integration into Python frameworks like CherryPy,
KID Templating, TurboGears, Django, Zope, Plone, Google AppEngine (GAE) etc.

Features 
- Translates HTML and CSS input into PDF files
- Is written pure Python and therefore platform independent
- Supports document specifics like columns, headers, footers, page numbers, custom Postscript and TrueType fonts, etc.
- Best support for frameworks like Django, Turbogears, CherryPy, Pylons, WSGI
- Simple integration into Python programms
- Also available as stand alone command line tool for Windows, MacOS X and Linux

%prep
%setup -n %tarname-%version

%build
%python_build

%install
%python_install

%files
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.33-alt1.1
- Rebuild with Python-2.7

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 3.0.33-alt1
- new version (3.0.33) import in git

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 3.0.32-alt1
- Build for ALT
