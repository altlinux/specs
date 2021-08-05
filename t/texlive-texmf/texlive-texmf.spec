# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-java
BuildRequires: gcc-c++ perl(Archive/Tar.pm) perl(Config/IniFiles.pm) perl(Data/Dumper/Concise.pm) perl(Date/Format.pm) perl(Date/Parse.pm) perl(Digest/SHA.pm) perl(Digest/SHA1.pm) perl(Encode.pm) perl(Encode/Alias.pm) perl(Encode/Locale.pm) perl(ExtUtils/MakeMaker.pm) perl(Fatal.pm) perl(File/Copy/Recursive.pm) perl(File/HomeDir.pm) perl(File/Slurp.pm) perl(File/Which.pm) perl(HTML/FormatText.pm) perl(HTML/TreeBuilder.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Status.pm) perl(IO/Compress/Zip.pm) perl(IO/String.pm) perl(IPC/System/Simple.pm) perl(JSON.pm) perl(LWP.pm) perl(LWP/Protocol/https.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(Locale/Maketext/Simple.pm) perl(Math/Trig.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Spreadsheet/ParseExcel.pm) perl(Term/ANSIColor.pm) perl(Term/ReadKey.pm)
BuildRequires: perl(Test/More.pm) perl(Text/Unidecode.pm) perl(Tk.pm) perl(Tk/Adjuster.pm) perl(Tk/BrowseEntry.pm) perl(Tk/Dialog.pm) perl(Tk/DirTree.pm) perl(Tk/HList.pm) perl(Tk/ItemStyle.pm) perl(Tk/NoteBook.pm) perl(Tk/ROText.pm) perl(Tk/widgets.pm) perl(URI/Escape.pm) perl(Unicode/GCString.pm) perl(WWW/Mechanize.pm) perl(XML/Parser.pm) perl(XML/XPath.pm) perl(XML/XPath/XMLParser.pm) perl(YAML/Tiny.pm) perl(autodie.pm) perl-devel python3-devel texinfo
# END SourceDeps(oneline)
#
#     `This package is an abomination.  It should not exist.'
#					ldv@ at 2020-04-09
    

%filter_from_requires /^.bin.sh5$/d
%filter_from_requires /^.bin.bsh$/d
%filter_from_requires /^.bin.ksh$/d
%filter_from_requires /^.usr.sbin.lsattr$/d
# optional in pdfannotextractor
%filter_from_requires /^.usr.bin.java$/d

%filter_from_requires /^perl(make-rules.pl)/d
%filter_from_requires /^perl(installer.ctan-mirrors.pl)/d
%filter_from_requires /^perl(installer.mirrors.pl)/d
%filter_from_requires /^perl(TeXLive.trans.pl)/d
%filter_from_requires /^python2.7(webquiz_util)/d
# no ruby deps, please
%filter_from_requires /^\(\/usr\/bin\/\)\?ruby$/d

# hacks around autoreq quirks when built in tetex environment
# we need specific version of tex: not tetex
%filter_from_requires /^tetex/d
%filter_from_requires /^.usr.bin.bibtex$/d
%filter_from_requires /^.usr.bin.chktex$/d
%filter_from_requires /^.usr.bin.deweb$/d
%filter_from_requires /^.usr.bin.dvips$/d
%filter_from_requires /^.usr.bin.kpseaccess$/d
%filter_from_requires /^.usr.bin.kpsewhich$/d
%filter_from_requires /^.usr.bin.latex$/d
%filter_from_requires /^.usr.bin.makeindex$/d
%filter_from_requires /^.usr.bin.mex$/d
%filter_from_requires /^.usr.bin.mf$/d
%filter_from_requires /^.usr.bin.mktexlsr$/d
%filter_from_requires /^.usr.bin.otftotfm$/d
%filter_from_requires /^.usr.bin.pdflatex$/d
%filter_from_requires /^.usr.bin.pltotf$/d
%filter_from_requires /^.usr.bin.t4ht$/d
%filter_from_requires /^.usr.bin.tex$/d
%filter_from_requires /^.usr.bin.tex4ht$/d
%filter_from_requires /^.usr.bin.texconfig$/d
%filter_from_requires /^.usr.bin.texconfig-dialog$/d
%filter_from_requires /^.usr.bin.texhash$/d
%filter_from_requires /^.usr.bin.texlinks$/d
%filter_from_requires /^.usr.bin.texlua$/d
%filter_from_requires /^.usr.bin.vptovf$/d
%filter_from_requires /^.usr.bin.xelatex$/d
%filter_from_requires /^.usr.bin.xetex$/d

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Compress with gzip instead of xz (faster):
#define _binary_payload		w9.gzdio
#define _source_payload		w9.gzdio


# disable python byte compiler
%global _python_bytecompile_extra 0

%global __requires_exclude ^perl\\((PDF::Reuse.*|Pedigree.*|Text::Unidecode|Tie::Watch|SelfLoader|TeXLive.*|Tk::path_tre|only|pdfTeX|script::MakeSPList)\\)|/usr/local/bin/fontforge|/bin/wish|bin/texlua
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_docdir}|^/usr/share/texmf-dist/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_docdir}|^/usr/share/texmf-dist/doc
# filter out bogus auto-requires
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^/usr/bin/lua
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^/usr/bin/texlua
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^/usr/bin/wish

%define enable_asymptote	0
%define enable_xindy		1

%define with_system_tex4ht	0

%define texmfbindir		%{_bindir}
%define texmfdir		%{_datadir}/texmf
%define texmfdistdir		%{_datadir}/texmf-dist
%define texmflocaldir		%{_datadir}/texmf-local
%define texmfextradir		%{_datadir}/texmf-extra
%define texmffontsdir		%{_datadir}/texmf-fonts
%define texmfprojectdir	%{_datadir}/texmf-project
%define texmfvardir		%{_localstatedir}/lib/texmf
%define texmfconfdir		%{_sysconfdir}/texmf


%define	__jar_repack %{nil}
%define	_enable_debug_packages %{nil}
%define	__debug_package %{nil}
%define __debug_install_post %{nil}

%define relYear 2021
%global tl_version %relYear
%global mga_tl_timestamp 20210325

Name:		texlive-texmf
Version:	%relYear
Release:	alt1_1
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/%{relYear}/texlive-%{mga_tl_timestamp}-texmf.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/%{relYear}/texlive-%{mga_tl_timestamp}-texmf.tar.xz.sha512
Source2:	XDvi-color
Source3:	http://www.tug.org/texlive/LICENSE.TL
Source4:	ftp://tug.org/historic/systems/texlive/%{relYear}/install-tl-unx.tar.gz#/install-tl-unx-%{relYear}.tgz
# Source5:	http://mirror.hmc.edu/ctan/systems/texlive/tlnet/tlpkg/texlive.tlpdb
Source6:	updmap-collection-basic.cfg
Source7:	updmap-dist.cfg
Source8:	updmap-fontsextra.cfg
Source9:	collection.basic
Source10:	fonts.extra
Source11:	fonts.asian
Source12:	fonts.sources

BuildArch:	noarch
# for pathfix.py
BuildRequires:	python3 python3-tools
BuildRequires:	pkgconfig(python3)

#-----------------------------------------------------------------------
Requires:	perl-Algorithm-Diff
Requires:	xdg-utils
Requires:	texlive >= %{tl_version}
Requires:	texlive-collection-basic = %{version}
Requires:	texlive-dist = %{version}-%{release}

%if !%{with_system_tex4ht}
%endif
# latex-beamer functionality is already included in texlive-texmf

Patch4: texlive-20160523-texmf-mageia-kpfix.patch

# fix doc package deps:
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^pear\\(animals.php\\)$
Requires(post): tex-common
Source44: import.info
Patch33: texlive-texmf-2017-alt-texmf-first.patch
BuildRequires: rpm-build-tex >= 0.4
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
Source8003: texlive-fix-info-dir-sections.patch

#add_cleanup_skiplist for safety if cleanup is enabled
%set_cleanup_method none
%add_cleanup_skiplist %{texmfdistdir}/doc/fonts/cmcyr/coding.bak

%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%{texmfdistdir}/tlpkg -I%buildroot%{texmfdistdir}/scripts/xetex/perl/lib -I%buildroot%{texmfdistdir}/scripts/pedigree-perl -I%buildroot%{texmfdistdir}/scripts/latexindent'
# PROLOG *.pl mistaken as a perl
%add_findreq_skiplist %{texmfdistdir}/fonts/source/*
# `kpsewhich ...` fails:  kpsewhich: unrecognized option '-var-value=TEXMFROOT'
# can be removed after safe upgrade to texlive 2016?
%add_findreq_skiplist %{texmfdistdir}/scripts/texlive/fmtutil.pl
%add_findreq_skiplist %{texmfdistdir}/scripts/texlive/updmap.pl
# perl bundle over shell, known no deps
%add_findreq_skiplist %{texmfdistdir}/scripts/a2ping/a2ping.pl
# TODO: bash syntax errors - fixme using bash --rpm-requires
%add_findreq_skiplist %{texmfdistdir}/scripts/pdfxup/pdfxup
%add_findreq_skiplist %{texmfdistdir}/scripts/pgfplots/pgf2pdf.sh
%add_findreq_skiplist %{texmfdistdir}/doc/*
%add_findreq_skiplist %{texmfdistdir}/dvips/pl/config.pl
%add_findreq_skiplist %{texmfdistdir}/scripts/latexindent/LatexIndent/*pm
%add_findreq_skiplist %{texmfdistdir}/scripts/tlshell/*.tcl
BuildRequires: perl(BibTeX/Parser.pm)


#-----------------------------------------------------------------------
%description
This package will install the standard TeX Live and MetaFont distribution.
It provides a comprehensive TeX system. It includes all the major
TeX-related programs, macro packages, and fonts that are free software,
including support for many languages around the world.

%files

#-----------------------------------------------------------------------
%package	-n texlive-collection-basic
Summary:	TeX Live essential package
Group:		Publishing
Requires:	texlive >= %{tl_version}
Requires(post):	texlive >= %{tl_version}
Provides: ht = %{tl_version}
Provides: pdfjam = %{tl_version}
Provides: tex4ht = %{tl_version}
Provides: tex4ht-xetex = %{tl_version}
Provides: texmf-tex4ht = %{tl_version}
Obsoletes: ht <= 2.1.0-alt1
Obsoletes: pdfjam <= 2.08-alt1
Obsoletes: tex4ht <= 1.0.2009_06_11_1038-alt1
Obsoletes: tex4ht-xetex <= 1.0.2009_06_11_1038-alt1
Obsoletes: texmf-tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: ht <= 2.1.0-alt1
Conflicts: pdfjam <= 2.08-alt1
Conflicts: tetex-core < 2.01
Conflicts: tetex-doc < 2.01
Conflicts: tex4ht <= 1.0.2009_06_11_1038-alt1
Conflicts: texlive-base-bin < 2009
Conflicts: texlive-extra-utils < 2009
Conflicts: texlive-latex-extra < 2009
Conflicts: texlive-latex-recommended < 2009
Conflicts: texlive-pstricks < 2009
Obsoletes: fonts-type1-cm-super-tex <= 0.3.3-alt8.qa1
Obsoletes: fonts-type1-cm-super-tex-afm <= 0.3.3-alt8.qa1
Obsoletes: fonts-type1-cm-super-tex-dvips <= 0.3.3-alt8.qa1
Obsoletes: fonts-type1-tipa-tex <= 1.3-alt4
Obsoletes: tetex-latex-cmap <= 1.0g-alt2
Obsoletes: texmf-latex-babelbib <= 1.29-alt1
Obsoletes: texmf-latex-csquotes <= 4.4d-alt2
Obsoletes: texmf-latex-etoolbox <= 2.1-alt2
Obsoletes: texmf-latex-koma-script
Obsoletes: texmf-latex-obsolete <= 0.1-alt1
Obsoletes: texmf-latex-tipa <= 1.3-alt4
Obsoletes: texmf-latex-xcolor <= 2.06-alt3
Obsoletes: texmf-pgf <= 2.10-alt0.1
Obsoletes: ctanify <= 1.1-alt1.1
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
#Requires: texlive = %{tl_version}
Provides: texlive-collection-fontsrecommended = %{tl_version}
Provides: texlive-collection-fontutils = %{tl_version}
Provides: texlive-collection-latex = %{tl_version}
Provides: texlive-collection-genericrecommended = %{tl_version}
Provides: tex(tex)
Provides: tex(latex-base)
Provides: tex(latex)
Provides: texlive-metapost = %{tl_version}
Conflicts: texlive-metapost < 2009
Obsoletes: texlive-metapost < 2009
Provides: texlive-omega = %{tl_version}
Conflicts: texlive-omega < 2009
Obsoletes: texlive-omega < 2009
Provides: texlive-pstricks = %{tl_version}
Conflicts: texlive-pstricks < 2009
Obsoletes: texlive-pstricks < 2009
Provides: texlive-base = %{tl_version}
Conflicts: texlive-base < 2009
Obsoletes: texlive-base < 2009
Provides: texlive-base-bin = %{tl_version}
Conflicts: texlive-base-bin < 2009
Obsoletes: texlive-base-bin < 2009
Provides: texlive-extra-utils = %{tl_version}
Conflicts: texlive-extra-utils < 2009
Obsoletes: texlive-extra-utils < 2009
Provides: texlive-font-utils = %{tl_version}
Conflicts: texlive-font-utils < 2009
Obsoletes: texlive-font-utils < 2009
Provides: texlive-fonts-recommended = %{tl_version}
Conflicts: texlive-fonts-recommended < 2009
Obsoletes: texlive-fonts-recommended < 2009
Provides: texlive-latex-base = %{tl_version}
Conflicts: texlive-latex-base < 2009
Obsoletes: texlive-latex-base < 2009
Provides: texlive-latex-recommended = %{tl_version}
Conflicts: texlive-latex-recommended < 2009
Obsoletes: texlive-latex-recommended < 2009
Obsoletes: texlive-common < 0.1.0.1
Provides: %{texmfdistdir}


%description	-n texlive-collection-basic
This package installs the essential TeX Live distribution packages.  They
should be sufficient for most users of TeX or TeX-related programs.

%files		-n texlive-collection-basic -f %{SOURCE9}
%{texmfbindir}/*
%{_datadir}/X11/app-defaults/XDvi*
%{_infodir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{texmfdistdir}/chktex
%if %{enable_asymptote}
%{texmfdistdir}/asymptote
%doc %{texmfdistdir}/doc/asymptote
%endif
%{texmfdistdir}/dvipdfmx
%{texmfdistdir}/hbf2gf
%{texmfdistdir}/LICENSE.TL
%{texmfdistdir}/texconfig
%{texmfdistdir}/texdoctk
%{texmfdistdir}/tlpkg
%{texmfdistdir}/ttf2pk
%{texmfdistdir}/xdvi
%if %{enable_xindy}
%{texmfdistdir}/xindy
%doc %{texmfdistdir}/doc/xindy
%endif
%{texmfdistdir}/bibtex
%{texmfdistdir}/dvips
%{texmfdistdir}/makeindex
%{texmfdistdir}/metafont
%{texmfdistdir}/metapost
%{texmfdistdir}/mft
%{texmfdistdir}/omega
%{texmfdistdir}/pbibtex
%{texmfdistdir}/scripts
%{texmfdistdir}/web2c
%if !%{with_system_tex4ht}
%{texmfdistdir}/tex4ht
%{_javadir}/tex4ht.jar
%endif
%{texmfdistdir}/texdoc
%dir %{texmflocaldir}
%ghost %{texmfdistdir}/ls-R
%ghost %{texmflocaldir}/ls-R

#context
%exclude %{texmfbindir}/mptopdf
%exclude %{texmfbindir}/mtxrun
%exclude %{texmfdistdir}/bibtex/bst/context
%exclude %{texmfdistdir}/scripts/context
%exclude %{texmfdistdir}/tex/generic/context
%exclude %{texmfdistdir}/fonts/map/pdftex/context
%exclude %{texmfdistdir}/metapost/context
# moved to corresponding packages
%exclude %{texmfdistdir}/web2c/updmap-dist.cfg
%exclude %{texmfdistdir}/web2c/updmap-fontsextra.cfg
%_sbindir/texlive-postinstall-rebuild-all
%_rpmlibdir/texlive-5-config.filetrigger
# sisyphus_check: check-subdirs ERROR: subdirectories packaging violation
%dir %{texmfdistdir}/fonts/lig

%exclude %_man1dir/t1ascii.1*
%exclude %_man1dir/t1asm.1*
%exclude %_man1dir/t1binary.1*
%exclude %_man1dir/t1disasm.1*
%exclude %_man1dir/t1mac.1*
%exclude %_man1dir/t1unmac.1*
%_rpmlibdir/texlive-collection-basic-files.req.list


%package	-n texlive-dist
Summary:	TeX Live distribution package
Group:		Publishing
Requires:	texlive-texmf >= %{version}-%{release}
Requires(post):	texlive-collection-basic = %{version}
#Requires(postun):	texlive-collection-basic
Requires(post):	texlive >= %{tl_version}
Requires(postun):	texlive >= %{tl_version}
Obsoletes: tetex-latex-feynmf <= 1.08-alt3.1.1
Obsoletes: texmf-fonts-kerkis <= 2.0-alt2_26
Obsoletes: texmf-latex-biblatex <= 2.5-alt1
Obsoletes: texmf-latex-biblatex-gost <= 0.7.1-alt1
Obsoletes: texmf-latex-currfile <= 0.7b-alt1
Obsoletes: texmf-latex-filehook <= 0.5d-alt1
Obsoletes: texmf-latex-fixme <= 4.1-alt1
Obsoletes: texmf-latex-linegoal
Obsoletes: texmf-latex-logreq <= 1.0-alt1
Obsoletes: texmf-latex-ltxnew
Obsoletes: texmf-latex-passivetex <= 20040310-alt1
Obsoletes: texmf-latex-pdfcomment <= 1.5d-alt2
Obsoletes: texmf-latex-tabu
Obsoletes: texmf-standalone <= 1.1b-alt1
Provides: passivetex = 2017
Provides: texlive-passivetex = 2017
Provides: latexmk = 4.52c-alt1
Obsoletes: latexmk <= 4.52c-alt1
Conflicts: latexmk <= 4.52c-alt1
Provides: prosper = 1.24
Obsoletes: prosper < 1.24
Obsoletes: texmf-latex-babelbib < 1.31
Obsoletes: texmf-latex-beamer < 3.41
Obsoletes: texmf-latex-biblatex < 3.6
Obsoletes: texmf-latex-biblatex-gost < 1.10
Obsoletes: texmf-latex-csquotes < 5.1
Obsoletes: texmf-latex-currfile <= 0.7c-alt1
Obsoletes: texmf-latex-etoolbox < 2.2
Obsoletes: texmf-latex-filehook <= 0.5d-alt1
Obsoletes: texmf-latex-fixme < 4.2
Obsoletes: texmf-latex-koma-script < 3.21
Obsoletes: texmf-latex-linegoal <= 2.9-alt1
Obsoletes: texmf-latex-logreq <= 1.0-alt1
Obsoletes: texmf-latex-ltxnew <= 1.3-alt1
Obsoletes: texmf-latex-passivetex = 20040310-alt1
Obsoletes: texmf-latex-pdfcomment < 2.3
Obsoletes: texmf-latex-tabu <= 2.8-alt1
Obsoletes: texmf-latex-tipa <= 1.3-alt4
Obsoletes: texmf-latex-xcolor < 2.12
Obsoletes: texmf-pgf < 3.0.1a
Obsoletes: texmf-standalone <= 1.2-alt1
Obsoletes: tetex-bibtex8 <= 3.71-alt1.qa1
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
#Requires: texlive = %{tl_version}
Provides: texlive-collection-langafrican = %{tl_version}
Provides: texlive-collection-langarabic = %{tl_version}
Provides: texlive-collection-langchinese = %{tl_version}
Provides: texlive-collection-langcjk = %{tl_version}
Provides: texlive-collection-langcyrillic = %{tl_version}
Provides: texlive-collection-langczechslovak = %{tl_version}
Provides: texlive-collection-langenglish = %{tl_version}
Provides: texlive-collection-langeuropean = %{tl_version}
Provides: texlive-collection-langfrench = %{tl_version}
Provides: texlive-collection-langgerman = %{tl_version}
Provides: texlive-collection-langgreek = %{tl_version}
Provides: texlive-collection-langindic = %{tl_version}
Provides: texlive-collection-langitalian = %{tl_version}
Provides: texlive-collection-langjapanese = %{tl_version}
Provides: texlive-collection-langkorean = %{tl_version}
Provides: texlive-collection-langother = %{tl_version}
Provides: texlive-collection-langpolish = %{tl_version}
Provides: texlive-collection-langportuguese = %{tl_version}
Provides: texlive-collection-langspanish = %{tl_version}

Provides: texlive-collection-bibtexextra = %{tl_version}
Provides: texlive-collection-formatsextra = %{tl_version}
Provides: texlive-collection-games = %{tl_version}
Provides: texlive-collection-genericextra = %{tl_version}
Provides: texlive-collection-htmlxml = %{tl_version}
Provides: texlive-collection-humanities = %{tl_version}
Provides: texlive-collection-latexrecommended = %{tl_version}
Provides: texlive-collection-latexextra = %{tl_version}
Provides: texlive-collection-luatex = %{tl_version}
Provides: texlive-collection-mathextra = %{tl_version}
Provides: texlive-collection-metapost = %{tl_version}
Provides: texlive-collection-music = %{tl_version}
Provides: texlive-collection-omega = %{tl_version}
Provides: texlive-collection-pictures = %{tl_version}
Provides: texlive-collection-plainextra = %{tl_version}
Provides: texlive-collection-pstricks = %{tl_version}
Provides: texlive-collection-publishers = %{tl_version}
Provides: texlive-collection-science = %{tl_version}
Provides: texlive-collection-xetex = %{tl_version}
Provides: tex(xetex)
Provides: tex(dvips)
Provides: tex(japanese)
Provides: tex(east-asian)
Provides: texlive-lang-indic = %{tl_version}
Conflicts: texlive-lang-indic < 2009
Obsoletes: texlive-lang-indic < 2009
Provides: texlive-music = %{tl_version}
Conflicts: texlive-music < 2009
Obsoletes: texlive-music < 2009
Provides: texlive-xetex = %{tl_version}
Conflicts: texlive-xetex < 2009
Obsoletes: texlive-xetex < 2009
Provides: texlive-bibtex-extra = %{tl_version}
Conflicts: texlive-bibtex-extra < 2009
Obsoletes: texlive-bibtex-extra < 2009
Provides: texlive-extra = %{tl_version}
Conflicts: texlive-extra < 2009
Obsoletes: texlive-extra < 2009
Provides: texlive-fonts-extra = %{tl_version}
Conflicts: texlive-fonts-extra < 2009
Obsoletes: texlive-fonts-extra < 2009
Provides: texlive-formats-extra = %{tl_version}
Conflicts: texlive-formats-extra < 2009
Obsoletes: texlive-formats-extra < 2009
Provides: texlive-games = %{tl_version}
Conflicts: texlive-games < 2009
Obsoletes: texlive-games < 2009
Provides: texlive-generic-extra = %{tl_version}
Conflicts: texlive-generic-extra < 2009
Obsoletes: texlive-generic-extra < 2009
Provides: texlive-generic-recommended = %{tl_version}
Conflicts: texlive-generic-recommended < 2009
Obsoletes: texlive-generic-recommended < 2009
Provides: texlive-humanities = %{tl_version}
Conflicts: texlive-humanities < 2009
Obsoletes: texlive-humanities < 2009
Provides: texlive-lang-african = %{tl_version}
Conflicts: texlive-lang-african < 2009
Obsoletes: texlive-lang-african < 2009
Provides: texlive-lang-arab = %{tl_version}
Conflicts: texlive-lang-arab < 2009
Obsoletes: texlive-lang-arab < 2009
Provides: texlive-lang-armenian = %{tl_version}
Conflicts: texlive-lang-armenian < 2009
Obsoletes: texlive-lang-armenian < 2009
Provides: texlive-lang-cjk = %{tl_version}
Conflicts: texlive-lang-cjk < 2009
Obsoletes: texlive-lang-cjk < 2009
Provides: texlive-lang-croatian = %{tl_version}
Conflicts: texlive-lang-croatian < 2009
Obsoletes: texlive-lang-croatian < 2009
Provides: texlive-lang-cyrillic = %{tl_version}
Conflicts: texlive-lang-cyrillic < 2009
Obsoletes: texlive-lang-cyrillic < 2009
Provides: texlive-lang-czechslovak = %{tl_version}
Conflicts: texlive-lang-czechslovak < 2009
Obsoletes: texlive-lang-czechslovak < 2009
Provides: texlive-lang-danish = %{tl_version}
Conflicts: texlive-lang-danish < 2009
Obsoletes: texlive-lang-danish < 2009
Provides: texlive-lang-dutch = %{tl_version}
Conflicts: texlive-lang-dutch < 2009
Obsoletes: texlive-lang-dutch < 2009
Provides: texlive-lang-finnish = %{tl_version}
Conflicts: texlive-lang-finnish < 2009
Obsoletes: texlive-lang-finnish < 2009
Provides: texlive-lang-french = %{tl_version}
Conflicts: texlive-lang-french < 2009
Obsoletes: texlive-lang-french < 2009
Provides: texlive-lang-german = %{tl_version}
Conflicts: texlive-lang-german < 2009
Obsoletes: texlive-lang-german < 2009
Provides: texlive-lang-greek = %{tl_version}
Conflicts: texlive-lang-greek < 2009
Obsoletes: texlive-lang-greek < 2009
Provides: texlive-lang-hebrew = %{tl_version}
Conflicts: texlive-lang-hebrew < 2009
Obsoletes: texlive-lang-hebrew < 2009
Provides: texlive-lang-hungarian = %{tl_version}
Conflicts: texlive-lang-hungarian < 2009
Obsoletes: texlive-lang-hungarian < 2009
Provides: texlive-lang-italian = %{tl_version}
Conflicts: texlive-lang-italian < 2009
Obsoletes: texlive-lang-italian < 2009
Provides: texlive-lang-latin = %{tl_version}
Conflicts: texlive-lang-latin < 2009
Obsoletes: texlive-lang-latin < 2009
Provides: texlive-lang-mongolian = %{tl_version}
Conflicts: texlive-lang-mongolian < 2009
Obsoletes: texlive-lang-mongolian < 2009
Provides: texlive-lang-norwegian = %{tl_version}
Conflicts: texlive-lang-norwegian < 2009
Obsoletes: texlive-lang-norwegian < 2009
Provides: texlive-lang-other = %{tl_version}
Conflicts: texlive-lang-other < 2009
Obsoletes: texlive-lang-other < 2009
Provides: texlive-lang-polish = %{tl_version}
Conflicts: texlive-lang-polish < 2009
Obsoletes: texlive-lang-polish < 2009
Provides: texlive-lang-portuguese = %{tl_version}
Conflicts: texlive-lang-portuguese < 2009
Obsoletes: texlive-lang-portuguese < 2009
Provides: texlive-lang-spanish = %{tl_version}
Conflicts: texlive-lang-spanish < 2009
Obsoletes: texlive-lang-spanish < 2009
Provides: texlive-lang-swedish = %{tl_version}
Conflicts: texlive-lang-swedish < 2009
Obsoletes: texlive-lang-swedish < 2009
Provides: texlive-lang-tibetan = %{tl_version}
Conflicts: texlive-lang-tibetan < 2009
Obsoletes: texlive-lang-tibetan < 2009
Provides: texlive-lang-ukenglish = %{tl_version}
Conflicts: texlive-lang-ukenglish < 2009
Obsoletes: texlive-lang-ukenglish < 2009
Provides: texlive-lang-vietnamese = %{tl_version}
Conflicts: texlive-lang-vietnamese < 2009
Obsoletes: texlive-lang-vietnamese < 2009
Provides: texlive-latex3 = %{tl_version}
Conflicts: texlive-latex3 < 2009
Obsoletes: texlive-latex3 < 2009
Provides: texlive-latex-extra = %{tl_version}
Conflicts: texlive-latex-extra < 2009
Obsoletes: texlive-latex-extra < 2009
Provides: texlive-math-extra = %{tl_version}
Conflicts: texlive-math-extra < 2009
Obsoletes: texlive-math-extra < 2009
Provides: texlive-pictures = %{tl_version}
Conflicts: texlive-pictures < 2009
Obsoletes: texlive-pictures < 2009
Provides: texlive-plain-extra = %{tl_version}
Conflicts: texlive-plain-extra < 2009
Obsoletes: texlive-plain-extra < 2009
Provides: texlive-publishers = %{tl_version}
Conflicts: texlive-publishers < 2009
Obsoletes: texlive-publishers < 2009
Provides: texlive-recommended = %{tl_version}
Conflicts: texlive-recommended < 2009
Obsoletes: texlive-recommended < 2009
Provides: texlive-science = %{tl_version}
Conflicts: texlive-science < 2009
Obsoletes: texlive-science < 2009


%description -n texlive-dist
This package brings the main TeX Live distribution packages (fonts and
TeX-related libraries) that are missing from the texlive-basic package.

%files		-n texlive-dist -f excludes
%{texmfdistdir}/psutils/paper.cfg
%{texmfdistdir}/fonts/afm/*
%{texmfdistdir}/fonts/cid
%{texmfdistdir}/fonts/cmap/*
%{texmfdistdir}/fonts/enc/*
%{texmfdistdir}/fonts/map/*
%{texmfdistdir}/fonts/misc
%{texmfdistdir}/fonts/ofm
%{texmfdistdir}/fonts/opentype/*
%{texmfdistdir}/fonts/ovf
%{texmfdistdir}/fonts/ovp
%{texmfdistdir}/fonts/sfd
%{texmfdistdir}/fonts/pk/ljfour/public/*
%{texmfdistdir}/fonts/tfm/*
%{texmfdistdir}/fonts/truetype/*
%{texmfdistdir}/fonts/type1/*
%{texmfdistdir}/fonts/vf/*
%{texmfdistdir}/tex/*

#context
%exclude %{texmfdistdir}/fonts/afm/hoekwater/context
%exclude %{texmfdistdir}/fonts/enc/dvips/context
%exclude %{texmfdistdir}/fonts/map/dvips/context
%exclude %{texmfdistdir}/fonts/map/luatex/context
%exclude %{texmfdistdir}/fonts/tfm/hoekwater/context
%exclude %{texmfdistdir}/fonts/type1/hoekwater/context
%exclude %{texmfdistdir}/tex/context
%exclude %{texmfdistdir}/tex/generic/context
%exclude %{texmfdistdir}/tex/latex/context
%exclude %{texmfdistdir}/fonts/misc/xetex/fontmapping/context

# xypic
%exclude %{texmfdistdir}/dvips/xypic
%exclude %{texmfdistdir}/fonts/afm/public/xypic
%exclude %{texmfdistdir}/fonts/enc/dvips/xypic
%exclude %{texmfdistdir}/fonts/map/dvips/xypic
%exclude %{texmfdistdir}/fonts/tfm/public/xypic
%exclude %{texmfdistdir}/fonts/type1/public/xypic
%exclude %{texmfdistdir}/tex/generic/xypic

# xetexconfig
%exclude %{texmfdistdir}/tex/xelatex/xetexconfig
%{texmfdistdir}/web2c/updmap-dist.cfg

%package	-n texlive-context
Summary:	Tex Live ConTeXt Package
Group:		Publishing
Requires:	texlive-texmf >= %{version}-%{release}
Requires:	ruby
Conflicts: tetex-context < 2.01
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
#Requires: texlive = %{tl_version}
Provides: texlive-collection-context = %{tl_version}

%description	-n texlive-context
This is the ConTeXt package of the TeX Live distribution. Use this only
if you rely on context for building tex documents.

%files		-n texlive-context
%{texmfdistdir}/fonts/afm/hoekwater/context
%{texmfdistdir}/fonts/enc/dvips/context
%{texmfdistdir}/fonts/map/dvips/context
%{texmfdistdir}/fonts/map/luatex/context
%{texmfdistdir}/fonts/map/pdftex/context
%{texmfdistdir}/fonts/misc/xetex/fontmapping/context
%{texmfdistdir}/fonts/tfm/hoekwater/context
%{texmfdistdir}/fonts/type1/hoekwater/context
%{texmfbindir}/mptopdf
%{texmfbindir}/mtxrun
%{texmfdistdir}/context
%{texmfdistdir}/scripts/context
%{texmfdistdir}/tex/context
%{texmfdistdir}/tex/latex/context
%{texmfdistdir}/bibtex/bst/context
%{texmfdistdir}/tex/generic/context
%{texmfdistdir}/metapost/context
%exclude %{texmfdistdir}/scripts/context/stubs/source
%exclude %{texmfdistdir}/scripts/context/stubs/setup
%exclude %{texmfdistdir}/scripts/context/stubs/install
%exclude %{texmfdistdir}/scripts/context/stubs/mswin
%exclude %{texmfdistdir}/scripts/context/stubs/win64

%package	-n texlive-doc
Summary:	Tex Live documentation
Group:		Publishing
Requires:	texlive-texmf >= %{version}-%{release}
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
Provides: texlive-doc-base = %{tl_version}
Conflicts: texlive-doc-base < 2009
Obsoletes: texlive-doc-base < 2009
Provides: texlive-doc-bg = %{tl_version}
Conflicts: texlive-doc-bg < 2009
Obsoletes: texlive-doc-bg < 2009
Provides: texlive-doc-cs+sk = %{tl_version}
Conflicts: texlive-doc-cs+sk < 2009
Obsoletes: texlive-doc-cs+sk < 2009
Provides: texlive-doc-de = %{tl_version}
Conflicts: texlive-doc-de < 2009
Obsoletes: texlive-doc-de < 2009
Provides: texlive-doc-el = %{tl_version}
Conflicts: texlive-doc-el < 2009
Obsoletes: texlive-doc-el < 2009
Provides: texlive-doc-en = %{tl_version}
Conflicts: texlive-doc-en < 2009
Obsoletes: texlive-doc-en < 2009
Provides: texlive-doc-es = %{tl_version}
Conflicts: texlive-doc-es < 2009
Obsoletes: texlive-doc-es < 2009
Provides: texlive-doc-fi = %{tl_version}
Conflicts: texlive-doc-fi < 2009
Obsoletes: texlive-doc-fi < 2009
Provides: texlive-doc-fr = %{tl_version}
Conflicts: texlive-doc-fr < 2009
Obsoletes: texlive-doc-fr < 2009
Provides: texlive-doc-it = %{tl_version}
Conflicts: texlive-doc-it < 2009
Obsoletes: texlive-doc-it < 2009
Provides: texlive-doc-ja = %{tl_version}
Conflicts: texlive-doc-ja < 2009
Obsoletes: texlive-doc-ja < 2009
Provides: texlive-doc-ko = %{tl_version}
Conflicts: texlive-doc-ko < 2009
Obsoletes: texlive-doc-ko < 2009
Provides: texlive-doc-mn = %{tl_version}
Conflicts: texlive-doc-mn < 2009
Obsoletes: texlive-doc-mn < 2009
Provides: texlive-doc-nl = %{tl_version}
Conflicts: texlive-doc-nl < 2009
Obsoletes: texlive-doc-nl < 2009
Provides: texlive-doc-pl = %{tl_version}
Conflicts: texlive-doc-pl < 2009
Obsoletes: texlive-doc-pl < 2009
Provides: texlive-doc-pt = %{tl_version}
Conflicts: texlive-doc-pt < 2009
Obsoletes: texlive-doc-pt < 2009
Provides: texlive-doc-ru = %{tl_version}
Conflicts: texlive-doc-ru < 2009
Obsoletes: texlive-doc-ru < 2009
Provides: texlive-doc-sl = %{tl_version}
Conflicts: texlive-doc-sl < 2009
Obsoletes: texlive-doc-sl < 2009
Provides: texlive-doc-th = %{tl_version}
Conflicts: texlive-doc-th < 2009
Obsoletes: texlive-doc-th < 2009
Provides: texlive-doc-tr = %{tl_version}
Conflicts: texlive-doc-tr < 2009
Obsoletes: texlive-doc-tr < 2009
Provides: texlive-doc-uk = %{tl_version}
Conflicts: texlive-doc-uk < 2009
Obsoletes: texlive-doc-uk < 2009
Provides: texlive-doc-vi = %{tl_version}
Conflicts: texlive-doc-vi < 2009
Obsoletes: texlive-doc-vi < 2009
Provides: texlive-doc-zh = %{tl_version}
Conflicts: texlive-doc-zh < 2009
Obsoletes: texlive-doc-zh < 2009

%description	-n texlive-doc
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-doc
#texmfdistdir/doc/*
%if %{enable_asymptote}
%exclude %{texmfdistdir}/doc/asymptote
%endif
%if %{enable_xindy}
%exclude %{texmfdistdir}/doc/xindy
%endif
%{texmfdistdir}/doc

#-----------------------------------------------------------------------
%package	-n texlive-fontsextra
Summary:	TeX Live extra fonts
Group:		Publishing
Requires:	texlive-texmf = %{version}
Requires(post):	texlive-dist = %{version}-%{release}
Requires(postun):	texlive >= %{tl_version}
Obsoletes: texmf-fonts-cm-lgc <= 0.5-alt2_20
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3
#Requires: texlive = %{tl_version}
Provides: texlive-collection-fontsextra = %{tl_version}

%description	-n texlive-fontsextra
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-fontsextra -f %{SOURCE10}
%{texmfdistdir}/web2c/updmap-fontsextra.cfg

%package	-n texlive-fonts-asian
Summary:	TeX Live extra fonts for asian languages
Group:		Publishing
Requires:	texlive-texmf = %{version}
Requires(post):	texlive-dist = %{version}-%{release}
Requires(postun):	texlive >= %{tl_version}
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3

%description	-n texlive-fonts-asian
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-fonts-asian -f %{SOURCE11}

%package	-n texlive-fonts-sources
Summary:	TeX Live font sources
Group:		Publishing
Requires:	texlive = %{version}
Requires(postun):	texlive >= %{tl_version}
AutoReq: yes,notex,nopython,nopython3
AutoProv: yes,nopython,nopython3

%description	-n texlive-fonts-sources
This package contains the source (mf) files for all fonts. This is usally only
needed if you build applications.

%files		-n texlive-fonts-sources -f %{SOURCE12}

%prep
%setup -q -n texlive-%{mga_tl_timestamp}-texmf

#remove source, as we don't need it and it saves some space
rm -rf texmf-dist/source
#remove all windows bat files
find . -name \*.bat -exec rm -f {} \;

%patch4 -p1

perl -pi -e 's%%^(TEXMFMAIN\s+= ).*%%$1%{texmfdistdir}%%;'		  \
	 -e 's%%^(TEXMFDIST\s+= ).*%%$1%{texmfdistdir}%%;'		  \
	 -e 's%%^(TEXMF\s+= .*)\}$%%$1,%{texmfdir}\}%%;'			  \
	 -e 's%%^(TEXMFLOCAL\s+= ).*%%$1%{texmflocaldir}%%;'		  \
	 -e 's%%^(TEXMFSYSVAR\s+= ).*%%$1%{texmfvardir}%%;'		  \
	 -e 's%%^(TEXMFSYSCONFIG\s+= ).*%%$1%{texmfconfdir}%%;'		  \
	 -e 's%%^(TEXMFHOME\s+= ).*%%$1\$HOME/texmf%%;'			  \
	 -e 's%%^(TEXMFVAR\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-var%%;'	  \
	 -e 's%%^(TEXMFCONFIG\s+= ).*%%$1\$HOME/.texlive%{relYear}/texmf-config%%;'\
	 -e 's%%^(OSFONTDIR\s+= ).*%%$1%{_datadir}/fonts%%;'		  \
	texmf-dist/web2c/texmf.cnf

perl -pi -e 's%%^(\s*TEXMFMAIN\s+=\s+").*%%$1%{texmfdistdir}",%%;'				\
	 -e 's%%TEXMFCONTEXT%%TEXMFDIST%%g;'						\
	 -e 's%%^(\s*TEXMFDIST\s+=\s+).*%%$1"%{texmfdistdir}",%%;'				\
	 -e 's%%^(TEXMF\s+= .*)\}$%%$1,%{texmfdir}\}%%;'					\
	 -e 's%%^(\s*TEXMFLOCAL\s+=\s+).*%%$1"%{texmflocaldir}",%%;'			\
	 -e 's%%^(\s*TEXMFSYSVAR\s+=\s+).*%%$1"%{texmfvardir}",%%;'			\
	 -e 's%%^(\s*TEXMFSYSCONFIG\s+=\s+).*%%$1"%{texmfconfdir}",%%;'			\
	 -e 's%%^(\s*TEXMFHOME\s+=\s+").*%%$1\$HOME/texmf",%%;'				\
	 -e 's%%^(\s*TEXMFVAR\s+=\s+").*%%$1\$HOME/.texlive%{relYear}/texmf-var",%%;'		\
	 -e 's%%^(\s*TEXMFCONFIG\s+=\s+").*%%$1\$HOME/.texlive%{relYear}/texmf-config",%%;'	\
	 -e 's%%^(\s*FONTCONFIG_PATH\s+=\s+").*%%$1%{_sysconfdir}/fonts",%%;'		\
	 -e 's|^local texmflocal.*$||;'							\
	 -e 's|^texmflocal.*$||;'							\
	texmf-dist/web2c/texmfcnf.lua

perl -pi -e 's%%^# (viewer_pdf = )xpdf.*%%$1xdg-open%%;'	\
	texmf-dist/texdoc/texdoc.cnf

# fix python shebangs
%{_bindir}/pathfix.py -pni "%{__python3} " \
	. \
	texmf-dist/scripts/pdfbook2/pdfbook2 \
	texmf-dist/scripts/de-macro/de-macro \

%patch33 -p0


#-----------------------------------------------------------------------
%build
cat %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} > excludes
perl -pi -e 's%\%\{texmfdistdir\}%\%exclude \%\{texmfdistdir\}%g;' excludes

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{texmfdistdir}
cp -la texmf-dist/* %{buildroot}%{texmfdistdir}

mkdir -p %{buildroot}%{texmfbindir}

pushd %{buildroot}%{texmfbindir}
	ln -sf %{texmfdistdir}/scripts/a2ping/a2ping.pl a2ping
	ln -sf %{texmfdistdir}/scripts/fontools/afm2afm afm2afm
	ln -sf %{texmfdistdir}/scripts/bundledoc/arlatex arlatex
	ln -sf %{texmfdistdir}/scripts/authorindex/authorindex authorindex
	ln -sf %{texmfdistdir}/scripts/fontools/autoinst autoinst
	ln -sf %{texmfdistdir}/scripts/bibexport/bibexport.sh bibexport
	ln -sf %{texmfdistdir}/scripts/bundledoc/bundledoc bundledoc
	ln -sf %{texmfdistdir}/scripts/cachepic/cachepic.tlu cachepic
	ln -sf %{texmfdistdir}/scripts/de-macro/de-macro de-macro
	ln -sf %{texmfdistdir}/scripts/dviasm/dviasm.py dviasm
	ln -sf %{texmfdistdir}/scripts/texlive-extra/e2pall.pl e2pall
	ln -sf %{texmfdistdir}/scripts/epstopdf/epstopdf.pl epstopdf
	ln -sf %{texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
	ln -sf %{texmfdistdir}/scripts/findhyph/findhyph findhyph
	ln -sf %{texmfdistdir}/scripts/fragmaster/fragmaster.pl fragmaster
%if !%{with_system_tex4ht}
	ln -sf %{texmfdistdir}/scripts/tex4ht/ht.sh ht
	ln -sf %{texmfdistdir}/scripts/tex4ht/htcontext.sh htcontext
	ln -sf %{texmfdistdir}/scripts/tex4ht/htlatex.sh htlatex
	ln -sf %{texmfdistdir}/scripts/tex4ht/htmex.sh htmex
	ln -sf %{texmfdistdir}/scripts/tex4ht/httex.sh httex
	ln -sf %{texmfdistdir}/scripts/tex4ht/httexi.sh httexi
	ln -sf %{texmfdistdir}/scripts/tex4ht/htxelatex.sh htxelatex
	ln -sf %{texmfdistdir}/scripts/tex4ht/htxetex.sh htxetex
%endif
	ln -sf %{texmfdistdir}/scripts/latex2man/latex2man latex2man
	ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff.pl latexdiff
	ln -sf %{texmfdistdir}/scripts/latexdiff/latexdiff-vc.pl latexdiff-vc
	ln -sf %{texmfdistdir}/scripts/latexmk/latexmk.pl latexmk
	ln -sf %{texmfdistdir}/scripts/latexdiff/latexrevise.pl latexrevise
	ln -sf %{texmfdistdir}/scripts/listings-ext/listings-ext.sh listings-ext.sh
	ln -sf %{texmfdistdir}/scripts/glossaries/makeglossaries makeglossaries
	ln -sf %{texmfdistdir}/scripts/mathspic/mathspic.pl mathspic
%if !%{with_system_tex4ht}
	ln -sf %{texmfdistdir}/scripts/tex4ht/mk4ht.pl mk4ht
%endif
	ln -sf %{texmfdistdir}/scripts/mkgrkindex/mkgrkindex mkgrkindex
	ln -sf %{texmfdistdir}/scripts/mkjobtexmf/mkjobtexmf.pl mkjobtexmf
	ln -sf %{texmfdistdir}/scripts/accfonts/mkt1font mkt1font
	ln -sf %{texmfdistdir}/scripts/context/perl/mptopdf.pl mptopdf
	ln -sf %{texmfdistdir}/scripts/fontools/ot2kpx ot2kpx
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdf180 pdf180
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdf270 pdf270
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdf90 pdf90
	ln -sf %{texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
	#ln -sf %{texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
	ln -sf %{texmfdistdir}/scripts/pdfbook2/pdfbook2 pdfbook2
	ln -sf %{texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfflip pdfflip
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam pdfjam
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjoin pdfjoin
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfnup pdfnup
	#ln -sf %{texmfdistdir}/scripts/pdfjam/pdfpun pdfpun
#    ln -sf %{texmfdistdir}/scripts/ppower4/pdfthumb.tlu pdfthumb
	ln -sf %{texmfdistdir}/scripts/perltex/perltex.pl perltex
#    ln -sf %{texmfdistdir}/scripts/fontools/pfm2kpx pfm2kpx
	ln -sf %{texmfdistdir}/scripts/pkfix/pkfix.pl pkfix
	ln -sf %{texmfdistdir}/scripts/pkfix-helper/pkfix-helper pkfix-helper
#    ln -sf %{texmfdistdir}/scripts/ppower4/ppower4.tlu ppower4
	ln -sf %{texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
	ln -sf %{texmfdistdir}/scripts/pst2pdf/pst2pdf.pl pst2pdf
	ln -sf %{texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
	ln -sf %{texmfdistdir}/scripts/epstopdf repstopdf
	ln -sf %{texmfdistdir}/scripts/pdfcrop rpdfcrop
	ln -sf %{texmfdistdir}/scripts/texdef latexdef
	ln -sf %{texmfdistdir}/scripts/texlive-extra/allcm.sh allec
	ln -sf %{texmfdistdir}/scripts/texlive-extra/kpsetool.sh kpsepath
	ln -sf %{texmfdistdir}/scripts/texlive-extra/kpsetool.sh kpsexpand
	ln -sf %{texmfdistdir}/scripts/texlive/fmtutil.pl mktexfmt
	ln -sf %{texmfdistdir}/scripts/texlive/mktexlsr texhash
	ln -sf %{texmfdistdir}/scripts/texlive/rungs.tlu rungs
#    ln -sf %{texmfdistdir}/scripts/fontools/showglyphs showglyphs
	ln -sf %{texmfdistdir}/scripts/splitindex/splitindex.pl splitindex
	ln -sf %{texmfdistdir}/scripts/simpdftex/simpdftex simpdftex
	ln -sf %{texmfdistdir}/scripts/svn-multi/svn-multi.pl svn-multi
	ln -sf %{texmfdistdir}/scripts/texcount/texcount.pl texcount
	ln -sf %{texmfdistdir}/scripts/texdiff/texdiff texdiff
	ln -sf %{texmfdistdir}/scripts/texdirflatten/texdirflatten texdirflatten
	ln -sf %{texmfdistdir}/scripts/texdoc/texdoc.tlu texdoc
	ln -sf %{texmfdistdir}/scripts/texloganalyser/texloganalyser texloganalyser
	ln -sf %{texmfdistdir}/scripts/thumbpdf/thumbpdf.pl thumbpdf
	ln -sf %{texmfdistdir}/scripts/ulqda/ulqda.pl ulqda
	ln -sf %{texmfdistdir}/scripts/vpe/vpe.pl vpe
	ln -sf %{texmfdistdir}/scripts/accfonts/vpl2ovp vpl2ovp
	ln -sf %{texmfdistdir}/scripts/accfonts/vpl2vpl vpl2vpl
	ln -sf %{texmfdistdir}/scripts/texlive/updmap.pl updmap
	ln -sf %{texmfdistdir}/scripts/texlive/updmap-sys.sh updmap-sys
	ln -sf %{texmfdistdir}/scripts/context/stubs/unix/mtxrun mtxrun
	ln -sf %{texmfdistdir}/scripts/texlive/fmtutil.pl fmtutil
	ln -sf %{texmfdistdir}/scripts/texlive/fmtutil-sys.sh fmtutil-sys
popd

    (cd  %{buildroot}%{texmfdistdir}/tex/generic/config ; ln -sf ../tex-ini-files/pdftexconfig.tex .)

	mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
	pushd %{buildroot}%{_datadir}/X11/app-defaults
	ln -sf %{texmfdistdir}/xdvi/XDvi XDvi
	cp %{SOURCE2} %{buildroot}%{_datadir}/X11/app-defaults
    popd

pushd %{buildroot}%{texmfdistdir}
%if !%{enable_asymptote}
    rm -fr asymptote doc/asymptote doc/info/asy* tex/latex/asymptote
%endif
%if !%{enable_xindy}
    rm -fr xindy doc/xindy scripts/xindy
%endif
    rm -fr dvipdfm
    perl -pi -e 's%%/usr/local%%/usr%%;' dvipdfmx/dvipdfmx.cfg
    rm -f ls-R README
    rm -fr doc/gzip
    cp -f %{SOURCE3} .

    find doc/man \( -name Makefile -o -name \*.pdf \) -exec rm -f {} \;
	# with_system_psutils
    rm -f doc/man/man1/{epsffit,extractres,fixdlsrps,fixfmps,fixmacps,fixpsditps,fixpspps,fixscribeps,fixtpps,fixwfwps,fixwpps,fixwwps,getafm,includeres,psbook,psmerge,psnup,psresize,psselect,pstops,psjoin,psutils}.1


    mkdir -p %{buildroot}%{_mandir}
    mv -f doc/man/* %{buildroot}%{_mandir}
    mkdir -p %{buildroot}%{_infodir}
    mv -f doc/info/*.info %{buildroot}%{_infodir}
popd

pushd %{buildroot}%{texmfdistdir}
%if %{with_system_tex4ht}
    rm -fr tex4ht
%endif
    rm -f ls-R README
    # .in files in documentation confuse find-provides
    rm -f doc/bibtex/urlbst/*.in
popd

%if !%{with_system_tex4ht}
	mkdir %{buildroot}%{_javadir}
	pushd %{buildroot}%{_javadir}
	    ln -sf %{texmfdistdir}/tex4ht/bin/tex4ht.jar tex4ht.jar
	popd
%endif
pushd %{buildroot}%{texmfdistdir}/doc/fonts
 find . -name \*.pdf -exec rm -rf {} \;
 rm -rf gnu-freefont/tools
popd


tar zxf %{SOURCE4}
mkdir -p %{buildroot}%{texmfdistdir}/tlpkg
cp -la install-tl-*/tlpkg/TeXLive %{buildroot}%{texmfdistdir}/tlpkg
cp -la install-tl-*/tlpkg/installer %{buildroot}%{texmfdistdir}/tlpkg
rm -rf %{buildroot}%{texmfdistdir}/tlpkg/installer/wget
rm -rf %{buildroot}%{texmfdistdir}/tlpkg/installer/xz


perl -pi -e 's|-var-value=TEXMFROOT|-var-value=TEXMFMAIN|g;'			\
    %{buildroot}%{texmfdistdir}/scripts/texlive/updmap.pl

mkdir -p %{buildroot}%{texmflocaldir}

touch %{buildroot}%{texmfdistdir}/ls-R
touch %{buildroot}%{texmflocaldir}/ls-R

pushd %{buildroot}%{texmfdistdir}
cp %{_sourcedir}/updmap-*.cfg web2c/
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/texlive-5-config.filetrigger << 'EOF'
#!/bin/sh
LC_ALL=C egrep -qs '^%{texmfdistdir}(/|$)' || exit 0
%_sbindir/texlive-postinstall-rebuild-all
EOF
chmod 755 %buildroot%_rpmlibdir/texlive-5-config.filetrigger
mkdir -p %buildroot%_sbindir
cat > %buildroot%_sbindir/texlive-postinstall-rebuild-all << 'EOF'
#!/bin/sh
LOGFILE=/dev/null
if [ -e %{texmfdistdir}/web2c/updmap-fontsextra.cfg ]; then
  cp %{texmfdistdir}/web2c/updmap-fontsextra.cfg %{texmfdistdir}/web2c/updmap.cfg
elif [ -e %{texmfdistdir}/web2c/updmap-dist.cfg ]; then
  cp %{texmfdistdir}/web2c/updmap-dist.cfg %{texmfdistdir}/web2c/updmap.cfg
elif [ -e %{texmfdistdir}/web2c/updmap-collection-basic.cfg ]; then
  cp %{texmfdistdir}/web2c/updmap-collection-basic.cfg %{texmfdistdir}/web2c/updmap.cfg
fi
yes|%{_bindir}/updmap-sys --syncwithtrees --force >> $LOGFILE 2>&1
yes|%{_bindir}/updmap-sys --syncwithtrees --force >> $LOGFILE 2>&1
# note: filetrigger in tex-common
# %{_bindir}/texhash > $LOGFILE 2>&1
# avoid autoreq dependency on mtxrun
MTXRUNEXE=%{_bindir}/mtxrun
[ -x $MTXRUNEXE ] && $MTXRUNEXE --generate >> $LOGFILE 2>&1
export TEXMF=%{texmfdistdir}
export TEXMFCNF=%{texmfdistdir}/web2c
export TEXMFCACHE=%{texmfvardir}
# fmtutil-sys on partial install cn't build --all formats, so exit code can be > 0
%{_bindir}/fmtutil-sys --no-strict --all >> $LOGFILE 2>&1 ||:
EOF
chmod 755 %buildroot%_sbindir/texlive-postinstall-rebuild-all
for rpm404_ghost in %{texmfdistdir}/ls-R %{texmflocaldir}/ls-R
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
# info
patch -p0 %buildroot%{_infodir}/texdraw.info < %SOURCE8003
sed -i '1s,^#!/usr/bin/env perl,#!/usr/bin/perl,' `grep -rl '^#!/usr/bin/env perl' %buildroot%{texmfdistdir}`
# merged from texlive-common = 0.1
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/texlive-collection-basic-files.req.list <<EOF
# texlive-base dirlist for %_rpmlibdir/files.req
%{texmfdistdir}	texlive-collection-basic
EOF



#-----------------------------------------------------------------------


%changelog
* Thu Aug 05 2021 Igor Vlasenko <viy@altlinux.org> 2021-alt1_1
- new version

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 2019-alt6_7
- removed conflict with psutils man pages

* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 2019-alt5_7
- fixed build

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 2019-alt4_7
- removed python2 scripts de-macro and dviasm.py (closes: #39169)

* Wed Nov 04 2020 Igor Vlasenko <viy@altlinux.ru> 2019-alt3_7
- added nopython to AutoReq: not to block py2 deprecation

* Wed Apr 08 2020 Dmitry V. Levin <ldv@altlinux.org> 2019-alt2_7
- NMU.
- Fixed python shebangs.
- Forcibly removed ruby dependencies.

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1_7
- new version

* Tue Sep 03 2019 Igor Vlasenko <viy@altlinux.ru> 2018-alt2_5
- rebuild formats with new texlive

* Wed Oct 17 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt1_5
- new version

* Tue Apr 10 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt8_2
- added latexmk symlink (closes: #34785)

* Mon Mar 12 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt7_2
- rebuild with rpm-build-tex 0.4.1

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt6_2
- added Provides: <$TEXMFDIST path>

* Sun Mar 11 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt5_2
- final release

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt4_2
- added prosper obsoletes

* Mon Mar 05 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt3_2
- added tex provides and latexmk

* Fri Mar 02 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt2_2
- updated filetrigger

* Fri Mar 02 2018 Igor Vlasenko <viy@altlinux.ru> 2017-alt1_2
- new version

