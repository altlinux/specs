%define srcName xcolor

Name:    tetex-latex-%srcName
Version: 2.06
Release: alt1.1
Summary: A LaTeX package that provides easy driver-independent access to several kinds of colors
Summary(ru_RU.KOI8-R): LaTeX макропакет для простого использования цвета
License: LPPL (LaTeX Project Public License)
Group:   Publishing
URL:     http://www.ukern.de/tex/xcolor.html

BuildArchitectures: noarch

Requires: tetex-core tetex-latex

Source0: %srcName-%version.tar.gz
#Source1: makefile
#Source2: chngpage.sty
Source3: chroma-1.00.tar.bz2

#BuildRequires: ghostscript-classic ghostscript-common ghostscript-utils glib libgimp-print tetex-core tetex-dvips tetex-latex


%description 
xcolor is a LaTeX package that provides easy driver-independent access 
to several kinds of colors, tints, shades, tones, and mixes of arbitrary colors 
by means of color expressions like \color{red!50!green!20!blue}.
It allows to select a document-wide target color model and offers tools for
 * automatic color schemes,
 * conversion between nine color models (rgb, cmy, cmyk, hsb, gray, RGB, HTML, HSB, Gray)
 * alternating table row colors,
 * color blending,
 * color masking, and
 * color separation.
			
#%description -l ru_RU.KOI8-R

%prep
%setup -q -n %srcName-%version
%setup -q -a 3 -n %srcName-%version
#%__cp -av %SOURCE1 %SOURCE2 ./

%build
#%make_build

%install
%__mkdir_p %buildroot{%_datadir/texmf/tex/latex/xcolor,%_docdir/chroma}
install -pD -m644 svgnam.def %buildroot%_datadir/texmf/tex/latex/xcolor/svgnam.def
install -pD -m644 xcolor.sty %buildroot%_datadir/texmf/tex/latex/xcolor/xcolor.sty

%files
%_datadir/texmf/tex/latex/xcolor/svgnam.def
%_datadir/texmf/tex/latex/xcolor/xcolor.sty
%doc ChangeLog README xcolor.pdf xcolor1.pdf xcolor2.pdf xcolor3.pdf xcolor4.pdf xcolor1.tex xcolor2.tex xcolor3.tex xcolor4.tex chroma

%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.06-alt1.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-xcolor

* Sat Oct 29 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.06-alt1
- integral changes from previous release

* Thu Nov 11 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt3
- package is making locally and install only now

* Tue Nov 02 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt2
- documentation package chroma is added

* Wed Oct 27 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt1
- initial release for Sisyphus
