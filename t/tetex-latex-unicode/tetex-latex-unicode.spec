Name:    tetex-latex-unicode
Version: 20041017
Release: alt1
Summary: Extended UTF-8 input encoding for LaTeX
License: LaTeX Project Public License
Group:   Publishing
URL:     http://tug.ctan.org/tex-archive/macros/latex/contrib/unicode

Source0: %name-%version.tar.bz2

BuildArch: noarch

Requires: tetex-latex

%description 
This bundle provides the ucs package, and utf8x.def, together with a large number of support files.

The utf8x.def definition file for use with inputenc  covers a wider range of Unicode characters than does utf8.def in the LaTeX distribution.  The ucs package provides facilities for efficient use of large sets of Unicode characters.


%prep
%setup -q

%install
install -d %buildroot%_datadir/texmf/tex/latex/unicode
install -d %buildroot%_datadir/texmf/tex/latex/unicode/{config,contrib,data}
install -m 644 *.sty *.def %buildroot%_datadir/texmf/tex/latex/unicode
install -m 644 data/*  %buildroot%_datadir/texmf/tex/latex/unicode/data
install -m 644 config/*  %buildroot%_datadir/texmf/tex/latex/unicode/config
install -m 644 contrib/*  %buildroot%_datadir/texmf/tex/latex/unicode/contrib

# install doc
install -d %buildroot%_docdir/%name-%version
install -d %buildroot%_datadir/texmf/doc/latex
# temorarily disable symlink to avoid requirement on tetex-doc
#ln -sf ../../../doc/%name-%version  %buildroot%_datadir/texmf/doc/latex/unicode


%post
[ -x /usr/bin/texhash ] && /usr/bin/texhash 2>/dev/null ||:


%postun
[ -x /usr/bin/texhash ] && /usr/bin/texhash 2>/dev/null ||:


%files
%_datadir/texmf/tex/latex/unicode
%_docdir/%name-%version
#%_datadir/texmf/doc/latex/unicode
%doc *.ps.gz *.pl FAQ INSTALL LICENSE README VERSION


%changelog
* Fri Jun 27 2008 Kirill Maslinsky <kirill@altlinux.org> 20041017-alt1
- version up
  + now provides utf8x input encoding

* Sun Jun 20 2004 Yury A. Zotov <yz@altlinux.ru> 20021217-alt1
- first build for Sisyphus
