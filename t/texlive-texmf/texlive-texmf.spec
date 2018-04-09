# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ perl(Config/IniFiles.pm) perl(Data/Dumper/Concise.pm) perl(Date/Format.pm) perl(Date/Parse.pm) perl(Digest/SHA.pm) perl(Digest/SHA1.pm) perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Fatal.pm) perl(File/Copy/Recursive.pm) perl(File/HomeDir.pm) perl(File/Which.pm) perl(HTML/FormatText.pm) perl(HTML/TreeBuilder.pm) perl(HTTP/Status.pm) perl(IO/String.pm) perl(IPC/System/Simple.pm) perl(LWP.pm) perl(LWP/Simple.pm) perl(LWP/UserAgent.pm) perl(Locale/Maketext/Simple.pm) perl(Math/Trig.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Pod/Usage.pm) perl(Spreadsheet/ParseExcel.pm) perl(Term/ANSIColor.pm) perl(Test/More.pm) perl(Text/Unidecode.pm) perl(Tk.pm) perl(Tk/Adjuster.pm) perl(Tk/BrowseEntry.pm) perl(Tk/Dialog.pm) perl(Tk/DialogBox.pm) perl(Tk/DirTree.pm) perl(Tk/Font.pm) perl(Tk/HList.pm)
BuildRequires: perl(Tk/ItemStyle.pm) perl(Tk/NoteBook.pm) perl(Tk/PNG.pm) perl(Tk/Pane.pm) perl(Tk/ProgressBar.pm) perl(Tk/ROText.pm) perl(Tk/widgets.pm) perl(URI/Escape.pm) perl(Unicode/GCString.pm) perl(WWW/Mechanize.pm) perl(XML/Parser.pm) perl(XML/XPath.pm) perl(XML/XPath/XMLParser.pm) perl(YAML/Tiny.pm) perl(autodie.pm) perl(encoding.pm) perl-devel texinfo
# END SourceDeps(oneline)

%filter_from_requires /^.bin.sh5$/d
%filter_from_requires /^.bin.bsh$/d
%filter_from_requires /^.bin.ksh$/d
%filter_from_requires /^.usr.sbin.lsattr$/d

%filter_from_requires /^perl(make-rules.pl)/d
%filter_from_requires /^perl(installer.ctan-mirrors.pl)/d
%filter_from_requires /^perl(installer.mirrors.pl)/d
%filter_from_requires /^perl(TeXLive.trans.pl)/d

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

%global __requires_exclude ^perl\\((PDF::Reuse.*|Pedigree.*|Text::Unidecode|Tie::Watch|SelfLoader|TeXLive.*|Tk::path_tre|only|pdfTeX|script::MakeSPList)\\)|/usr/local/bin/fontforge
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{_docdir}|^/usr/share/texmf-dist/doc
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_docdir}|^/usr/share/texmf-dist/doc

%define enable_asymptote	0
%define enable_xindy		1

%define with_system_dialog	1
%define with_system_lcdf	0
%define with_system_poppler	0
%define with_system_psutils	1
%define with_system_t1lib	1
%define with_system_tex4ht	0
%define with_system_teckit	0

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

%define relYear 2017
%global tl_version %relYear
%global mga_tl_timestamp 20170524

Name:		texlive-texmf
Version:	%relYear
Release:	alt8_2
Summary:	The TeX formatting system
Group:		Publishing
License:	http://www.tug.org/texlive/LICENSE.TL
URL:		http://tug.org/texlive/
Source0:	ftp://tug.org/historic/systems/texlive/%{relYear}/texlive-%{mga_tl_timestamp}-texmf.tar.xz
Source1:	ftp://tug.org/historic/systems/texlive/%{relYear}/texlive-%{mga_tl_timestamp}-texmf.tar.xz.sha512
Source2:	XDvi-color
Source3:	http://www.tug.org/texlive/LICENSE.TL
Source4:	ftp://tug.org/historic/systems/texlive/%{relYear}/install-tl-unx.tar.gz
Source5:	http://mirror.hmc.edu/ctan/systems/texlive/tlnet/tlpkg/texlive.tlpdb
Source6:	updmap-collection-basic.cfg
Source7:	updmap-dist.cfg
Source8:	updmap-fontsextra.cfg
Source10:	default.template
Source11:	basic.profile
Source12:	fonts-basic.profile
Source13:	context.profile
Source14:	omega.profile
Source15:	luatex.profile
Source16:	lang-roman.profile
Source17:	publish.profile
Source18:	html.profile
Source19:	music.profile
Source20:	games.profile
Source21:	lang-arabic.profile
Source22:	lang-asian.profile
Source23:	lang-cyrillic_greek.profile
Source24:	lang-other.profile
Source25:	fonts-extra.profile

BuildArch:	noarch

#-----------------------------------------------------------------------
Requires:	perl-Algorithm-Diff
Requires:	xdg-utils
Requires:	texlive >= %{tl_version}
Requires:	texlive-collection-basic = %{version}-%{release}
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
AutoReq: yes,notex
Source8000: texlive-20170524-texmf-dist-scripts-perl-526.patch
Source8001: texlive-texmf-dist-scripts-system-PDF-Reuse.patch
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
BuildRequires: python-modules-encodings
BuildRequires: perl(BibTeX/Parser.pm)
BuildRequires: perl(PDF/Reuse.pm)


#-----------------------------------------------------------------------
%description
This package will install the standard TeX Live and MetaFont distribution.
It provides a comprehensive TeX system. It includes all the major
TeX-related programs, macro packages, and fonts that are free software,
including support for many languages around the world.

%files

#-----------------------------------------------------------------------
%package	-n texlive-collection-basic
Summary:	TeX Live extra fonts
Group:		Publishing
Requires:	texlive = %{version}
Requires(post):	texlive = %{version}
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
AutoReq: yes,notex
#Requires: texlive = %{tl_version}
Provides: texlive-collection-fontsrecommended = %{tl_version}
Provides: texlive-collection-fontutils = %{tl_version}
Provides: texlive-collection-latex = %{tl_version}
Provides: texlive-collection-genericrecommended = %{tl_version}
Provides: tex(tex)
Provides: tex(latex-base)
Provides: tex(latex)
Requires: perl(PDF/Reuse.pm)
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

%files		-n texlive-collection-basic
%{texmfbindir}/*
%{_datadir}/X11/app-defaults/XDvi*
%{_infodir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{texmfdistdir}
%{texmfdistdir}/chktex
%dir %{texmfdistdir}/doc
%{texmfdistdir}/doc/tetex
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
%dir %{texmfdistdir}/tex
%{texmfdistdir}/web2c
%if !%{with_system_tex4ht}
%{texmfdistdir}/tex4ht
%{_javadir}/tex4ht.jar
%endif
%{texmfdistdir}/texdoc
%dir %{texmflocaldir}

%dir %{texmfdistdir}/fonts
%dir %{texmfdistdir}/fonts/afm
%dir %{texmfdistdir}/fonts/afm/adobe
%dir %{texmfdistdir}/fonts/afm/bitstrea
%dir %{texmfdistdir}/fonts/afm/hoekwater
%dir %{texmfdistdir}/fonts/afm/public
%dir %{texmfdistdir}/fonts/afm/urw
%dir %{texmfdistdir}/fonts/cmap
%dir %{texmfdistdir}/fonts/enc
%dir %{texmfdistdir}/fonts/enc/dvips
%dir %{texmfdistdir}/fonts/map
%dir %{texmfdistdir}/fonts/map/dvips
%dir %{texmfdistdir}/fonts/opentype
%dir %{texmfdistdir}/fonts/opentype/public
%dir %{texmfdistdir}/fonts/map/vtex
%dir %{texmfdistdir}/fonts/pk
%dir %{texmfdistdir}/fonts/pk/ljfour
%dir %{texmfdistdir}/fonts/pk/ljfour/public
%dir %{texmfdistdir}/fonts/source
%dir %{texmfdistdir}/fonts/source/jknappen
%dir %{texmfdistdir}/fonts/source/public
%dir %{texmfdistdir}/fonts/tfm
%dir %{texmfdistdir}/fonts/tfm/adobe
%dir %{texmfdistdir}/fonts/tfm/bitstrea
%dir %{texmfdistdir}/fonts/tfm/jknappen
%dir %{texmfdistdir}/fonts/tfm/monotype
%dir %{texmfdistdir}/fonts/tfm/public
%dir %{texmfdistdir}/fonts/tfm/urw35vf
%dir %{texmfdistdir}/fonts/truetype
%dir %{texmfdistdir}/fonts/truetype/public
%dir %{texmfdistdir}/fonts/type1
%dir %{texmfdistdir}/fonts/type1/adobe
%dir %{texmfdistdir}/fonts/type1/bitstrea
%dir %{texmfdistdir}/fonts/type1/hoekwater
%dir %{texmfdistdir}/fonts/type1/public
%dir %{texmfdistdir}/fonts/type1/urw
%dir %{texmfdistdir}/fonts/vf
%dir %{texmfdistdir}/fonts/vf/adobe
%dir %{texmfdistdir}/fonts/vf/bitstrea
%dir %{texmfdistdir}/fonts/vf/monotype
%dir %{texmfdistdir}/fonts/vf/public
%dir %{texmfdistdir}/fonts/vf/urw35vf
%dir %{texmfdistdir}/tex/generic
%dir %{texmfdistdir}/tex/latex
%dir %{texmfdistdir}/tex/luatex
%dir %{texmfdistdir}/tex/plain
%dir %{texmfdistdir}/tex/xelatex
# ae,algorithms,amscls,amsfonts,amsmath,anysize,avantgar,babel,babel-english,babelbib,beamer,beton,bibtex,bookman,booktabs,caption,caption,carlisle,charter,cite,cm,cm-super,cmap,cmextra,colortbl,courier,cprotect,crop,csquotes,ctable,dvipdfmx,dvipdfmx-def,dvips,ec,enctex,enumitem,eso-pic,etex,etex-pkg,etoolbox,euler,euro,eurosym,extsizes,fancybox,fancyhdr,fancyref,fancyvrb,fix2col,float,fontspec,footmisc,fp,fpl,geometry,glyphlist,graphics,gsftopk,helvetic,hyperref,hyph-utf8,hyphen-base,ifluatex,ifxetex,index,jknapltx,koma-script,kpathsea,l3experimental,l3kernel,l3packages,latex,latex-bin,latex-fonts,latexconfig,listings,lm,lm-math,ltxmisc,lua-alt-getopt,luaotfload,luatex,luatexbase,makeindex,marginnote,marvosym,mathpazo,mdwtools,memoir,metafont,metalogo,mflogo,mfnfss,mfware,mh,microtype,minitoc,misc,mparhack,mptopdf,ms,natbib,ncntrsbk,ntgclass,oberdiek,palatino,parallel,parskip,pdfpages,pdftex,pdftex-def,pgf,plain,powerdot,psfrag,pslatex,psnfss,pspicture,pst-blur,pst-grad,pst-slpe,pst-text,pstricks,pxfonts,qstest,rcs,rotating,rsfs,sansmath,sauerj,section,seminar,sepnum,setspace,soul,subfig,symbol,tetex,tex,tex-gyre,tex-gyre-math,texconfig,texlive-scripts,texlive.infra,textcase,thumbpdf,times,tipa,tools,txfonts,type1cm,typehtml,underscore,unicode-math,url,utopia,wasy,wasysym,xcolor,xdvi,xkeyval,xunicode,zapfchan,zapfding
%{texmfdistdir}/fonts/afm/adobe/avantgar
%{texmfdistdir}/fonts/afm/adobe/bookman
%{texmfdistdir}/fonts/afm/adobe/courier
%{texmfdistdir}/fonts/afm/adobe/helvetic
%{texmfdistdir}/fonts/afm/adobe/ncntrsbk
%{texmfdistdir}/fonts/afm/adobe/palatino
%{texmfdistdir}/fonts/afm/adobe/symbol
%{texmfdistdir}/fonts/afm/adobe/times
%{texmfdistdir}/fonts/afm/adobe/utopia
%{texmfdistdir}/fonts/afm/adobe/zapfchan
%{texmfdistdir}/fonts/afm/adobe/zapfding
%{texmfdistdir}/fonts/afm/bitstrea/charter
%{texmfdistdir}/fonts/afm/public/amsfonts
%{texmfdistdir}/fonts/afm/public/cm-super
%{texmfdistdir}/fonts/afm/public/fpl
%{texmfdistdir}/fonts/afm/public/lm
%{texmfdistdir}/fonts/afm/public/marvosym
%{texmfdistdir}/fonts/afm/public/mathpazo
%{texmfdistdir}/fonts/afm/public/pxfonts
%{texmfdistdir}/fonts/afm/public/rsfs
%{texmfdistdir}/fonts/afm/public/tex-gyre
%{texmfdistdir}/fonts/afm/public/txfonts
%{texmfdistdir}/fonts/afm/urw/avantgar
%{texmfdistdir}/fonts/afm/urw/bookman
%{texmfdistdir}/fonts/afm/urw/courier
%{texmfdistdir}/fonts/afm/urw/helvetic
%{texmfdistdir}/fonts/afm/urw/ncntrsbk
%{texmfdistdir}/fonts/afm/urw/palatino
%{texmfdistdir}/fonts/afm/urw/symbol
%{texmfdistdir}/fonts/afm/urw/times
%{texmfdistdir}/fonts/afm/urw/zapfchan
%{texmfdistdir}/fonts/afm/urw/zapfding
%{texmfdistdir}/fonts/enc/dvips/base
%{texmfdistdir}/fonts/enc/dvips/cm-super
%{texmfdistdir}/fonts/enc/dvips/lm
%{texmfdistdir}/fonts/enc/dvips/tex-gyre
%{texmfdistdir}/fonts/enc/dvips/tetex
%{texmfdistdir}/fonts/enc/dvips/txfonts
%{texmfdistdir}/fonts/lig/afm2pl
%{texmfdistdir}/fonts/map/dvipdfmx
%{texmfdistdir}/fonts/map/dvips/amsfonts
%{texmfdistdir}/fonts/map/dvips/avantgar
%{texmfdistdir}/fonts/map/dvips/bookman
%{texmfdistdir}/fonts/map/dvips/cm
%{texmfdistdir}/fonts/map/dvips/cm-super
%{texmfdistdir}/fonts/map/dvips/courier
%{texmfdistdir}/fonts/map/dvips/eurosym
%{texmfdistdir}/fonts/map/dvips/helvetic
%{texmfdistdir}/fonts/map/dvips/lm
%{texmfdistdir}/fonts/map/dvips/marvosym
%{texmfdistdir}/fonts/map/dvips/ncntrsbk
%{texmfdistdir}/fonts/map/dvips/palatino
%{texmfdistdir}/fonts/map/dvips/pslatex
%{texmfdistdir}/fonts/map/dvips/psnfss
%{texmfdistdir}/fonts/map/dvips/pxfonts
%{texmfdistdir}/fonts/map/dvips/rsfs
%{texmfdistdir}/fonts/map/dvips/symbol
%{texmfdistdir}/fonts/map/dvips/tex-gyre
%{texmfdistdir}/fonts/map/dvips/tetex
%{texmfdistdir}/fonts/map/dvips/times
%{texmfdistdir}/fonts/map/dvips/tipa
%{texmfdistdir}/fonts/map/dvips/txfonts
%{texmfdistdir}/fonts/map/dvips/zapfchan
%{texmfdistdir}/fonts/map/dvips/zapfding
%{texmfdistdir}/fonts/map/glyphlist
%{texmfdistdir}/fonts/map/pdftex
%{texmfdistdir}/fonts/map/vtex/cm-super
%{texmfdistdir}/fonts/opentype/public/lm
%{texmfdistdir}/fonts/opentype/public/tex-gyre
%{texmfdistdir}/fonts/opentype/public/tex-gyre-math
%{texmfdistdir}/fonts/pk/ljfour/public/cm
%{texmfdistdir}/fonts/source/jknappen/ec
%{texmfdistdir}/fonts/source/public/amsfonts
%{texmfdistdir}/fonts/source/public/cm
%{texmfdistdir}/fonts/source/public/cmextra
%{texmfdistdir}/fonts/source/public/eurosym
%{texmfdistdir}/fonts/source/public/latex-fonts
%{texmfdistdir}/fonts/source/public/mflogo
%{texmfdistdir}/fonts/source/public/rsfs
%{texmfdistdir}/fonts/source/public/tipa
%{texmfdistdir}/fonts/tfm/adobe/avantgar
%{texmfdistdir}/fonts/tfm/adobe/bookman
%{texmfdistdir}/fonts/tfm/adobe/courier
%{texmfdistdir}/fonts/tfm/adobe/helvetic
%{texmfdistdir}/fonts/tfm/adobe/ncntrsbk
%{texmfdistdir}/fonts/tfm/adobe/palatino
%{texmfdistdir}/fonts/tfm/adobe/symbol
%{texmfdistdir}/fonts/tfm/adobe/times
%{texmfdistdir}/fonts/tfm/adobe/zapfchan
%{texmfdistdir}/fonts/tfm/adobe/zapfding
%{texmfdistdir}/fonts/tfm/bitstrea/charter
%{texmfdistdir}/fonts/tfm/jknappen/ec
%{texmfdistdir}/fonts/tfm/monotype/helvetic
%{texmfdistdir}/fonts/tfm/monotype/symbol
%{texmfdistdir}/fonts/tfm/public/ae
%{texmfdistdir}/fonts/tfm/public/amsfonts
%{texmfdistdir}/fonts/tfm/public/cm
%{texmfdistdir}/fonts/tfm/public/cmextra
%{texmfdistdir}/fonts/tfm/public/eurosym
%{texmfdistdir}/fonts/tfm/public/latex-fonts
%{texmfdistdir}/fonts/tfm/public/lm
%{texmfdistdir}/fonts/tfm/public/marvosym
%{texmfdistdir}/fonts/tfm/public/mathpazo
%{texmfdistdir}/fonts/tfm/public/mflogo
%{texmfdistdir}/fonts/tfm/public/pslatex
%{texmfdistdir}/fonts/tfm/public/pxfonts
%{texmfdistdir}/fonts/tfm/public/rsfs
%{texmfdistdir}/fonts/tfm/public/tex-gyre
%{texmfdistdir}/fonts/tfm/public/tipa
%{texmfdistdir}/fonts/tfm/public/txfonts
%{texmfdistdir}/fonts/tfm/urw35vf/avantgar
%{texmfdistdir}/fonts/tfm/urw35vf/bookman
%{texmfdistdir}/fonts/tfm/urw35vf/courier
%{texmfdistdir}/fonts/tfm/urw35vf/helvetic
%{texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk
%{texmfdistdir}/fonts/tfm/urw35vf/palatino
%{texmfdistdir}/fonts/tfm/urw35vf/symbol
%{texmfdistdir}/fonts/tfm/urw35vf/times
%{texmfdistdir}/fonts/tfm/urw35vf/zapfchan
%{texmfdistdir}/fonts/tfm/urw35vf/zapfding
%{texmfdistdir}/fonts/truetype/public/marvosym
%{texmfdistdir}/fonts/type1/adobe/courier
%{texmfdistdir}/fonts/type1/adobe/utopia
%{texmfdistdir}/fonts/type1/bitstrea/charter
%{texmfdistdir}/fonts/type1/public/amsfonts
%{texmfdistdir}/fonts/type1/public/cm-super
%{texmfdistdir}/fonts/type1/public/eurosym
%{texmfdistdir}/fonts/type1/public/fpl
%{texmfdistdir}/fonts/type1/public/lm
%{texmfdistdir}/fonts/type1/public/marvosym
%{texmfdistdir}/fonts/type1/public/mathpazo
%{texmfdistdir}/fonts/type1/public/pxfonts
%{texmfdistdir}/fonts/type1/public/rsfs
%{texmfdistdir}/fonts/type1/public/tex-gyre
%{texmfdistdir}/fonts/type1/public/tipa
%{texmfdistdir}/fonts/type1/public/txfonts
%{texmfdistdir}/fonts/type1/urw/avantgar
%{texmfdistdir}/fonts/type1/urw/bookman
%{texmfdistdir}/fonts/type1/urw/courier
%{texmfdistdir}/fonts/type1/urw/helvetic
%{texmfdistdir}/fonts/type1/urw/ncntrsbk
%{texmfdistdir}/fonts/type1/urw/palatino
%{texmfdistdir}/fonts/type1/urw/symbol
%{texmfdistdir}/fonts/type1/urw/times
%{texmfdistdir}/fonts/type1/urw/zapfchan
%{texmfdistdir}/fonts/type1/urw/zapfding
%{texmfdistdir}/fonts/vf/adobe/avantgar
%{texmfdistdir}/fonts/vf/adobe/bookman
%{texmfdistdir}/fonts/vf/adobe/courier
%{texmfdistdir}/fonts/vf/adobe/helvetic
%{texmfdistdir}/fonts/vf/adobe/ncntrsbk
%{texmfdistdir}/fonts/vf/adobe/palatino
%{texmfdistdir}/fonts/vf/adobe/times
%{texmfdistdir}/fonts/vf/adobe/utopia
%{texmfdistdir}/fonts/vf/adobe/zapfchan
%{texmfdistdir}/fonts/vf/bitstrea/charter
%{texmfdistdir}/fonts/vf/monotype/helvetic
%{texmfdistdir}/fonts/vf/public/ae
%{texmfdistdir}/fonts/vf/public/mathpazo
%{texmfdistdir}/fonts/vf/public/pslatex
%{texmfdistdir}/fonts/vf/public/pxfonts
%{texmfdistdir}/fonts/vf/public/txfonts
%{texmfdistdir}/fonts/vf/urw35vf/avantgar
%{texmfdistdir}/fonts/vf/urw35vf/bookman
%{texmfdistdir}/fonts/vf/urw35vf/courier
%{texmfdistdir}/fonts/vf/urw35vf/helvetic
%{texmfdistdir}/fonts/vf/urw35vf/ncntrsbk
%{texmfdistdir}/fonts/vf/urw35vf/palatino
%{texmfdistdir}/fonts/vf/urw35vf/times
%{texmfdistdir}/fonts/vf/urw35vf/zapfchan
%{texmfdistdir}/tex/generic/babel
%{texmfdistdir}/tex/generic/config
%{texmfdistdir}/tex/generic/dvips
%{texmfdistdir}/tex/generic/enctex
%{texmfdistdir}/tex/generic/hyphen
%{texmfdistdir}/tex/generic/ifxetex
%{texmfdistdir}/tex/generic/oberdiek
%{texmfdistdir}/tex/generic/pdftex
%{texmfdistdir}/tex/generic/pgf
%{texmfdistdir}/tex/generic/pst-blur
%{texmfdistdir}/tex/generic/pst-grad
%{texmfdistdir}/tex/generic/pst-slpe
%{texmfdistdir}/tex/generic/pst-text
%{texmfdistdir}/tex/generic/pstricks
%{texmfdistdir}/tex/generic/tex-ini-files
%{texmfdistdir}/tex/generic/thumbpdf
%{texmfdistdir}/tex/generic/xkeyval
%{texmfdistdir}/tex/latex/ae
%{texmfdistdir}/tex/latex/algorithms
%{texmfdistdir}/tex/latex/amscls
%{texmfdistdir}/tex/latex/amsfonts
%{texmfdistdir}/tex/latex/amsmath
%{texmfdistdir}/tex/latex/anysize
%{texmfdistdir}/tex/latex/avantgar
%{texmfdistdir}/tex/latex/babelbib
%{texmfdistdir}/tex/latex/base
%{texmfdistdir}/tex/latex/beamer
%{texmfdistdir}/tex/latex/beton
%{texmfdistdir}/tex/latex/bookman
%{texmfdistdir}/tex/latex/booktabs
%{texmfdistdir}/tex/latex/caption
%{texmfdistdir}/tex/latex/carlisle
%{texmfdistdir}/tex/latex/cite
%{texmfdistdir}/tex/latex/cm-super
%{texmfdistdir}/tex/latex/cmap
%{texmfdistdir}/tex/latex/colortbl
%{texmfdistdir}/tex/latex/courier
%{texmfdistdir}/tex/latex/cprotect
%{texmfdistdir}/tex/latex/crop
%{texmfdistdir}/tex/latex/csquotes
%{texmfdistdir}/tex/latex/ctable
%{texmfdistdir}/tex/latex/enumitem
%{texmfdistdir}/tex/latex/eso-pic
%{texmfdistdir}/tex/latex/etex-pkg
%{texmfdistdir}/tex/latex/etoolbox
%{texmfdistdir}/tex/latex/euler
%{texmfdistdir}/tex/latex/euro
%{texmfdistdir}/tex/latex/eurosym
%{texmfdistdir}/tex/latex/extsizes
%{texmfdistdir}/tex/latex/fancybox
%{texmfdistdir}/tex/latex/fancyhdr
%{texmfdistdir}/tex/latex/fancyref
%{texmfdistdir}/tex/latex/fancyvrb
%{texmfdistdir}/tex/latex/fix2col
%{texmfdistdir}/tex/latex/float
%{texmfdistdir}/tex/latex/fontspec
%{texmfdistdir}/tex/latex/footmisc
%{texmfdistdir}/tex/latex/fp
%{texmfdistdir}/tex/latex/geometry
%{texmfdistdir}/tex/latex/graphics
%{texmfdistdir}/tex/latex/graphics-cfg
%{texmfdistdir}/tex/latex/helvetic
%{texmfdistdir}/tex/latex/hyperref
%{texmfdistdir}/tex/latex/index
%{texmfdistdir}/tex/latex/jknapltx
%{texmfdistdir}/tex/latex/koma-script
%{texmfdistdir}/tex/latex/l3kernel
%{texmfdistdir}/tex/latex/l3packages
%{texmfdistdir}/tex/latex/latexconfig
%{texmfdistdir}/tex/latex/listings
%{texmfdistdir}/tex/latex/lm
%{texmfdistdir}/tex/latex/ltxmisc
%{texmfdistdir}/tex/latex/marginnote
%{texmfdistdir}/tex/latex/marvosym
%{texmfdistdir}/tex/latex/mdwtools
%{texmfdistdir}/tex/latex/memoir
%{texmfdistdir}/tex/latex/metalogo
%{texmfdistdir}/tex/latex/mflogo
%{texmfdistdir}/tex/latex/mfnfss
%{texmfdistdir}/tex/latex/microtype
%{texmfdistdir}/tex/latex/minitoc
%{texmfdistdir}/tex/latex/mparhack
%{texmfdistdir}/tex/latex/ms
%{texmfdistdir}/tex/latex/natbib
%{texmfdistdir}/tex/latex/ncntrsbk
%{texmfdistdir}/tex/latex/ntgclass
%{texmfdistdir}/tex/latex/oberdiek
%{texmfdistdir}/tex/latex/palatino
%{texmfdistdir}/tex/latex/parallel
%{texmfdistdir}/tex/latex/parskip
%{texmfdistdir}/tex/latex/pdfpages
%{texmfdistdir}/tex/latex/pgf
%{texmfdistdir}/tex/latex/powerdot
%{texmfdistdir}/tex/latex/psfrag
%{texmfdistdir}/tex/latex/pslatex
%{texmfdistdir}/tex/latex/psnfss
%{texmfdistdir}/tex/latex/pspicture
%{texmfdistdir}/tex/latex/pst-blur
%{texmfdistdir}/tex/latex/pst-grad
%{texmfdistdir}/tex/latex/pst-slpe
%{texmfdistdir}/tex/latex/pst-text
%{texmfdistdir}/tex/latex/pstricks
%{texmfdistdir}/tex/latex/pxfonts
%{texmfdistdir}/tex/latex/qstest
%{texmfdistdir}/tex/latex/rcs
%{texmfdistdir}/tex/latex/sansmath
%{texmfdistdir}/tex/latex/sauerj
%{texmfdistdir}/tex/latex/section
%{texmfdistdir}/tex/latex/seminar
%{texmfdistdir}/tex/latex/sepnum
%{texmfdistdir}/tex/latex/setspace
%{texmfdistdir}/tex/latex/soul
%{texmfdistdir}/tex/latex/subfig
%{texmfdistdir}/tex/latex/symbol
%{texmfdistdir}/tex/latex/tex-gyre
%{texmfdistdir}/tex/latex/textcase
%{texmfdistdir}/tex/latex/times
%{texmfdistdir}/tex/latex/tipa
%{texmfdistdir}/tex/latex/tools
%{texmfdistdir}/tex/latex/txfonts
%{texmfdistdir}/tex/latex/type1cm
%{texmfdistdir}/tex/latex/typehtml
%{texmfdistdir}/tex/latex/underscore
%{texmfdistdir}/tex/latex/unicode-math
%{texmfdistdir}/tex/latex/url
%{texmfdistdir}/tex/latex/wasysym
%{texmfdistdir}/tex/latex/xcolor
%{texmfdistdir}/tex/latex/xkeyval
%{texmfdistdir}/tex/latex/zapfchan
%{texmfdistdir}/tex/latex/zapfding
%{texmfdistdir}/tex/luatex/luaotfload
%{texmfdistdir}/tex/luatex/luatexbase
%{texmfdistdir}/tex/plain/amsfonts
%{texmfdistdir}/tex/plain/base
%{texmfdistdir}/tex/plain/config
%{texmfdistdir}/tex/plain/etex
%{texmfdistdir}/tex/plain/fp
%{texmfdistdir}/tex/plain/pgf
%{texmfdistdir}/tex/plain/rsfs
%{texmfdistdir}/tex/xelatex/xunicode
%ghost %{texmfdistdir}/ls-R
%ghost %{texmflocaldir}/ls-R

# xypic
%{texmfdistdir}/fonts/afm/public/xypic
%{texmfdistdir}/fonts/enc/dvips/xypic
%{texmfdistdir}/fonts/map/dvips/xypic
%{texmfdistdir}/fonts/source/public/xypic
%{texmfdistdir}/fonts/tfm/public/xypic
%{texmfdistdir}/fonts/type1/public/xypic
%{texmfdistdir}/tex/generic/xypic

# comment
%{texmfdistdir}/tex/latex/comment

# preprint
%{texmfdistdir}/tex/latex/preprint

# hyph-utf8, ruhyphen, dehypht, xecyr, ukrhyph, omegahyph
%{texmfdistdir}/tex/generic/hyph-utf8
%{texmfdistdir}/tex/generic/ruhyphen
%{texmfdistdir}/tex/generic/dehyph-exptl
%{texmfdistdir}/tex/generic/xecyr
%{texmfdistdir}/tex/generic/ukrhyph
%{texmfdistdir}/tex/generic/omegahyph

# xetexconfig
%{texmfdistdir}/tex/xelatex/xetexconfig

%exclude %{texmfdistdir}/tlpkg/installer/wget
%exclude %{texmfdistdir}/tlpkg/installer/xz

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
%_rpmlibdir/texlive-5-config.filetrigger
# forein binaries
%exclude %{texmfdistdir}/tlpkg/installer/wget*
%exclude %{texmfdistdir}/tlpkg/installer/xz*
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
Summary:	TeX Live extra fonts
Group:		Publishing
Requires:	texlive-texmf = %{version}-%{release}
Requires(post):	texlive-collection-basic = %{version}-%{release}
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
AutoReq: yes,notex
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
#if_with backport_p8
Provides: texmf(latex/atbegshi)
Provides: texmf(latex/ucs)
Provides: texmf(latex/xcolor)
Provides: texmf(latex/etoolbox)
Provides: texmf(latex/kvoptions)
Provides: texmf(latex/logreq)
Provides: texmf(latex/pdftexcmds)
Provides: texmf(latex/everypage)
Provides: texmf(latex/tex4ht)
Provides: texmf(latex/tipa)
Provides: texmf(latex/tone)
#endif


%description -n texlive-dist
This package brings the main TeX Live distribution packages (fonts and
TeX-related libraries) that are missing from the texlive-basic package.

%files		-n texlive-dist
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
%{texmfdistdir}/fonts/source/*
%{texmfdistdir}/fonts/tfm/*
%{texmfdistdir}/fonts/truetype/*
%{texmfdistdir}/fonts/type1/*
%{texmfdistdir}/fonts/vf/*
%{texmfdistdir}/tex/*

# collection-basic
%exclude %{texmfdistdir}/fonts/afm/adobe/avantgar
%exclude %{texmfdistdir}/fonts/afm/adobe/bookman
%exclude %{texmfdistdir}/fonts/afm/adobe/courier
%exclude %{texmfdistdir}/fonts/afm/adobe/helvetic
%exclude %{texmfdistdir}/fonts/afm/adobe/ncntrsbk
%exclude %{texmfdistdir}/fonts/afm/adobe/palatino
%exclude %{texmfdistdir}/fonts/afm/adobe/symbol
%exclude %{texmfdistdir}/fonts/afm/adobe/times
%exclude %{texmfdistdir}/fonts/afm/adobe/utopia
%exclude %{texmfdistdir}/fonts/afm/adobe/zapfchan
%exclude %{texmfdistdir}/fonts/afm/adobe/zapfding
%exclude %{texmfdistdir}/fonts/afm/bitstrea/charter
%exclude %{texmfdistdir}/fonts/afm/public/amsfonts
%exclude %{texmfdistdir}/fonts/afm/public/cm-super
%exclude %{texmfdistdir}/fonts/afm/public/fpl
%exclude %{texmfdistdir}/fonts/afm/public/lm
%exclude %{texmfdistdir}/fonts/afm/public/marvosym
%exclude %{texmfdistdir}/fonts/afm/public/mathpazo
%exclude %{texmfdistdir}/fonts/afm/public/pxfonts
%exclude %{texmfdistdir}/fonts/afm/public/rsfs
%exclude %{texmfdistdir}/fonts/afm/public/tex-gyre
%exclude %{texmfdistdir}/fonts/afm/public/txfonts
%exclude %{texmfdistdir}/fonts/afm/urw/avantgar
%exclude %{texmfdistdir}/fonts/afm/urw/bookman
%exclude %{texmfdistdir}/fonts/afm/urw/courier
%exclude %{texmfdistdir}/fonts/afm/urw/helvetic
%exclude %{texmfdistdir}/fonts/afm/urw/ncntrsbk
%exclude %{texmfdistdir}/fonts/afm/urw/palatino
%exclude %{texmfdistdir}/fonts/afm/urw/symbol
%exclude %{texmfdistdir}/fonts/afm/urw/times
%exclude %{texmfdistdir}/fonts/afm/urw/zapfchan
%exclude %{texmfdistdir}/fonts/afm/urw/zapfding
%exclude %{texmfdistdir}/fonts/enc/dvips/base
%exclude %{texmfdistdir}/fonts/enc/dvips/cm-super
%exclude %{texmfdistdir}/fonts/enc/dvips/lm
%exclude %{texmfdistdir}/fonts/enc/dvips/tex-gyre
%exclude %{texmfdistdir}/fonts/enc/dvips/tetex
%exclude %{texmfdistdir}/fonts/enc/dvips/txfonts
%exclude %{texmfdistdir}/fonts/lig/afm2pl
%exclude %{texmfdistdir}/fonts/map/dvipdfmx
%exclude %{texmfdistdir}/fonts/map/dvips/amsfonts
%exclude %{texmfdistdir}/fonts/map/dvips/avantgar
%exclude %{texmfdistdir}/fonts/map/dvips/bookman
%exclude %{texmfdistdir}/fonts/map/dvips/cm
%exclude %{texmfdistdir}/fonts/map/dvips/cm-super
%exclude %{texmfdistdir}/fonts/map/dvips/courier
%exclude %{texmfdistdir}/fonts/map/dvips/eurosym
%exclude %{texmfdistdir}/fonts/map/dvips/helvetic
%exclude %{texmfdistdir}/fonts/map/dvips/lm
%exclude %{texmfdistdir}/fonts/map/dvips/marvosym
%exclude %{texmfdistdir}/fonts/map/dvips/ncntrsbk
%exclude %{texmfdistdir}/fonts/map/dvips/palatino
%exclude %{texmfdistdir}/fonts/map/dvips/pslatex
%exclude %{texmfdistdir}/fonts/map/dvips/psnfss
%exclude %{texmfdistdir}/fonts/map/dvips/pxfonts
%exclude %{texmfdistdir}/fonts/map/dvips/rsfs
%exclude %{texmfdistdir}/fonts/map/dvips/symbol
%exclude %{texmfdistdir}/fonts/map/dvips/tex-gyre
%exclude %{texmfdistdir}/fonts/map/dvips/tetex
%exclude %{texmfdistdir}/fonts/map/dvips/times
%exclude %{texmfdistdir}/fonts/map/dvips/tipa
%exclude %{texmfdistdir}/fonts/map/dvips/txfonts
%exclude %{texmfdistdir}/fonts/map/dvips/zapfchan
%exclude %{texmfdistdir}/fonts/map/dvips/zapfding
%exclude %{texmfdistdir}/fonts/map/glyphlist
%exclude %{texmfdistdir}/fonts/map/pdftex
%exclude %{texmfdistdir}/fonts/map/vtex/cm-super
%exclude %{texmfdistdir}/fonts/opentype/public/lm
%exclude %{texmfdistdir}/fonts/opentype/public/tex-gyre
%exclude %{texmfdistdir}/fonts/opentype/public/tex-gyre-math
%exclude %{texmfdistdir}/fonts/pk/ljfour/public/cm
%exclude %{texmfdistdir}/fonts/source/jknappen/ec
%exclude %{texmfdistdir}/fonts/source/public/amsfonts
%exclude %{texmfdistdir}/fonts/source/public/cm
%exclude %{texmfdistdir}/fonts/source/public/cmextra
%exclude %{texmfdistdir}/fonts/source/public/eurosym
%exclude %{texmfdistdir}/fonts/source/public/latex-fonts
%exclude %{texmfdistdir}/fonts/source/public/mflogo
%exclude %{texmfdistdir}/fonts/source/public/rsfs
%exclude %{texmfdistdir}/fonts/source/public/tipa
%exclude %{texmfdistdir}/fonts/tfm/adobe/avantgar
%exclude %{texmfdistdir}/fonts/tfm/adobe/bookman
%exclude %{texmfdistdir}/fonts/tfm/adobe/courier
%exclude %{texmfdistdir}/fonts/tfm/adobe/helvetic
%exclude %{texmfdistdir}/fonts/tfm/adobe/ncntrsbk
%exclude %{texmfdistdir}/fonts/tfm/adobe/palatino
%exclude %{texmfdistdir}/fonts/tfm/adobe/symbol
%exclude %{texmfdistdir}/fonts/tfm/adobe/times
%exclude %{texmfdistdir}/fonts/tfm/adobe/zapfchan
%exclude %{texmfdistdir}/fonts/tfm/adobe/zapfding
%exclude %{texmfdistdir}/fonts/tfm/bitstrea/charter
%exclude %{texmfdistdir}/fonts/tfm/jknappen/ec
%exclude %{texmfdistdir}/fonts/tfm/monotype/helvetic
%exclude %{texmfdistdir}/fonts/tfm/monotype/symbol
%exclude %{texmfdistdir}/fonts/tfm/public/ae
%exclude %{texmfdistdir}/fonts/tfm/public/amsfonts
%exclude %{texmfdistdir}/fonts/tfm/public/cm
%exclude %{texmfdistdir}/fonts/tfm/public/cmextra
%exclude %{texmfdistdir}/fonts/tfm/public/eurosym
%exclude %{texmfdistdir}/fonts/tfm/public/latex-fonts
%exclude %{texmfdistdir}/fonts/tfm/public/lm
%exclude %{texmfdistdir}/fonts/tfm/public/marvosym
%exclude %{texmfdistdir}/fonts/tfm/public/mathpazo
%exclude %{texmfdistdir}/fonts/tfm/public/mflogo
%exclude %{texmfdistdir}/fonts/tfm/public/pslatex
%exclude %{texmfdistdir}/fonts/tfm/public/pxfonts
%exclude %{texmfdistdir}/fonts/tfm/public/rsfs
%exclude %{texmfdistdir}/fonts/tfm/public/tex-gyre
%exclude %{texmfdistdir}/fonts/tfm/public/tipa
%exclude %{texmfdistdir}/fonts/tfm/public/txfonts
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/avantgar
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/bookman
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/courier
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/helvetic
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/ncntrsbk
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/palatino
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/symbol
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/times
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/zapfchan
%exclude %{texmfdistdir}/fonts/tfm/urw35vf/zapfding
%exclude %{texmfdistdir}/fonts/truetype/public/marvosym
%exclude %{texmfdistdir}/fonts/type1/adobe/courier
%exclude %{texmfdistdir}/fonts/type1/adobe/utopia
%exclude %{texmfdistdir}/fonts/type1/bitstrea/charter
%exclude %{texmfdistdir}/fonts/type1/public/amsfonts
%exclude %{texmfdistdir}/fonts/type1/public/cm-super
%exclude %{texmfdistdir}/fonts/type1/public/eurosym
%exclude %{texmfdistdir}/fonts/type1/public/fpl
%exclude %{texmfdistdir}/fonts/type1/public/lm
%exclude %{texmfdistdir}/fonts/type1/public/marvosym
%exclude %{texmfdistdir}/fonts/type1/public/mathpazo
%exclude %{texmfdistdir}/fonts/type1/public/pxfonts
%exclude %{texmfdistdir}/fonts/type1/public/rsfs
%exclude %{texmfdistdir}/fonts/type1/public/tex-gyre
%exclude %{texmfdistdir}/fonts/type1/public/tipa
%exclude %{texmfdistdir}/fonts/type1/public/txfonts
%exclude %{texmfdistdir}/fonts/type1/urw/avantgar
%exclude %{texmfdistdir}/fonts/type1/urw/bookman
%exclude %{texmfdistdir}/fonts/type1/urw/courier
%exclude %{texmfdistdir}/fonts/type1/urw/helvetic
%exclude %{texmfdistdir}/fonts/type1/urw/ncntrsbk
%exclude %{texmfdistdir}/fonts/type1/urw/palatino
%exclude %{texmfdistdir}/fonts/type1/urw/symbol
%exclude %{texmfdistdir}/fonts/type1/urw/times
%exclude %{texmfdistdir}/fonts/type1/urw/zapfchan
%exclude %{texmfdistdir}/fonts/type1/urw/zapfding
%exclude %{texmfdistdir}/fonts/vf/adobe/avantgar
%exclude %{texmfdistdir}/fonts/vf/adobe/bookman
%exclude %{texmfdistdir}/fonts/vf/adobe/courier
%exclude %{texmfdistdir}/fonts/vf/adobe/helvetic
%exclude %{texmfdistdir}/fonts/vf/adobe/ncntrsbk
%exclude %{texmfdistdir}/fonts/vf/adobe/palatino
%exclude %{texmfdistdir}/fonts/vf/adobe/times
%exclude %{texmfdistdir}/fonts/vf/adobe/utopia
%exclude %{texmfdistdir}/fonts/vf/adobe/zapfchan
%exclude %{texmfdistdir}/fonts/vf/bitstrea/charter
%exclude %{texmfdistdir}/fonts/vf/monotype/helvetic
%exclude %{texmfdistdir}/fonts/vf/public/ae
%exclude %{texmfdistdir}/fonts/vf/public/mathpazo
%exclude %{texmfdistdir}/fonts/vf/public/pslatex
%exclude %{texmfdistdir}/fonts/vf/public/pxfonts
%exclude %{texmfdistdir}/fonts/vf/public/txfonts
%exclude %{texmfdistdir}/fonts/vf/urw35vf/avantgar
%exclude %{texmfdistdir}/fonts/vf/urw35vf/bookman
%exclude %{texmfdistdir}/fonts/vf/urw35vf/courier
%exclude %{texmfdistdir}/fonts/vf/urw35vf/helvetic
%exclude %{texmfdistdir}/fonts/vf/urw35vf/ncntrsbk
%exclude %{texmfdistdir}/fonts/vf/urw35vf/palatino
%exclude %{texmfdistdir}/fonts/vf/urw35vf/times
%exclude %{texmfdistdir}/fonts/vf/urw35vf/zapfchan
%exclude %{texmfdistdir}/tex/generic/babel
%exclude %{texmfdistdir}/tex/generic/config
%exclude %{texmfdistdir}/tex/generic/dvips
%exclude %{texmfdistdir}/tex/generic/enctex
%exclude %{texmfdistdir}/tex/generic/hyphen
%exclude %{texmfdistdir}/tex/generic/ifxetex
%exclude %{texmfdistdir}/tex/generic/oberdiek
%exclude %{texmfdistdir}/tex/generic/oberdiek/ifluatex.sty
%exclude %{texmfdistdir}/tex/generic/pdftex
%exclude %{texmfdistdir}/tex/generic/pgf
%exclude %{texmfdistdir}/tex/generic/pst-blur
%exclude %{texmfdistdir}/tex/generic/pst-grad
%exclude %{texmfdistdir}/tex/generic/pst-slpe
%exclude %{texmfdistdir}/tex/generic/pst-text
%exclude %{texmfdistdir}/tex/generic/pstricks
%exclude %{texmfdistdir}/tex/generic/tex-ini-files
%exclude %{texmfdistdir}/tex/generic/thumbpdf
%exclude %{texmfdistdir}/tex/generic/xkeyval
%exclude %{texmfdistdir}/tex/latex/ae
%exclude %{texmfdistdir}/tex/latex/algorithms
%exclude %{texmfdistdir}/tex/latex/amscls
%exclude %{texmfdistdir}/tex/latex/amsfonts
%exclude %{texmfdistdir}/tex/latex/amsmath
%exclude %{texmfdistdir}/tex/latex/anysize
%exclude %{texmfdistdir}/tex/latex/avantgar
%exclude %{texmfdistdir}/tex/latex/babelbib
%exclude %{texmfdistdir}/tex/latex/base
%exclude %{texmfdistdir}/tex/latex/beamer
%exclude %{texmfdistdir}/tex/latex/beton
%exclude %{texmfdistdir}/tex/latex/bookman
%exclude %{texmfdistdir}/tex/latex/booktabs
%exclude %{texmfdistdir}/tex/latex/caption
%exclude %{texmfdistdir}/tex/latex/carlisle
%exclude %{texmfdistdir}/tex/latex/cite
%exclude %{texmfdistdir}/tex/latex/cm-super
%exclude %{texmfdistdir}/tex/latex/cmap
%exclude %{texmfdistdir}/tex/latex/colortbl
%exclude %{texmfdistdir}/tex/latex/courier
%exclude %{texmfdistdir}/tex/latex/cprotect
%exclude %{texmfdistdir}/tex/latex/crop
%exclude %{texmfdistdir}/tex/latex/csquotes
%exclude %{texmfdistdir}/tex/latex/ctable
%exclude %{texmfdistdir}/tex/latex/enumitem
%exclude %{texmfdistdir}/tex/latex/eso-pic
%exclude %{texmfdistdir}/tex/latex/etex-pkg
%exclude %{texmfdistdir}/tex/latex/etoolbox
%exclude %{texmfdistdir}/tex/latex/euler
%exclude %{texmfdistdir}/tex/latex/euro
%exclude %{texmfdistdir}/tex/latex/eurosym
%exclude %{texmfdistdir}/tex/latex/extsizes
%exclude %{texmfdistdir}/tex/latex/fancybox
%exclude %{texmfdistdir}/tex/latex/fancyhdr
%exclude %{texmfdistdir}/tex/latex/fancyref
%exclude %{texmfdistdir}/tex/latex/fancyvrb
%exclude %{texmfdistdir}/tex/latex/fix2col
%exclude %{texmfdistdir}/tex/latex/float
%exclude %{texmfdistdir}/tex/latex/fontspec
%exclude %{texmfdistdir}/tex/latex/footmisc
%exclude %{texmfdistdir}/tex/latex/fp
%exclude %{texmfdistdir}/tex/latex/geometry
%exclude %{texmfdistdir}/tex/latex/graphics
%exclude %{texmfdistdir}/tex/latex/graphics-cfg
%exclude %{texmfdistdir}/tex/latex/helvetic
%exclude %{texmfdistdir}/tex/latex/hyperref
%exclude %{texmfdistdir}/tex/latex/index
%exclude %{texmfdistdir}/tex/latex/jknapltx
%exclude %{texmfdistdir}/tex/latex/koma-script
%exclude %{texmfdistdir}/tex/latex/l3kernel
%exclude %{texmfdistdir}/tex/latex/l3packages
%exclude %{texmfdistdir}/tex/latex/latexconfig
%exclude %{texmfdistdir}/tex/latex/listings
%exclude %{texmfdistdir}/tex/latex/lm
%exclude %{texmfdistdir}/tex/latex/ltxmisc
%exclude %{texmfdistdir}/tex/latex/marginnote
%exclude %{texmfdistdir}/tex/latex/marvosym
%exclude %{texmfdistdir}/tex/latex/mdwtools
%exclude %{texmfdistdir}/tex/latex/memoir
%exclude %{texmfdistdir}/tex/latex/metalogo
%exclude %{texmfdistdir}/tex/latex/mflogo
%exclude %{texmfdistdir}/tex/latex/mfnfss
%exclude %{texmfdistdir}/tex/latex/microtype
%exclude %{texmfdistdir}/tex/latex/minitoc
%exclude %{texmfdistdir}/tex/latex/mparhack
%exclude %{texmfdistdir}/tex/latex/ms
%exclude %{texmfdistdir}/tex/latex/natbib
%exclude %{texmfdistdir}/tex/latex/ncntrsbk
%exclude %{texmfdistdir}/tex/latex/ntgclass
%exclude %{texmfdistdir}/tex/latex/oberdiek
%exclude %{texmfdistdir}/tex/latex/palatino
%exclude %{texmfdistdir}/tex/latex/parallel
%exclude %{texmfdistdir}/tex/latex/parskip
%exclude %{texmfdistdir}/tex/latex/pdfpages
%exclude %{texmfdistdir}/tex/latex/pgf
%exclude %{texmfdistdir}/tex/latex/powerdot
%exclude %{texmfdistdir}/tex/latex/psfrag
%exclude %{texmfdistdir}/tex/latex/pslatex
%exclude %{texmfdistdir}/tex/latex/psnfss
%exclude %{texmfdistdir}/tex/latex/pspicture
%exclude %{texmfdistdir}/tex/latex/pst-blur
%exclude %{texmfdistdir}/tex/latex/pst-grad
%exclude %{texmfdistdir}/tex/latex/pst-slpe
%exclude %{texmfdistdir}/tex/latex/pst-text
%exclude %{texmfdistdir}/tex/latex/pstricks
%exclude %{texmfdistdir}/tex/latex/pxfonts
%exclude %{texmfdistdir}/tex/latex/qstest
%exclude %{texmfdistdir}/tex/latex/rcs
%exclude %{texmfdistdir}/tex/latex/sansmath
%exclude %{texmfdistdir}/tex/latex/sauerj
%exclude %{texmfdistdir}/tex/latex/section
%exclude %{texmfdistdir}/tex/latex/seminar
%exclude %{texmfdistdir}/tex/latex/sepnum
%exclude %{texmfdistdir}/tex/latex/setspace
%exclude %{texmfdistdir}/tex/latex/soul
%exclude %{texmfdistdir}/tex/latex/subfig
%exclude %{texmfdistdir}/tex/latex/symbol
%exclude %{texmfdistdir}/tex/latex/tex-gyre
%exclude %{texmfdistdir}/tex/latex/textcase
%exclude %{texmfdistdir}/tex/latex/times
%exclude %{texmfdistdir}/tex/latex/tipa
%exclude %{texmfdistdir}/tex/latex/tools
%exclude %{texmfdistdir}/tex/latex/txfonts
%exclude %{texmfdistdir}/tex/latex/type1cm
%exclude %{texmfdistdir}/tex/latex/typehtml
%exclude %{texmfdistdir}/tex/latex/underscore
%exclude %{texmfdistdir}/tex/latex/unicode-math
%exclude %{texmfdistdir}/tex/latex/url
%exclude %{texmfdistdir}/tex/latex/wasysym
%exclude %{texmfdistdir}/tex/latex/xcolor
%exclude %{texmfdistdir}/tex/latex/xkeyval
%exclude %{texmfdistdir}/tex/latex/zapfchan
%exclude %{texmfdistdir}/tex/latex/zapfding
%exclude %{texmfdistdir}/tex/luatex/luaotfload
%exclude %{texmfdistdir}/tex/luatex/luatexbase
%exclude %{texmfdistdir}/tex/plain/amsfonts
%exclude %{texmfdistdir}/tex/plain/base
%exclude %{texmfdistdir}/tex/plain/config
%exclude %{texmfdistdir}/tex/plain/etex
%exclude %{texmfdistdir}/tex/plain/fp
%exclude %{texmfdistdir}/tex/plain/pgf
%exclude %{texmfdistdir}/tex/plain/rsfs
%exclude %{texmfdistdir}/tex/xelatex/xunicode

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
%exclude %{texmfdistdir}/fonts/source/public/xypic
%exclude %{texmfdistdir}/fonts/tfm/public/xypic
%exclude %{texmfdistdir}/fonts/type1/public/xypic
%exclude %{texmfdistdir}/tex/generic/xypic
# comment
%exclude %{texmfdistdir}/tex/latex/comment
# preprint
%exclude %{texmfdistdir}/tex/latex/preprint

# hyph-utf8, ruhyphen, dehypht, xecyr, ukrhyph, omegahyph
%exclude %{texmfdistdir}/tex/generic/hyph-utf8
%exclude %{texmfdistdir}/tex/generic/ruhyphen
%exclude %{texmfdistdir}/tex/generic/dehyph-exptl
%exclude %{texmfdistdir}/tex/generic/xecyr
%exclude %{texmfdistdir}/tex/generic/ukrhyph
%exclude %{texmfdistdir}/tex/generic/omegahyph

# xetexconfig
%exclude %{texmfdistdir}/tex/xelatex/xetexconfig

# collection-fontsextra
# allrunes
%exclude %{texmfdistdir}/fonts/map/dvips/allrunes
%exclude %{texmfdistdir}/fonts/source/public/allrunes
%exclude %{texmfdistdir}/fonts/type1/public/allrunes
%exclude %{texmfdistdir}/tex/latex/allrunes
# antiqua
%exclude %{texmfdistdir}/fonts/afm/urw/antiqua
%exclude %{texmfdistdir}/fonts/map/dvips/antiqua
%exclude %{texmfdistdir}/fonts/tfm/urw/antiqua
%exclude %{texmfdistdir}/fonts/type1/urw/antiqua
%exclude %{texmfdistdir}/fonts/vf/urw/antiqua
%exclude %{texmfdistdir}/tex/latex/antiqua
# antt
%exclude %{texmfdistdir}/fonts/afm/public/antt
%exclude %{texmfdistdir}/fonts/enc/dvips/antt
%exclude %{texmfdistdir}/fonts/map/dvips/antt
%exclude %{texmfdistdir}/fonts/opentype/public/antt
%exclude %{texmfdistdir}/fonts/tfm/public/antt
%exclude %{texmfdistdir}/fonts/type1/public/antt
%exclude %{texmfdistdir}/tex/latex/antt
%exclude %{texmfdistdir}/tex/plain/antt
# archaic
%exclude %{texmfdistdir}/fonts/afm/public/archaic
%exclude %{texmfdistdir}/fonts/map/dvips/archaic
%exclude %{texmfdistdir}/fonts/source/public/archaic
%exclude %{texmfdistdir}/fonts/tfm/public/archaic
%exclude %{texmfdistdir}/fonts/type1/public/archaic
%exclude %{texmfdistdir}/tex/latex/archaic
# arev
%exclude %{texmfdistdir}/fonts/afm/public/arev
%exclude %{texmfdistdir}/fonts/enc/dvips/arev
%exclude %{texmfdistdir}/fonts/map/dvips/arev
%exclude %{texmfdistdir}/fonts/tfm/public/arev
%exclude %{texmfdistdir}/fonts/type1/public/arev
%exclude %{texmfdistdir}/fonts/vf/public/arev
%exclude %{texmfdistdir}/tex/latex/arev
# astro
%exclude %{texmfdistdir}/fonts/source/public/astro
%exclude %{texmfdistdir}/fonts/tfm/public/astro
# augie
%exclude %{texmfdistdir}/fonts/afm/public/augie
%exclude %{texmfdistdir}/fonts/map/dvips/augie
%exclude %{texmfdistdir}/fonts/tfm/public/augie
%exclude %{texmfdistdir}/fonts/type1/public/augie
%exclude %{texmfdistdir}/fonts/vf/public/augie
%exclude %{texmfdistdir}/tex/latex/augie
# auncial-new
%exclude %{texmfdistdir}/fonts/afm/public/auncial-new
%exclude %{texmfdistdir}/fonts/map/dvips/auncial-new
%exclude %{texmfdistdir}/fonts/tfm/public/auncial-new
%exclude %{texmfdistdir}/fonts/type1/public/auncial-new
%exclude %{texmfdistdir}/tex/latex/auncial-new
# aurical
%exclude %{texmfdistdir}/fonts/afm/public/aurical
%exclude %{texmfdistdir}/fonts/map/dvips/aurical
%exclude %{texmfdistdir}/fonts/source/public/aurical
%exclude %{texmfdistdir}/fonts/tfm/public/aurical
%exclude %{texmfdistdir}/fonts/type1/public/aurical
%exclude %{texmfdistdir}/tex/latex/aurical
# barcodes
%exclude %{texmfdistdir}/fonts/source/public/barcodes
%exclude %{texmfdistdir}/fonts/tfm/public/barcodes
%exclude %{texmfdistdir}/tex/latex/barcodes
# baskervald
%exclude %{texmfdistdir}/fonts/afm/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/enc/dvips/baskervald
%exclude %{texmfdistdir}/fonts/map/dvips/baskervald
%exclude %{texmfdistdir}/fonts/tfm/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/type1/arkandis/baskervald
%exclude %{texmfdistdir}/fonts/vf/arkandis/baskervald
%exclude %{texmfdistdir}/tex/latex/baskervald
# bbding
%exclude %{texmfdistdir}/fonts/source/public/bbding
%exclude %{texmfdistdir}/fonts/tfm/public/bbding
%exclude %{texmfdistdir}/tex/latex/bbding
# bbm
%exclude %{texmfdistdir}/fonts/source/public/bbm
%exclude %{texmfdistdir}/fonts/tfm/public/bbm
# bbm-macros
%exclude %{texmfdistdir}/tex/latex/bbm-macros
# bbold
%exclude %{texmfdistdir}/fonts/source/public/bbold
%exclude %{texmfdistdir}/fonts/tfm/public/bbold
%exclude %{texmfdistdir}/tex/latex/bbold
# belleek
%exclude %{texmfdistdir}/fonts/map/dvips/belleek
%exclude %{texmfdistdir}/fonts/truetype/public/belleek
%exclude %{texmfdistdir}/fonts/type1/public/belleek
# bera
%exclude %{texmfdistdir}/fonts/afm/public/bera
%exclude %{texmfdistdir}/fonts/map/dvips/bera
%exclude %{texmfdistdir}/fonts/tfm/public/bera
%exclude %{texmfdistdir}/fonts/type1/public/bera
%exclude %{texmfdistdir}/fonts/vf/public/bera
%exclude %{texmfdistdir}/tex/latex/bera
# blacklettert1
%exclude %{texmfdistdir}/fonts/tfm/public/blacklettert1
%exclude %{texmfdistdir}/fonts/vf/public/blacklettert1
%exclude %{texmfdistdir}/tex/latex/blacklettert1
# boisik
%exclude %{texmfdistdir}/fonts/source/public/boisik
%exclude %{texmfdistdir}/fonts/tfm/public/boisik
%exclude %{texmfdistdir}/tex/latex/boisik
# bookhands
%exclude %{texmfdistdir}/fonts/afm/public/bookhands
%exclude %{texmfdistdir}/fonts/map/dvips/bookhands
%exclude %{texmfdistdir}/fonts/source/public/bookhands
%exclude %{texmfdistdir}/fonts/tfm/public/bookhands
%exclude %{texmfdistdir}/fonts/type1/public/bookhands
%exclude %{texmfdistdir}/tex/latex/bookhands
# boondox
%exclude %{texmfdistdir}/fonts/map/dvips/boondox
%exclude %{texmfdistdir}/fonts/tfm/public/boondox
%exclude %{texmfdistdir}/fonts/type1/public/boondox
%exclude %{texmfdistdir}/fonts/vf/public/boondox
%exclude %{texmfdistdir}/tex/latex/boondox
# braille
%exclude %{texmfdistdir}/tex/latex/braille
# brushscr
%exclude %{texmfdistdir}/dvips/brushscr
%exclude %{texmfdistdir}/fonts/afm/public/brushscr
%exclude %{texmfdistdir}/fonts/map/dvips/brushscr
%exclude %{texmfdistdir}/fonts/tfm/public/brushscr
%exclude %{texmfdistdir}/fonts/type1/public/brushscr
%exclude %{texmfdistdir}/fonts/vf/public/brushscr
%exclude %{texmfdistdir}/tex/latex/brushscr
# calligra
%exclude %{texmfdistdir}/fonts/source/public/calligra
%exclude %{texmfdistdir}/fonts/tfm/public/calligra
# cantarell
%exclude %{texmfdistdir}/fonts/afm/public/cantarell
%exclude %{texmfdistdir}/fonts/enc/dvips/cantarell
%exclude %{texmfdistdir}/fonts/map/dvips/cantarell
%exclude %{texmfdistdir}/fonts/tfm/public/cantarell
%exclude %{texmfdistdir}/fonts/type1/public/cantarell
%exclude %{texmfdistdir}/fonts/vf/public/cantarell
%exclude %{texmfdistdir}/tex/latex/cantarell
# carolmin-ps
%exclude %{texmfdistdir}/fonts/afm/public/carolmin-ps
%exclude %{texmfdistdir}/fonts/map/dvips/carolmin-ps
%exclude %{texmfdistdir}/fonts/type1/public/carolmin-ps
# ccicons
%exclude %{texmfdistdir}/fonts/enc/dvips/ccicons
%exclude %{texmfdistdir}/fonts/map/dvips/ccicons
%exclude %{texmfdistdir}/fonts/tfm/public/ccicons
%exclude %{texmfdistdir}/fonts/type1/public/ccicons
%exclude %{texmfdistdir}/tex/latex/ccicons
# cfr-lm
%exclude %{texmfdistdir}/fonts/enc/dvips/cfr-lm
%exclude %{texmfdistdir}/fonts/map/dvips/cfr-lm
%exclude %{texmfdistdir}/fonts/tfm/public/cfr-lm
%exclude %{texmfdistdir}/fonts/vf/public/cfr-lm
%exclude %{texmfdistdir}/tex/latex/cfr-lm
# cherokee
%exclude %{texmfdistdir}/fonts/source/public/cherokee
%exclude %{texmfdistdir}/fonts/tfm/public/cherokee
%exclude %{texmfdistdir}/tex/latex/cherokee
# cm-lgc
%exclude %{texmfdistdir}/fonts/afm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/enc/dvips/cm-lgc
%exclude %{texmfdistdir}/fonts/map/dvips/cm-lgc
%exclude %{texmfdistdir}/fonts/ofm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/ovf/public/cm-lgc
%exclude %{texmfdistdir}/fonts/tfm/public/cm-lgc
%exclude %{texmfdistdir}/fonts/type1/public/cm-lgc
%exclude %{texmfdistdir}/fonts/vf/public/cm-lgc
%exclude %{texmfdistdir}/tex/latex/cm-lgc
# cm-unicode
%exclude %{texmfdistdir}/fonts/afm/public/cm-unicode
%exclude %{texmfdistdir}/fonts/enc/dvips/cm-unicode
%exclude %{texmfdistdir}/fonts/map/dvips/cm-unicode
%exclude %{texmfdistdir}/fonts/opentype/public/cm-unicode
%exclude %{texmfdistdir}/fonts/type1/public/cm-unicode
# cmbright
%exclude %{texmfdistdir}/fonts/source/public/cmbright
%exclude %{texmfdistdir}/fonts/tfm/public/cmbright
%exclude %{texmfdistdir}/tex/latex/cmbright
# cmll
%exclude %{texmfdistdir}/fonts/map/dvips/cmll
%exclude %{texmfdistdir}/fonts/source/public/cmll
%exclude %{texmfdistdir}/fonts/tfm/public/cmll
%exclude %{texmfdistdir}/fonts/type1/public/cmll
%exclude %{texmfdistdir}/tex/latex/cmll
# cmpica
%exclude %{texmfdistdir}/fonts/source/public/cmpica
%exclude %{texmfdistdir}/fonts/tfm/public/cmpica
# collection-basic
%exclude %{texmfdistdir}/tex/latex/collref
# concmath-fonts
%exclude %{texmfdistdir}/fonts/source/public/concmath-fonts
%exclude %{texmfdistdir}/fonts/tfm/public/concmath-fonts
# courier-scaled
%exclude %{texmfdistdir}/tex/latex/courier-scaled
# cryst
%exclude %{texmfdistdir}/fonts/afm/public/cryst
%exclude %{texmfdistdir}/fonts/source/public/cryst
%exclude %{texmfdistdir}/fonts/tfm/public/cryst
%exclude %{texmfdistdir}/fonts/type1/public/cryst
# cyklop
%exclude %{texmfdistdir}/fonts/afm/public/cyklop
%exclude %{texmfdistdir}/fonts/enc/dvips/cyklop
%exclude %{texmfdistdir}/fonts/map/dvips/cyklop
%exclude %{texmfdistdir}/fonts/opentype/public/cyklop
%exclude %{texmfdistdir}/fonts/tfm/public/cyklop
%exclude %{texmfdistdir}/fonts/type1/public/cyklop
%exclude %{texmfdistdir}/tex/latex/cyklop
# dancers
%exclude %{texmfdistdir}/fonts/source/public/dancers
%exclude %{texmfdistdir}/fonts/tfm/public/dancers
# dice
%exclude %{texmfdistdir}/fonts/source/public/dice
%exclude %{texmfdistdir}/fonts/tfm/public/dice
# dictsym
%exclude %{texmfdistdir}/fonts/afm/public/dictsym
%exclude %{texmfdistdir}/fonts/map/dvips/dictsym
%exclude %{texmfdistdir}/fonts/tfm/public/dictsym
%exclude %{texmfdistdir}/fonts/type1/public/dictsym
%exclude %{texmfdistdir}/tex/latex/dictsym
# dingbat
%exclude %{texmfdistdir}/fonts/source/public/dingbat
%exclude %{texmfdistdir}/fonts/tfm/public/dingbat
%exclude %{texmfdistdir}/tex/latex/dingbat
# doublestroke
%exclude %{texmfdistdir}/fonts/map/dvips/doublestroke
%exclude %{texmfdistdir}/fonts/source/public/doublestroke
%exclude %{texmfdistdir}/fonts/tfm/public/doublestroke
%exclude %{texmfdistdir}/fonts/type1/public/doublestroke
%exclude %{texmfdistdir}/tex/latex/doublestroke
# dozenal
%exclude %{texmfdistdir}/fonts/map/dvips/dozenal
%exclude %{texmfdistdir}/fonts/source/public/dozenal
%exclude %{texmfdistdir}/fonts/tfm/public/dozenal
%exclude %{texmfdistdir}/fonts/type1/public/dozenal
%exclude %{texmfdistdir}/tex/latex/dozenal
# duerer
%exclude %{texmfdistdir}/fonts/source/public/duerer
%exclude %{texmfdistdir}/fonts/tfm/public/duerer
# duerer-latex
%exclude %{texmfdistdir}/tex/latex/duerer-latex
# ean
%exclude %{texmfdistdir}/tex/generic/ean
# ecc
%exclude %{texmfdistdir}/fonts/source/public/ecc
%exclude %{texmfdistdir}/fonts/tfm/public/ecc
# eco
%exclude %{texmfdistdir}/fonts/tfm/public/eco
%exclude %{texmfdistdir}/fonts/vf/public/eco
%exclude %{texmfdistdir}/tex/latex/eco
# eiad
%exclude %{texmfdistdir}/fonts/source/public/eiad
%exclude %{texmfdistdir}/fonts/tfm/public/eiad
%exclude %{texmfdistdir}/tex/latex/eiad
# eiad-ltx
%exclude %{texmfdistdir}/fonts/source/public/eiad-ltx
%exclude %{texmfdistdir}/tex/latex/eiad-ltx
# elvish
%exclude %{texmfdistdir}/fonts/source/public/elvish
%exclude %{texmfdistdir}/fonts/tfm/public/elvish
# epigrafica
%exclude %{texmfdistdir}/fonts/afm/public/epigrafica
%exclude %{texmfdistdir}/fonts/enc/dvips/epigrafica
%exclude %{texmfdistdir}/fonts/map/dvips/epigrafica
%exclude %{texmfdistdir}/fonts/tfm/public/epigrafica
%exclude %{texmfdistdir}/fonts/type1/public/epigrafica
%exclude %{texmfdistdir}/fonts/vf/public/epigrafica
%exclude %{texmfdistdir}/tex/latex/epigrafica
# epsdice
%exclude %{texmfdistdir}/tex/latex/epsdice
# esstix
%exclude %{texmfdistdir}/fonts/afm/esstix
%exclude %{texmfdistdir}/fonts/map/dvips/esstix
%exclude %{texmfdistdir}/fonts/tfm/public/esstix
%exclude %{texmfdistdir}/fonts/type1/public/esstix
%exclude %{texmfdistdir}/fonts/vf/public/esstix
%exclude %{texmfdistdir}/tex/latex/esstix
# esvect
%exclude %{texmfdistdir}/fonts/map/dvips/esvect
%exclude %{texmfdistdir}/fonts/source/public/esvect
%exclude %{texmfdistdir}/fonts/tfm/public/esvect
%exclude %{texmfdistdir}/fonts/type1/public/esvect
%exclude %{texmfdistdir}/tex/latex/esvect
# eulervm
%exclude %{texmfdistdir}/fonts/tfm/public/eulervm
%exclude %{texmfdistdir}/fonts/vf/public/eulervm
%exclude %{texmfdistdir}/tex/latex/eulervm
# euxm
%exclude %{texmfdistdir}/fonts/source/public/euxm
%exclude %{texmfdistdir}/fonts/tfm/public/euxm
# fdsymbol
%exclude %{texmfdistdir}/fonts/enc/dvips/fdsymbol
%exclude %{texmfdistdir}/fonts/map/dvips/fdsymbol
%exclude %{texmfdistdir}/fonts/source/public/fdsymbol
%exclude %{texmfdistdir}/fonts/tfm/public/fdsymbol
%exclude %{texmfdistdir}/fonts/type1/public/fdsymbol
%exclude %{texmfdistdir}/tex/latex/fdsymbol
# feyn
%exclude %{texmfdistdir}/fonts/source/public/feyn
%exclude %{texmfdistdir}/fonts/tfm/public/feyn
%exclude %{texmfdistdir}/tex/latex/feyn
# fge
%exclude %{texmfdistdir}/fonts/map/dvips/fge
%exclude %{texmfdistdir}/fonts/source/public/fge
%exclude %{texmfdistdir}/fonts/tfm/public/fge
%exclude %{texmfdistdir}/fonts/type1/public/fge
%exclude %{texmfdistdir}/tex/latex/fge
# foekfont
%exclude %{texmfdistdir}/fonts/map/dvips/foekfont
%exclude %{texmfdistdir}/fonts/tfm/public/foekfont
%exclude %{texmfdistdir}/fonts/type1/public/foekfont
%exclude %{texmfdistdir}/tex/latex/foekfont
# fonetika
%exclude %{texmfdistdir}/fonts/afm/public/fonetika
%exclude %{texmfdistdir}/fonts/map/dvips/fonetika
%exclude %{texmfdistdir}/fonts/tfm/public/fonetika
%exclude %{texmfdistdir}/fonts/truetype/public/fonetika
%exclude %{texmfdistdir}/fonts/type1/public/fonetika
%exclude %{texmfdistdir}/tex/latex/fonetika
# fourier
%exclude %{texmfdistdir}/fonts/afm/public/fourier
%exclude %{texmfdistdir}/fonts/map/dvips/fourier
%exclude %{texmfdistdir}/fonts/tfm/public/fourier
%exclude %{texmfdistdir}/fonts/type1/public/fourier
%exclude %{texmfdistdir}/fonts/vf/public/fourier
%exclude %{texmfdistdir}/tex/latex/fourier
# fouriernc
%exclude %{texmfdistdir}/fonts/afm/public/fouriernc
%exclude %{texmfdistdir}/fonts/tfm/public/fouriernc
%exclude %{texmfdistdir}/fonts/vf/public/fouriernc
%exclude %{texmfdistdir}/tex/latex/fouriernc
# frcursive
%exclude %{texmfdistdir}/fonts/source/public/frcursive
%exclude %{texmfdistdir}/fonts/tfm/public/frcursive
%exclude %{texmfdistdir}/tex/latex/frcursive
# genealogy
%exclude %{texmfdistdir}/fonts/source/public/genealogy
%exclude %{texmfdistdir}/fonts/tfm/public/genealogy
# gfsartemisia
%exclude %{texmfdistdir}/fonts/afm/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsartemisia
%exclude %{texmfdistdir}/fonts/map/dvips/gfsartemisia
%exclude %{texmfdistdir}/fonts/opentype/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/tfm/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/type1/public/gfsartemisia
%exclude %{texmfdistdir}/fonts/vf/public/gfsartemisia
%exclude %{texmfdistdir}/tex/latex/gfsartemisia
# gfsbodoni
%exclude %{texmfdistdir}/fonts/afm/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsbodoni
%exclude %{texmfdistdir}/fonts/map/dvips/gfsbodoni
%exclude %{texmfdistdir}/fonts/opentype/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/tfm/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/type1/public/gfsbodoni
%exclude %{texmfdistdir}/fonts/vf/public/gfsbodoni
%exclude %{texmfdistdir}/tex/latex/gfsbodoni
# gfscomplutum
%exclude %{texmfdistdir}/fonts/afm/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/enc/dvips/gfscomplutum
%exclude %{texmfdistdir}/fonts/map/dvips/gfscomplutum
%exclude %{texmfdistdir}/fonts/opentype/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/tfm/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/type1/public/gfscomplutum
%exclude %{texmfdistdir}/fonts/vf/public/gfscomplutum
%exclude %{texmfdistdir}/tex/latex/gfscomplutum
# gfsdidot
%exclude %{texmfdistdir}/fonts/afm/public/gfsdidot
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsdidot
%exclude %{texmfdistdir}/fonts/map/dvips/gfsdidot
%exclude %{texmfdistdir}/fonts/opentype/public/gfsdidot
%exclude %{texmfdistdir}/fonts/tfm/public/gfsdidot
%exclude %{texmfdistdir}/fonts/type1/public/gfsdidot
%exclude %{texmfdistdir}/fonts/vf/public/gfsdidot
%exclude %{texmfdistdir}/tex/latex/gfsdidot
# gfsneohellenic
%exclude %{texmfdistdir}/fonts/afm/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/enc/dvips/gfsneohellenic
%exclude %{texmfdistdir}/fonts/map/dvips/gfsneohellenic
%exclude %{texmfdistdir}/fonts/opentype/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/tfm/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/type1/public/gfsneohellenic
%exclude %{texmfdistdir}/fonts/vf/public/gfsneohellenic
%exclude %{texmfdistdir}/tex/latex/gfsneohellenic
# gfssolomos
%exclude %{texmfdistdir}/fonts/afm/public/gfssolomos
%exclude %{texmfdistdir}/fonts/enc/dvips/gfssolomos
%exclude %{texmfdistdir}/fonts/map/dvips/gfssolomos
%exclude %{texmfdistdir}/fonts/opentype/public/gfssolomos
%exclude %{texmfdistdir}/fonts/tfm/public/gfssolomos
%exclude %{texmfdistdir}/fonts/type1/public/gfssolomos
%exclude %{texmfdistdir}/fonts/vf/public/gfssolomos
%exclude %{texmfdistdir}/tex/latex/gfssolomos
# gnu-freefont
%exclude %{texmfdistdir}/fonts/opentype/public/gnu-freefont
%exclude %{texmfdistdir}/fonts/truetype/public/gnu-freefont
# greenpoint
%exclude %{texmfdistdir}/fonts/source/public/greenpoint
%exclude %{texmfdistdir}/fonts/tfm/public/greenpoint
# grotesq
%exclude %{texmfdistdir}/fonts/afm/urw/grotesq
%exclude %{texmfdistdir}/fonts/map/dvips/grotesq
%exclude %{texmfdistdir}/fonts/tfm/urw/grotesq
%exclude %{texmfdistdir}/fonts/type1/urw/grotesq
%exclude %{texmfdistdir}/fonts/vf/urw/grotesq
%exclude %{texmfdistdir}/tex/latex/grotesq
# hands
%exclude %{texmfdistdir}/fonts/source/public/hands
%exclude %{texmfdistdir}/fonts/tfm/public/hands
# hfbright
%exclude %{texmfdistdir}/fonts/afm/public/hfbright
%exclude %{texmfdistdir}/fonts/enc/dvips/hfbright
%exclude %{texmfdistdir}/fonts/map/dvips/hfbright
%exclude %{texmfdistdir}/fonts/type1/public/hfbright
# hfoldsty
%exclude %{texmfdistdir}/fonts/tfm/public/hfoldsty
%exclude %{texmfdistdir}/fonts/vf/public/hfoldsty
%exclude %{texmfdistdir}/tex/latex/hfoldsty
# ifsym
%exclude %{texmfdistdir}/fonts/source/public/ifsym
%exclude %{texmfdistdir}/fonts/tfm/public/ifsym
%exclude %{texmfdistdir}/tex/latex/ifsym
# inconsolata
%exclude %{texmfdistdir}/fonts/enc/dvips/inconsolata
%exclude %{texmfdistdir}/fonts/map/dvips/inconsolata
%exclude %{texmfdistdir}/fonts/opentype/public/inconsolata
%exclude %{texmfdistdir}/fonts/tfm/public/inconsolata
%exclude %{texmfdistdir}/fonts/type1/public/inconsolata
%exclude %{texmfdistdir}/tex/latex/inconsolata
# initials
%exclude %{texmfdistdir}/dvips/initials
%exclude %{texmfdistdir}/fonts/afm/public/initials
%exclude %{texmfdistdir}/fonts/map/dvips/initials
%exclude %{texmfdistdir}/fonts/tfm/public/initials
%exclude %{texmfdistdir}/fonts/type1/public/initials
%exclude %{texmfdistdir}/tex/latex/initials
# jablantile
%exclude %{texmfdistdir}/fonts/source/public/jablantile
# junicode
%exclude %{texmfdistdir}/fonts/truetype/public/junicode
# kixfont
%exclude %{texmfdistdir}/fonts/source/public/kixfont
%exclude %{texmfdistdir}/fonts/tfm/public/kixfont
# knuthotherfonts
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/committee
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/halftone
%exclude %{texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook
# kpfonts
%exclude %{texmfdistdir}/fonts/afm/public/kpfonts
%exclude %{texmfdistdir}/fonts/enc/dvips/kpfonts
%exclude %{texmfdistdir}/fonts/enc/pdftex/kpfonts
%exclude %{texmfdistdir}/fonts/map/dvips/kpfonts
%exclude %{texmfdistdir}/fonts/source/public/kpfonts
%exclude %{texmfdistdir}/fonts/tfm/public/kpfonts
%exclude %{texmfdistdir}/fonts/type1/public/kpfonts
%exclude %{texmfdistdir}/fonts/vf/public/kpfonts
%exclude %{texmfdistdir}/tex/latex/kpfonts
# lfb
%exclude %{texmfdistdir}/fonts/source/public/lfb
%exclude %{texmfdistdir}/fonts/tfm/public/lfb
# libris
%exclude %{texmfdistdir}/fonts/afm/arkandis/libris
%exclude %{texmfdistdir}/fonts/enc/dvips/libris
%exclude %{texmfdistdir}/fonts/map/dvips/libris
%exclude %{texmfdistdir}/fonts/tfm/arkandis/libris
%exclude %{texmfdistdir}/fonts/type1/arkandis/libris
%exclude %{texmfdistdir}/fonts/vf/arkandis/libris
%exclude %{texmfdistdir}/tex/latex/libris
# linearA
%exclude %{texmfdistdir}/fonts/afm/public/linearA
%exclude %{texmfdistdir}/fonts/map/dvips/linearA
%exclude %{texmfdistdir}/fonts/tfm/public/linearA
%exclude %{texmfdistdir}/fonts/type1/public/linearA
%exclude %{texmfdistdir}/tex/latex/linearA
# lxfonts
%exclude %{texmfdistdir}/fonts/map/dvips/lxfonts
%exclude %{texmfdistdir}/fonts/source/public/lxfonts
%exclude %{texmfdistdir}/fonts/tfm/public/lxfonts
%exclude %{texmfdistdir}/fonts/type1/public/lxfonts
%exclude %{texmfdistdir}/tex/latex/lxfonts
# ly1
%exclude %{texmfdistdir}/fonts/enc/dvips/ly1
%exclude %{texmfdistdir}/fonts/map/dvips/ly1
%exclude %{texmfdistdir}/fonts/tfm/adobe/ly1
%exclude %{texmfdistdir}/fonts/vf/adobe/ly1
%exclude %{texmfdistdir}/tex/latex/ly1
%exclude %{texmfdistdir}/tex/plain/ly1
# mathabx
%exclude %{texmfdistdir}/fonts/source/public/mathabx
%exclude %{texmfdistdir}/fonts/tfm/public/mathabx
%exclude %{texmfdistdir}/tex/generic/mathabx
# mathdesign
%exclude %{texmfdistdir}/dvips/mathdesign
%exclude %{texmfdistdir}/fonts/map/dvips/mathdesign
%exclude %{texmfdistdir}/tex/latex/mathdesign
# mnsymbol
%exclude %{texmfdistdir}/fonts/enc/dvips/mnsymbol
%exclude %{texmfdistdir}/fonts/map/dvips/mnsymbol
%exclude %{texmfdistdir}/fonts/map/vtex/mnsymbol
%exclude %{texmfdistdir}/fonts/opentype/public/mnsymbol
%exclude %{texmfdistdir}/fonts/source/public/mnsymbol
%exclude %{texmfdistdir}/fonts/tfm/public/mnsymbol
%exclude %{texmfdistdir}/fonts/type1/public/mnsymbol
%exclude %{texmfdistdir}/tex/latex/mnsymbol
# nkarta
%exclude %{texmfdistdir}/fonts/source/public/nkarta
%exclude %{texmfdistdir}/fonts/tfm/public/nkarta
%exclude %{texmfdistdir}/metapost/nkarta
# ocherokee
%exclude %{texmfdistdir}/fonts/afm/public/ocherokee
%exclude %{texmfdistdir}/fonts/map/dvips/ocherokee
%exclude %{texmfdistdir}/fonts/ofm/public/ocherokee
%exclude %{texmfdistdir}/fonts/ovf/public/ocherokee
%exclude %{texmfdistdir}/fonts/ovp/public/ocherokee
%exclude %{texmfdistdir}/fonts/tfm/public/ocherokee
%exclude %{texmfdistdir}/fonts/type1/public/ocherokee
%exclude %{texmfdistdir}/omega/ocp/ocherokee
%exclude %{texmfdistdir}/omega/otp/ocherokee
# ogham
%exclude %{texmfdistdir}/fonts/source/public/ogham
%exclude %{texmfdistdir}/fonts/tfm/public/ogham
# oinuit
%exclude %{texmfdistdir}/fonts/map/dvips/oinuit
%exclude %{texmfdistdir}/fonts/ofm/public/oinuit
%exclude %{texmfdistdir}/fonts/ovf/public/oinuit
%exclude %{texmfdistdir}/fonts/tfm/public/oinuit
%exclude %{texmfdistdir}/fonts/type1/public/oinuit
%exclude %{texmfdistdir}/omega/ocp/oinuit
%exclude %{texmfdistdir}/tex/lambda/oinuit
# oldlatin
%exclude %{texmfdistdir}/fonts/source/public/oldlatin
%exclude %{texmfdistdir}/fonts/tfm/public/oldlatin
# oldstandard
%exclude %{texmfdistdir}/fonts/opentype/public/oldstandard
# orkhun
%exclude %{texmfdistdir}/fonts/source/public/orkhun
%exclude %{texmfdistdir}/fonts/tfm/public/orkhun
# pacioli
%exclude %{texmfdistdir}/fonts/source/public/pacioli
%exclude %{texmfdistdir}/fonts/tfm/public/pacioli
%exclude %{texmfdistdir}/tex/latex/pacioli
# phaistos
%exclude %{texmfdistdir}/fonts/afm/public/phaistos
%exclude %{texmfdistdir}/fonts/map/dvips/phaistos
%exclude %{texmfdistdir}/fonts/opentype/public/phaistos
%exclude %{texmfdistdir}/fonts/tfm/public/phaistos
%exclude %{texmfdistdir}/fonts/type1/public/phaistos
%exclude %{texmfdistdir}/tex/latex/phaistos
# phonetic
%exclude %{texmfdistdir}/fonts/source/public/phonetic
%exclude %{texmfdistdir}/fonts/tfm/public/phonetic
%exclude %{texmfdistdir}/tex/latex/phonetic
# pigpen
%exclude %{texmfdistdir}/fonts/map/dvips/pigpen
%exclude %{texmfdistdir}/fonts/source/public/pigpen
%exclude %{texmfdistdir}/fonts/tfm/public/pigpen
%exclude %{texmfdistdir}/fonts/type1/public/pigpen
%exclude %{texmfdistdir}/tex/latex/pigpen
# prodint
%exclude %{texmfdistdir}/fonts/afm/public/prodint
%exclude %{texmfdistdir}/fonts/map/dvips/prodint
%exclude %{texmfdistdir}/fonts/tfm/public/prodint
%exclude %{texmfdistdir}/fonts/type1/public/prodint
%exclude %{texmfdistdir}/tex/latex/prodint
# punk
%exclude %{texmfdistdir}/fonts/source/public/punk
%exclude %{texmfdistdir}/fonts/tfm/public/punk
# recycle
%exclude %{texmfdistdir}/fonts/map/dvips/recycle
%exclude %{texmfdistdir}/fonts/source/public/recycle
%exclude %{texmfdistdir}/fonts/tfm/public/recycle
%exclude %{texmfdistdir}/fonts/type1/public/recycle
%exclude %{texmfdistdir}/tex/latex/recycle
# romande
%exclude %{texmfdistdir}/fonts/afm/arkandis/romande
%exclude %{texmfdistdir}/fonts/enc/dvips/romande
%exclude %{texmfdistdir}/fonts/map/dvips/romande
%exclude %{texmfdistdir}/fonts/tfm/arkandis/romande
%exclude %{texmfdistdir}/fonts/type1/arkandis/romande
%exclude %{texmfdistdir}/fonts/vf/arkandis/romande
%exclude %{texmfdistdir}/tex/latex/romande
# rsfso
%exclude %{texmfdistdir}/fonts/map/dvips/rsfso
%exclude %{texmfdistdir}/fonts/tfm/public/rsfso
%exclude %{texmfdistdir}/fonts/vf/public/rsfso
# sauter
%exclude %{texmfdistdir}/fonts/source/public/sauter
# sauterfonts
%exclude %{texmfdistdir}/tex/latex/sauterfonts
# semaphor
%exclude %{texmfdistdir}/fonts/afm/public/semaphor
%exclude %{texmfdistdir}/fonts/enc/dvips/semaphor
%exclude %{texmfdistdir}/fonts/map/dvips/semaphor
%exclude %{texmfdistdir}/fonts/opentype/public/semaphor
%exclude %{texmfdistdir}/fonts/source/public/semaphor
%exclude %{texmfdistdir}/fonts/tfm/public/semaphor
%exclude %{texmfdistdir}/fonts/type1/public/semaphor
%exclude %{texmfdistdir}/tex/context/third/semaphor
%exclude %{texmfdistdir}/tex/latex/semaphor
%exclude %{texmfdistdir}/tex/plain/semaphor
# skull
%exclude %{texmfdistdir}/fonts/source/public/skull
%exclude %{texmfdistdir}/tex/latex/skull
# staves
%exclude %{texmfdistdir}/fonts/map/dvips/staves
%exclude %{texmfdistdir}/fonts/tfm/public/staves
%exclude %{texmfdistdir}/fonts/type1/public/staves
%exclude %{texmfdistdir}/tex/latex/staves
# stix
%exclude %{texmfdistdir}/fonts/opentype/public/stix
# tapir
%exclude %{texmfdistdir}/fonts/source/public/tapir
%exclude %{texmfdistdir}/fonts/type1/public/tapir
# tengwarscript
%exclude %{texmfdistdir}/fonts/enc/dvips/tengwarscript
%exclude %{texmfdistdir}/fonts/map/dvips/tengwarscript
%exclude %{texmfdistdir}/fonts/tfm/public/tengwarscript
%exclude %{texmfdistdir}/fonts/vf/public/tengwarscript
%exclude %{texmfdistdir}/tex/latex/tengwarscript
# tpslifonts
%exclude %{texmfdistdir}/tex/latex/tpslifonts
# trajan
%exclude %{texmfdistdir}/fonts/afm/public/trajan
%exclude %{texmfdistdir}/fonts/map/dvips/trajan
%exclude %{texmfdistdir}/fonts/tfm/public/trajan
%exclude %{texmfdistdir}/fonts/type1/public/trajan
%exclude %{texmfdistdir}/tex/latex/trajan
# txfontsb
%exclude %{texmfdistdir}/fonts/afm/public/txfontsb
%exclude %{texmfdistdir}/fonts/enc/dvips/txfontsb
%exclude %{texmfdistdir}/fonts/map/dvips/txfontsb
%exclude %{texmfdistdir}/fonts/tfm/public/txfontsb
%exclude %{texmfdistdir}/fonts/type1/public/txfontsb
%exclude %{texmfdistdir}/fonts/vf/public/txfontsb
%exclude %{texmfdistdir}/tex/latex/txfontsb
# umtypewriter
%exclude %{texmfdistdir}/fonts/opentype/public/umtypewriter
# universa
%exclude %{texmfdistdir}/fonts/source/public/universa
%exclude %{texmfdistdir}/fonts/tfm/public/universa
%exclude %{texmfdistdir}/tex/latex/universa
# urwchancal
%exclude %{texmfdistdir}/fonts/tfm/urw/urwchancal
%exclude %{texmfdistdir}/fonts/vf/urw/urwchancal
%exclude %{texmfdistdir}/tex/latex/urwchancal
# venturisadf
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturis
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/afm/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/enc/dvips/venturisadf
%exclude %{texmfdistdir}/fonts/map/dvips/venturis
%exclude %{texmfdistdir}/fonts/map/dvips/venturis2
%exclude %{texmfdistdir}/fonts/map/dvips/venturisold
%exclude %{texmfdistdir}/fonts/map/dvips/venturissans
%exclude %{texmfdistdir}/fonts/map/dvips/venturissans2
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturis
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/tfm/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturis
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/type1/arkandis/venturissans2
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturis
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturis2
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturisold
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturissans
%exclude %{texmfdistdir}/fonts/vf/arkandis/venturissans2
%exclude %{texmfdistdir}/tex/latex/venturis
%exclude %{texmfdistdir}/tex/latex/venturis2
%exclude %{texmfdistdir}/tex/latex/venturisadf
%exclude %{texmfdistdir}/tex/latex/venturisold
%exclude %{texmfdistdir}/tex/latex/venturissans
%exclude %{texmfdistdir}/tex/latex/venturissans2
# wsuipa
%exclude %{texmfdistdir}/fonts/source/public/wsuipa
%exclude %{texmfdistdir}/fonts/tfm/public/wsuipa
%exclude %{texmfdistdir}/tex/latex/wsuipa
# xits
%exclude %{texmfdistdir}/fonts/opentype/public/xits
# yfonts
%exclude %{texmfdistdir}/tex/latex/yfonts
%{texmfdistdir}/web2c/updmap-dist.cfg

%package	-n texlive-context
Summary:	Tex Live ConTeXt Package
Group:		Publishing
Requires:	texlive-texmf = %{version}-%{release}
Requires:	ruby ruby-tools
Conflicts: tetex-context < 2.01
AutoReq: yes,notex
#Requires: texlive = %{tl_version}
Provides: texlive-collection-context = %{tl_version}

%description	-n texlive-context
This is the ConTeXt package of the TeX Live distribution. Use this only
if you rely on context for building tex documents.

%files		-n texlive-context
%dir %{texmfdistdir}/tex/context
%dir %{texmfdistdir}/tex/context/base
%dir %{texmfdistdir}/tex/context/third
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
Requires:	texlive-texmf = %{version}-%{release}
AutoReq: yes,notex
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

%package	-n texlive-fontsextra
Summary:	TeX Live extra fonts
Group:		Publishing
Requires:	texlive-texmf = %{version}
Requires(post):	texlive-dist = %{version}-%{release}
Requires(postun):	texlive >= %{tl_version}
Obsoletes: texmf-fonts-cm-lgc <= 0.5-alt2_20
AutoReq: yes,notex
#Requires: texlive = %{tl_version}
Provides: texlive-collection-fontsextra = %{tl_version}

%description	-n texlive-fontsextra
TeX Live is an easy way to get up and running with the TeX document
production system. It provides a comprehensive TeX system. It includes
all the major TeX-related programs, macro packages, and fonts that are
free software, including support for many languages around the world.

%files		-n texlive-fontsextra
# collection-fontsextra
# allrunes
%{texmfdistdir}/fonts/map/dvips/allrunes
%{texmfdistdir}/fonts/source/public/allrunes
%{texmfdistdir}/fonts/type1/public/allrunes
%{texmfdistdir}/tex/latex/allrunes
# antiqua
%{texmfdistdir}/fonts/afm/urw/antiqua
%{texmfdistdir}/fonts/map/dvips/antiqua
%{texmfdistdir}/fonts/tfm/urw/antiqua
%{texmfdistdir}/fonts/type1/urw/antiqua
%{texmfdistdir}/fonts/vf/urw/antiqua
%{texmfdistdir}/tex/latex/antiqua
# antt
%{texmfdistdir}/fonts/afm/public/antt
%{texmfdistdir}/fonts/enc/dvips/antt
%{texmfdistdir}/fonts/map/dvips/antt
%{texmfdistdir}/fonts/opentype/public/antt
%{texmfdistdir}/fonts/tfm/public/antt
%{texmfdistdir}/fonts/type1/public/antt
%{texmfdistdir}/tex/latex/antt
%{texmfdistdir}/tex/plain/antt
# archaic
%{texmfdistdir}/fonts/afm/public/archaic
%{texmfdistdir}/fonts/map/dvips/archaic
%{texmfdistdir}/fonts/source/public/archaic
%{texmfdistdir}/fonts/tfm/public/archaic
%{texmfdistdir}/fonts/type1/public/archaic
%{texmfdistdir}/tex/latex/archaic
# arev
%{texmfdistdir}/fonts/afm/public/arev
%{texmfdistdir}/fonts/enc/dvips/arev
%{texmfdistdir}/fonts/map/dvips/arev
%{texmfdistdir}/fonts/tfm/public/arev
%{texmfdistdir}/fonts/type1/public/arev
%{texmfdistdir}/fonts/vf/public/arev
%{texmfdistdir}/tex/latex/arev
# astro
%{texmfdistdir}/fonts/source/public/astro
%{texmfdistdir}/fonts/tfm/public/astro
# augie
%{texmfdistdir}/fonts/afm/public/augie
%{texmfdistdir}/fonts/map/dvips/augie
%{texmfdistdir}/fonts/tfm/public/augie
%{texmfdistdir}/fonts/type1/public/augie
%{texmfdistdir}/fonts/vf/public/augie
%{texmfdistdir}/tex/latex/augie
# auncial-new
%{texmfdistdir}/fonts/afm/public/auncial-new
%{texmfdistdir}/fonts/map/dvips/auncial-new
%{texmfdistdir}/fonts/tfm/public/auncial-new
%{texmfdistdir}/fonts/type1/public/auncial-new
%{texmfdistdir}/tex/latex/auncial-new
# aurical
%{texmfdistdir}/fonts/afm/public/aurical
%{texmfdistdir}/fonts/map/dvips/aurical
%{texmfdistdir}/fonts/source/public/aurical
%{texmfdistdir}/fonts/tfm/public/aurical
%{texmfdistdir}/fonts/type1/public/aurical
%{texmfdistdir}/tex/latex/aurical
# barcodes
%{texmfdistdir}/fonts/source/public/barcodes
%{texmfdistdir}/fonts/tfm/public/barcodes
%{texmfdistdir}/tex/latex/barcodes
# baskervald
%{texmfdistdir}/fonts/afm/arkandis/baskervald
%{texmfdistdir}/fonts/enc/dvips/baskervald
%{texmfdistdir}/fonts/map/dvips/baskervald
%{texmfdistdir}/fonts/tfm/arkandis/baskervald
%{texmfdistdir}/fonts/type1/arkandis/baskervald
%{texmfdistdir}/fonts/vf/arkandis/baskervald
%{texmfdistdir}/tex/latex/baskervald
# bbding
%{texmfdistdir}/fonts/source/public/bbding
%{texmfdistdir}/fonts/tfm/public/bbding
%{texmfdistdir}/tex/latex/bbding
# bbm
%{texmfdistdir}/fonts/source/public/bbm
%{texmfdistdir}/fonts/tfm/public/bbm
# bbm-macros
%{texmfdistdir}/tex/latex/bbm-macros
# bbold
%{texmfdistdir}/fonts/source/public/bbold
%{texmfdistdir}/fonts/tfm/public/bbold
%{texmfdistdir}/tex/latex/bbold
# belleek
%{texmfdistdir}/fonts/map/dvips/belleek
%{texmfdistdir}/fonts/truetype/public/belleek
%{texmfdistdir}/fonts/type1/public/belleek
# bera
%{texmfdistdir}/fonts/afm/public/bera
%{texmfdistdir}/fonts/map/dvips/bera
%{texmfdistdir}/fonts/tfm/public/bera
%{texmfdistdir}/fonts/type1/public/bera
%{texmfdistdir}/fonts/vf/public/bera
%{texmfdistdir}/tex/latex/bera
# blacklettert1
%{texmfdistdir}/fonts/tfm/public/blacklettert1
%{texmfdistdir}/fonts/vf/public/blacklettert1
%{texmfdistdir}/tex/latex/blacklettert1
# boisik
%{texmfdistdir}/fonts/source/public/boisik
%{texmfdistdir}/fonts/tfm/public/boisik
%{texmfdistdir}/tex/latex/boisik
# bookhands
%{texmfdistdir}/fonts/afm/public/bookhands
%{texmfdistdir}/fonts/map/dvips/bookhands
%{texmfdistdir}/fonts/source/public/bookhands
%{texmfdistdir}/fonts/tfm/public/bookhands
%{texmfdistdir}/fonts/type1/public/bookhands
%{texmfdistdir}/tex/latex/bookhands
# boondox
%{texmfdistdir}/fonts/map/dvips/boondox
%{texmfdistdir}/fonts/tfm/public/boondox
%{texmfdistdir}/fonts/type1/public/boondox
%{texmfdistdir}/fonts/vf/public/boondox
%{texmfdistdir}/tex/latex/boondox
# braille
%{texmfdistdir}/tex/latex/braille
# brushscr
%{texmfdistdir}/dvips/brushscr
%{texmfdistdir}/fonts/afm/public/brushscr
%{texmfdistdir}/fonts/map/dvips/brushscr
%{texmfdistdir}/fonts/tfm/public/brushscr
%{texmfdistdir}/fonts/type1/public/brushscr
%{texmfdistdir}/fonts/vf/public/brushscr
%{texmfdistdir}/tex/latex/brushscr
# calligra
%{texmfdistdir}/fonts/source/public/calligra
%{texmfdistdir}/fonts/tfm/public/calligra
# cantarell
%{texmfdistdir}/fonts/afm/public/cantarell
%{texmfdistdir}/fonts/enc/dvips/cantarell
%{texmfdistdir}/fonts/map/dvips/cantarell
%{texmfdistdir}/fonts/tfm/public/cantarell
%{texmfdistdir}/fonts/type1/public/cantarell
%{texmfdistdir}/fonts/vf/public/cantarell
%{texmfdistdir}/tex/latex/cantarell
# carolmin-ps
%{texmfdistdir}/fonts/afm/public/carolmin-ps
%{texmfdistdir}/fonts/map/dvips/carolmin-ps
%{texmfdistdir}/fonts/type1/public/carolmin-ps
# ccicons
%{texmfdistdir}/fonts/enc/dvips/ccicons
%{texmfdistdir}/fonts/map/dvips/ccicons
%{texmfdistdir}/fonts/tfm/public/ccicons
%{texmfdistdir}/fonts/type1/public/ccicons
%{texmfdistdir}/tex/latex/ccicons
# cfr-lm
%{texmfdistdir}/fonts/enc/dvips/cfr-lm
%{texmfdistdir}/fonts/map/dvips/cfr-lm
%{texmfdistdir}/fonts/tfm/public/cfr-lm
%{texmfdistdir}/fonts/vf/public/cfr-lm
%{texmfdistdir}/tex/latex/cfr-lm
# cherokee
%{texmfdistdir}/fonts/source/public/cherokee
%{texmfdistdir}/fonts/tfm/public/cherokee
%{texmfdistdir}/tex/latex/cherokee
# cm-lgc
%{texmfdistdir}/fonts/afm/public/cm-lgc
%{texmfdistdir}/fonts/enc/dvips/cm-lgc
%{texmfdistdir}/fonts/map/dvips/cm-lgc
%{texmfdistdir}/fonts/ofm/public/cm-lgc
%{texmfdistdir}/fonts/ovf/public/cm-lgc
%{texmfdistdir}/fonts/tfm/public/cm-lgc
%{texmfdistdir}/fonts/type1/public/cm-lgc
%{texmfdistdir}/fonts/vf/public/cm-lgc
%{texmfdistdir}/tex/latex/cm-lgc
# cm-unicode
%{texmfdistdir}/fonts/afm/public/cm-unicode
%{texmfdistdir}/fonts/enc/dvips/cm-unicode
%{texmfdistdir}/fonts/map/dvips/cm-unicode
%{texmfdistdir}/fonts/opentype/public/cm-unicode
%{texmfdistdir}/fonts/type1/public/cm-unicode
# cmbright
%{texmfdistdir}/fonts/source/public/cmbright
%{texmfdistdir}/fonts/tfm/public/cmbright
%{texmfdistdir}/tex/latex/cmbright
# cmll
%{texmfdistdir}/fonts/map/dvips/cmll
%{texmfdistdir}/fonts/source/public/cmll
%{texmfdistdir}/fonts/tfm/public/cmll
%{texmfdistdir}/fonts/type1/public/cmll
%{texmfdistdir}/tex/latex/cmll
# cmpica
%{texmfdistdir}/fonts/source/public/cmpica
%{texmfdistdir}/fonts/tfm/public/cmpica
# collection-basic
%{texmfdistdir}/tex/latex/collref
# concmath-fonts
%{texmfdistdir}/fonts/source/public/concmath-fonts
%{texmfdistdir}/fonts/tfm/public/concmath-fonts
# courier-scaled
%{texmfdistdir}/tex/latex/courier-scaled
# cryst
%{texmfdistdir}/fonts/afm/public/cryst
%{texmfdistdir}/fonts/source/public/cryst
%{texmfdistdir}/fonts/tfm/public/cryst
%{texmfdistdir}/fonts/type1/public/cryst
# cyklop
%{texmfdistdir}/fonts/afm/public/cyklop
%{texmfdistdir}/fonts/enc/dvips/cyklop
%{texmfdistdir}/fonts/map/dvips/cyklop
%{texmfdistdir}/fonts/opentype/public/cyklop
%{texmfdistdir}/fonts/tfm/public/cyklop
%{texmfdistdir}/fonts/type1/public/cyklop
%{texmfdistdir}/tex/latex/cyklop
# dancers
%{texmfdistdir}/fonts/source/public/dancers
%{texmfdistdir}/fonts/tfm/public/dancers
# dice
%{texmfdistdir}/fonts/source/public/dice
%{texmfdistdir}/fonts/tfm/public/dice
# dictsym
%{texmfdistdir}/fonts/afm/public/dictsym
%{texmfdistdir}/fonts/map/dvips/dictsym
%{texmfdistdir}/fonts/tfm/public/dictsym
%{texmfdistdir}/fonts/type1/public/dictsym
%{texmfdistdir}/tex/latex/dictsym
# dingbat
%{texmfdistdir}/fonts/source/public/dingbat
%{texmfdistdir}/fonts/tfm/public/dingbat
%{texmfdistdir}/tex/latex/dingbat
# doublestroke
%{texmfdistdir}/fonts/map/dvips/doublestroke
%{texmfdistdir}/fonts/source/public/doublestroke
%{texmfdistdir}/fonts/tfm/public/doublestroke
%{texmfdistdir}/fonts/type1/public/doublestroke
%{texmfdistdir}/tex/latex/doublestroke
# dozenal
%{texmfdistdir}/fonts/map/dvips/dozenal
%{texmfdistdir}/fonts/source/public/dozenal
%{texmfdistdir}/fonts/tfm/public/dozenal
%{texmfdistdir}/fonts/type1/public/dozenal
%{texmfdistdir}/tex/latex/dozenal
# duerer
%{texmfdistdir}/fonts/source/public/duerer
%{texmfdistdir}/fonts/tfm/public/duerer
# duerer-latex
%{texmfdistdir}/tex/latex/duerer-latex
# ean
%{texmfdistdir}/tex/generic/ean
# ecc
%{texmfdistdir}/fonts/source/public/ecc
%{texmfdistdir}/fonts/tfm/public/ecc
# eco
%{texmfdistdir}/fonts/tfm/public/eco
%{texmfdistdir}/fonts/vf/public/eco
%{texmfdistdir}/tex/latex/eco
# eiad
%{texmfdistdir}/fonts/source/public/eiad
%{texmfdistdir}/fonts/tfm/public/eiad
%{texmfdistdir}/tex/latex/eiad
# eiad-ltx
%{texmfdistdir}/fonts/source/public/eiad-ltx
%{texmfdistdir}/tex/latex/eiad-ltx
# elvish
%{texmfdistdir}/fonts/source/public/elvish
%{texmfdistdir}/fonts/tfm/public/elvish
# epigrafica
%{texmfdistdir}/fonts/afm/public/epigrafica
%{texmfdistdir}/fonts/enc/dvips/epigrafica
%{texmfdistdir}/fonts/map/dvips/epigrafica
%{texmfdistdir}/fonts/tfm/public/epigrafica
%{texmfdistdir}/fonts/type1/public/epigrafica
%{texmfdistdir}/fonts/vf/public/epigrafica
%{texmfdistdir}/tex/latex/epigrafica
# epsdice
%{texmfdistdir}/tex/latex/epsdice
# esstix
%{texmfdistdir}/fonts/afm/esstix
%{texmfdistdir}/fonts/map/dvips/esstix
%{texmfdistdir}/fonts/tfm/public/esstix
%{texmfdistdir}/fonts/type1/public/esstix
%{texmfdistdir}/fonts/vf/public/esstix
%{texmfdistdir}/tex/latex/esstix
# esvect
%{texmfdistdir}/fonts/map/dvips/esvect
%{texmfdistdir}/fonts/source/public/esvect
%{texmfdistdir}/fonts/tfm/public/esvect
%{texmfdistdir}/fonts/type1/public/esvect
%{texmfdistdir}/tex/latex/esvect
# eulervm
%{texmfdistdir}/fonts/tfm/public/eulervm
%{texmfdistdir}/fonts/vf/public/eulervm
%{texmfdistdir}/tex/latex/eulervm
# euxm
%{texmfdistdir}/fonts/source/public/euxm
%{texmfdistdir}/fonts/tfm/public/euxm
# fdsymbol
%{texmfdistdir}/fonts/enc/dvips/fdsymbol
%{texmfdistdir}/fonts/map/dvips/fdsymbol
%{texmfdistdir}/fonts/source/public/fdsymbol
%{texmfdistdir}/fonts/tfm/public/fdsymbol
%{texmfdistdir}/fonts/type1/public/fdsymbol
%{texmfdistdir}/tex/latex/fdsymbol
# feyn
%{texmfdistdir}/fonts/source/public/feyn
%{texmfdistdir}/fonts/tfm/public/feyn
%{texmfdistdir}/tex/latex/feyn
# fge
%{texmfdistdir}/fonts/map/dvips/fge
%{texmfdistdir}/fonts/source/public/fge
%{texmfdistdir}/fonts/tfm/public/fge
%{texmfdistdir}/fonts/type1/public/fge
%{texmfdistdir}/tex/latex/fge
# foekfont
%{texmfdistdir}/fonts/map/dvips/foekfont
%{texmfdistdir}/fonts/tfm/public/foekfont
%{texmfdistdir}/fonts/type1/public/foekfont
%{texmfdistdir}/tex/latex/foekfont
# fonetika
%{texmfdistdir}/fonts/afm/public/fonetika
%{texmfdistdir}/fonts/map/dvips/fonetika
%{texmfdistdir}/fonts/tfm/public/fonetika
%{texmfdistdir}/fonts/truetype/public/fonetika
%{texmfdistdir}/fonts/type1/public/fonetika
%{texmfdistdir}/tex/latex/fonetika
# fourier
%{texmfdistdir}/fonts/afm/public/fourier
%{texmfdistdir}/fonts/map/dvips/fourier
%{texmfdistdir}/fonts/tfm/public/fourier
%{texmfdistdir}/fonts/type1/public/fourier
%{texmfdistdir}/fonts/vf/public/fourier
%{texmfdistdir}/tex/latex/fourier
# fouriernc
%{texmfdistdir}/fonts/afm/public/fouriernc
%{texmfdistdir}/fonts/tfm/public/fouriernc
%{texmfdistdir}/fonts/vf/public/fouriernc
%{texmfdistdir}/tex/latex/fouriernc
# frcursive
%{texmfdistdir}/fonts/source/public/frcursive
%{texmfdistdir}/fonts/tfm/public/frcursive
%{texmfdistdir}/tex/latex/frcursive
# genealogy
%{texmfdistdir}/fonts/source/public/genealogy
%{texmfdistdir}/fonts/tfm/public/genealogy
# gfsartemisia
%{texmfdistdir}/fonts/afm/public/gfsartemisia
%{texmfdistdir}/fonts/enc/dvips/gfsartemisia
%{texmfdistdir}/fonts/map/dvips/gfsartemisia
%{texmfdistdir}/fonts/opentype/public/gfsartemisia
%{texmfdistdir}/fonts/tfm/public/gfsartemisia
%{texmfdistdir}/fonts/type1/public/gfsartemisia
%{texmfdistdir}/fonts/vf/public/gfsartemisia
%{texmfdistdir}/tex/latex/gfsartemisia
# gfsbodoni
%{texmfdistdir}/fonts/afm/public/gfsbodoni
%{texmfdistdir}/fonts/enc/dvips/gfsbodoni
%{texmfdistdir}/fonts/map/dvips/gfsbodoni
%{texmfdistdir}/fonts/opentype/public/gfsbodoni
%{texmfdistdir}/fonts/tfm/public/gfsbodoni
%{texmfdistdir}/fonts/type1/public/gfsbodoni
%{texmfdistdir}/fonts/vf/public/gfsbodoni
%{texmfdistdir}/tex/latex/gfsbodoni
# gfscomplutum
%{texmfdistdir}/fonts/afm/public/gfscomplutum
%{texmfdistdir}/fonts/enc/dvips/gfscomplutum
%{texmfdistdir}/fonts/map/dvips/gfscomplutum
%{texmfdistdir}/fonts/opentype/public/gfscomplutum
%{texmfdistdir}/fonts/tfm/public/gfscomplutum
%{texmfdistdir}/fonts/type1/public/gfscomplutum
%{texmfdistdir}/fonts/vf/public/gfscomplutum
%{texmfdistdir}/tex/latex/gfscomplutum
# gfsdidot
%{texmfdistdir}/fonts/afm/public/gfsdidot
%{texmfdistdir}/fonts/enc/dvips/gfsdidot
%{texmfdistdir}/fonts/map/dvips/gfsdidot
%{texmfdistdir}/fonts/opentype/public/gfsdidot
%{texmfdistdir}/fonts/tfm/public/gfsdidot
%{texmfdistdir}/fonts/type1/public/gfsdidot
%{texmfdistdir}/fonts/vf/public/gfsdidot
%{texmfdistdir}/tex/latex/gfsdidot
# gfsneohellenic
%{texmfdistdir}/fonts/afm/public/gfsneohellenic
%{texmfdistdir}/fonts/enc/dvips/gfsneohellenic
%{texmfdistdir}/fonts/map/dvips/gfsneohellenic
%{texmfdistdir}/fonts/opentype/public/gfsneohellenic
%{texmfdistdir}/fonts/tfm/public/gfsneohellenic
%{texmfdistdir}/fonts/type1/public/gfsneohellenic
%{texmfdistdir}/fonts/vf/public/gfsneohellenic
%{texmfdistdir}/tex/latex/gfsneohellenic
# gfssolomos
%{texmfdistdir}/fonts/afm/public/gfssolomos
%{texmfdistdir}/fonts/enc/dvips/gfssolomos
%{texmfdistdir}/fonts/map/dvips/gfssolomos
%{texmfdistdir}/fonts/opentype/public/gfssolomos
%{texmfdistdir}/fonts/tfm/public/gfssolomos
%{texmfdistdir}/fonts/type1/public/gfssolomos
%{texmfdistdir}/fonts/vf/public/gfssolomos
%{texmfdistdir}/tex/latex/gfssolomos
# gnu-freefont
%{texmfdistdir}/fonts/opentype/public/gnu-freefont
%{texmfdistdir}/fonts/truetype/public/gnu-freefont
# greenpoint
%{texmfdistdir}/fonts/source/public/greenpoint
%{texmfdistdir}/fonts/tfm/public/greenpoint
# grotesq
%{texmfdistdir}/fonts/afm/urw/grotesq
%{texmfdistdir}/fonts/map/dvips/grotesq
%{texmfdistdir}/fonts/tfm/urw/grotesq
%{texmfdistdir}/fonts/type1/urw/grotesq
%{texmfdistdir}/fonts/vf/urw/grotesq
%{texmfdistdir}/tex/latex/grotesq
# hands
%{texmfdistdir}/fonts/source/public/hands
%{texmfdistdir}/fonts/tfm/public/hands
# hfbright
%{texmfdistdir}/fonts/afm/public/hfbright
%{texmfdistdir}/fonts/enc/dvips/hfbright
%{texmfdistdir}/fonts/map/dvips/hfbright
%{texmfdistdir}/fonts/type1/public/hfbright
# hfoldsty
%{texmfdistdir}/fonts/tfm/public/hfoldsty
%{texmfdistdir}/fonts/vf/public/hfoldsty
%{texmfdistdir}/tex/latex/hfoldsty
# ifsym
%{texmfdistdir}/fonts/source/public/ifsym
%{texmfdistdir}/fonts/tfm/public/ifsym
%{texmfdistdir}/tex/latex/ifsym
# inconsolata
%{texmfdistdir}/fonts/enc/dvips/inconsolata
%{texmfdistdir}/fonts/map/dvips/inconsolata
%{texmfdistdir}/fonts/opentype/public/inconsolata
%{texmfdistdir}/fonts/tfm/public/inconsolata
%{texmfdistdir}/fonts/type1/public/inconsolata
%{texmfdistdir}/tex/latex/inconsolata
# initials
%{texmfdistdir}/dvips/initials
%{texmfdistdir}/fonts/afm/public/initials
%{texmfdistdir}/fonts/map/dvips/initials
%{texmfdistdir}/fonts/tfm/public/initials
%{texmfdistdir}/fonts/type1/public/initials
%{texmfdistdir}/tex/latex/initials
# jablantile
%{texmfdistdir}/fonts/source/public/jablantile
# junicode
%{texmfdistdir}/fonts/truetype/public/junicode
# kixfont
%{texmfdistdir}/fonts/source/public/kixfont
%{texmfdistdir}/fonts/tfm/public/kixfont
# knuthotherfonts
%{texmfdistdir}/fonts/source/public/knuthotherfonts/committee
%{texmfdistdir}/fonts/source/public/knuthotherfonts/halftone
%{texmfdistdir}/fonts/source/public/knuthotherfonts/mfbook
# kpfonts
%{texmfdistdir}/fonts/afm/public/kpfonts
%{texmfdistdir}/fonts/enc/dvips/kpfonts
%{texmfdistdir}/fonts/enc/pdftex/kpfonts
%{texmfdistdir}/fonts/map/dvips/kpfonts
%{texmfdistdir}/fonts/source/public/kpfonts
%{texmfdistdir}/fonts/tfm/public/kpfonts
%{texmfdistdir}/fonts/type1/public/kpfonts
%{texmfdistdir}/fonts/vf/public/kpfonts
%{texmfdistdir}/tex/latex/kpfonts
# lfb
%{texmfdistdir}/fonts/source/public/lfb
%{texmfdistdir}/fonts/tfm/public/lfb
# libris
%{texmfdistdir}/fonts/afm/arkandis/libris
%{texmfdistdir}/fonts/enc/dvips/libris
%{texmfdistdir}/fonts/map/dvips/libris
%{texmfdistdir}/fonts/tfm/arkandis/libris
%{texmfdistdir}/fonts/type1/arkandis/libris
%{texmfdistdir}/fonts/vf/arkandis/libris
%{texmfdistdir}/tex/latex/libris
# linearA
%{texmfdistdir}/fonts/afm/public/linearA
%{texmfdistdir}/fonts/map/dvips/linearA
%{texmfdistdir}/fonts/tfm/public/linearA
%{texmfdistdir}/fonts/type1/public/linearA
%{texmfdistdir}/tex/latex/linearA
# lxfonts
%{texmfdistdir}/fonts/map/dvips/lxfonts
%{texmfdistdir}/fonts/source/public/lxfonts
%{texmfdistdir}/fonts/tfm/public/lxfonts
%{texmfdistdir}/fonts/type1/public/lxfonts
%{texmfdistdir}/tex/latex/lxfonts
# ly1
%{texmfdistdir}/fonts/enc/dvips/ly1
%{texmfdistdir}/fonts/map/dvips/ly1
%{texmfdistdir}/fonts/tfm/adobe/ly1
%{texmfdistdir}/fonts/vf/adobe/ly1
%{texmfdistdir}/tex/latex/ly1
%{texmfdistdir}/tex/plain/ly1
# mathabx
%{texmfdistdir}/fonts/source/public/mathabx
%{texmfdistdir}/fonts/tfm/public/mathabx
%{texmfdistdir}/tex/generic/mathabx
# mathdesign
%{texmfdistdir}/dvips/mathdesign
%{texmfdistdir}/fonts/map/dvips/mathdesign
%{texmfdistdir}/tex/latex/mathdesign
# mnsymbol
%{texmfdistdir}/fonts/enc/dvips/mnsymbol
%{texmfdistdir}/fonts/map/dvips/mnsymbol
%{texmfdistdir}/fonts/map/vtex/mnsymbol
%{texmfdistdir}/fonts/opentype/public/mnsymbol
%{texmfdistdir}/fonts/source/public/mnsymbol
%{texmfdistdir}/fonts/tfm/public/mnsymbol
%{texmfdistdir}/fonts/type1/public/mnsymbol
%{texmfdistdir}/tex/latex/mnsymbol
# nkarta
%{texmfdistdir}/fonts/source/public/nkarta
%{texmfdistdir}/fonts/tfm/public/nkarta
%{texmfdistdir}/metapost/nkarta
# ocherokee
%{texmfdistdir}/fonts/afm/public/ocherokee
%{texmfdistdir}/fonts/map/dvips/ocherokee
%{texmfdistdir}/fonts/ofm/public/ocherokee
%{texmfdistdir}/fonts/ovf/public/ocherokee
%{texmfdistdir}/fonts/ovp/public/ocherokee
%{texmfdistdir}/fonts/tfm/public/ocherokee
%{texmfdistdir}/fonts/type1/public/ocherokee
%{texmfdistdir}/omega/ocp/ocherokee
%{texmfdistdir}/omega/otp/ocherokee
# ogham
%{texmfdistdir}/fonts/source/public/ogham
%{texmfdistdir}/fonts/tfm/public/ogham
# oinuit
%{texmfdistdir}/fonts/map/dvips/oinuit
%{texmfdistdir}/fonts/ofm/public/oinuit
%{texmfdistdir}/fonts/ovf/public/oinuit
%{texmfdistdir}/fonts/tfm/public/oinuit
%{texmfdistdir}/fonts/type1/public/oinuit
%{texmfdistdir}/omega/ocp/oinuit
%{texmfdistdir}/tex/lambda/oinuit
# oldlatin
%{texmfdistdir}/fonts/source/public/oldlatin
%{texmfdistdir}/fonts/tfm/public/oldlatin
# oldstandard
%{texmfdistdir}/fonts/opentype/public/oldstandard
# orkhun
%{texmfdistdir}/fonts/source/public/orkhun
%{texmfdistdir}/fonts/tfm/public/orkhun
# pacioli
%{texmfdistdir}/fonts/source/public/pacioli
%{texmfdistdir}/fonts/tfm/public/pacioli
%{texmfdistdir}/tex/latex/pacioli
# phaistos
%{texmfdistdir}/fonts/afm/public/phaistos
%{texmfdistdir}/fonts/map/dvips/phaistos
%{texmfdistdir}/fonts/opentype/public/phaistos
%{texmfdistdir}/fonts/tfm/public/phaistos
%{texmfdistdir}/fonts/type1/public/phaistos
%{texmfdistdir}/tex/latex/phaistos
# phonetic
%{texmfdistdir}/fonts/source/public/phonetic
%{texmfdistdir}/fonts/tfm/public/phonetic
%{texmfdistdir}/tex/latex/phonetic
# pigpen
%{texmfdistdir}/fonts/map/dvips/pigpen
%{texmfdistdir}/fonts/source/public/pigpen
%{texmfdistdir}/fonts/tfm/public/pigpen
%{texmfdistdir}/fonts/type1/public/pigpen
%{texmfdistdir}/tex/latex/pigpen
# prodint
%{texmfdistdir}/fonts/afm/public/prodint
%{texmfdistdir}/fonts/map/dvips/prodint
%{texmfdistdir}/fonts/tfm/public/prodint
%{texmfdistdir}/fonts/type1/public/prodint
%{texmfdistdir}/tex/latex/prodint
# punk
%{texmfdistdir}/fonts/source/public/punk
%{texmfdistdir}/fonts/tfm/public/punk
# recycle
%{texmfdistdir}/fonts/map/dvips/recycle
%{texmfdistdir}/fonts/source/public/recycle
%{texmfdistdir}/fonts/tfm/public/recycle
%{texmfdistdir}/fonts/type1/public/recycle
%{texmfdistdir}/tex/latex/recycle
# romande
%{texmfdistdir}/fonts/afm/arkandis/romande
%{texmfdistdir}/fonts/enc/dvips/romande
%{texmfdistdir}/fonts/map/dvips/romande
%{texmfdistdir}/fonts/tfm/arkandis/romande
%{texmfdistdir}/fonts/type1/arkandis/romande
%{texmfdistdir}/fonts/vf/arkandis/romande
%{texmfdistdir}/tex/latex/romande
# rsfso
%{texmfdistdir}/fonts/map/dvips/rsfso
%{texmfdistdir}/fonts/tfm/public/rsfso
%{texmfdistdir}/fonts/vf/public/rsfso
# sauter
%{texmfdistdir}/fonts/source/public/sauter
# sauterfonts
%{texmfdistdir}/tex/latex/sauterfonts
# semaphor
%{texmfdistdir}/fonts/afm/public/semaphor
%{texmfdistdir}/fonts/enc/dvips/semaphor
%{texmfdistdir}/fonts/map/dvips/semaphor
%{texmfdistdir}/fonts/opentype/public/semaphor
%{texmfdistdir}/fonts/source/public/semaphor
%{texmfdistdir}/fonts/tfm/public/semaphor
%{texmfdistdir}/fonts/type1/public/semaphor
#%{texmfdistdir}/tex/context/third/semaphor
%{texmfdistdir}/tex/latex/semaphor
%{texmfdistdir}/tex/plain/semaphor
# skull
%{texmfdistdir}/fonts/source/public/skull
%{texmfdistdir}/tex/latex/skull
# staves
%{texmfdistdir}/fonts/map/dvips/staves
%{texmfdistdir}/fonts/tfm/public/staves
%{texmfdistdir}/fonts/type1/public/staves
%{texmfdistdir}/tex/latex/staves
# stix
%{texmfdistdir}/fonts/opentype/public/stix
# tapir
%{texmfdistdir}/fonts/source/public/tapir
%{texmfdistdir}/fonts/type1/public/tapir
# tengwarscript
%{texmfdistdir}/fonts/enc/dvips/tengwarscript
%{texmfdistdir}/fonts/map/dvips/tengwarscript
%{texmfdistdir}/fonts/tfm/public/tengwarscript
%{texmfdistdir}/fonts/vf/public/tengwarscript
%{texmfdistdir}/tex/latex/tengwarscript
# tpslifonts
%{texmfdistdir}/tex/latex/tpslifonts
# trajan
%{texmfdistdir}/fonts/afm/public/trajan
%{texmfdistdir}/fonts/map/dvips/trajan
%{texmfdistdir}/fonts/tfm/public/trajan
%{texmfdistdir}/fonts/type1/public/trajan
%{texmfdistdir}/tex/latex/trajan
# txfontsb
%{texmfdistdir}/fonts/afm/public/txfontsb
%{texmfdistdir}/fonts/enc/dvips/txfontsb
%{texmfdistdir}/fonts/map/dvips/txfontsb
%{texmfdistdir}/fonts/tfm/public/txfontsb
%{texmfdistdir}/fonts/type1/public/txfontsb
%{texmfdistdir}/fonts/vf/public/txfontsb
%{texmfdistdir}/tex/latex/txfontsb
# umtypewriter
%{texmfdistdir}/fonts/opentype/public/umtypewriter
# universa
%{texmfdistdir}/fonts/source/public/universa
%{texmfdistdir}/fonts/tfm/public/universa
%{texmfdistdir}/tex/latex/universa
# urwchancal
%{texmfdistdir}/fonts/tfm/urw/urwchancal
%{texmfdistdir}/fonts/vf/urw/urwchancal
%{texmfdistdir}/tex/latex/urwchancal
# venturisadf
%{texmfdistdir}/fonts/afm/arkandis/venturis
%{texmfdistdir}/fonts/afm/arkandis/venturis2
%{texmfdistdir}/fonts/afm/arkandis/venturisold
%{texmfdistdir}/fonts/afm/arkandis/venturissans
%{texmfdistdir}/fonts/afm/arkandis/venturissans2
%{texmfdistdir}/fonts/enc/dvips/venturisadf
%{texmfdistdir}/fonts/map/dvips/venturis
%{texmfdistdir}/fonts/map/dvips/venturis2
%{texmfdistdir}/fonts/map/dvips/venturisold
%{texmfdistdir}/fonts/map/dvips/venturissans
%{texmfdistdir}/fonts/map/dvips/venturissans2
%{texmfdistdir}/fonts/tfm/arkandis/venturis
%{texmfdistdir}/fonts/tfm/arkandis/venturis2
%{texmfdistdir}/fonts/tfm/arkandis/venturisold
%{texmfdistdir}/fonts/tfm/arkandis/venturissans
%{texmfdistdir}/fonts/tfm/arkandis/venturissans2
%{texmfdistdir}/fonts/type1/arkandis/venturis
%{texmfdistdir}/fonts/type1/arkandis/venturis2
%{texmfdistdir}/fonts/type1/arkandis/venturisold
%{texmfdistdir}/fonts/type1/arkandis/venturissans
%{texmfdistdir}/fonts/type1/arkandis/venturissans2
%{texmfdistdir}/fonts/vf/arkandis/venturis
%{texmfdistdir}/fonts/vf/arkandis/venturis2
%{texmfdistdir}/fonts/vf/arkandis/venturisold
%{texmfdistdir}/fonts/vf/arkandis/venturissans
%{texmfdistdir}/fonts/vf/arkandis/venturissans2
%{texmfdistdir}/tex/latex/venturis
%{texmfdistdir}/tex/latex/venturis2
%{texmfdistdir}/tex/latex/venturisadf
%{texmfdistdir}/tex/latex/venturisold
%{texmfdistdir}/tex/latex/venturissans
%{texmfdistdir}/tex/latex/venturissans2
# wsuipa
%{texmfdistdir}/fonts/source/public/wsuipa
%{texmfdistdir}/fonts/tfm/public/wsuipa
%{texmfdistdir}/tex/latex/wsuipa
# xits
%{texmfdistdir}/fonts/opentype/public/xits
# yfonts
%{texmfdistdir}/tex/latex/yfonts
%{texmfdistdir}/web2c/updmap-fontsextra.cfg

%prep
%setup -q -n texlive-%{mga_tl_timestamp}-texmf
#remove source, as we don't need it and it saves some space
rm -rf texmf-dist/source

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
%patch33 -p0

#-----------------------------------------------------------------------
%build

#-----------------------------------------------------------------------
%install
mkdir -p %{buildroot}%{texmfdistdir}
cp -lfar texmf-dist/* %{buildroot}%{texmfdistdir}

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
#    ln -sf %{texmfdistdir}/scripts/fontools/cmap2enc cmap2enc
	ln -sf %{texmfdistdir}/scripts/de-macro/de-macro de-macro
	ln -sf %{texmfdistdir}/scripts/dviasm/dviasm.py dviasm
	ln -sf %{texmfdistdir}/scripts/texlive/e2pall.pl e2pall
#    ln -sf %{texmfdistdir}/scripts/bengali/ebong.py ebong
#    ln -sf %{texmfdistdir}/scripts/epspdf/epspdf epspdf
#    ln -sf %{texmfdistdir}/scripts/epspdf/epspdftk epspdftk
	ln -sf %{texmfdistdir}/scripts/epstopdf/epstopdf.pl epstopdf
	ln -sf %{texmfdistdir}/scripts/fig4latex/fig4latex fig4latex
	ln -sf %{texmfdistdir}/scripts/findhyph/findhyph findhyph
#    ln -sf %{texmfdistdir}/scripts/fontools/font2afm font2afm
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
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdf180 pdf180
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdf270 pdf270
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdf90 pdf90
	ln -sf %{texmfdistdir}/scripts/pax/pdfannotextractor.pl pdfannotextractor
	ln -sf %{texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfbook pdfbook
	ln -sf %{texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfflip pdfflip
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam pdfjam
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-pocketmod pdfjam-pocketmod
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides3up pdfjam-slides3up
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjam-slides6up pdfjam-slides6up
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfjoin pdfjoin
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfnup pdfnup
	ln -sf %{texmfdistdir}/scripts/pdfjam/pdfpun pdfpun
#    ln -sf %{texmfdistdir}/scripts/ppower4/pdfthumb.tlu pdfthumb
	ln -sf %{texmfdistdir}/scripts/perltex/perltex.pl perltex
#    ln -sf %{texmfdistdir}/scripts/fontools/pfm2kpx pfm2kpx
	ln -sf %{texmfdistdir}/scripts/pkfix/pkfix.pl pkfix
	ln -sf %{texmfdistdir}/scripts/pkfix-helper/pkfix-helper pkfix-helper
#    ln -sf %{texmfdistdir}/scripts/ppower4/ppower4.tlu ppower4
	ln -sf %{texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
	ln -sf %{texmfdistdir}/scripts/pst2pdf/pst2pdf.pl pst2pdf
	ln -sf %{texmfdistdir}/scripts/purifyeps/purifyeps purifyeps
	ln -sf epstopdf repstopdf
	ln -sf pdfcrop rpdfcrop
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
%if %{with_system_psutils}
    rm -f doc/man/man1/{epsffit,extractres,fixdlsrps,fixfmps,fixmacps,fixpsditps,fixpspps,fixscribeps,fixtpps,fixwfwps,fixwpps,fixwwps,getafm,includeres,psbook,psmerge,psnup,psresize,psselect,pstops}.1
%endif

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

tar zxf %{SOURCE4}
mkdir -p %{buildroot}%{texmfdistdir}/tlpkg
cp -lfar install-tl-*/tlpkg/TeXLive %{buildroot}%{texmfdistdir}/tlpkg
cp -lfar install-tl-*/tlpkg/installer %{buildroot}%{texmfdistdir}/tlpkg

perl -pi -e 's|-var-value=TEXMFROOT|-var-value=TEXMFMAIN|g;'			\
    %{buildroot}%{texmfdistdir}/scripts/texlive/updmap.pl

mkdir -p %{buildroot}%{texmflocaldir}

touch %{buildroot}%{texmfdistdir}/ls-R
touch %{buildroot}%{texmflocaldir}/ls-R

pushd %{buildroot}%{texmfdistdir}
cp %{_sourcedir}/updmap-*.cfg web2c/
mkdir -p %buildroot/%_rpmlibdir
cat > %buildroot/%_rpmlibdir/texlive-5-config.filetrigger << 'EOF'
#!/bin/sh
LC_ALL=C egrep -qs '^%{texmfdistdir}(/|$)' || exit 0
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
%{_bindir}/fmtutil-sys --all >> $LOGFILE 2>&1 ||:
EOF
chmod 755 %buildroot/%_rpmlibdir/texlive-5-config.filetrigger

# touching all ghosts; hack for rpm 4.0.4
for rpm404_ghost in %{texmfdistdir}/ls-R %{texmflocaldir}/ls-R
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done
# verify-elf: ERROR: [...]/tlpkg/installer/wget/wget.i386-freebsd: ELF object for "noarch" architecture
rm -rf %{buildroot}%{texmfdistdir}/tlpkg/installer/wget/*
rm -rf %{buildroot}%{texmfdistdir}/tlpkg/installer/xz/*
# can't be moved to %%post - see tar xf's in %%install
pushd %buildroot%{texmfdistdir}
patch -p0 < %SOURCE8000
patch -p0 < %SOURCE8001
popd
# info
patch -p0 %buildroot%{_infodir}/texdraw.info < %SOURCE8003
# remove bundled perl-PDF-Reuse
rm -rf %buildroot%{texmfdistdir}/scripts/xetex/perl/lib
# merged from texlive-common = 0.1
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/texlive-collection-basic-files.req.list <<EOF
# texlive-base dirlist for %_rpmlibdir/files.req
%{texmfdistdir}	texlive-collection-basic
EOF




#-----------------------------------------------------------------------


%changelog
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

