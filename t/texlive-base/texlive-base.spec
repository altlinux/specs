Name: texlive-base
Version: 2008.0
Release: alt0.15
Packager: Grigory Batalov <bga@altlinux.org>

Summary: Essential programs and files
License: Distributable
Group: Publishing
Url: http://tug.org/texlive/

Source0: %name-texmf-%version-%release.tar
Source1: %name-texmf-dist-%version-%release.tar
Source2: %name-alt-%version.tar

BuildArch: noarch
BuildRequires: tex-common texlive-common
BuildRequires(pre): rpm-build-texmf
BuildRequires: less vim-console rpm-utils automake autoconf
BuildRequires: perl-Pod-Parser

Requires: texlive-base-bin, texlive-doc-base
# to complete base TeX system:
Requires: texlive-latex-base

%set_compress_method none

# don't check documentation and sources
%add_findreq_skiplist %_datadir/texmf/doc/*
%add_findreq_skiplist %_datadir/texmf-texlive/doc/*
%add_findreq_skiplist %_datadir/texmf/source/*
%add_findreq_skiplist %_datadir/texmf-texlive/source/*

# texlive-latex-base
#_datadir/texmf-texlive/tex/latex/amscls/amsrbeta.sty
%add_texmf_req_skip latex/amsjpa
%add_texmf_req_skip latex/inicap
#_datadir/texmf-texlive/tex/latex/ltxmisc/verbasef.sty
%add_texmf_req_skip latex/here

# texlive-latex-recommended
#_datadir/texmf-texlive/tex/latex/powerdot/powerdot-pazik.sty
%add_texmf_req_skip latex/pst-char
#_datadir/texmf-texlive/tex/latex/listings/lstdoc.sty
%add_texmf_req_skip latex/lgrind
#_datadir/texmf-texlive/tex/latex/memoir/memoir.cls
%add_texmf_req_skip latex/ifetex
#_datadir/texmf-texlive/tex/latex/ucs/mkrenc.def
%add_texmf_req_skip latex/makor

%description
These files are regarded as basic for any TeX system, covering plain
TeX macros, Computer Modern fonts, and configuration for common
drivers; no LaTeX.

%package -n texlive-fonts-recommended
Group: Publishing
Summary: Recommended fonts
Requires: texlive-base

%description -n texlive-fonts-recommended
(none)

%package -n texlive-generic-recommended
Group: Publishing
Summary: Recommended generic packages
Requires: texlive-base

%description -n texlive-generic-recommended
Recommended packages that work with multiple formats.

%package -n texlive-latex-base
Group: Publishing
Summary: Basic LaTeX packages
Requires: texlive-base, texlive-base-bin
# file conflicts
Conflicts: tetex-core
Conflicts: tetex-latex

%description -n texlive-latex-base
These packages are either mandated by the core LaTeX team, or otherwise
highly recommended.

%package -n texlive-latex-recommended
Group: Publishing
Summary: LaTeX recommended packages
Requires: texlive-latex-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-latex-recommended
A collection of recommended add-on packages for LaTeX which have
widespread use

%package -n texlive-pictures
Group: Publishing
Summary: Graphics packages
Requires: texlive-base

%description -n texlive-pictures
(none)

%package -n texlive-recommended
Group: Publishing
Summary: Recommended TeXLive subsystem
Requires: texlive-base, texlive-latex-recommended, texlive-fonts-recommended, texlive-math-extra, texlive-lang-cyrillic

%description -n texlive-recommended
Virtual package depending on real recommended TeXLive subsystem

%prep
%setup -c -T -a2
sed -i -e 's,hilberpgfcvs.tex.bak$,hilberpgfcvs.tex,g' \
	alt-linux/texlive-pictures.files

%install
mkdir -p %buildroot/%_datadir
tar xf %SOURCE0 -C %buildroot/%_datadir/
tar xf %SOURCE1 -C %buildroot/%_datadir/

(cd %buildroot/%_datadir/texmf-dist/doc/latex/tufte-latex/graphics/;
 mv hilberpgfcvs.tex.bak hilberpgfcvs.tex)

mkdir -p %buildroot/%_sysconfdir/texmf/{fmt.d,updmap.d,language.d}
cp alt-linux/*.cfg %buildroot/%_sysconfdir/texmf/updmap.d/
cp alt-linux/*.def %buildroot/%_sysconfdir/texmf/language.d/

mv %buildroot/%_datadir/texmf-dist %buildroot/%_datadir/texmf-texlive

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_cachedir/texmf
mkdir -p %buildroot/%_cachedir/texmf/tex
mkdir -p %buildroot/%_cachedir/texmf/tex/generic
mkdir -p %buildroot/%_cachedir/texmf/tex/generic/config
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/language.d
mkdir -p %buildroot/%_sysconfdir/texmf/metafont
mkdir -p %buildroot/%_sysconfdir/texmf/metafont/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain/config
mv %buildroot/%_datadir/texmf-texlive/metafont/config/cmmf.ini %buildroot/%_sysconfdir/texmf/metafont/config/cmmf.ini
mv %buildroot/%_datadir/texmf-texlive/metafont/config/mf.ini %buildroot/%_sysconfdir/texmf/metafont/config/mf.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/aleph.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/aleph.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/bplain.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/bplain.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/etex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/etex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/luatex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/luatex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/omega.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/omega.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/pdfbplain.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/pdfbplain.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/pdfetex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/pdfetex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/pdfluatex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/pdfluatex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/tex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/tex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/config/xetex.ini %buildroot/%_sysconfdir/texmf/tex/plain/config/xetex.ini
mv %buildroot/%_datadir/texmf/tex/generic/config/language.dat %buildroot/%_cachedir/texmf/tex/generic/config/language.dat
mv %buildroot/%_datadir/texmf/tex/generic/config/language.def %buildroot/%_cachedir/texmf/tex/generic/config/language.def
mv %buildroot/%_datadir/texmf/tex/generic/config/language.us %buildroot/%_sysconfdir/texmf/language.d/00-language.dat
mv %buildroot/%_datadir/texmf/tex/generic/config/language.us.def %buildroot/%_sysconfdir/texmf/language.d/00-language.def
ln -s ../fmtutil/format.latex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-latex-base-latex.cnf
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/generic
mkdir -p %buildroot/%_sysconfdir/texmf/tex/generic/babel
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex/config
rm -f %buildroot/%_bindir/latex
ln -s %_bindir/pdftex %buildroot/%_bindir/latex
rm -f %buildroot/%_bindir/pdflatex
ln -s %_bindir/pdftex %buildroot/%_bindir/pdflatex
mv %buildroot/%_datadir/texmf-texlive/tex/generic/babel/frenchb.cfg %buildroot/%_sysconfdir/texmf/tex/generic/babel/frenchb.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/generic/babel/hyphen.cfg %buildroot/%_sysconfdir/texmf/tex/generic/babel/hyphen.cfg
mv %buildroot/%_datadir/texmf/doc/man/man1/latex.1 %buildroot/%_mandir/man1/latex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/latex.pdf %buildroot/%_mandir/man1/latex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pdflatex.1 %buildroot/%_mandir/man1/pdflatex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pdflatex.pdf %buildroot/%_mandir/man1/pdflatex.pdf
mv %buildroot/%_datadir/texmf/fmtutil/format.latex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.latex.cnf
mv %buildroot/%_datadir/texmf/tex/latex/config/color.cfg %buildroot/%_sysconfdir/texmf/tex/latex/config/color.cfg
mv %buildroot/%_datadir/texmf/tex/latex/config/graphics.cfg %buildroot/%_sysconfdir/texmf/tex/latex/config/graphics.cfg
mv %buildroot/%_datadir/texmf/tex/latex/config/hyperref.cfg %buildroot/%_sysconfdir/texmf/tex/latex/config/hyperref.cfg
mkdir -p %buildroot/%_mandir/man1
rm -f %buildroot/%_bindir/thumbpdf
ln -s %_datadir/texmf-texlive/scripts/thumbpdf/thumbpdf.pl %buildroot/%_bindir/thumbpdf
mv %buildroot/%_datadir/texmf/doc/man/man1/thumbpdf.1 %buildroot/%_mandir/man1/thumbpdf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/thumbpdf.pdf %buildroot/%_mandir/man1/thumbpdf.pdf
rm -f %buildroot/%_bindir/perltex
ln -s %_datadir/texmf-texlive/scripts/perltex/perltex.pl %buildroot/%_bindir/perltex
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/generic
mkdir -p %buildroot/%_sysconfdir/texmf/tex/generic/xypic
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex/pict2e
rm -f %buildroot/%_bindir/epspdf
ln -s %_datadir/texmf-texlive/scripts/epspdf/epspdf %buildroot/%_bindir/epspdf
rm -f %buildroot/%_bindir/epspdftk
ln -s %_datadir/texmf-texlive/scripts/epspdf/epspdftk %buildroot/%_bindir/epspdftk
mv %buildroot/%_datadir/texmf-texlive/tex/generic/xypic/xylatex.ini %buildroot/%_sysconfdir/texmf/tex/generic/xypic/xylatex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/generic/xypic/xytex.ini %buildroot/%_sysconfdir/texmf/tex/generic/xypic/xytex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/latex/pict2e/pict2e.cfg %buildroot/%_sysconfdir/texmf/tex/latex/pict2e/pict2e.cfg

%files -n texlive-base -f alt-linux/texlive-base.files

%files -n texlive-fonts-recommended -f alt-linux/texlive-fonts-recommended.files

%files -n texlive-generic-recommended -f alt-linux/texlive-generic-recommended.files

%files -n texlive-latex-base -f alt-linux/texlive-latex-base.files

%files -n texlive-latex-recommended -f alt-linux/texlive-latex-recommended.files

%files -n texlive-pictures -f alt-linux/texlive-pictures.files

%files -n texlive-recommended

%changelog
* Sat Mar 12 2011 Kirill Maslinsky <kirill@altlinux.org> 2008.0-alt0.15
- Move perltex and marginnote here from texlive-latex-extra

* Tue Jul 28 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.14
- Remove dependencies from recommended packages to extra.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.13
- Relocate TeX packages to break cyclic dependencies between collections.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.12
- Skip latex unmets.
- Include lmodern fonts.

* Thu Mar 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.10
- Re-arrange documentation
  + leave texmf/doc and texmf-texlive/doc untouched
  + move man1 and man5 pages to %%_mandir

* Thu Feb 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.9
- Add tex-common and texlive-common to BuildRequires.
- Set conflicts with tetex-* packages.

* Fri Feb 20 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.8
- Move bin-latex back to texlive-latex-base.

* Tue Nov 25 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.5
- Move bin-latex to texlive-base-bin.

* Fri Oct 31 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.4
- Sources repacked.

* Wed Oct 08 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.1
- Initial build for ALT Linux.
