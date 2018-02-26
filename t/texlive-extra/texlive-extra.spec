Name: texlive-extra
Version: 2008.0
Release: alt0.16
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Extra TeXLive fonts, formats, etc.
License: Distributable
Group: Publishing
Url: http://tug.org/texlive/

Source0: %name-texmf-dist-%version-%release.tar
Source1: %name-alt-%version.tar
Source2: %name-texmf-%version-%release.tar

BuildArch: noarch

BuildRequires: tex-common texlive-common
BuildRequires(pre): rpm-build-texmf
BuildRequires: less vim-console rpm-utils automake autoconf
BuildRequires: perl-Encode perl-Spreadsheet-ParseExcel perl-Pod-Parser

Requires: texlive-latex-extra texlive-fonts-extra

%set_compress_method none

# don't check documentation and sources
%add_findreq_skiplist %_datadir/texmf/doc/*
%add_findreq_skiplist %_datadir/texmf-texlive/doc/*
%add_findreq_skiplist %_datadir/texmf/source/*
%add_findreq_skiplist %_datadir/texmf-texlive/source/*

# fonts with .pl extension
%add_findreq_skiplist %_datadir/texmf-texlive/fonts/tfm/public/kpfonts/*

# depend on missing Perl modules
%add_findreq_skiplist %_datadir/texmf-texlive/fonts/source/public/wsuipa/compilefonts

# texlive-generic-extra
#_datadir/texmf-texlive/tex/generic/ofs/ofs-slt.tex
%add_texmf_req_skip latex/styl

# texlive-latex-extra
#_datadir/texmf-texlive/tex/latex/gcite/gcite.sty
%add_texmf_req_skip latex/biblatex
#_datadir/texmf-texlive/tex/latex/timesht/timesht.cls
%add_texmf_req_skip latex/calendar
#_datadir/texmf-texlive/tex/latex/fancytooltips/fancytooltips.sty
#_datadir/texmf-texlive/tex/latex/fancytooltips/fancytooltips.sty
%add_texmf_req_skip latex/eforms
#_datadir/texmf-texlive/tex/latex/eCards/eCards.sty
%add_texmf_req_skip latex/exerquiz
#_datadir/texmf-texlive/tex/latex/ifmslide/ifmslide.sty
%add_texmf_req_skip latex/fixseminar
#_datadir/texmf-texlive/tex/latex/HA-prosper/Styles/TCS/HAPTCSTealBlue.sty
#_datadir/texmf-texlive/tex/latex/HA-prosper/Styles/TCS/HAPTCSgrad.sty
%add_texmf_req_skip latex/gradient
#_datadir/texmf-texlive/tex/latex/lhelp/lhelp.sty
%add_texmf_req_skip latex/lhelpx
#_datadir/texmf-texlive/tex/latex/ednotes/ednotes.sty
%add_texmf_req_skip latex/linenox0
#_datadir/texmf-texlive/tex/latex/rmpage/rmpage.sty
#_datadir/texmf-texlive/tex/latex/rmpage/rmpage.sty
%add_texmf_req_skip latex/lucasual
%add_texmf_req_skip latex/lucida-helvetica
#_datadir/texmf-texlive/tex/latex/ucs/mkrenc.def
%add_texmf_req_skip latex/makor
#_datadir/texmf-texlive/tex/latex/maple/mtn.cls
%add_texmf_req_skip latex/mapleenv
#_datadir/texmf-texlive/tex/latex/mtgreek/mtgreek.sty
#_datadir/texmf-texlive/tex/latex/kluwer/klups.sty
#_datadir/texmf-texlive/tex/latex/kluwer/klups.sty
#_datadir/texmf-texlive/tex/latex/nrc/nrc1.cls
#_datadir/texmf-texlive/tex/latex/nrc/nrc2.cls
%add_texmf_req_skip latex/mathtime
#_datadir/texmf-texlive/tex/latex/timesht/timesht.cls
%add_texmf_req_skip latex/mygoth
#_datadir/texmf-texlive/tex/latex/xoptarg/xoptarg.sty
%add_texmf_req_skip latex/newcommand
#_datadir/texmf-texlive/tex/latex/ifmslide/ifmslide.sty
%add_texmf_req_skip latex/texpower
#_datadir/texmf-texlive/tex/latex/gmdoc/gmdocc.cls
%add_texmf_req_skip latex/tgpagella
#_datadir/texmf-texlive/tex/latex/thmtools/thm-kv.sty
%add_texmf_req_skip latex/thmbox
#_datadir/texmf-texlive/tex/latex/eCards/eCards.sty
%add_texmf_req_skip latex/web
#_datadir/texmf-texlive/tex/latex/gmutils/gmutils.sty
%add_texmf_req_skip latex/xltxtra

# texlive-publishers
#_datadir/texmf-texlive/tex/latex/classicthesis/classicthesis.sty
%add_texmf_req_skip latex/MinionPro
# texmf(latex/a4-mancs)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/muthesis/third-rep.cls
# texmf(latex/axodraw)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/hep/hep.sty
# texmf(latex/ccmap)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/thuthesis/thuthesis.cls
# texmf(latex/citesort)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/imac/imac.sty
# texmf(latex/CJKpunct)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/thuthesis/thuthesis.cls
# texmf(latex/dogma)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/nostarch/nostarch.cls
# texmf(latex/feynmf)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/hep/hep.sty
# texmf(latex/futurans)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/nostarch/nostarch.cls
# texmf(latex/nbaskerv)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/nostarch/nostarch.cls
# texmf(latex/thsmc)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/nostarch/nostarch.cls
# texmf(latex/wrisym)
%add_findreq_skiplist %_datadir/texmf-texlive/tex/latex/ebsthesis/ebsthesis.cls

%description
Virtual package depending on real extra TeXLive subsystem

%package -n texlive-bibtex-extra
Group: Publishing
Summary: Extra BibTeX styles
Requires: texlive-latex-base

%description -n texlive-bibtex-extra
Additional BibTeX styles and bibliography databases.

%package -n texlive-fonts-extra
Group: Publishing
Summary: Extra fonts
Requires: texlive-base

%description -n texlive-fonts-extra
(none)

%package -n texlive-formats-extra
Group: Publishing
Summary: Extra formats
Requires: texlive-base, texlive-base-bin, texlive-latex-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-formats-extra
A collection of TeX `formats', ie large-scale macro packages designed
to be dumped into .fmt file

%package -n texlive-games
Group: Publishing
Summary: Games typesetting (chess, etc)
Requires: texlive-latex-base

%description -n texlive-games
Setups for typesetting various board games, including chess

%package -n texlive-generic-extra
Group: Publishing
Summary: Extra generic packages
Requires: texlive-base

%description -n texlive-generic-extra
Extra packages that work with multiple formats.

%package -n texlive-humanities
Group: Publishing
Summary: Humanities packages

%description -n texlive-humanities
Packages for law, linguistics, the social sciences, the humanities,
etc.

%package -n texlive-latex3
Group: Publishing
Summary: LaTeX3 packages
Requires: texlive-latex-base

%description -n texlive-latex3
(none)

%package -n texlive-latex-extra
Group: Publishing
Summary: LaTeX supplementary packages
Requires: texlive-base-bin, texlive-latex-base

%description -n texlive-latex-extra
A large collection of add-on packages for LaTeX.

%package -n texlive-math-extra
Group: Publishing
Summary: Advanced math typesetting
Requires: texlive-base-bin, texlive-fonts-recommended, texlive-latex-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-math-extra
Extra math

%package -n texlive-plain-extra
Group: Publishing
Summary: Plain TeX supplementary packages
Requires: texlive-base

%description -n texlive-plain-extra
A collection of add-on packages and macros for plain TeX.

%package -n texlive-pstricks
Group: Publishing
Summary: PSTricks packages
Requires: texlive-base, texlive-generic-recommended

%description -n texlive-pstricks
Additional PSTricks packages

%package -n texlive-publishers
Group: Publishing
Summary: Support for publishers and theses
Requires: texlive-latex-base

%description -n texlive-publishers
(none)

%package -n texlive-science
Group: Publishing
Summary: Typesetting for natural and computer sciences
Requires: texlive-latex-base

%description -n texlive-science
Typesetting for natural and computer sciences

%prep
%setup -c -T -a1
sed -i  -e '/splitindex-Linux-i386$/d' \
	-e '/splitindex-OpenBSD-i386$/d' \
	-e '/splitindex.exe$/d' \
	alt-linux/texlive-latex-extra.files

sed -i -e 's,README.orig$,README,g' \
	alt-linux/texlive-publishers.files

%install
mkdir -p %buildroot/%_datadir
tar xf %SOURCE0 -C %buildroot/%_datadir/
tar xf %SOURCE2 -C %buildroot/%_datadir/

mkdir -p %buildroot/%_sysconfdir/texmf/updmap.d
cp alt-linux/*.cfg %buildroot/%_sysconfdir/texmf/updmap.d/

# Remove ULTRIX and AIX shell dependence, and ksh as well
#egrep -lr '(RUNNING_SH5|RUNNING_BSH)' %buildroot%_bindir | xargs -r sed -i \
find	%buildroot%_datadir/texmf-dist/scripts \
	-type f -print0 | xargs -r0 sed -i \
	-e '1{h;d}' \
	-e '/./{H;$!d;}' \
	-e 'x;/RUNNING_SH5/d' \
	-e '/RUNNING_BSH/d' \
	-e '/RUNNING_KSH/d'

rm -f %buildroot/%_datadir/texmf-dist/doc/latex/splitindex/*{i386,exe}
(cd %buildroot/%_datadir/texmf-dist/doc/latex/nddiss/example-v1.3/;
 mv README.orig README)

mv %buildroot/%_datadir/texmf-dist %buildroot/%_datadir/texmf-texlive

mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_sysconfdir/texmf/fmt.d
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/dvips
mkdir -p %buildroot/%_sysconfdir/texmf/dvips/antp
mkdir -p %buildroot/%_sysconfdir/texmf/dvips/zefonts
mv %buildroot/%_datadir/texmf-texlive/dvips/antp/antp.cfg %buildroot/%_sysconfdir/texmf/dvips/antp/antp.cfg
mv %buildroot/%_datadir/texmf-texlive/dvips/zefonts/slantcm.cfg %buildroot/%_sysconfdir/texmf/dvips/zefonts/slantcm.cfg
ln -s ../fmtutil/format.eplain.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-formats-extra-eplain.cnf
ln -s ../fmtutil/format.physe.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-formats-extra-physe.cnf
ln -s ../fmtutil/format.texsis.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-formats-extra-texsis.cnf
ln -s ../fmtutil/format.phyzzx.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-formats-extra-phyzzx.cnf
ln -s ../fmtutil/format.mltex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-formats-extra-mltex.cnf
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/alatex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/alatex/base
mkdir -p %buildroot/%_sysconfdir/texmf/tex/mltex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/mltex/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex/physe
mkdir -p %buildroot/%_sysconfdir/texmf/tex/physe/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex/phyzzx
mkdir -p %buildroot/%_sysconfdir/texmf/tex/phyzzx/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex/psizzl
mkdir -p %buildroot/%_sysconfdir/texmf/tex/psizzl/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex/texsis
mkdir -p %buildroot/%_sysconfdir/texmf/tex/texsis/config
mv %buildroot/%_datadir/texmf-texlive/tex/alatex/base/metaclas.cfg %buildroot/%_sysconfdir/texmf/tex/alatex/base/metaclas.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/mltex/config/mltex.ini %buildroot/%_sysconfdir/texmf/tex/mltex/config/mltex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/physe/config/physe.ini %buildroot/%_sysconfdir/texmf/tex/physe/config/physe.ini
mv %buildroot/%_datadir/texmf-texlive/tex/phyzzx/config/phyzzx.ini %buildroot/%_sysconfdir/texmf/tex/phyzzx/config/phyzzx.ini
mv %buildroot/%_datadir/texmf-texlive/tex/psizzl/config/psizzl.ini %buildroot/%_sysconfdir/texmf/tex/psizzl/config/psizzl.ini
mv %buildroot/%_datadir/texmf-texlive/tex/texsis/config/texsis.ini %buildroot/%_sysconfdir/texmf/tex/texsis/config/texsis.ini
mv %buildroot/%_datadir/texmf/doc/man/man1/eplain.1 %buildroot/%_mandir/man1/eplain.1
mv %buildroot/%_datadir/texmf/doc/man/man1/eplain.pdf %buildroot/%_mandir/man1/eplain.pdf
mv %buildroot/%_datadir/texmf/fmtutil/format.eplain.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.eplain.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.mltex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.mltex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.physe.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.physe.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.phyzzx.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.phyzzx.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.texsis.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.texsis.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/latex/contour
rm -f %buildroot/%_bindir/makeglossaries
ln -s %_datadir/texmf-texlive/scripts/glossaries/makeglossaries %buildroot/%_bindir/makeglossaries
rm -f %buildroot/%_bindir/vpe
ln -s %_datadir/texmf-texlive/scripts/vpe/vpe.pl %buildroot/%_bindir/vpe
mv %buildroot/%_datadir/texmf-texlive/tex/latex/contour/contour.cfg %buildroot/%_sysconfdir/texmf/tex/latex/contour/contour.cfg
ln -s ../fmtutil/format.amstex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-math-extra-amstex.cnf
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/amstex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/amstex/config
mv %buildroot/%_datadir/texmf-texlive/tex/amstex/config/amstex.ini %buildroot/%_sysconfdir/texmf/tex/amstex/config/amstex.ini
mv %buildroot/%_datadir/texmf/doc/man/man1/amstex.1 %buildroot/%_mandir/man1/amstex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/amstex.pdf %buildroot/%_mandir/man1/amstex.pdf
mv %buildroot/%_datadir/texmf/fmtutil/format.amstex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.amstex.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain/hyplain
mv %buildroot/%_datadir/texmf-texlive/tex/plain/hyplain/hypdfplain.ini %buildroot/%_sysconfdir/texmf/tex/plain/hyplain/hypdfplain.ini
rm -f %buildroot/%_bindir/pst2pdf
ln -s %_datadir/texmf-texlive/scripts/pst2pdf/pst2pdf.pl %buildroot/%_bindir/pst2pdf

%files -n texlive-bibtex-extra -f alt-linux/texlive-bibtex-extra.files

%files -n texlive-fonts-extra -f alt-linux/texlive-fonts-extra.files

%files -n texlive-formats-extra -f alt-linux/texlive-formats-extra.files

%files -n texlive-games -f alt-linux/texlive-games.files

%files -n texlive-generic-extra -f alt-linux/texlive-generic-extra.files

%files -n texlive-humanities -f alt-linux/texlive-humanities.files

%files -n texlive-latex3 -f alt-linux/texlive-latex3.files

%files -n texlive-latex-extra -f alt-linux/texlive-latex-extra.files

%files -n texlive-math-extra -f alt-linux/texlive-math-extra.files

%files -n texlive-plain-extra -f alt-linux/texlive-plain-extra.files

%files -n texlive-pstricks -f alt-linux/texlive-pstricks.files

%files -n texlive-publishers -f alt-linux/texlive-publishers.files

%files -n texlive-science -f alt-linux/texlive-science.files

%files -n texlive-extra

%changelog
* Sun Mar 13 2011 Kirill Maslinsky <kirill@altlinux.org> 2008.0-alt0.16
- skip artificial unmet dependency

* Sat Mar 12 2011 Kirill Maslinsky <kirill@altlinux.org> 2008.0-alt0.15
- Remove perltex and marginnote (moved into texlive-latex-recommended)

* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 2008.0-alt0.14.1
- Fixed build with new perl.

* Tue Jul 28 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.14
- Remove dependencies from recommended packages to extra.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.13
- Relocate TeX packages to break cyclic dependencies between collections.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.12
- Skip latex unmets.

* Thu Mar 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.10
- Re-arrange documentation
  + leave texmf/doc and texmf-texlive/doc untouched
  + move man1 and man5 pages to %%_mandir

* Thu Feb 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.9
- Add tex-common and texlive-common to BuildRequires.
- Set conflicts with tetex-* packages.

* Fri Oct 31 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.4
- Sources repacked.

* Wed Oct 08 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.1
- Initial build for ALT Linux.
