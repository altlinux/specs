Name: texlive-bin
Version: 2008.0
Release: alt0.15.7

Summary: Essential binaries
License: Distributable
Group: Publishing
Url: http://tug.org/texlive/

Source0: %name-texmf-%version-%release.tar
Source1: %name-texmf-dist-%version-%release.tar
Source2: texlive-source-%version.tar
Source3: %name-alt-%version.tar
Source5: config.trigger
Source6: tlmgr
#Patch0: %name-%version-%release.patch
Patch1: texlive-source-%version-%release.patch
Patch2: texlive-source-2008.0-alt-mubyte_cswrite.patch
Patch3: texlive-bin-2008-alt-perl522.patch
Patch4: %name-2008-alt-parallel-build.patch
Patch5: %name-2008-alt-gcc6.patch
Source7: texlive-bin-texmf-dist-2008.0-alt-perl522.patch

# Automatically added by buildreq on Mon Sep 22 2008
BuildRequires: flex fontconfig-devel libfreetype-devel gcc-c++ libXaw-devel libfreetype-devel libgd2-devel libpng12-devel libtinfo-devel libXpm-devel t1lib-devel

BuildRequires: tex-common texlive-common
BuildRequires(pre): rpm-build-texmf
BuildRequires: help2man
BuildRequires: perl-Tk perl-PDF-Reuse perl-Pod-Parser
BuildRequires: less vim-console rpm-utils automake autoconf
BuildRequires: python-dev

# because of lpr
%add_findreq_skiplist %_bindir/dvired

%add_findreq_skiplist %_datadir/texmf-texlive/scripts/xetex/perl/xdv2pdf_mergemarks
%add_findreq_skiplist %_datadir/texmf/scripts/texlive/*
%add_findreq_skiplist %_datadir/texmf/scripts/xindy/*
%add_findreq_skiplist %_datadir/texmf/scripts/a2ping/a2ping.pl

%set_compress_method none

# don't check documentation and sources
%add_findreq_skiplist %_datadir/texmf/doc/*
%add_findreq_skiplist %_datadir/texmf-texlive/doc/*
%add_findreq_skiplist %_datadir/texmf/source/*
%add_findreq_skiplist %_datadir/texmf-texlive/source/*

%description
These programs are regarded as basic for any TeX system.

%package -n libkpathsea
Summary: TeX Live: path search library for TeX (runtime part)
Group: System/Libraries

%description -n libkpathsea
This package contains the runtime part of the Kpathsea[rch] library,
which implements generic path searching, configuration, and
TeX-specific file searching.

%package -n libkpathsea-devel
Summary: TeX Live: path search library for TeX (development part)
Group: Development/C
Requires: libkpathsea = %version-%release
# file conflicts
Conflicts: tetex-core
Conflicts: tetex-devel

%description -n libkpathsea-devel
This package contains the static library and header files for the
Kpathsea[rch] library.

%package -n texlive-base-bin
Group: Publishing
Summary: Essential binaries
# file conflicts
Conflicts: tetex-afm
Conflicts: tetex-core
Conflicts: tetex-dvips
Conflicts: tetex-xdvi
Requires: tex-common >= 0.2

%description -n texlive-base-bin
These programs are regarded as basic for any TeX system.

%package -n texlive-extra-utils
Group: Publishing
Summary: TeX auxiliary programs
Requires: texlive-base, texlive-base-bin
# file conflicts
Conflicts: tetex-core
Conflicts: tetex-doc
Conflicts: tetex-dvilj
Conflicts: tetex-bibtex8

%description -n texlive-extra-utils
Various useful, but non-essential, support programs. Includes programs
and macros for DVI file manipulation, literate programming, patgen,
etc.

%package -n texlive-font-utils
Group: Publishing
Summary: TeX font-related programs
Requires: texlive-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-font-utils
Programs for conversion between font formats, testing fonts (virtual
fonts stuff, .gf and .pk manipulation, mft, fontinst, etc.)

%package -n texlive-lang-indic
Group: Publishing
Summary: Indic scripts
Requires: texlive-base

%description -n texlive-lang-indic
Essential indic

%package -n texlive-metapost
Group: Publishing
Summary: MetaPost (and Metafont) drawing packages
Requires: texlive-base, texlive-base-bin
# file conflicts
Conflicts: tetex-core

%description -n texlive-metapost
(none)

%package -n texlive-music
Group: Publishing
Summary: Music typesetting
Requires: texlive-latex-base

%description -n texlive-music
Music typesetting packages

%package -n texlive-omega
Group: Publishing
Summary: Omega
Requires: texlive-base
# file conflicts
Conflicts: tetex-core
Conflicts: tetex-dvips

%description -n texlive-omega
Omega, a 16-bit extended TeX by John Plaice and Yannis Haralambous

%package -n texlive-xetex
Group: Publishing
Summary: XeTeX packages
Requires: texlive-base

%description -n texlive-xetex
Packages for XeTeX, the Unicode/OpenType-enabled TeX by Jonathan Kew,
http://scripts.sil.org/xetex.

%prep
%setup -c -T -a2 -a3
sed -e 's,@TEXMFSYSVAR@,%_cachedir/texmf,g' %SOURCE6 > alt-linux/tlmgr
%ifarch e2k
# just like with libzio
sed -i 's,makecontext,makecontext_e2k,' `find -name lcoco.c`
%endif

cd source
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p0

sed -i  -e 's,^TEXMFSYSCONFIG =.*,TEXMFSYSCONFIG = %_sysconfdir/texmf,g' \
	-e 's,^TEXMFSYSVAR =.*,TEXMFSYSVAR = %_cachedir/texmf,g' \
	-e 's,^VARTEXFONTS =.*,VARTEXFONTS = $TEXMFVAR/fonts,g' \
	-e 's,^TEXMFVAR =.*,TEXMFVAR = ~/.texmf-var,g' \
	-e 's,^TEXMFCONFIG =.*,TEXMFCONFIG = ~/.texmf-config,g' \
	texk/kpathsea/texmf.cnf

# Fix linkage.
find -type f -print0 |
	xargs -r0 egrep -lZ 'sys_lib_(dl)?search_path_spec=' -- |
	xargs -r0 subst -p 's|\(sys_lib_\(dl\)\?search_path_spec=\)"[^"]*"|\1"/%_lib %_libdir"|' --

%build
cd source
%ifarch e2k
# lcc 1.21: avoid that -std=gnu++11/-std=gnu11 kludges from rpm-build alt100.96.E2K.4
export CXXFLAGS="%optflags"
export CFLAGS="%optflags"
%endif
%configure \
	--enable-shared \
	--without-lcdf-typetools --without-dvipng --without-dvipdfmx \
	--without-dvi2tty --without-texinfo --without-musixflx --without-texi2html \
	--without-ps2eps --without-psutils --without-sam2p \
	--without-t1utils --without-dvi2tty --without-dvidvi \
	--without-lacheck --without-tex4htk --without-ttf2pk --without-xindy \
	--with-cjkutils \
	--with-luatex \
	--with-system-zlib \
	--with-system-pnglib \
	--with-system-t1lib \
	--with-system-freetype \
	--with-freetype-include=%_includedir/freetype \
	--with-system-freetype2 \
	--with-freetype2-include=%_includedir \
	--with-system-gd \
	--with-system-icu \
	--with-icu-libdir=%_libdir

%make_build

%install
mkdir -p %buildroot%_man5dir %buildroot/%_datadir %buildroot/%_rpmlibdir
install -m755 %SOURCE5 %buildroot/%_rpmlibdir/texlive-5-config.filetrigger
# copy distro
tar xf %SOURCE0 -C %buildroot/%_datadir/
tar xf %SOURCE1 -C %buildroot/%_datadir/
# patch dvipdfm version; don't forget to apply in source tree
sed -i -e 's,^V 2$,V 3,g' %buildroot/%_texmfmain/dvipdfm/config/config

pushd %buildroot/%_datadir/texmf-dist
patch -p0 < %SOURCE7
popd

mkdir -p %buildroot/%_sysconfdir/texmf/{updmap.d,language.d}
cp alt-linux/*.cfg %buildroot/%_sysconfdir/texmf/updmap.d/
cp alt-linux/*.{dat,def} %buildroot/%_sysconfdir/texmf/language.d/

cd source
%makeinstall texmf=%buildroot%_datadir/texmf

# replace X.Org-depentent metafont with console version
rm -f %buildroot%_bindir/mf
ln -s mf-nowin %buildroot%_bindir/mf

# replace tlmgr with our own version
install -D -m755 ../alt-linux/tlmgr %buildroot/%_bindir/tlmgr


# remove links to unproper scripts
false && find %buildroot%_bindir -type l | \
	while read src; do
		dest=`readlink "$src"`;
		[ "${dest#../texmf}" = "$dest" ] || rm -f "$src";
	done
rm -f %buildroot%_bindir/getnonfreefonts-sys
# Remove ULTRIX and AIX shell dependence, and ksh as well
#egrep -lr '(RUNNING_SH5|RUNNING_BSH)' %buildroot%_bindir | xargs -r sed -i \
find	%buildroot%_bindir \
	%buildroot%_datadir/texmf/texconfig \
	%buildroot%_datadir/texmf-dist/scripts \
	-type f -print0 | xargs -r0 sed -i \
	-e '1{h;d}' \
	-e '/./{H;$!d;}' \
	-e 'x;/RUNNING_SH5/d' \
	-e '/RUNNING_BSH/d' \
	-e '/RUNNING_KSH/d'
# remove unexpected executables
rm -f %buildroot%_datadir/texmf/doc/latex/splitindex/*{-i386,.exe}
# get back owerwritten config
install -m644 texk/kpathsea/texmf.cnf %buildroot%_datadir/texmf/web2c/

mv %buildroot/%_datadir/texmf-dist %buildroot/%_datadir/texmf-texlive

mkdir -p %buildroot/%_sysconfdir/texmf/fmt.d
ln -s ../fmtutil/format.metafont.cnf %buildroot/%_sysconfdir/texmf/fmt.d/10-texlive-base-bin-metafont.cnf
ln -s ../fmtutil/format.tex.cnf %buildroot/%_sysconfdir/texmf/fmt.d/10-texlive-base-bin-tex.cnf
ln -s ../fmtutil/format.pdftex.cnf %buildroot/%_sysconfdir/texmf/fmt.d/10-texlive-base-bin-pdftex.cnf
ln -s ../fmtutil/format.luatex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-base-bin-luatex.cnf
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_cachedir/texmf
mkdir -p %buildroot/%_cachedir/texmf/web2c
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_mandir/man5
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/dvips
mkdir -p %buildroot/%_sysconfdir/texmf/dvips/config
mkdir -p %buildroot/%_sysconfdir/texmf/fmt.d
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/updmap.d
mkdir -p %buildroot/%_sysconfdir/texmf/web2c
rm -f %buildroot/%_bindir/pkfix
ln -s %_datadir/texmf/scripts/pkfix/pkfix.pl %buildroot/%_bindir/pkfix
rm -f %buildroot/%_bindir/ps4pdf
ln -s %_datadir/texmf-texlive/scripts/pst-pdf/ps4pdf %buildroot/%_bindir/ps4pdf
rm -f %buildroot/%_bindir/rungs
ln -s %_datadir/texmf/scripts/texlive/rungs.tlu %buildroot/%_bindir/rungs
rm -f %buildroot/%_bindir/simpdftex
ln -s %_datadir/texmf/scripts/simpdftex/simpdftex %buildroot/%_bindir/simpdftex
mv %buildroot/%_datadir/texmf/doc/man/man1/afm2tfm.1 %buildroot/%_mandir/man1/afm2tfm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/afm2tfm.pdf %buildroot/%_mandir/man1/afm2tfm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/allcm.1 %buildroot/%_mandir/man1/allcm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/allcm.pdf %buildroot/%_mandir/man1/allcm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/allec.1 %buildroot/%_mandir/man1/allec.1
mv %buildroot/%_datadir/texmf/doc/man/man1/allec.pdf %buildroot/%_mandir/man1/allec.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/allneeded.1 %buildroot/%_mandir/man1/allneeded.1
mv %buildroot/%_datadir/texmf/doc/man/man1/allneeded.pdf %buildroot/%_mandir/man1/allneeded.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/bg5conv.1 %buildroot/%_mandir/man1/bg5conv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/bg5conv.pdf %buildroot/%_mandir/man1/bg5conv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/bibtex.1 %buildroot/%_mandir/man1/bibtex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/bibtex.pdf %buildroot/%_mandir/man1/bibtex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/cef5conv.1 %buildroot/%_mandir/man1/cef5conv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/cef5conv.pdf %buildroot/%_mandir/man1/cef5conv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/cefconv.1 %buildroot/%_mandir/man1/cefconv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/cefconv.pdf %buildroot/%_mandir/man1/cefconv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/cefsconv.1 %buildroot/%_mandir/man1/cefsconv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/cefsconv.pdf %buildroot/%_mandir/man1/cefsconv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipdfm.1 %buildroot/%_mandir/man1/dvipdfm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipdfm.pdf %buildroot/%_mandir/man1/dvipdfm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvips.1 %buildroot/%_mandir/man1/dvips.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvips.pdf %buildroot/%_mandir/man1/dvips.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvired.1 %buildroot/%_mandir/man1/dvired.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvired.pdf %buildroot/%_mandir/man1/dvired.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ebb.1 %buildroot/%_mandir/man1/ebb.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ebb.pdf %buildroot/%_mandir/man1/ebb.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/etex.1 %buildroot/%_mandir/man1/etex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/etex.pdf %buildroot/%_mandir/man1/etex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/extconv.1 %buildroot/%_mandir/man1/extconv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/extconv.pdf %buildroot/%_mandir/man1/extconv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/fmtutil-sys.1 %buildroot/%_mandir/man1/fmtutil-sys.1
mv %buildroot/%_datadir/texmf/doc/man/man1/fmtutil-sys.pdf %buildroot/%_mandir/man1/fmtutil-sys.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/fmtutil.1 %buildroot/%_mandir/man1/fmtutil.1
mv %buildroot/%_datadir/texmf/doc/man/man1/fmtutil.pdf %buildroot/%_mandir/man1/fmtutil.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/fontinst.1 %buildroot/%_mandir/man1/fontinst.1
mv %buildroot/%_datadir/texmf/doc/man/man1/fontinst.pdf %buildroot/%_mandir/man1/fontinst.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/gftodvi.1 %buildroot/%_mandir/man1/gftodvi.1
mv %buildroot/%_datadir/texmf/doc/man/man1/gftodvi.pdf %buildroot/%_mandir/man1/gftodvi.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/gftopk.1 %buildroot/%_mandir/man1/gftopk.1
mv %buildroot/%_datadir/texmf/doc/man/man1/gftopk.pdf %buildroot/%_mandir/man1/gftopk.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/gftype.1 %buildroot/%_mandir/man1/gftype.1
mv %buildroot/%_datadir/texmf/doc/man/man1/gftype.pdf %buildroot/%_mandir/man1/gftype.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/gsftopk.1 %buildroot/%_mandir/man1/gsftopk.1
mv %buildroot/%_datadir/texmf/doc/man/man1/gsftopk.pdf %buildroot/%_mandir/man1/gsftopk.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/hbf2gf.1 %buildroot/%_mandir/man1/hbf2gf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/hbf2gf.pdf %buildroot/%_mandir/man1/hbf2gf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpseaccess.1 %buildroot/%_mandir/man1/kpseaccess.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpseaccess.pdf %buildroot/%_mandir/man1/kpseaccess.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsepath.1 %buildroot/%_mandir/man1/kpsepath.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsepath.pdf %buildroot/%_mandir/man1/kpsepath.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsereadlink.1 %buildroot/%_mandir/man1/kpsereadlink.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsereadlink.pdf %buildroot/%_mandir/man1/kpsereadlink.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsestat.1 %buildroot/%_mandir/man1/kpsestat.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsestat.pdf %buildroot/%_mandir/man1/kpsestat.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsetool.1 %buildroot/%_mandir/man1/kpsetool.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsetool.pdf %buildroot/%_mandir/man1/kpsetool.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsewhere.1 %buildroot/%_mandir/man1/kpsewhere.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsewhere.pdf %buildroot/%_mandir/man1/kpsewhere.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsewhich.1 %buildroot/%_mandir/man1/kpsewhich.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsewhich.pdf %buildroot/%_mandir/man1/kpsewhich.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsexpand.1 %buildroot/%_mandir/man1/kpsexpand.1
mv %buildroot/%_datadir/texmf/doc/man/man1/kpsexpand.pdf %buildroot/%_mandir/man1/kpsexpand.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/makeindex.1 %buildroot/%_mandir/man1/makeindex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/makeindex.pdf %buildroot/%_mandir/man1/makeindex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mf-nowin.1 %buildroot/%_mandir/man1/mf-nowin.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mf-nowin.pdf %buildroot/%_mandir/man1/mf-nowin.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mf.1 %buildroot/%_mandir/man1/mf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mf.pdf %buildroot/%_mandir/man1/mf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mft.1 %buildroot/%_mandir/man1/mft.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mft.pdf %buildroot/%_mandir/man1/mft.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mkindex.1 %buildroot/%_mandir/man1/mkindex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mkindex.pdf %buildroot/%_mandir/man1/mkindex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mkofm.1 %buildroot/%_mandir/man1/mkofm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mkofm.pdf %buildroot/%_mandir/man1/mkofm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexfmt.1 %buildroot/%_mandir/man1/mktexfmt.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexfmt.pdf %buildroot/%_mandir/man1/mktexfmt.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexlsr.1 %buildroot/%_mandir/man1/mktexlsr.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexlsr.pdf %buildroot/%_mandir/man1/mktexlsr.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexmf.1 %buildroot/%_mandir/man1/mktexmf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexmf.pdf %buildroot/%_mandir/man1/mktexmf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexpk.1 %buildroot/%_mandir/man1/mktexpk.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mktexpk.pdf %buildroot/%_mandir/man1/mktexpk.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mktextfm.1 %buildroot/%_mandir/man1/mktextfm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mktextfm.pdf %buildroot/%_mandir/man1/mktextfm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pdfetex.1 %buildroot/%_mandir/man1/pdfetex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pdfetex.pdf %buildroot/%_mandir/man1/pdfetex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pdftex.1 %buildroot/%_mandir/man1/pdftex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pdftex.pdf %buildroot/%_mandir/man1/pdftex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pktogf.1 %buildroot/%_mandir/man1/pktogf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pktogf.pdf %buildroot/%_mandir/man1/pktogf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pktype.1 %buildroot/%_mandir/man1/pktype.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pktype.pdf %buildroot/%_mandir/man1/pktype.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/rubibtex.1 %buildroot/%_mandir/man1/rubibtex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/rubibtex.pdf %buildroot/%_mandir/man1/rubibtex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/rumakeindex.1 %buildroot/%_mandir/man1/rumakeindex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/rumakeindex.pdf %buildroot/%_mandir/man1/rumakeindex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/sjisconv.1 %buildroot/%_mandir/man1/sjisconv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/sjisconv.pdf %buildroot/%_mandir/man1/sjisconv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tcdialog.1 %buildroot/%_mandir/man1/tcdialog.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tcdialog.pdf %buildroot/%_mandir/man1/tcdialog.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tex.1 %buildroot/%_mandir/man1/tex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tex.pdf %buildroot/%_mandir/man1/tex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texconfig-sys.1 %buildroot/%_mandir/man1/texconfig-sys.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texconfig-sys.pdf %buildroot/%_mandir/man1/texconfig-sys.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texconfig.1 %buildroot/%_mandir/man1/texconfig.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texconfig.pdf %buildroot/%_mandir/man1/texconfig.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texhash.1 %buildroot/%_mandir/man1/texhash.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texhash.pdf %buildroot/%_mandir/man1/texhash.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texlinks.1 %buildroot/%_mandir/man1/texlinks.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texlinks.pdf %buildroot/%_mandir/man1/texlinks.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tlmgr.1 %buildroot/%_mandir/man1/tlmgr.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tlmgr.pdf %buildroot/%_mandir/man1/tlmgr.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/updmap-sys.1 %buildroot/%_mandir/man1/updmap-sys.1
mv %buildroot/%_datadir/texmf/doc/man/man1/updmap-sys.pdf %buildroot/%_mandir/man1/updmap-sys.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/updmap.1 %buildroot/%_mandir/man1/updmap.1
mv %buildroot/%_datadir/texmf/doc/man/man1/updmap.pdf %buildroot/%_mandir/man1/updmap.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/vlna.1 %buildroot/%_mandir/man1/vlna.1
mv %buildroot/%_datadir/texmf/doc/man/man1/vlna.pdf %buildroot/%_mandir/man1/vlna.pdf
mv %buildroot/%_datadir/texmf/doc/man/man5/fmtutil.cnf.5 %buildroot/%_mandir/man5/fmtutil.cnf.5
mv %buildroot/%_datadir/texmf/doc/man/man5/fmtutil.cnf.pdf %buildroot/%_mandir/man5/fmtutil.cnf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man5/updmap.cfg.5 %buildroot/%_mandir/man5/updmap.cfg.5
mv %buildroot/%_datadir/texmf/doc/man/man5/updmap.cfg.pdf %buildroot/%_mandir/man5/updmap.cfg.pdf
mv %buildroot/%_datadir/texmf/dvips/config/canonex.cfg %buildroot/%_sysconfdir/texmf/dvips/config/canonex.cfg
mv %buildroot/%_datadir/texmf/dvips/config/cx.cfg %buildroot/%_sysconfdir/texmf/dvips/config/cx.cfg
mv %buildroot/%_datadir/texmf/dvips/config/deskjet.cfg %buildroot/%_sysconfdir/texmf/dvips/config/deskjet.cfg
mv %buildroot/%_datadir/texmf/dvips/config/dfaxhigh.cfg %buildroot/%_sysconfdir/texmf/dvips/config/dfaxhigh.cfg
mv %buildroot/%_datadir/texmf/dvips/config/dvired.cfg %buildroot/%_sysconfdir/texmf/dvips/config/dvired.cfg
mv %buildroot/%_datadir/texmf/dvips/config/epson.cfg %buildroot/%_sysconfdir/texmf/dvips/config/epson.cfg
mv %buildroot/%_datadir/texmf/dvips/config/ibmvga.cfg %buildroot/%_sysconfdir/texmf/dvips/config/ibmvga.cfg
mv %buildroot/%_datadir/texmf/dvips/config/ljfour.cfg %buildroot/%_sysconfdir/texmf/dvips/config/ljfour.cfg
mv %buildroot/%_datadir/texmf/dvips/config/qms.cfg %buildroot/%_sysconfdir/texmf/dvips/config/qms.cfg
mv %buildroot/%_datadir/texmf/dvips/config/toshiba.cfg %buildroot/%_sysconfdir/texmf/dvips/config/toshiba.cfg
mv %buildroot/%_datadir/texmf/fmtutil/fmtutil-hdr.cnf %buildroot/%_sysconfdir/texmf/fmt.d/00-fmtutil.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.cyramstex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.cyramstex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.cyrtex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.cyrtex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.cyrtexinfo.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.cyrtexinfo.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.luatex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.luatex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.metafont.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.metafont.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.pdftex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.pdftex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.tex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.tex.cnf
mv %buildroot/%_datadir/texmf/web2c/context.cnf %buildroot/%_sysconfdir/texmf/web2c/context.cnf
mv %buildroot/%_datadir/texmf/web2c/fmtutil.cnf %buildroot/%_cachedir/texmf/web2c/fmtutil.cnf
mv %buildroot/%_datadir/texmf/web2c/mktex.cnf %buildroot/%_sysconfdir/texmf/web2c/mktex.cnf
mv %buildroot/%_datadir/texmf/web2c/texmf.cnf %buildroot/%_sysconfdir/texmf/web2c/texmf.cnf
mv %buildroot/%_datadir/texmf/web2c/updmap-hdr.cfg %buildroot/%_sysconfdir/texmf/updmap.d/00-updmap.cfg
mv %buildroot/%_datadir/texmf/web2c/updmap.cfg %buildroot/%_cachedir/texmf/web2c/updmap.cfg
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_mandir/man5
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/texdoc
mkdir -p %buildroot/%_sysconfdir/texmf/xdvi
rm -f %buildroot/%_bindir/a2ping
ln -s %_datadir/texmf/scripts/a2ping/a2ping.pl %buildroot/%_bindir/a2ping
rm -f %buildroot/%_bindir/dviasm
ln -s %_datadir/texmf-texlive/scripts/dviasm/dviasm.py %buildroot/%_bindir/dviasm
rm -f %buildroot/%_bindir/e2pall
ln -s %_datadir/texmf/scripts/tetex/e2pall.pl %buildroot/%_bindir/e2pall
rm -f %buildroot/%_bindir/epstopdf
ln -s %_datadir/texmf/scripts/epstopdf/epstopdf.pl %buildroot/%_bindir/epstopdf
rm -f %buildroot/%_bindir/mkjobtexmf
ln -s %_datadir/texmf-texlive/scripts/mkjobtexmf/mkjobtexmf.pl %buildroot/%_bindir/mkjobtexmf
rm -f %buildroot/%_bindir/pdfatfi
ln -s %_datadir/texmf-texlive/scripts/oberdiek/pdfatfi.pl %buildroot/%_bindir/pdfatfi
rm -f %buildroot/%_bindir/pdfcrop
ln -s %_datadir/texmf-texlive/scripts/pdfcrop/pdfcrop.pl %buildroot/%_bindir/pdfcrop
rm -f %buildroot/%_bindir/texcount
ln -s %_datadir/texmf-texlive/scripts/texcount/TeXcount.pl %buildroot/%_bindir/texcount
rm -f %buildroot/%_bindir/texdoc
ln -s %_datadir/texmf/scripts/texlive/texdoc.tlu %buildroot/%_bindir/texdoc
rm -f %buildroot/%_bindir/texdoctk
ln -s %_datadir/texmf/scripts/tetex/texdoctk.pl %buildroot/%_bindir/texdoctk
mv %buildroot/%_datadir/texmf/doc/man/man1/a2ping.1 %buildroot/%_mandir/man1/a2ping.1
mv %buildroot/%_datadir/texmf/doc/man/man1/a2ping.pdf %buildroot/%_mandir/man1/a2ping.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ctangle.1 %buildroot/%_mandir/man1/ctangle.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ctangle.pdf %buildroot/%_mandir/man1/ctangle.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ctie.1 %buildroot/%_mandir/man1/ctie.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ctie.pdf %buildroot/%_mandir/man1/ctie.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/cweave.1 %buildroot/%_mandir/man1/cweave.1
mv %buildroot/%_datadir/texmf/doc/man/man1/cweave.pdf %buildroot/%_mandir/man1/cweave.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/cweb.1 %buildroot/%_mandir/man1/cweb.1
mv %buildroot/%_datadir/texmf/doc/man/man1/cweb.pdf %buildroot/%_mandir/man1/cweb.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/detex.1 %buildroot/%_mandir/man1/detex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/detex.pdf %buildroot/%_mandir/man1/detex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dt2dv.1 %buildroot/%_mandir/man1/dt2dv.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dt2dv.pdf %buildroot/%_mandir/man1/dt2dv.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dv2dt.1 %buildroot/%_mandir/man1/dv2dt.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dv2dt.pdf %buildroot/%_mandir/man1/dv2dt.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvi2fax.1 %buildroot/%_mandir/man1/dvi2fax.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvi2fax.pdf %buildroot/%_mandir/man1/dvi2fax.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvibook.1 %buildroot/%_mandir/man1/dvibook.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvibook.pdf %buildroot/%_mandir/man1/dvibook.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dviconcat.1 %buildroot/%_mandir/man1/dviconcat.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dviconcat.pdf %buildroot/%_mandir/man1/dviconcat.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvicopy.1 %buildroot/%_mandir/man1/dvicopy.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvicopy.pdf %buildroot/%_mandir/man1/dvicopy.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvihp.1 %buildroot/%_mandir/man1/dvihp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvihp.pdf %buildroot/%_mandir/man1/dvihp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj.1 %buildroot/%_mandir/man1/dvilj.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj.pdf %buildroot/%_mandir/man1/dvilj.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj2p.1 %buildroot/%_mandir/man1/dvilj2p.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj2p.pdf %buildroot/%_mandir/man1/dvilj2p.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj4.1 %buildroot/%_mandir/man1/dvilj4.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj4.pdf %buildroot/%_mandir/man1/dvilj4.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj4l.1 %buildroot/%_mandir/man1/dvilj4l.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj4l.pdf %buildroot/%_mandir/man1/dvilj4l.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj6.1 %buildroot/%_mandir/man1/dvilj6.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvilj6.pdf %buildroot/%_mandir/man1/dvilj6.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipdft.1 %buildroot/%_mandir/man1/dvipdft.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipdft.pdf %buildroot/%_mandir/man1/dvipdft.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipos.1 %buildroot/%_mandir/man1/dvipos.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvipos.pdf %buildroot/%_mandir/man1/dvipos.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dviselect.1 %buildroot/%_mandir/man1/dviselect.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dviselect.pdf %buildroot/%_mandir/man1/dviselect.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitodvi.1 %buildroot/%_mandir/man1/dvitodvi.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitodvi.pdf %buildroot/%_mandir/man1/dvitodvi.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitype.1 %buildroot/%_mandir/man1/dvitype.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitype.pdf %buildroot/%_mandir/man1/dvitype.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/e2pall.1 %buildroot/%_mandir/man1/e2pall.1
mv %buildroot/%_datadir/texmf/doc/man/man1/e2pall.pdf %buildroot/%_mandir/man1/e2pall.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/epstopdf.1 %buildroot/%_mandir/man1/epstopdf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/epstopdf.pdf %buildroot/%_mandir/man1/epstopdf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mkjobtexmf.1 %buildroot/%_mandir/man1/mkjobtexmf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mkjobtexmf.pdf %buildroot/%_mandir/man1/mkjobtexmf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/oxdvi.1 %buildroot/%_mandir/man1/oxdvi.1
mv %buildroot/%_datadir/texmf/doc/man/man1/oxdvi.pdf %buildroot/%_mandir/man1/oxdvi.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/patgen.1 %buildroot/%_mandir/man1/patgen.1
mv %buildroot/%_datadir/texmf/doc/man/man1/patgen.pdf %buildroot/%_mandir/man1/patgen.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pdftosrc.1 %buildroot/%_mandir/man1/pdftosrc.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pdftosrc.pdf %buildroot/%_mandir/man1/pdftosrc.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pooltype.1 %buildroot/%_mandir/man1/pooltype.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pooltype.pdf %buildroot/%_mandir/man1/pooltype.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/synctex.1 %buildroot/%_mandir/man1/synctex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/synctex.pdf %buildroot/%_mandir/man1/synctex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/t1mapper.1 %buildroot/%_mandir/man1/t1mapper.1
mv %buildroot/%_datadir/texmf/doc/man/man1/t1mapper.pdf %buildroot/%_mandir/man1/t1mapper.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tangle.1 %buildroot/%_mandir/man1/tangle.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tangle.pdf %buildroot/%_mandir/man1/tangle.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texdoc.1 %buildroot/%_mandir/man1/texdoc.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texdoc.pdf %buildroot/%_mandir/man1/texdoc.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/texdoctk.1 %buildroot/%_mandir/man1/texdoctk.1
mv %buildroot/%_datadir/texmf/doc/man/man1/texdoctk.pdf %buildroot/%_mandir/man1/texdoctk.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tie.1 %buildroot/%_mandir/man1/tie.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tie.pdf %buildroot/%_mandir/man1/tie.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tpic2pdftex.1 %buildroot/%_mandir/man1/tpic2pdftex.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tpic2pdftex.pdf %buildroot/%_mandir/man1/tpic2pdftex.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/weave.1 %buildroot/%_mandir/man1/weave.1
mv %buildroot/%_datadir/texmf/doc/man/man1/weave.pdf %buildroot/%_mandir/man1/weave.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/xdvi.1 %buildroot/%_mandir/man1/xdvi.1
mv %buildroot/%_datadir/texmf/doc/man/man1/xdvi.pdf %buildroot/%_mandir/man1/xdvi.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/xdvizilla.pdf %buildroot/%_mandir/man1/xdvizilla.pdf
mv %buildroot/%_datadir/texmf/doc/man/man5/synctex.5 %buildroot/%_mandir/man5/synctex.5
mv %buildroot/%_datadir/texmf/doc/man/man5/synctex.pdf %buildroot/%_mandir/man5/synctex.pdf
mv %buildroot/%_datadir/texmf/texdoc/texdoc.cnf %buildroot/%_sysconfdir/texmf/texdoc/texdoc.cnf
mv %buildroot/%_datadir/texmf/xdvi/XDvi %buildroot/%_sysconfdir/texmf/xdvi/XDvi
mv %buildroot/%_datadir/texmf/xdvi/xdvi.cfg %buildroot/%_sysconfdir/texmf/xdvi/xdvi.cfg
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/fontinst
mkdir -p %buildroot/%_sysconfdir/texmf/tex/fontinst/base
mv %buildroot/%_datadir/texmf-texlive/tex/fontinst/base/fontinst.ini %buildroot/%_sysconfdir/texmf/tex/fontinst/base/fontinst.ini
mv %buildroot/%_datadir/texmf/doc/man/man1/afm2pl.1 %buildroot/%_mandir/man1/afm2pl.1
mv %buildroot/%_datadir/texmf/doc/man/man1/afm2pl.pdf %buildroot/%_mandir/man1/afm2pl.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mag.1 %buildroot/%_mandir/man1/mag.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mag.pdf %buildroot/%_mandir/man1/mag.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pfb2pfa.1 %buildroot/%_mandir/man1/pfb2pfa.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pfb2pfa.pdf %buildroot/%_mandir/man1/pfb2pfa.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pk2bm.1 %buildroot/%_mandir/man1/pk2bm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pk2bm.pdf %buildroot/%_mandir/man1/pk2bm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/pltotf.1 %buildroot/%_mandir/man1/pltotf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/pltotf.pdf %buildroot/%_mandir/man1/pltotf.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ps2pk.1 %buildroot/%_mandir/man1/ps2pk.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ps2pk.pdf %buildroot/%_mandir/man1/ps2pk.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/tftopl.1 %buildroot/%_mandir/man1/tftopl.1
mv %buildroot/%_datadir/texmf/doc/man/man1/tftopl.pdf %buildroot/%_mandir/man1/tftopl.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/vftovp.1 %buildroot/%_mandir/man1/vftovp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/vftovp.pdf %buildroot/%_mandir/man1/vftovp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/vptovf.1 %buildroot/%_mandir/man1/vptovf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/vptovf.pdf %buildroot/%_mandir/man1/vptovf.pdf
rm -f %buildroot/%_bindir/ebong
ln -s %_datadir/texmf-texlive/scripts/bengali/ebong.py %buildroot/%_bindir/ebong
ln -s ../fmtutil/format.metapost.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-metapost-metapost.cnf
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/metapost
mkdir -p %buildroot/%_sysconfdir/texmf/metapost/config
mv %buildroot/%_datadir/texmf-texlive/metapost/config/mfmp.ini %buildroot/%_sysconfdir/texmf/metapost/config/mfmp.ini
mv %buildroot/%_datadir/texmf-texlive/metapost/config/mpost.ini %buildroot/%_sysconfdir/texmf/metapost/config/mpost.ini
mv %buildroot/%_datadir/texmf/doc/man/man1/dmp.1 %buildroot/%_mandir/man1/dmp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dmp.pdf %buildroot/%_mandir/man1/dmp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitomp.1 %buildroot/%_mandir/man1/dvitomp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/dvitomp.pdf %buildroot/%_mandir/man1/dvitomp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/makempx.1 %buildroot/%_mandir/man1/makempx.1
mv %buildroot/%_datadir/texmf/doc/man/man1/makempx.pdf %buildroot/%_mandir/man1/makempx.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mpost.1 %buildroot/%_mandir/man1/mpost.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mpost.pdf %buildroot/%_mandir/man1/mpost.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mpto.1 %buildroot/%_mandir/man1/mpto.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mpto.pdf %buildroot/%_mandir/man1/mpto.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/newer.1 %buildroot/%_mandir/man1/newer.1
mv %buildroot/%_datadir/texmf/doc/man/man1/newer.pdf %buildroot/%_mandir/man1/newer.pdf
mv %buildroot/%_datadir/texmf/fmtutil/format.metapost.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.metapost.cnf
ln -s ../fmtutil/format.aleph.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-omega-aleph.cnf
ln -s ../fmtutil/format.omega.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-omega-omega.cnf
mkdir -p %buildroot/%_mandir/man1
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/dvips
mkdir -p %buildroot/%_sysconfdir/texmf/dvips/omega
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/lambda
mkdir -p %buildroot/%_sysconfdir/texmf/tex/lambda/antomega
mkdir -p %buildroot/%_sysconfdir/texmf/tex/lambda/base
mkdir -p %buildroot/%_sysconfdir/texmf/tex/lambda/config
mv %buildroot/%_datadir/texmf-texlive/dvips/omega/omega.cfg %buildroot/%_sysconfdir/texmf/dvips/omega/omega.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/lambda/antomega/antomega.cfg %buildroot/%_sysconfdir/texmf/tex/lambda/antomega/antomega.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/lambda/antomega/hyphen.cfg %buildroot/%_sysconfdir/texmf/tex/lambda/antomega/hyphen.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/lambda/base/omarab.cfg %buildroot/%_sysconfdir/texmf/tex/lambda/base/omarab.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/lambda/base/omlgc.cfg %buildroot/%_sysconfdir/texmf/tex/lambda/base/omlgc.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/lambda/config/lambda.ini %buildroot/%_sysconfdir/texmf/tex/lambda/config/lambda.ini
mv %buildroot/%_datadir/texmf/doc/man/man1/lambda.1 %buildroot/%_mandir/man1/lambda.1
mv %buildroot/%_datadir/texmf/doc/man/man1/lambda.pdf %buildroot/%_mandir/man1/lambda.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/mkocp.1 %buildroot/%_mandir/man1/mkocp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/mkocp.pdf %buildroot/%_mandir/man1/mkocp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/odvicopy.1 %buildroot/%_mandir/man1/odvicopy.1
mv %buildroot/%_datadir/texmf/doc/man/man1/odvicopy.pdf %buildroot/%_mandir/man1/odvicopy.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/odvips.1 %buildroot/%_mandir/man1/odvips.1
mv %buildroot/%_datadir/texmf/doc/man/man1/odvips.pdf %buildroot/%_mandir/man1/odvips.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/odvitype.1 %buildroot/%_mandir/man1/odvitype.1
mv %buildroot/%_datadir/texmf/doc/man/man1/odvitype.pdf %buildroot/%_mandir/man1/odvitype.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ofm2opl.1 %buildroot/%_mandir/man1/ofm2opl.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ofm2opl.pdf %buildroot/%_mandir/man1/ofm2opl.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/omega.1 %buildroot/%_mandir/man1/omega.1
mv %buildroot/%_datadir/texmf/doc/man/man1/omega.pdf %buildroot/%_mandir/man1/omega.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/opl2ofm.1 %buildroot/%_mandir/man1/opl2ofm.1
mv %buildroot/%_datadir/texmf/doc/man/man1/opl2ofm.pdf %buildroot/%_mandir/man1/opl2ofm.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/otp2ocp.1 %buildroot/%_mandir/man1/otp2ocp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/otp2ocp.pdf %buildroot/%_mandir/man1/otp2ocp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/outocp.1 %buildroot/%_mandir/man1/outocp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/outocp.pdf %buildroot/%_mandir/man1/outocp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ovf2ovp.1 %buildroot/%_mandir/man1/ovf2ovp.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ovf2ovp.pdf %buildroot/%_mandir/man1/ovf2ovp.pdf
mv %buildroot/%_datadir/texmf/doc/man/man1/ovp2ovf.1 %buildroot/%_mandir/man1/ovp2ovf.1
mv %buildroot/%_datadir/texmf/doc/man/man1/ovp2ovf.pdf %buildroot/%_mandir/man1/ovp2ovf.pdf
mv %buildroot/%_datadir/texmf/fmtutil/format.aleph.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.aleph.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.omega.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.omega.cnf
ln -s ../fmtutil/format.xetex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-xetex-xetex.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/xelatex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/xelatex/fontspec
mkdir -p %buildroot/%_sysconfdir/texmf/tex/xelatex/xetexconfig
mv %buildroot/%_datadir/texmf-texlive/tex/xelatex/fontspec/fontspec.cfg %buildroot/%_sysconfdir/texmf/tex/xelatex/fontspec/fontspec.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/xelatex/xetexconfig/crop.cfg %buildroot/%_sysconfdir/texmf/tex/xelatex/xetexconfig/crop.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/xelatex/xetexconfig/geometry.cfg %buildroot/%_sysconfdir/texmf/tex/xelatex/xetexconfig/geometry.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/xelatex/xetexconfig/hyperref.cfg %buildroot/%_sysconfdir/texmf/tex/xelatex/xetexconfig/hyperref.cfg
mv %buildroot/%_datadir/texmf/fmtutil/format.xetex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.xetex.cnf

ln -s %_sysconfdir/texmf/web2c/texmf.cnf %buildroot%_datadir/texmf/web2c/texmf.cnf

%files -n libkpathsea
%_libdir/*.so.*

%files -n libkpathsea-devel
%_libdir/*.so
%_libdir/*.a
%_includedir/kpathsea

%files -n texlive-base-bin -f alt-linux/texlive-base-bin.files
%_bindir/tlmgr
%_datadir/texmf/web2c/texmf.cnf
%_rpmlibdir/texlive-*.filetrigger

%files -n texlive-extra-utils -f alt-linux/texlive-extra-utils.files

%files -n texlive-font-utils -f alt-linux/texlive-font-utils.files

%files -n texlive-lang-indic -f alt-linux/texlive-lang-indic.files

%files -n texlive-metapost -f alt-linux/texlive-metapost.files

%files -n texlive-music -f alt-linux/texlive-music.files

%files -n texlive-omega -f alt-linux/texlive-omega.files

%files -n texlive-xetex -f alt-linux/texlive-xetex.files

%changelog
* Tue Dec 05 2017 Andrew Savchenko <bircoph@altlinux.org> 2008.0-alt0.15.7
- Fix parallel build.
- Fix hbf2gf linking error: undefined reference to `read_row'.

* Sun Nov 12 2017 Michael Shigorin <mike@altlinux.org> 2008.0-alt0.15.6.2
- E2K: avoid -std=gnu++11

* Fri Jan 27 2017 Michael Shigorin <mike@altlinux.org> 2008.0-alt0.15.6.1
- E2K: use makecontext_e2k()

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2008.0-alt0.15.6
- bugfixes for perl 5.22

* Tue Apr 09 2013 Fr. Br. George <george@altlinux.ru> 2008.0-alt0.15.5
- Fix off-by-one bug in tex

* Tue Apr 02 2013 Fr. Br. George <george@altlinux.ru> 2008.0-alt0.15.4
- Rebuild with libpng12

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2008.0-alt0.15.3
- Rebuild with Python-2.7

* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 2008.0-alt0.15.2
- Fixed build with new perl.
- Fixed RPATH.

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008.0-alt0.15.1
- Rebuilt with python 2.6

* Fri Oct 30 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.15
- Increase maximum compatible PDF version to 1.3 (ALT #22006).
- Set conflict on extra-utils with tetex-bibtex8 (ALT #20798).
- Move bin-xdvi to extra-utils due to X11 requirement.
- Replace X.Org-depentent metafont with console version.
- Move mkocp to texlive-omega (and thus break dependence).
- Move dvi2fax and dvipdft to extra-utils due to ghostscript dependence.

* Tue Jul 28 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.14
- Remove dependencies from recommended packages to extra.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.12
- Fix build with gcc4.4.
- Include luatex and xelatex.

* Thu Apr 23 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.11
- Move texhash filetrigger to tex-common and require it.

* Thu Mar 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.10
- Re-arrange documentation
  + leave texmf/doc and texmf-texlive/doc untouched
  + move man1 and man5 pages to %%_mandir
- Built with system-wide T1 library.

* Thu Feb 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.9
- Add tex-common and texlive-common to BuildRequires.
- Set conflicts with tetex-* packages.
- Set TEXMFSYSVAR to /var/cache/texmf.
- Remove .texlive2008 prefix from TEXMFCONFIG and TEXMFVAR.

* Fri Feb 20 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.8
- Move bin-latex to texlive-latex-base.

* Tue Feb 17 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.7
- CJK (Chinese, Japanese, Korean) support was added.

* Sat Dec 13 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.6
- Restore mktex.cnf.

* Tue Nov 25 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.5
- Move bin-cyrillic to texlive-base-bin.
- Move bin-vlna.i386-linux to texlive-base-bin.
- Move bin-latex to texlive-base-bin.

* Fri Oct 31 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.4
- Sources repacked.

* Wed Oct 22 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.2
- Correct FreeType headers path
- Use tinfo as a termlib in texinfo
- Fix freetype headers includes (CPPFLAGS)
- Debian patches:
  + 16_texdoctk
  + 53_builtin-searchpath-fix
  + 54_checklib_fixes
- Link libTECkit with zlib
- Fix script linking by providing kpsewhich with LD_LIBRARY_PATH
- Turn TEXMFSYSCONFIG back to TEXMFMAIN
- Install linked scripts into correct place

* Wed Oct 08 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.1
- Initial build for ALT Linux.
