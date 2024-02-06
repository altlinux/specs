%define _unpackaged_files_terminate_build 1
%define docdir %_docdir/%name-%version

Name: asciidoc
Version: 10.2.0
Release: alt1

Summary: asciidoc converts an AsciiDoc text file to DocBook, HTML or LinuxDoc

Group: Text tools
License: GPL-2.0-or-later
Url: http://asciidoc.org

BuildArch: noarch

# Source-url: https://github.com/asciidoc-py/asciidoc-py/releases/download/%version/asciidoc-%version.tar.gz
Source: %name-%version.tar
Patch1: asciidoc-table-separator.patch

BuildRequires(pre): rpm-build-tex
BuildRequires: python3-devel python3-module-pip python3-module-setuptools python3-module-wheel
BuildRequires: xsltproc docbook-style-xsl
#BuildRequires: source-highlight
#BuildRequires: graphviz

%description
The asciidoc(1) command translates the AsciiDoc text file to the backend
formatted file.

AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

%package a2x
Summary: a2x converts AsciiDoc text file to PDF, XHTML, HTML Help, manpage or plain text
Group: Text tools
Requires: %name = %version-%release
Requires: xsltproc docbook-style-xsl
Requires: w3m
# Requires: lynx
# Requires: source-highlight

%description a2x
A DocBook toolchain wrapper script that translates an AsciiDoc text
file to PDF, XHTML (single page or chunked), man page, HTML Help
or plain text formats. PDF, XHTML, man page and HTML Help formats are
generated using the asciidoc(1)/xsltproc(1)/DocBook XSL Stylesheets
toolchain. Plain text is produced by passing asciidoc(1) generated HTML
through lynx(1). The htmlhelp format option generates .hhp, .hhc and
.html files suitable for compilation to an HTML Help .chm file.

Install asciidoc-latex if you need generate PDF files.

%package latex
Summary: Support for asciidoc LaTeX output
Group: Text tools
Requires: %name = %EVR
Requires: dblatex

%description latex
Support for asciidoc LaTeX output.

%package doc
Summary: AsciiDoc documentation and examples
Group: Development/Documentation

%description doc
The asciidoc(1) command translates the AsciiDoc text file to the backend
formatted file.

AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

This package contains AsciiDoc documentation and examples.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure docdir=%docdir

%install
%make_install DESTDIR=%buildroot install docs manpages
mkdir -p %buildroot%_man1dir
mv %buildroot%docdir/doc/{asciidoc.1,a2x.1,testasciidoc.1} %buildroot%_man1dir/
install -pD %buildroot%python3_sitelibdir/%name/resources/dblatex/asciidoc-dblatex.sty \
  %buildroot%_texmfmain/tex/latex/%name/asciidoc-dblatex.sty

# install extra docs for asciidoc package
install -d %buildroot%docdir/
install -pD -m644 COPYRIGHT  %buildroot%docdir/

%files
%_bindir/%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/asciidoc/resources/filters/latex
%exclude %python3_sitelibdir/asciidoc/resources/filters/music

%_man1dir/%name.*
%_man1dir/test%name.*
%dir %docdir
%doc %docdir/BUGS.adoc
%doc %docdir/CHANGELOG.adoc
%doc %docdir/COPYRIGHT
%doc %docdir/README.md

%files a2x
%_bindir/a2x
%_man1dir/a2x.*

%files latex
%python3_sitelibdir/%name/resources/filters/latex
%_texmfmain/tex/latex/%name/

%files doc
%doc %docdir
%exclude %docdir/BUGS.adoc
%exclude %docdir/CHANGELOG.adoc
%exclude %docdir/COPYRIGHT
%exclude %docdir/README.md

%changelog
* Tue Feb 06 2024 Alexey Shabalin <shaba@altlinux.org> 10.2.0-alt1
- 10.2.0
- fix invalid escape sequence (ALT#49310)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 9.1.0-alt2
- use w3m (as default text generator) instead of lynx
- drop source-highlight require (it is recommended only)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 9.1.0-alt1
- cleanup spec, build new version from tarball
- switch to python3
- move dblatex files and dependency to latex subpackage
- don't pack vim-plugin-asciidoc-syntax (no more .vim files here)

* Thu May 20 2021 Slava Aseev <ptrnine@altlinux.org> 8.6.9-alt1.3
- Fix FTBFS due to missing rpm-build-python

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 8.6.9-alt1.2
- FTBFS: set correct python2 executable in shebang.

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 8.6.9-alt1.1
- NMU: rebuild with rpm-build-tex

* Tue Dec 03 2013  Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.6.9-alt1
- Version 8.6.9

* Thu Oct 31 2013  Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.6.8-alt1
- Version 8.6.8 (ALT #29536)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 8.6.3-alt1.1
- Rebuild with Python-2.7

* Fri Dec 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.6.3-alt1
- Version 8.6.3 (ALT #24716)

* Mon Feb 08 2010 Artem Zolochevskiy <azol@altlinux.ru> 8.5.3-alt1
- update to 8.5.3

* Wed Jan 20 2010 Artem Zolochevskiy <azol@altlinux.ru> 8.5.2-alt2
- place TeX stylesheet to TEXMFMAIN-Tree (thx Kirill Maslinsky)

* Tue Dec 15 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.5.2-alt1
- update to 8.5.2

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.5.1-alt1.1
- Rebuilt with python 2.6

* Fri Nov 06 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.5.1-alt1
- new version

* Fri Oct 09 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.5.0-alt1
- new version
- executables: drop .py suffix

* Tue Jun 02 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.4.5-alt1
- new version

* Mon Apr 27 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.4.4-alt1
- new version

* Mon Apr 13 2009 Artem Zolochevskiy <azol@altlinux.ru> 8.4.3-alt1
- new version
- add patch: skip all conbinations of leading comments and attribute entries
- asciidoc-doc no more requires asciidoc

* Tue Oct 07 2008 Andrey Rahmatullin <wrar@altlinux.ru> 8.2.7-alt1
- Sisyphus build

* Sun Oct 05 2008 Andrey Rahmatullin <wrar@altlinux.ru> 8.2.7-alt0.1
- 8.2.7

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 7.1.2-alt2.1
- Rebuilt with python-2.5.

* Wed May 03 2006 Andrei Bulava <abulava@altlinux.ru> 7.1.2-alt2
- split documentation into a separate subpackage
- added COPYING as a symlink to the system-wide GPL-2 text

* Wed Apr 26 2006 Andrei Bulava <abulava@altlinux.ru> 7.1.2-alt1
- 7.1.2
- packaged a2x(1) as a subpackage

* Tue Sep 20 2005 Andrei Bulava <abulava@altlinux.ru> 7.0.2-alt1
- 7.0.2
- made noarch indeed (doesn't use %%_libexecdir any more)
- eliminated absolute symlinks

* Fri Jul 08 2005 Andrei Bulava <abulava@altlinux.ru> 7.0.1-alt1
- 7.0.1
- rebundled according to "Appendix B: Packager Notes" of AsciiDoc
  User Guide

* Wed Jun 22 2005 Andrei Bulava <abulava@altlinux.ru> 7.0.0-alt1
- initial build for ALT Linux

