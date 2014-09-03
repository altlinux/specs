%define tarname tracwikiprintplugin
Name: python-module-trac-wikiprintplugin
%define r_minor r13287
Version: 1.9.3
Release: alt1.%r_minor

Summary: Make wiki pages easily printable, exporting to PDF (book or article format) or printable HTML format (page contents without trac headers/footers)

Group: Development/Python
License: GPL
Url: http://trac-hacks.org/wiki/tracwikiprintplugin

# http://trac-hacks.org/svn/tracwikiprintplugin/0.11/
Source: %{tarname}-%r_minor.zip
Patch: python-module-trac-wikiprintplugin-fix-error-in-html-output.patch

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

Requires: python-module-imaging

%description
Make wiki pages easily printable, exporting to PDF (book or article format) or printable HTML format
(page contents without trac headers/footers).

PDF export is based on xhtml2pdf/PISA pure python libraries, instead of depending on an external application.

WikiPrint features:
- Fully customizable header/footers for PDF
- Syntax highlighting in exported format, using pygments
- Customizable front page for PDF book format
- Automatic creation of Table of Contents if [[PageOutline]] or [[TOC]] Macro is used
- The style of the resulting PDF or HTML can be fully customized using CSS files.

%prep
%setup -n %tarname
#patch -p2

%build
%python_build

%install
%python_install

chmod -R a+r %buildroot%python_sitelibdir/wikiprint

%files
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt1.r13287
- Version 1.9.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2-alt1.r7916.1
- Rebuild with Python-2.7

* Mon May 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.8.2-alt1.r7916
- Build for ALT
