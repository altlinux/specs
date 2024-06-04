# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/ccache /usr/bin/doxygen /usr/bin/xmlto /usr/bin/zip boost-devel boost-filesystem-devel boost-program_options-devel bzlib-devel gcc-c++ glib2-devel gobject-introspection-devel imake libICE-devel libSM-devel libX11-devel libXt-devel libjpeg-devel libopenmotif-devel libtiff-devel perl(Archive/Tar.pm) perl(BibTeX/Parser.pm) perl(BibTeX/Parser/Author.pm) perl(Date/Format.pm) perl(Date/Parse.pm) perl(Digest/SHA1.pm) perl(Encode.pm) perl(Encode/Alias.pm) perl(Encode/Locale.pm) perl(Fatal.pm) perl(File/Copy/Recursive.pm) perl(File/Which.pm) perl(HTML/FormatText.pm) perl(HTML/TreeBuilder.pm) perl(HTTP/Request/Common.pm) perl(IO/Compress/Zip.pm) perl(IPC/System/Simple.pm) perl(JSON.pm) perl(LWP/Protocol/https.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(LaTeX/ToUnicode.pm) perl(Locale/Maketext/Simple.pm)
BuildRequires: perl(Math/Trig.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Spreadsheet/ParseExcel.pm) perl(Statistics/Descriptive.pm) perl(Statistics/Distributions.pm) perl(Term/ANSIColor.pm) perl(Term/ReadKey.pm) perl(Tk.pm) perl(Tk/Dialog.pm) perl(Tk/NoteBook.pm) perl(URI/Escape.pm) perl(Unicode/Normalize.pm) perl(WWW/Mechanize.pm) perl(autodie.pm) pkgconfig(sdl2) python3-devel rpm-build-perl rpm-build-python3 texinfo xorg-cf-files zlib-devel
# END SourceDeps(oneline)
# findreq artefacts
# let's drop the dep for now
%filter_from_requires /^gambit$/d
# noise
%filter_from_requires /^.bin.sh5$/d
%filter_from_requires /^.bin.bsh$/d
%filter_from_requires /^.bin.ksh$/d
%filter_from_requires /^perl(make-rules.pl)/d
%filter_from_requires /^perl(installer.ctan-mirrors.pl)/d
%filter_from_requires /^perl(installer.mirrors.pl)/d
%filter_from_requires /^perl(TeXLive.trans.pl)/d

BuildRequires: pkgconfig(bzip2) libpixman-devel
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/hg
#define _binary_payload		w9.gzdio
#define _source_payload		w9.gzdio

%global __requires_exclude ^perl\\((PDF::Reuse.*|Pedigree.*|TeXLive.*|Tk::path_tre|only|pdfTeX|script::MakeSPList)\\)|pear\\(animals.php\\)
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_docdir}

# - let asymptote be packaged separately, as the generated one is known
#   to not be fully functional
%define enable_asymptote	0

# luajit supports only these architectures
%ifarch %ix86 x86_64 %arm aarch64 %mips
%define enable_luajittex	1
%define enable_mfluajit		1
%else
%define enable_luajittex	0
%define enable_mfluajit		0
%endif
%ifarch loongarch64 riscv64
# XXX: no libffcall, no clisp here
%def_disable xindy
%else
%def_enable xindy
%endif

# in its own package
%define with_system_lcdf	0
%define with_system_tex4ht	0
%define with_system_teckit	1


%define texmfbindir		%{_bindir}
%define texmfdir		%{_datadir}/texmf
%define texmfdistdir		%{_datadir}/texmf-dist
%define texmflocaldir		%{_datadir}/texmf-local
%define texmfextradir		%{_datadir}/texmf-extra
%define texmffontsdir		%{_datadir}/texmf-fonts
%define texmfprojectdir		%{_datadir}/texmf-project
%define texmfvardir		%{_localstatedir}/lib/texmf
%define texmfconfdir		%{_sysconfdir}/texmf
%define relYear	2022
%global tl_version %relYear
%global mga_tl_timestamp 20220321


#-----------------------------------------------------------------------
Name:		texlive
Version:	%relYear
Release:	alt0_11
Summary:	The TeX formatting system
Group:		Publishing
License:	https://www.tug.org/texlive/LICENSE.TL
URL:		https://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/%{relYear}/%{name}-%{mga_tl_timestamp}-source.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/%{relYear}/%{name}-%{mga_tl_timestamp}-source.tar.xz.sha512

Requires:	ghostscript-module-X


#-----------------------------------------------------------------------
Requires:	dialog
Requires:	ghostscript
%if %{enable_asymptote}
Requires:	gv
Requires:	tkinter
%endif
%if %{with_system_lcdf}
Requires:	lcdf-typetoools
%else
%endif
Requires:	psutils
%if %{with_system_teckit}
Requires:	libteckit-utils
%endif
%if %{with_system_tex4ht}
Requires:	tex4ht
%else
%endif
Requires:	texlive-collection-basic

# Fix upgrade for luatex (mga#12303)

#-----------------------------------------------------------------------
BuildRequires:	autoconf-archive
BuildRequires:	bison
%if_enabled xindy
BuildRequires:	clisp
BuildRequires:	libffcall libffcall-devel
%endif
BuildRequires:	libgs-devel
BuildRequires:	pkgconfig(gmp)
BuildRequires:	pkgconfig(graphite2)
BuildRequires:	libicu-devel
BuildRequires:	libpaper-devel
BuildRequires:	mercurial mercurial-hgext
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdlib)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(libbrotlienc)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwoff2enc)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	libpotrace-devel
BuildRequires:	t1lib-devel
BuildRequires:	texlive
BuildRequires:	texlive-dist
BuildRequires:	texlive-fonts-sources
BuildRequires:	pkgconfig(libxxhash)
%if %{with_system_teckit}
BuildRequires:	libteckit-devel
%endif
%if %{enable_asymptote}
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	flex
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	libsigsegv-devel
BuildRequires:	ghostscript-utils
BuildRequires:	pkgconfig(gsl)
BuildRequires:	libglvnd-devel
BuildRequires:	makeinfo
%endif

#-----------------------------------------------------------------------
Patch1: texlive-20160523-mageia-format.patch
%if %{enable_asymptote}
Patch2: texlive-20160523-mageia-asymptote.patch
%endif
Patch4: texlive-20160523-texmf-mageia-kpfix.patch
Patch5: includePatch.patch
Patch7: texlive-dvisvgm-system-libs.patch
Patch8: mga-fix-build-with-gs10.patch
Patch9: texlive-use-grep-E-and-grep-F-instead-of-deprecated-egrep-fgrep.patch
Patch10: CVE-2023-32700.patch
Patch11: texlive-2022-alt-pngout-mpmath-concurrency.patch
Source44: import.info
Provides: dvipng = %{tl_version}
Provides: lcdf-typetools = %{tl_version}
Provides: ps2eps = %{tl_version}
Provides: tex4ht = %{tl_version}
Obsoletes: dvipng <= 1.14-alt1.qa1.1
Obsoletes: lcdf-typetools <= 2.104-alt1
Obsoletes: ps2eps <= 1.68-alt1
Obsoletes: tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: dvipng <= 1.14-alt1.qa1.1
Conflicts: lcdf-typetools <= 2.104-alt1
Conflicts: ps2eps <= 1.68-alt1
Conflicts: tetex-afm < 2.01
Conflicts: tetex-bibtex8 < 2.01
Conflicts: tetex-core < 2.01
Conflicts: tetex-dvilj < 2.01
Conflicts: tetex-dvips < 2.01
Conflicts: tetex-latex < 2.01
Conflicts: tetex-xdvi < 2.01
Conflicts: tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: texlive-base-bin < 2009
Conflicts: texlive-extra-utils < 2009
Conflicts: texlive-font-utils < 2009
Conflicts: texlive-lang-indic < 2009
Conflicts: texlive-latex-base < 2009
Conflicts: texlive-metapost < 2009
Conflicts: texlive-omega < 2009
Conflicts: texlive-xetex < 2009
Patch33: texlive-2017-alt-texmf-first.patch
Patch34: texlive-2018-alt-gcc8.patch
Patch35: texlive-2022-dvisvgm-alt-cxx.patch
Provides: texlive-collection-binextra = %{tl_version}
Patch36: texlive-2018-e2k-luatex.patch

#-----------------------------------------------------------------------
%description
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files
%{texmfbindir}/*
%dir %{texmfvardir}
%ghost %{texmfvardir}/ls-R
%dir %{texmfconfdir}/web2c
%ghost %{texmfconfdir}/ls-R
%ghost %config(noreplace) %{texmfconfdir}/web2c/updmap.cfg


%define	kpathsea_major	6
%define	kpathsea	libkpathsea%{kpathsea_major}
%exclude %{texmfbindir}/teckit_compile

%package	-n %{kpathsea}
Summary:	Path searching library for TeX-related files
Group:		System/Libraries

%description	-n %{kpathsea}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.

%files		-n %{kpathsea}
%{_libdir}/libkpathsea.so.%{kpathsea_major}
%{_libdir}/libkpathsea.so.%{kpathsea_major}.*

#-----------------------------------------------------------------------
%define	kpathsea_devel		libkpathsea-devel

%package	-n %{kpathsea_devel}
Summary:	Kpathsea development files
Group:		Development/C
Provides:	kpathsea-devel = %{version}-%{release}

%description	-n %{kpathsea_devel}
Kpathsea implements generic path searching, configuration,
and TeX-specific file searching.
This package includes the kpathsea development files.

%files		-n %{kpathsea_devel}
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_libdir}/pkgconfig/kpathsea.pc

#-----------------------------------------------------------------------
%define	texlua_major	5
%define	texluajit_major	2
%define	texlua	libtexlua%{texlua_major}

%package	-n %{texlua}
Summary:	Library for TeXlua
Group:		System/Libraries

%description	-n %{texlua}
TeXlua library

%files		-n %{texlua}
%{_libdir}/libtexlua53.so.%{texlua_major}
%{_libdir}/libtexlua53.so.%{texlua_major}.*
%if %{enable_luajittex}
%{_libdir}/libtexluajit.so.%{texluajit_major}
%{_libdir}/libtexluajit.so.%{texluajit_major}.*
%endif


#-----------------------------------------------------------------------
%define	texlua_devel		libtexlua-devel

%package	-n %{texlua_devel}
Summary:	Library for TeXlua
Group:		Development/C
Provides:	texlua-devel = %{version}-%{release}

%description	-n %{texlua_devel}
TeXlua library
This package includes the TeXlua development files.

%files		-n %{texlua_devel}
%{_includedir}/texlua53
%{_libdir}/libtexlua53.so
%{_libdir}/pkgconfig/texlua53.pc
%if %{enable_luajittex}
%{_includedir}/texluajit
%{_libdir}/libtexluajit.so
%{_libdir}/pkgconfig/texluajit.pc
%endif

#-----------------------------------------------------------------------
%define	synctex_major	2
%define	synctex	libsynctex%{synctex_major}

%package	-n %{synctex}
Summary:	Library for SyncTeX
Group:		System/Libraries

%description	-n %{synctex}
synctex library

%files		-n %{synctex}
%{_libdir}/libsynctex.so.%{synctex_major}
%{_libdir}/libsynctex.so.%{synctex_major}.*

#-----------------------------------------------------------------------
%define	synctex_devel		libsynctex-devel

%package	-n %{synctex_devel}
Summary:	Library for SyncTeX
Group:		Development/C
Provides:	synctex-devel = %{version}-%{release}

%description	-n %{synctex_devel}
synctex library
This package includes the synctex development files.

%files		-n %{synctex_devel}
%{_includedir}/synctex
%{_libdir}/libsynctex.so
%{_libdir}/pkgconfig/synctex.pc

#-----------------------------------------------------------------------
%define	ptexenc_major	1
%define	ptexenc	libptexenc%{ptexenc_major}

%package	-n %{ptexenc}
Summary:	Library for Japanese pTeX
Group:		System/Libraries

%description	-n %{ptexenc}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.

%files		-n %{ptexenc}
%{_libdir}/libptexenc.so.%{ptexenc_major}
%{_libdir}/libptexenc.so.%{ptexenc_major}.*

#-----------------------------------------------------------------------
%define	ptexenc_devel		libptexenc-devel

%package	-n %{ptexenc_devel}
Summary:	Library for Japanese pTeX
Group:		Development/C
Provides:	ptexenc-devel = %{version}-%{release}

%description	-n %{ptexenc_devel}
ptexenc is a useful library for Japanese pTeX
(which stands for publishing TeX, and is an extension of
TeX by ASCII Co.) and its surrounding tools.
This package includes the ptexenc development files.

%files		-n %{ptexenc_devel}
%{_includedir}/ptexenc
%{_libdir}/libptexenc.so
%{_libdir}/pkgconfig/ptexenc.pc

########################################################################

#-----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{mga_tl_timestamp}-source
hg init -q .
hg add -q .
hg commit -q --user "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"
cat %_sourcedir/texlive-20160523-mageia-format.patch | hg import -  -q -m texlive-20160523-mageia-format.patch --user "rpmbuild <rpmbuild>"
%if %{enable_asymptote}
cat %_sourcedir/texlive-20160523-mageia-asymptote.patch | hg import -  -q -m texlive-20160523-mageia-asymptote.patch --user "rpmbuild <rpmbuild>"
%endif
cat %_sourcedir/texlive-20160523-texmf-mageia-kpfix.patch | hg import -  -q -m texlive-20160523-texmf-mageia-kpfix.patch --user "rpmbuild <rpmbuild>"
cat %_sourcedir/includePatch.patch | hg import -  -q -m includePatch.patch --user "rpmbuild <rpmbuild>"
cat %_sourcedir/texlive-dvisvgm-system-libs.patch | hg import -  -q -m texlive-dvisvgm-system-libs.patch --user "rpmbuild <rpmbuild>"
cat %_sourcedir/mga-fix-build-with-gs10.patch | hg import -  -q -m mga-fix-build-with-gs10.patch --user "rpmbuild <rpmbuild>"
cat %_sourcedir/texlive-use-grep-E-and-grep-F-instead-of-deprecated-egrep-fgrep.patch | hg import -  -q -m texlive-use-grep-E-and-grep-F-instead-of-deprecated-egrep-fgrep.patch --user "rpmbuild <rpmbuild>"
cat %_sourcedir/CVE-2023-32700.patch | hg import -  -q -m CVE-2023-32700.patch --user "rpmbuild <rpmbuild>"
hg import -q -m "$(basename %PATCH11)" --user "rpmbuild <rpmbuild>" %PATCH11


# setup default builtin values, added to paths.h from texmf.cnf
perl -pi -e 's%%^(TEXMFMAIN\s+= ).*%%$1%{texmfdistdir}%%;'			  \
	 -e 's%%^(TEXMFDIST\s+= ).*%%$1%{texmfdistdir}%%;'			  \
	 -e 's%%^(TEXMFLOCAL\s+= ).*%%$1%{texmflocaldir}%%;'			  \
	 -e 's%%^(TEXMFSYSVAR\s+= ).*%%$1%{texmfvardir}%%;'		  \
	 -e 's%%^(TEXMFSYSCONFIG\s+= ).*%%$1%{texmfconfdir}%%;'		  \
	 -e 's%%^(TEXMFHOME\s+= ).*%%$1\$HOME/texmf%%;'			  \
	 -e 's%%^(TEXMFVAR\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-var%%;'	  \
	 -e 's%%^(TEXMFCONFIG\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-config%%;'\
	 -e 's%%^(OSFONTDIR\s+= ).*%%$1%{_datadir}/fonts%%;'		  \
	texk/kpathsea/texmf.cnf
%patch33 -p0
%patch34 -p1
%patch35 -p1
# viy@: no need: configure fails, but we use system library
rm -rf libs/cairo
%patch36 -p2

%if ! %{enable_luajittex}
# even if building luajit is disabled, build scripts still call
# configure from libs/*. let's just drop the luajit sources here.
rm -rf libs/luajit
%endif

#-----------------------------------------------------------------------
%build
export CXXFLAGS="%{optflags} -std=c++14"

#for dvisvgm system libs patches
./reautoconf

mkdir -p Work
pushd Work

%define _configure_script ../configure
CONFIGURE_TOP=.. \
%configure							\
%if %{with_system_lcdf}
	--disable-lcdf-typetools				\
%endif
%if %{with_system_teckit}
	--disable-teckit					\
	--with-teckit-includes=%{_includedir}/teckit		\
%endif
%if %{with_system_tex4ht}
	--disable-tex4htk					\
%endif
	--with-banner-add="/Mageia"	\
	--disable-dialog \
	--disable-linked-scripts \
	--disable-native-texlive-build \
	--disable-psutils \
	--disable-static \
	--disable-t1utils \
	--enable-dvi2tty \
	--enable-missing \
	--enable-shared \
	--enable-xdvik \
%if_enabled xindy
	--enable-xindy \
	--enable-xindy-rules \
%else
	--disable-xindy \
	--disable-xindy-rules \
%endif
	--with-freetype2-includes=%{_includedir}/freetype2	\
	--without-system-xpdf \
	--with-system-cairo \
	--with-system-freetype2 \
	--with-system-gd \
	--with-system-gmp \
	--with-system-graphite2 \
	--with-system-harfbuzz \
	--with-system-icu \
	--with-system-libpaper \
	--with-system-libpng \
	--with-system-mpfr \
	--with-system-pixman \
	--with-system-poppler \
	--with-system-t1lib \
%if %{enable_luajittex}
	--enable-luajittex					\
%else
	--disable-luajittex					\
	--disable-luajithbtex					\
%endif
%if %{enable_mfluajit}
	--enable-mfluajit					\
%else
	--disable-mfluajit					\
%endif
	--with-system-zlib \
	--with-system-zziplib
%define _configure_script ./configure
%make_build

popd

%if %{enable_asymptote}
pushd utils/asymptote
%configure							\
	--enable-gc=system					\
	--enable-texlive-build					\
	--datadir=%{texmfdir}
%make_build
popd
%endif

#-----------------------------------------------------------------------
%install
pushd Work
%makeinstall_std
popd

%if %{enable_asymptote}
pushd utils/asymptote
%makeinstall_std
popd
%endif

mkdir -p %{buildroot}%{_datadir}
for dir in texmf texmf-dist; do
    if [ -d %{buildroot}%{_prefix}/$dir ]; then
	rm -fr %{buildroot}%{_datadir}/$dir
	mv %{buildroot}%{_prefix}/$dir %{buildroot}%{_datadir}
    fi
done

mkdir -p %{buildroot}%{texmfvardir}
mkdir -p %{buildroot}%{texmfconfdir}

%if %{with_system_lcdf}
# stray directory left
rm -fr %{buildroot}%{_datadir}/lcdf-typetools-for-tex-live
%endif

pushd %{buildroot}%{texmfbindir}
	# missing symbolic links
	ln -sf aleph lamed
	ln -sf luatex dvilualatex
	ln -sf luatex dviluatex
	ln -sf luahbtex lualatex
	ln -sf pdftex amstex
	ln -sf pdftex cslatex
	ln -sf pdftex csplain
	ln -sf pdftex eplain
	ln -sf pdftex etex
	ln -sf pdftex latex
	ln -sf pdftex mex
	ln -sf pdftex mltex
	ln -sf pdftex mllatex
	ln -sf pdftex pdfcslatex
	ln -sf pdftex pdfcsplain
	ln -sf pdftex pdfetex
	ln -sf pdftex pdflatex
	ln -sf pdftex pdfmex
	ln -sf pdftex physe
	ln -sf pdftex phyzzx
	ln -sf pdftex utf8mex
	ln -sf pdftex texsis
	ln -sf ptex platex
	ln -sf mpost metafun
	ln -sf mpost mfplain
	ln -sf xetex xelatex

    # correct symlinks
    for file in *; do
	link=`readlink $file` || :
	if [ "x$link" != "x" ]; then
	    ln -sf `echo $link |					\
		sed	-e 's|\.\./.*texmf-dist/|%{texmfdistdir}/|'	\
			-e 's|\.\./.*texmf/|%{texmfdir}/|'`		\
		$file
	fi
    done
	ln -sf %{_bindir}/dialog tcdialog
%if %{enable_asymptote}
	ln -sf %{texmfdir}/asymptote/GUI/xasy.py xasy
%endif
	# install scripts from texlive-texmf
	rm -f a2ping afm2afm arlatex authorindex autoinst bibexport		\
	bundledoc cachepic cmap2enc de-macro dviasm ebong e2pall	\
	epspdf epspdftk epstopdf fig4latex findhyph font2afm		\
	fragmaster ht htcontext htlatex htmex httex httexi htxelatex	\
	htxetex latex2man latexdiff latexdiff-vc latexmk latexrevise	\
	listings-ext.sh makeglossaries mathspic mk4ht mkgrkindex	\
	mkjobtexmf mkluatexfontdb mkt1font mptopdf ot2kpx pdf180	\
	pdf270 pdf90 pdfannotextractor pdfatfi pdfbook pdfcrop	\
	pdfflip pdfjam pdfjam-pocketmod pdfjam-slides3up		\
	pdfjam-slides6up pdfjoin pdfnup pdfpun pdfthumb perltex	\
	pfm2kpx pkfix  pkfix-helper ppower4 ps4pdf pst2pdf purifyeps	\
	repstopdf rpdfcrop rungs showglyphs simpdftex splitindex	\
	svn-multi texcount texdiff texdirflatten texdoc texdoctk	\
	texloganalyser thumbpdf tlmgr ulqda updmap vpe vpl2ovp	\
	vpl2vpl
popd

# use texmf data
rm -fr %{buildroot}%{texmfdir} %{buildroot}%{texmfdistdir}

# install manual pages and info files from texlive-texmf tarball
rm -fr %{buildroot}%{_mandir} %{buildroot}%{_infodir}

rm -f %{buildroot}%{_datadir}/applications/xdvi.desktop

# drop .la files
find %{buildroot} -name "*.la" -delete
for rpm404_ghost in %{texmfvardir}/ls-R %{texmfconfdir}/ls-R %{texmfconfdir}/web2c/updmap.cfg
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done


%post 
rm -f %{texmfdir}/ls-R %{texmfdistdir}/ls-R %{texmfconfdir}/ls-R


#-----------------------------------------------------------------------
%changelog
* Tue Jun 04 2024 Ivan A. Melnikov <iv@altlinux.org> 2022-alt0_11
- NMU: fix FTBFS on riscv64 (no clisp here either).

* Tue Mar 12 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2022-alt0_10
- NMU: fixed FTBFS on LoongArch (no clisp here yet). While at it fixed
  sporadic build failures due to missing dependencies between targers
  in makefiles.

* Fri Mar 08 2024 Igor Vlasenko <viy@altlinux.org> 2022-alt0_9
- new version (test release)

* Thu Jul 27 2023 Mikhail Tergoev <fidel@altlinux.org> 2021-alt5_3
- NMU: fixed build with gcc-13 (ALT bug 46864)

* Tue Jul 11 2023 Mikhail Tergoev <fidel@altlinux.org> 2021-alt4_3
- NMU: fixed build (force compiling with gcc-12)

* Wed Jun 22 2022 Igor Vlasenko <viy@altlinux.org> 2021-alt3_3
- fixed build

* Tue Jan 04 2022 Igor Vlasenko <viy@altlinux.org> 2021-alt2_3
- riscv64 support

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 2021-alt1_3
- fixed build

* Thu Aug 05 2021 Igor Vlasenko <viy@altlinux.org> 2021-alt1_2
- new version

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 2019-alt2_7
- fixed build with gcc10

* Wed Mar 11 2020 Nikita Ermakov <arei@altlinux.org> 2019-alt1_7
- Make texlive build with poppler >= 0.83.

* Mon Nov 04 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1_6
- filetrigger fixes

* Thu Oct 31 2019 Andrey Savchenko <bircoph@altlinux.org> 2019-alt1_3
- Use external ligraphite2 and harfbuzz. This fixes build on E2K.
- Remove obsolete E2K patches.

* Sat Jul 20 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1_2
- new version

* Fri May 24 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2018-alt3_12
- Fixed build on architectures not supported by luajit.

* Tue Apr 09 2019 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_12
- fixed build with poppler 75 (closes: #35567)

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_10
- fixed build

* Wed Dec 05 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_7
- built with new poppler (closes: #35711)

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_4
- rebuild with new icu

* Tue Oct 16 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt1_4
- new version; fixes CVE-2018-17407

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_4
- luatex bugfix thanks to lakostis@ (closes: #35024)

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_3
- final release

* Thu Mar 01 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt1_3
- new version

