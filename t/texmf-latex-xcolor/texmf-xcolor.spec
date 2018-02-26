%define srcName xcolor

Name:    texmf-latex-%srcName
Version: 2.06
Release: alt3
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: A LaTeX package that provides easy driver-independent access to several kinds of colors
Summary(ru_RU.KOI8-R): LaTeX макропакет для простого использования цвета
License: %lppl
Group:   Publishing
URL:     http://www.ukern.de/tex/xcolor.html

BuildArchitectures: noarch

Source0: %srcName-%version.tar.gz
Source3: chroma-1.00.tar.bz2

#BuildRequires: ghostscript-classic ghostscript-common ghostscript-utils glib libgimp-print tetex-core tetex-dvips tetex-latex
BuildRequires(pre): rpm-build-texmf tex-common rpm-build-licenses

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

%build
#%make_build

%install
mkdir -p %buildroot{%_texmfmain/tex/latex/xcolor,%_docdir/chroma}
install -pD -m644 svgnam.def %buildroot%_texmfmain/tex/latex/xcolor/svgnam.def
install -pD -m644 xcolor.sty %buildroot%_texmfmain/tex/latex/xcolor/xcolor.sty

%files
%dir %_texmfmain/tex/
%dir %_texmfmain/tex/latex/
%dir %_texmfmain/tex/latex/xcolor/
%_texmfmain/tex/latex/xcolor/svgnam.def
%_texmfmain/tex/latex/xcolor/xcolor.sty
%doc ChangeLog README xcolor.pdf xcolor1.pdf xcolor2.pdf xcolor3.pdf xcolor4.pdf xcolor1.tex xcolor2.tex xcolor3.tex xcolor4.tex chroma

%changelog
* Fri Jun 12 2009 Grigory Batalov <bga@altlinux.ru> 2.06-alt3
- Include own directories in the package.
- Specify license as %%lppl.
- Place files into %%_texmfmain.

* Mon Jun 08 2009 Grigory Batalov <bga@altlinux.ru> 2.06-alt2
- Rebuilt in new environment.
- texhash calls were removed due to filetrigger usage.
- Package was renamed to texmf-latex-xcolor because of TeX distribution independence.

* Sat Oct 29 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.06-alt1
- integral changes from previous release

* Thu Nov 11 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt3
- package is making locally and install only now

* Tue Nov 02 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt2
- documentation package chroma is added

* Wed Oct 27 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 2.00-alt1
- initial release for Sisyphus
