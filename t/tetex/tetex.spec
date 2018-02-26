# -*- rpm-spec -*-
# $Id: tetex,v 1.25 2003/01/26 17:08:54 ab Exp $

Name: tetex
Version: 2.0
Release: alt11

%define pkgname         teTeX
%define texversion    2.0-rc1
%define _compress_method  bzip2
%set_autoconf_version 2.13
%set_automake_version 1.4
%define _perl_lib_path %_datadir/texmf/context/perltk

Summary: The TeX text formatting system
License: Distributable
Group: Publishing
Url: http://www.tug.org/teTeX/
Packager: teTeX Development Team <tetex@packages.altlinux.org>

Source0: ftp://ftp.dante.de/pub/tex-archive/systems/unix/teTeX/1.0/distrib/sources/%pkgname-src-%texversion.tar
Source1: ftp://ftp.dante.de/pub/tex-archive/systems/unix/teTeX/1.0/distrib/sources/%pkgname-texmf-%texversion.tar
Source2: ec-plain.tar
Source4: icons-xdvi.tar
Source5: context-russian.tar
Source10: tetex.cron

# Emacs command settings:
Source101: %pkgname-xdvi.el
Source102: %pkgname-dvips.el
Source103: %pkgname-dvilj.el
 
Patch1: %pkgname-fmtutil-alt.patch
Patch2: %pkgname-klibtool-ldconfig-alt.patch
Patch3: %pkgname-tfmgen-alt.patch
Patch4: %pkgname-xdvik-large-fontmap-alt.patch
Patch5: %pkgname-texmf.in-alt.patch
Patch6: %pkgname-perltk-alt.patch
Patch7: %pkgname-2.0-updmap-cnfdir-alt.patch
Patch8: %pkgname-texk-alt.patch

Patch11: %pkgname-1.0-ipl_i18n.patch
Patch12: %pkgname-texmf-cyrtex-t2a-alt.patch
Patch13: %pkgname-texmf-defaults-alt.patch
Patch14: %pkgname-2.0-gentoo-dvi-draw.patch
Patch15: %pkgname-2.0-alt-deps.patch

# Security fixes
Patch20: %pkgname-CVE-2004-0888.patch
Patch21: %pkgname-CVE-2004-1125.patch
Patch22: %pkgname-CVE-2005-0064.patch
Patch23: %pkgname-CVE-2005-3191_3192.patch

Obsoletes: tetex-texmf-src
PreReq: tetex-core = %PACKAGE_VERSION-%release, cm-super-fonts-tex

%package core
Summary: The core of TeX text formatting system
License: Distributable
Group: Publishing
Url: http://www.tug.org/teTeX/

%define lib_suffix %nil
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
#Provides: libkpathsea.so%lib_suffix
Provides: tetex-fonts-source

PreReq: coreutils
Requires: texinfo >= 0:4.13-alt1
Requires: dialog
Requires: tex-common >= 0.2
Requires: tetex-latex = %version-%release

Obsoletes: dvipdfm, tetex-fonts-source

BuildRequires(pre): rpm-build-texmf
BuildRequires: flex-old gcc-c++ imake libXaw-devel libexpat-devel libpng-devel
BuildRequires: libssl-devel perl-Tk t1lib-devel w3c-libwww-devel xorg-cf-files

%add_texmf_req_skip latex/amsjpa
%add_texmf_req_skip latex/vtexhtml
%add_texmf_req_skip latex/iilcr

%description
teTeX is an implementation of TeX for Linux or UNIX systems.  TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.  Usually,
TeX is used in conjunction with a higher level formatting package like
LaTeX or PlainTeX, since TeX by itself is not very user-friendly.

Install teTeX if you want to use the TeX text formatting system.  If you
are installing teTeX, you would probably also need to install tetex-afm (a
PostScript(TM) font converter for TeX), tetex-dvilj (for converting .dvi
files to HP PCL format for printing on HP and HP compatible printers),
tetex-dvips (for converting .dvi files to PostScript format for printing
on PostScript printers), tetex-latex (a higher level formatting package
which provides an easier-to-use interface for TeX) and tetex-xdvi (for
previewing .dvi files in X).  Unless you're an expert at using TeX,
you'll also want to install the tetex-doc package, which includes the
documentation for TeX.

%description core
teTeX is an implementation of TeX for Linux or UNIX systems.  TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.  Usually,
TeX is used in conjunction with a higher level formatting package like
LaTeX or PlainTeX, since TeX by itself is not very user-friendly.

%package latex
Summary: The LaTeX front end for the TeX text formatting system
Group: Publishing
PreReq: tetex-core = %PACKAGE_VERSION-%release

%description latex
LaTeX is a front end for the TeX text formatting system.  Easier to
use than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-latex.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvilj (for converting .dvi files to HP PCL format for
printing on HP and HP compatible printers), tetex-dvips (for converting
.dvi files to PostScript format for printing on PostScript printers) and
tetex-xdvi (for previewing .dvi files in X).  If you're not an expert
at TeX, you'll probably also want to install the tetex-doc package,
which contains documentation for TeX.

%package xdvi
Summary: An X viewer for DVI files
Group: Publishing
PreReq: tetex-core = %PACKAGE_VERSION-%release

%description xdvi
Xdvi allows you to preview the TeX text formatting system's output .dvi
files on an X Window System.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-xdvi.  In addition, you
will need to install tetex-afm (a PostScript font converter for TeX),
tetex-dvilj (for converting .dvi files to HP PCL format for printing on
HP and HP compatible printers), tetex-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), and tetex-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX).  If you're not a TeX expert, you'll probably also
want to install the tetex-doc package, which contains documentation for
the TeX text formatting system.

%package dvips
Summary: A DVI to PostScript converter for the TeX text formatting system
Group: Publishing
PreReq: tetex-core = %PACKAGE_VERSION-%release

%description dvips
Dvips converts .dvi files produced by the TeX text formatting system
(or by another processor like GFtoDVI) to PostScript(TM) format.
Normally the PostScript file is sent directly to your printer.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-dvips.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvilj (for converting .dvi files to HP PCL format for
printing on HP and HP compatible printers), tetex-latex (a higher level
formatting package which provides an easier-to-use interface for TeX)
and tetex-xdvi (for previewing .dvi files in X).  If you're installing
TeX and you're not an expert at it, you'll also want to install the
tetex-doc package, which contains documentation for the TeX system.

%package dvilj
Summary: A DVI to HP PCL (Printer Control Language) converter
Group: Publishing
PreReq: tetex-core = %PACKAGE_VERSION-%release

%description dvilj
Dvilj and dvilj's siblings (included in this package) will convert TeX
text formatting system output .dvi files to HP PCL (HP Printer Control
Language) commands.  Using dvilj, you can print TeX files to HP LaserJet+
and fully compatible printers.  With dvilj2p, you can print to HP LaserJet
IIP and fully compatible printers.  And with dvilj4, you can print to
HP LaserJet4 and fully compatible printers.

If you are installing teTeX, so that you can use the TeX text formatting
system, you will also need to install tetex-dvilj.  In addition, you will
need to install tetex-afm (for converting PostScript font description
files), tetex-dvips (for converting .dvi files to PostScript format for
printing on PostScript printers), tetex-latex (a higher level formatting
package which provides an easier-to-use interface for TeX) and tetex-xdvi
(for previewing .dvi files in X).  If you're installing TeX and you're
not a TeX expert, you'll also want to install the tetex-doc package,
which contains documentation for TeX.

%package afm
Summary: A converter for PostScript(TM) font metric files, for use with TeX
Group: Publishing
PreReq: tetex-core = %PACKAGE_VERSION-%release

%description afm
tetex-afm provides afm2tfm, a converter for PostScript font metric files.
PostScript fonts are accompanied by .afm font metric files which describe
the characteristics of each font.  To use PostScript fonts with TeX,
TeX needs .tfm files that contain similar information.  Afm2tfm will
convert .afm files to .tfm files.

If you are installing tetex in order to use the TeX text formatting
system, you will need to install tetex-afm.  You will also need to install
tetex-dvilj (for converting .dvi files to HP PCL format for printing on
HP and HP compatible printers), tetex-dvips (for converting .dvi files
to PostScript format for printing on PostScript printers), tetex-latex
(a higher level formatting package which provides an easier-to-use
interface for TeX) and tetex-xdvi (for previewing .dvi files in X).
Unless you're an expert at using TeX, you'll probably also want to
install the tetex-doc package, which includes documentation for TeX.

%package doc
Summary: The documentation files for the TeX text formatting system
Group: Publishing
AutoReq: no
Requires: tetex-core = %PACKAGE_VERSION-%release

%description doc
This package contains documentation for the TeX text formatting system.

If you want to use TeX and you're not an expert at it, you should
install the tetex-doc package.  You'll also need to install the tetex
package, tetex-afm (a PostScript font converter for TeX), tetex-dvilj
(for converting .dvi files to HP PCL format for printing on HP and HP
compatible printers), tetex-dvips (for converting .dvi files to PostScript
format for printing on PostScript printers), tetex-latex (a higher level
formatting package which provides an easier-to-use interface for TeX)
and tetex-xdvi (for previewing .dvi files).

%package devel
Summary: Development files for KPathsea library
Group: Development/C
Requires: tetex-core = %PACKAGE_VERSION-%release

%description devel
This package contains development files for KPathsea library used in
teTeX to find files in TeX source tree.

%package context
Summary: The ConTeXt frontend for the TeX text formatting system
Group: Publishing
Requires: tetex-core = %PACKAGE_VERSION-%release

%description context
ConTeXt is a front end for the TeX text formatting system.  It is well
suited for creation of complex interactive documents like ebooks or
assesments.  Documents prepared with ConTeXt's aid look good both in
PDF format and when printed on paper.

%prep
%setup -q -n %pkgname-src-%texversion
mkdir texmf
pushd texmf
tar xf %SOURCE1
tar xf %SOURCE5
popd
tar xf %SOURCE2
pushd ec-plain
    mkdir -p ../texmf/fonts/source/ec-plain
    cp *.mf ../texmf/fonts/source/ec-plain/
popd

# teTeX patches
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# texmf patches
pushd texmf
%patch11 -p2
#%patch12 -p2

# Remove mappings from dvips/config as they will be re-generated in %_sysconfdir/tex-fonts
for i in builtin35.map download35.map dvipdfm_dl14.map dvipdfm.map dvipdfm_ndl14.map \
  pdftex_dl14.map pdftex.map pdftex_ndl14.map ps2pk.map psfonts.map ../base/psfonts.map \
  psfonts_pk.map psfonts_t1.map ; do
    rm -f dvips/config/$i
done

%patch13 -p1
popd

# Hack out dependencies on /bin/sh5 and /bin/bsh.
grep -ErlZ 'exec /bin/(sh5|bsh)' . |
	xargs -r0 sed -i 's,exec /bin/\(sh5\|bsh\),exec /bin/sh,g' --

# Fix dvi-draw.c
%patch14 -p1

# Fix extra deps in shell scripts
%patch15 -p1

# Security patches
%patch20 -p1
%patch21 -p1 
%patch22 -p1
%patch23 -p1

# Fix build with glibc-2.10+
sed -i s/getline/texk_getline/g \
	texk/dvipsk/afm2tfm.c texk/web2c/mpware/mpto.c
sed -i 's|^.*grep @error@ \$output_files.*|sed -i s/getline/webc_getline/g \$output_files; &|' texk/web2c/web2c/convert

%build
sh ./reautoconf
%configure \
	--with-system-zlib \
	--with-system-pnglib \
	--with-system-t1lib \
	--with-system-ncurses \
	--with-system-tifflib \
	--with-system-wwwlib \
	--disable-multiplatform \
	--without-dialog \
	--without-texinfo \
	--without-t1utils \
	--enable-ipc \
	--enable-a4 \
	--disable-shared \
	--enable-static 
	

# SMP-incompatible build.
make

%install
mkdir -p %buildroot%_datadir/texmf
mkdir -p %buildroot%_localstatedir/texmf
mkdir -p %buildroot%_cachedir/texmf
mkdir -p %buildroot%_sysconfdir/tex-fonts{,.d}

pushd texmf
tar cf - . | tar xf - -C %buildroot%_datadir/texmf
popd

export LD_LIBRARY_PATH=%buildroot%_libdir
export MT_DONT_INSTALL_PK=1

%makeinstall texmf=%buildroot%_datadir/texmf
cp %buildroot%_datadir/texmf/web2c/updmap.cfg %buildroot%_sysconfdir/tex-fonts.d/00updmap.cfg

# Remove texinfo files.
find %buildroot -type f -name texi2pdf\* -delete
rm -r %buildroot%_datadir/texmf/tex/texinfo

#
# Generate tfm metrics for all standard fonts
#
export PATH=%buildroot%_bindir:$PATH
export TEXMFMAIN=%buildroot%_datadir/texmf
for e in T1 OT1 T2A T2B T2C X2 ; do
    allcm -n -e $e 2>/dev/null
done

unset LD_LIBRARY_PATH

rm -f %buildroot%_infodir/dir

# Explicitly remove readlink (better implementation added in coreutils).
find %buildroot -name 'readlink*' -delete

# these are links

install -pDm755 %_sourcedir/%name.cron %buildroot%_sysconfdir/cron.daily/%name

find %buildroot%_man1dir -type f -print0 |
	xargs -r0 chmod 644
ln -s mf.1 %buildroot%_man1dir/mfw.1

# call the brp-compress script before creating the file list
/usr/lib/rpm/brp.d/032-compress.brp

### Files list
find %buildroot -type f -or -type l | \
	sed -e "s|%buildroot||g" | \
	grep -v "^/etc" | grep -v '.orig$' | \
	sed -e 's|.*\.cnf$|%%config(noreplace) &|' \
            -e 's|%_datadir/texmf/dvips/config/config\.ps$|%%config(noreplace) &|' \
	    -e 's|%_datadir/texmf/dvips/config/config\.\(generic\|pdf\|www\)$|%%config &|' \
	    -e 's|%_datadir/texmf/xdvi/XDvi|%%config &|' \
	    -e 's|%%config\(noreplace\) %_datadir/texmf/web2c/texmf\.cnf$|%%config\(replace\) %_datadir/texmf/web2c/texmf\.cnf|' \
	    >filelist.full

find %buildroot%_datadir/texmf -mindepth  1 -type d | \
	sed "\,%_datadir/texmf/doc$,d; s|^%buildroot|\%%attr(755,root,root) \%%dir |" >> filelist.full

# subpackages
grep -v "/doc/" filelist.full | grep latex 	> filelist.latex

grep -v "/doc/" filelist.full | grep xdvi | \
	grep -v "%_datadir/texmf/tex"		> filelist.xdvi

# Move metafont to xdvi due to xorg deps
for f in mfw mf inimf virmf; do
	echo "%_bindir/$f"
	echo "%_man1dir/$f.1"
done >>filelist.xdvi

# Do not include dvips configs into dvips subpackage as they are now
# required by XDvi as well
grep -v "/doc/" filelist.full | grep dvips | \
	grep -v "%_datadir/texmf/tex" | \
	grep -v "%_datadir/texmf/dvips"		> filelist.dvips
echo "%_bindir/dvired" >> filelist.dvips
echo "%_bindir/dvi2fax" >> filelist.dvips

grep -v "/doc/" filelist.full | grep dvilj | \
	grep -v "%_datadir/texmf/tex/latex" 	> filelist.dvilj

grep -v "/doc/" filelist.full | grep afm 	> filelist.afm

grep "/doc/" filelist.full 			> filelist.doc_temp
grep "texdoc" filelist.full			>> filelist.doc_temp
sort -u -o filelist.doc_temp filelist.doc_temp
cat filelist.doc_temp | grep -v "/doc/context" | sort | uniq -u	> filelist.doc

grep "/usr/include/" filelist.full 		> filelist.devel

# Separate ConTeXt
egrep "%_datadir/texmf/(tex/|doc/|)context" filelist.full	> filelist.context
egrep "%_bindir/(texexec|texshow|texfind|texfont|texutil|mptopdf|fdf2tan|makempy)" filelist.full >>filelist.context
egrep "%_cachedir/texmf/web2c/(cont-.*|metafun|mptopdf)" filelist.full >>filelist.context
egrep "%_man1dir/(cont-en|cont-de|cont-nl|texexec|texshow|texutil)" filelist.full >>filelist.context

# now files listed only once, i.e. not included in any subpackage, will
# go in the main package
cat filelist.full \
    filelist.latex \
    filelist.xdvi \
    filelist.dvips \
    filelist.dvilj \
    filelist.afm \
    filelist.devel \
    filelist.doc \
    filelist.context | \
    sort | uniq -u > filelist.core
    
 find texk -type f -\( \
    -name ChangeLog -or \
    -name 'README*' \
    -\) |sed -e 's|^texk/|%%doc &|'|egrep -v "(make|etc|djgpp)/" > filelist.main

# xdvi menu things
mkdir -p %buildroot%_menudir
cat > %buildroot%_menudir/tetex-xdvi <<EOF
?package(tetex-xdvi): command="%_bindir/xdvi" needs="X11" \
icon="dvi.xpm" section="Applications/Publishing" title="xdvi" \
longtitle="DVI files viewer"
EOF

#mdk icons
install -d %buildroot%_iconsdir
tar xf %SOURCE4 -C %buildroot%_iconsdir

# Settings for Emacs' TeX mode:
%define _emacssite %_sysconfdir/emacs/site-start.d
dest="%buildroot%_emacssite"
mkdir -p "$dest"
pkg=xdvi
 install -pm644 %SOURCE101 "$dest"/$pkg.el
 echo "%%config(noreplace) %_emacssite/$pkg.el" >> filelist.$pkg
pkg=dvips
 install -p -m0644 %SOURCE102 "$dest"/$pkg.el
 echo "%%config(noreplace) %_emacssite/$pkg.el" >> filelist.$pkg
pkg=dvilj
 install -p -m0644 %SOURCE103 "$dest"/$pkg.el
 for f in $(cat filelist.dvilj | fgrep /usr/bin/dvilj); do
    name="$(basename "$f")"
    echo ";(setq tex-dvi-print-command \"$name -e- * | lpr\")" >> "$dest"/$pkg.el
 done
 echo "%%config(noreplace) %_emacssite/$pkg.el" >> filelist.$pkg
unset dest

%pre core
if [ -d %_datadir/texmf/dvipdfm/config ]; then
	rm -rf %_datadir/texmf/dvipdfm/config
fi

%post core
x=/usr/bin/updmap && [ -x "$x" ] && "$x"  2>/dev/null ||:

%preun core
x=/usr/bin/updmap && [ -x "$x" ] && "$x"  2>/dev/null ||:

%files -f filelist.core core
%attr(1777,root,root) %dir %_localstatedir/texmf
%attr(755,root,root) %dir %_sysconfdir/tex-fonts
%attr(755,root,root) %dir %_cachedir/texmf/web2c
%config %_sysconfdir/cron.daily/%name
%config %_sysconfdir/tex-fonts.d/*

%files -f filelist.latex latex
%attr(755,root,root) %dir %_cachedir/texmf/web2c

%files -f filelist.context context
%attr(755,root,root) %dir %_cachedir/texmf/web2c

%files -f filelist.xdvi xdvi
%_menudir/tetex-xdvi
%_iconsdir/*.xpm
%_iconsdir/*/*.xpm
%doc texk/xdvik/README.t1fonts

%files -f filelist.dvips dvips

%files -f filelist.dvilj dvilj

%files -f filelist.afm afm

%files -f filelist.doc doc

%files -f filelist.devel devel

%files -f filelist.main
%doc PROBLEMS* README ChangeLog

%changelog
* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt11
- Repair build with rpm >= 4.0.4-alt100.45 (thanks vitty@)

* Sat Jul 25 2009 Kirill Maslinsky <kirill@altlinux.org> 2.0-alt10
- built with rpm-build-texmf

* Sun May 17 2009 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt9
- tetex-core: Removed files packaged in texinfo >= 4.13-alt1.
- Removed install-info invocations.
- Fixed build with glibc >= 2.10.

* Sat Apr 25 2009 Grigory Batalov <bga@altlinux.ru> 2.0-alt8
- Hide hbf2gf call from rpm findreq to avoid texlive dependence.

* Thu Apr 23 2009 Grigory Batalov <bga@altlinux.ru> 2.0-alt7
- %%_datadir/texmf/doc was moved to tex-common.
- Require tex-common because of it's filetriggers.
- Don't call texhash in %%post-scripts as filetrigger will do it.
- Remove obsolete %%update_menus call.

* Tue Feb 24 2009 Grigory Batalov <bga@altlinux.ru> 2.0-alt6
- %%_sysconfdir/tex-fonts.d and %%_cachedir/texmf were moved to tex-common.

* Mon Sep 01 2008 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt5
- Packaged intermediate subdirectories to fix build.

* Tue Apr 01 2008 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt4
- Dropped readlink remnants to fix build.
- Tweaked shell scripts to avoid extra requirements.
- Packaged symlinks to %_bindir/mfw in -xdvi subpackage
  (as long as %_bindir/mfw executable is packaged there).

* Sat Apr 01 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt3
- Updated build dependencies, rebuilt in new environment.

* Mon Feb 06 2006 Vladimir Lettiev <crux@altlinux.ru> 2.0-alt2.4
- Fix compile failure in dvi-draw.c (patch from gentoo #118264)

* Fri Dec 30 2005 Vladimir Lettiev <crux@altlinux.ru> 2.0-alt2.3
- SECURITY FIXES:
  + CVE-2004-0888
  + CVE-2004-1125 
  + CVE-2005-0064
  + CVE-2005-3191, CVE-2005-3192
- Fix build: changed buildrequires flex -> flex-old
- Build with system w3c-libwww (this also fix CVE-2005-3183)

* Tue May 03 2005 Anton D. Kachalov <mouse@altlinux.org> 2.0-alt2.2
- x86_64 support

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt2.1
- Rebuilt with libstdc++.so.6.

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt2
- %name-core: corrected dependencies.
- %name-core: fixed shell dependencies in texconfig and fmtutil.
- %name-context: fixed perltk build problems (at).
- Fixed "/bin/sh5" and "/bin/bsh" dependencies.
- %name-xpdf: rebuilt with libt1.so.5
- Eliminated %%clean section.

* Sun Jan 26 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt1
- 2.0 release candidate 1

* Mon Jan 20 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.9
- Remove %_datadir/texmf/dvipdfm/config directory before installing
  tetex-core because structure of that subtree has been changed in
  20030107 beta.

* Fri Jan 17 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.8
- 2.0 beta (20030112)
- Finally updmap is working with new config files scheme (see patch7)
- tetex-fonts-source brought back into tetex-core after
  Vladimir Volovich (vvv@vsu.ru) suggestions
- Added:
    + exmi font family for use with EC fonts in PlainTeX
    + Russian and Ukrainian ConTeXt support (Olya Briginets and me)
- Removed:
    + rupdmap because need functionality was integrated back into updmap
- Separated:
    + ConTeXt moved to a subpackage

* Sun Jan 12 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.7
- 2.0 beta (20030107)
- Slightly modified source decomposition
- Fixed portability issues in rupdmap for Ruby 1.6/1.8 betas
- Added default umask of 022 in rupdmap to make sure that 
  created files are always readble by world
- Obsoletes dvipdfm since it is now part of teTeX
- More documentation (ChangeLogs and README) from sources added 

* Tue Jan 07 2003 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.6
- 2.0 beta (20021210):
    + updated pdftex to version 1.10a-RC1
- Fix dependency on cm-super-fonts-tex for %name main package

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.5
- Added common documentation to tetex package
- Moved texdoc{,tk} to doc subpackage

* Fri Nov 22 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.4
- Moved tetex base to tetex-core in order to eliminate dependency
  loop with fonts-cm-super-tex. Now tetex package pre-requires tetex-core 
  and fonts-cm-super-tex while the latter pre-requires tetex-core only.

* Fri Nov 22 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.3
- Imported rupdmap-1.0 into main tetex package
- spec cleanups
- Forward provide ConTeXT perl modules so that perlreq output for
  tetex package will have some meaning

* Thu Nov 21 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.2
- 2.0 beta (20021116)
- use cm-super fonts from fonts-cm-super-tex package

* Wed Oct 23 2002 Alexander Bokovoy <ab@altlinux.ru> 2.0-alt0.1
- 2.0 beta (20021017)
- All system wide libraries are used instead of locally provided ones
- Rebuild with gcc 3.2
- Type1 support enabled by default
- MetaFont sources distributed in tetex-fonts-source subpackage
- Use ALT-specific updmap implementation (rupdmap)

* Tue Aug 27 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0.7-ipl21mdk
- Dropped %_bindir/readlink (better implementation added in
  fileutils-4.1.11-alt3) and added dependence on /bin/readlink.
- Moved cm-super subpackager under with/without logic control and disabled
  packaging by default.
- Updated Packager tag.
- Specfile remains dirty, any volunteers to cleanup?

* Sun Dec 23 2001 Ivan Zakharyaschev <imz@altlinux.ru> 1.0.7-ipl20mdk
- fix an error in the way how dvilj* were suggested to call from Emacs for 
  printing (introduced in the previous change): they used to print to a
  file, now they pass the output to "lpr".

* Sat Dec  8 2001 Ivan Zakharyaschev <imz@altlinux.ru> 1.0.7-ipl19mdk
- now subpackages that provide commands for viewing/printing DVIs
  put scripts that set corresponding Emacs' TeX mode variables to
  %_emacssite.

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.7-ipl18mdk
- Specfile partial cleanup.
- Rebuilt with libpng.so.3

* Tue Sep 25 2001 Alexander Bokovoy <ab@altlinux.ru> 1.0.7-ipl17mdk
- %name-cm-super package added with Cyrillic Type 1 fonts for
  EC/TC and LH from Vladimir Volovich.
- Type1 support in dvips is enabled by default
- Updmap now automagically adds cm-super fonts if they are installed

* Thu Mar 15 2001 AEN <aen@logic.ru> 1.0.7-ipl16mdk
- math accented patch from Ivan Zakharyashev

* Mon Dec 04 2000 AEN <aen@logic.ru>
- belarusian & kazakh support in babel
- rebuild for RE

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.7-14mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Sun Oct 22 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.7-13mdk
- BuildRequires: ed

* Tue Oct 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0.7-12mdk
- Allow to build (aka fix filelist)

* Tue Oct 03 2000 Daouda Lo <daouda@mandrakesoft.com> 1.0.7-11mdk
- add icons to xdvi menu entry.

* Mon Sep 25 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-10mdk
- included some of changes to SPEC files made by Alexander Skwar <ASkware@DigitalProjectcs.com>
  (more macros, fixed location of some manpage).

* Mon Aug 28 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-9mdk
- changed mandir to %%{_mandir}, and infodir to %%{_infodir}.
- xdvi menu name coherent.

* Fri Aug 25 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-8mdk
- added noreplace to *.cnf (Preston Brown <pbrown@redhat.com>)
- added noreplace to config.ps file.
- removed bzip2 of man pages (now handled by spec-helper).
- removed perl script to handle bzip2 files for filelists (now handled
  by spec-helper).
- increased trie size for allowing more hyphenation patterns (i18n).

* Fri Jun 02 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-7mdk
- updated the LaTeX hyperref package to version 6.70f for getting jadetex
  working.
- added support for spanish, portuguese and sweden pattern hyphenation in the
  default LaTeX format files (hope trie values are enough...).

* Fri May 05 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-6mdk
- fixed man pages permission.

* Sat Apr 29 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-5mdk
- changed arrays texmf.cnf the array value for jadetex, pdfjadetex, according to
  the Christoph, Rahtz, Pepping's "Installing JadeTeX" document.

* Sat Apr 01 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-4mdk
- change group (now "Publishing") according to the new scheme.
- removed wmconfig and .desktop entries for xdvi, and added the new menu
  entry.

* Fri Mar 03 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.7-3mdk
- updated teTeX-texmf to version 1.0.2.

* Fri Feb 11 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com>
- updated to version 1.0.7.
- merged k6 and arm patches into teTeX-1.0-arch.patch
- sligtly increased internal array main_memory, so that latex
  doesn't have problems with big macro packages such as pstricks
  or Xy-TeX.
- integrate teTeX-1.0-tektrokix.patch (fixes a typo) from Jeff
  Johnson <jbj@redhat.com>.

* Wed Dec 08 1999 - David BAUDENS <baudens@mandrakesoft.com>
- AMD K6 is not an i686 processor (another)
- Replace $RPM_ARCH by %%{_target_cpu}

* Thu Nov 11 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- mark /usr/share/texmf/dvips/config.ps as %%config
  (Jeff Johnson <jbj@redhat.com>, #4842)
- mark also config.pdf, config.www and config.generic as %%config.
- added BuildPreReq.

* Thu Aug 26 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fine tuning subpackage package list.
- added teTeX dependence to package xdvi (it cannot works without fonts).

* Wed Aug 25 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- cleaned %%clean. Now spec file support buildroot.
- added support for 'resolution' in dvi-to-ps.fpi as well as
  the config.generic file.
- fixed a problem in manpage links (reported by Dusan
  Gabrijelcic <dusan@kamra.e5.ijs.si>).
- moved mfw to tetex-xdvi to have main tetex package rpm indepedendent from
  X11 libraries (Jeff Johnson <jbj@redhat.com> in rawhide).
- added PAPERSIZE option to dvi-to-ps.fpi (Jeff Jonhson <jfj@redhat.com>
  in rawhide).

* Wed Aug 04 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- fixed VARTEXFONTS path in config file.

* Wed Jul 14 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- updated to 1.0.6.
- used src-1.0.6 archive and thus removed some patches.

* Sat Jun 26 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- mandrake adaptions.
- speed up TEXMFCNF path.

* Fri Jun 25 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- fixed new bugs reported by Thomas Esser (included
  patch 1.0.5-1.0.6-pre).
- added amstex, bamstex and bplain to the list of format files to build.

* Wed Jun 23 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- fixed and removed unneeded things in teTeX-1.0-texmfcnf.patch,
  according to Thomas Esser suggestions.

* Sun Jun 20 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- upgraded to teTeX 1.0.5.
- merged .spec file with Jeff Johnson's 1.0.1 .spec file from rawhide.

* Sun Jun 13 1999 Giuseppe Ghibò <ghibo@caesar.polito.it>
- upgraded to teTeX 1.0 final.
- removed texmf.cnf external config file, and provided
  as patch.
- removed ``texconfig init'' (now it's included into 'make install').
- moved texmf unpacking to buildroot before 'make install'.
- added italian hyphenation.

* Thu Jun 03 1999 Kayvan A. Sylvan <kayvan@sylvan.com>
- upgraded snapshot
- Fixed PATH setting for ``texconfig init''. As it was, you could
  not build a working teTeX on a machine with teTeX installed.

* Thu Apr 01 1999 Cristian Gafton <gafton@redhat.com>
- upgraded snapshot

* Tue Mar 23 1999 Erik Troan <ewt@redhat.com>
- set limits for jadetex

* Tue Mar 23 1999 Cristian Gafton <gafton@redhat.com>
- I think I have got the buildroot problems right this time
- auto rebuild in the new build environment (release 15)

* Fri Mar 19 1999 Cristian Gafton <gafton@redhat.com>
- fix buildroot problems

* Mon Mar 15 1999 Michael Maher <mike@redhat.com>
- fixed BUG: 978

* Thu Mar 11 1999 Cristian Gafton <gafton@redhat.com>
- slight changes in the packaging (unpack texmf directly into the buildroot
  and build it there)
- added texmfsrc source tarball to comply with the license

* Mon Mar 07 1999 Michael Maher <mike@redhat.com>
- updated package

* Mon Jan 11 1999 Cristian Gafton <gafton@redhat.com>
- add patch to make it compile on the arm (RmS)
- build for glibc 2.1
- use tar hack instead of the cp -a to overcome cp's brokeness re: symlinks
  handling

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- enable italian formatting

* Mon Oct 05 1998 Cristian Gafton <gafton@redhat.com>
- requires ed
- Fixed obsoletes line
- credted the doc subpackage
- fully buildroot
- require dialog in the main package
- add support for wmconfig in for the xdvi package

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 0.9
- texmf-src package is gone
- use /var/lib/texmf instead of /var/tmp/texmf

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- make sub-packages depend on teTeX (problem #214)

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- eliminate environment when running texhash (problem #849)

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Feb  5 1998 Otto Hammersmith <otto@redhat.com>
- added install-info support (dvips, fontname and kpathsea)
- combined the two changelogs in the spec file.

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- Fixed dvi-to-ps.fpi to create temp files more safely.

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr  8 1997 Michael Fulbright <msf@redhat.com>
- Removed afmdoit from file list (mistakenly added in release 3 rpm)

* Mon Mar 24 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to tetex-lib to 0.4pl8 and fixed cron tmpwatch entry to not
  delete /var/lib/texmf/fonts and /var/lib/texmf/texfonts

* Fri Mar 07 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl7.

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl6, and fixed file permissions on /var/lib/texmf/texfonts
  so normal users could create fonts on demand.
