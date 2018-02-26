Name: asciidoc
Version: 8.6.3
Release: alt1.1

Summary: asciidoc converts an AsciiDoc text file to DocBook, HTML or LinuxDoc
Group: Text tools
License: GPLv2+
Url: http://www.methods.co.nz/asciidoc/
Packager: Artem Zolochevskiy <azol@altlinux.ru>
BuildArch: noarch

# http://www.methods.co.nz/asciidoc/%name-%version.tar.gz
Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-vim
%define _unpackaged_files_terminate_build 1
%define docdir %_docdir/%name-%version

BuildRequires: rpm-build-texmf

%description
The asciidoc(1) command translates the AsciiDoc text file to the backend
formatted file.

AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.


%package a2x
Summary: a2x converts AsciiDoc text file to PDF, XHTML, HTML Help, manpage or plain text
Group: Text tools
Requires: %name = %version-%release
Requires: lynx xsltproc docbook-style-xsl dblatex

%description a2x
A DocBook toolchain wrapper script that translates an AsciiDoc text
file to PDF, XHTML (single page or chunked), man page, HTML Help
or plain text formats. PDF, XHTML, man page and HTML Help formats are
generated using the asciidoc(1)/xsltproc(1)/DocBook XSL Stylesheets
toolchain. Plain text is produced by passing asciidoc(1) generated HTML
through lynx(1). The htmlhelp format option generates .hhp, .hhc and
.html files suitable for compilation to an HTML Help .chm file.


%package doc
Summary: AsciiDoc documentation and examples
Group: Development/Documentation

%description doc
The asciidoc(1) command translates the AsciiDoc text file to the backend
formatted file.

AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

This package contains AsciiDoc documentation and examples.


%package -n vim-plugin-asciidoc-syntax
Summary: Vim syntax highlighting for AsciiDoc files
Group: Editors
PreReq: vim-common

%description -n vim-plugin-asciidoc-syntax
The asciidoc(1) command translates the AsciiDoc text file to the backend
formatted file.

AsciiDoc is a text document format for writing short documents, articles,
books and UNIX man pages.

This package contains AsciiDoc syntax highlighting support for Vim.


%prep
%setup
%patch -p1

%build
%configure docdir=%docdir

%install
%make_install DESTDIR=%buildroot install docs
mv -f %buildroot%_bindir/%name.py %buildroot%_bindir/%name
mv -f %buildroot%_bindir/a2x.py %buildroot%_bindir/a2x
install -pD %buildroot%_sysconfdir/%name/dblatex/asciidoc-dblatex.sty \
  %buildroot%_texmfmain/tex/latex/%name/asciidoc-dblatex.sty

# install vim plugin
install -d %buildroot{%vim_ftdetect_dir,%vim_syntax_dir}
install -p -m644 vim/ftdetect/asciidoc_filetype.vim %buildroot%vim_ftdetect_dir/
install -p -m644 vim/syntax/asciidoc.vim %buildroot%vim_syntax_dir/

# install extra docs for asciidoc package
install -d %buildroot%docdir/
install -pD -m644 COPYRIGHT  %buildroot%docdir/

%files
%_bindir/%name

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/dblatex/
%config(noreplace) %_sysconfdir/%name/filters/
%_sysconfdir/%name/images
%config(noreplace) %_sysconfdir/%name/javascripts/
%config(noreplace) %_sysconfdir/%name/stylesheets/

%_man1dir/%name.*
%dir %docdir
%doc %docdir/BUGS
%doc %docdir/CHANGELOG
%doc %docdir/COPYRIGHT
%doc %docdir/README

%files a2x
%_bindir/a2x
%config(noreplace) %_sysconfdir/%name/docbook-xsl/
%_man1dir/a2x.*
%_texmfmain/tex/latex/%name/

%files doc
%doc %docdir
%exclude %docdir/BUGS
%exclude %docdir/CHANGELOG
%exclude %docdir/COPYRIGHT
%exclude %docdir/README

%files -n vim-plugin-asciidoc-syntax
%vim_ftdetect_dir/*.vim
%vim_syntax_dir/*.vim

%changelog
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

