Name: TeXmacs
Version: 1.0.7.15
Release: alt1

Summary: A WYSIWYG mathematical text editor
License: GPL
Group: Editors
URL: http://www.texmacs.org

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: ftp://ftp.texmacs.org/pub/TeXmacs/targz/TeXmacs-%version-src.tar.gz
Source1: TeXmacs-16.xpm
Source2: TeXmacs-36.xpm
Source3: TeXmacs-48.xpm
Source4: TeXmacs.desktop

Patch1: TeXmacs-1.0.6.11-maxima.patch
Patch2: TeXmacs-1.0.4-axiom.patch
Patch5: TeXmacs-1.6.0.7-rdelim.patch
Patch7: TeXmacs-psfix.patch
Patch8: texmacs-CVE-2010-3394.patch

Requires: guile18 /usr/bin/latex slocate libltdl

#BuildRequires: guile18 guile18-devel xorg-devel tetex gcc4.3 gcc4.3-c++ autoconf libltdl-devel
BuildRequires: guile18 guile18-devel tetex gcc gcc-c++ autoconf libltdl-devel

BuildPreReq: libX11-devel libICE-devel libfreetype-devel ghostscript
BuildPreReq: libXext-devel zlib-devel
# libqt4-devel kdevelop-qmake qconf

%add_python_req_skip  sage

%description
GNU TeXmacs is a free scientific text editor, which was both inspired
by TeX and GNU Emacs. The editor allows you to write structured documents
via a WYSIWYG (what-you-see-is-what-you-get) and user friendly interface. 
New styles may be created by the user. The program implements high-quality 
typesetting algorithms and TeX fonts, which help you to produce 
professionally looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface
for computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and
write your own extensions to the editor.

In the future, TeXmacs is planned to evoluate towards
a complete scientific office suite, with spreadsheet capacities,
a technical drawing editor and a presentation mode.


%prep
%setup -q -nTeXmacs-%version-src

#patch1 -p1
#patch2 -p1

%patch5 -p1
%patch7 -p1
#patch8 -p1
sed -i "s|LDPATH = \@CONFIG_BPATH\@|LDPATH =|" src/makefile.in
sed -i "s|5\.14\.\*|5.15.*|" plugins/maxima/bin/tm_maxima

%build
#export CC=gcc-4.3 CXX=g++-4.3
#set_automake_version 1.10
#set_autoconf_version 2.5
#autoconf

#CC="gcc"`echo "%optflags" | %__sed -e "s:%optflags_default::"`
#export CC
#CXX="g++"`echo "%optflags" | %__sed -e "s:%optflags_default::"`
#export CXX
sed -i 's|\-static||g' configure
sed -i 's|\-O3|-g -O3|g' configure
./configure --prefix=%prefix --libexecdir=%_libexecdir --mandir=%_mandir \
     --build=%_target_platform --host=%_target_platform --target=%_target_platform --disable-qt

make 

%install
%define _findreq_default_method lib

make DESTDIR=%buildroot install
export GUILE_DATA_PATH=`guile-config info pkgdatadir`
export GUILE_LOAD_PATH=`find $GUILE_DATA_PATH -type d | grep ice-9 | grep 6`
#cp -r -f $GUILE_LOAD_PATH %buildroot%_datadir/TeXmacs/progs
cp -r -f TeXmacs/progs/ %buildroot%_datadir/TeXmacs/progs
#chmod -f 644 %buildroot%_datadir/TeXmacs/progs/ice-9/*
#chmod -f 755 %buildroot%_datadir/TeXmacs/progs/ice-9
mkdir -p %buildroot/etc/X11/applnk/Applications
mkdir -p %buildroot/usr/share/application-registry
mkdir -p %buildroot/usr/share/mime-info
mkdir -p %buildroot/usr/share/pixmaps
cp -f %buildroot%_datadir/TeXmacs/misc/mime/texmacs.desktop %buildroot/etc/X11/applnk/Applications
cp -f %buildroot%_datadir/TeXmacs/misc/mime/texmacs.applications %buildroot/usr/share/application-registry
cp %buildroot%_datadir/TeXmacs/misc/mime/texmacs.keys %buildroot/usr/share/mime-info
cp %buildroot%_datadir/TeXmacs/misc/mime/texmacs.mime %buildroot/usr/share/mime-info
cp %buildroot%_datadir/TeXmacs/misc/pixmaps/TeXmacs.xpm %buildroot/usr/share/pixmaps

install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir
install -d %buildroot%_liconsdir

install -d %buildroot%_menudir

install -D -m644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -D -m644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -D -m644 %SOURCE3 %buildroot%_liconsdir/%name.xpm

# menu entry
install -D -m644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
#mkdir -p %buildroot%_menudir
#cat >%buildroot%_menudir/%name <<EOF
#?package(%name): command="%_bindir/texmacs" section="Applications/Editors" \
#icon="TeXmacs.xpm" needs="x11" title="TeXmacs" \
#longtitle="A WYSIWYG mathematical text editor"
#EOF

%files
%_bindir/texmacs
%_bindir/fig2ps
%_includedir/TeXmacs.h
%_mandir/man1/texmacs.1*
%_mandir/man1/fig2ps.1*
%_datadir/TeXmacs
%_libexecdir/TeXmacs
%exclude /etc/X11/applnk/Applications/texmacs.desktop
/usr/share/application-registry/texmacs.applications
/usr/share/mime-info/texmacs.keys
/usr/share/mime-info/texmacs.mime
/usr/share/pixmaps/TeXmacs.xpm
/usr/share/icons/gnome/scalable/apps/TeXmacs.svg
/usr/share/icons/gnome/scalable/mimetypes/text-texmacs.svg
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm



%changelog
* Sun Apr 15 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.15-alt1
- 1.0.7.15
- build without qt

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7.11-alt1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.11-alt1
- 1.0.7.11

* Wed Aug 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7.10-alt1.2
- Fixed build

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7.10-alt1.1
- Fixed build

* Fri Mar 11 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.10-alt1
- 1.0.7.10

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.9-alt1
- 1.0.7.9

* Sun Nov 28 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.8-alt1
- 1.0.7.8

* Sat Oct 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.7-alt1
- 1.0.7.7
- fix CVE-2010-3394 (Etienne Millon) (Closes: #24328)

* Thu Sep 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.6-alt1
- 1.0.7.6

* Fri Jul 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.5-alt1
- 1.0.7.5

* Sat Jun 05 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.4-alt2
- rebuild once again with guile18

* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.4-alt1
- 1.0.7.4

* Sat Nov 28 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.3-alt1
- 1.0.7.3

* Thu Sep 03 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.2-alt2
- fix desktop file
- fix icons locations

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.2-alt1.1
- change requires from tetex-latex to /usr/bin/latex (Closes: #20275)

* Sat Aug 01 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.7.2-alt1
- 1.0.7.2

* Fri Oct 17 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Fri Sep 19 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.6.15-alt0.2
- add %%add_python_req_skip  sage, fix bug #17167

* Tue Sep 09 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.6.15-alt0.1
- 1.0.6.15

* Sun Sep 23 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.11-alt1
- TeXmacs 1.0.6.11.
- Maxima 5.13.
- Russian description and summary removed.

* Sun May 06 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.9-alt1
- TeXmacs 1.0.6.9.
- Maxima 5.12.

* Tue Dec 26 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.7-alt1
- Maxima 5.11 for all Lisp implementations.

* Sat Dec 23 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.6-alt4
- Maxima 5.11.

* Sat Oct 14 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.6-alt3
- Rebuilt with new toolchain.

* Wed Sep 27 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.6-alt2
- Maxima 5.10.0 compatibility fix.

* Thu Sep 21 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6.6-alt1
- TeXmacs 1.0.6.6.

* Mon May 15 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6-alt2
- Force gcc 3.4 due to gcc 4.1 incompatibility.

* Sun Apr 02 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.6-alt1
- TeXmacs 1.0.6.

* Sun Oct 23 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.5-alt2
- Rebuild for x86_64.

* Tue May 03 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.5-alt1
- TeXmacs 1.0.5.

* Sat Sep 25 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.4-alt1
- TeXmacs 1.0.4-R3.

* Sat Jun 05 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.3-alt3
- Russian LaTeX export fixed.
- Bug #3802 fixed.

* Thu May 27 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.3-alt2
- fix for Maxima versions.  

* Wed May 12 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.3-alt1
- TeXmacs 1.0.3-R2.

* Sun Nov 30 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.2.9-alt2
- Axiom support.

* Sat Nov 29 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.2.9-alt1
- TeXmacs 1.0.2.9
- Better Maxima session support.

* Thu Oct 02 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.2-alt1
- TeXmacs 1.0.2
- menu entry, icons, Russian description.

* Wed Sep 17 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1.23-alt1
- TeXmacs 1.0.1.23
- require on slocate and tetex-latex

* Tue Aug 26 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt4
- pass -march -mcpu to configure/make via CC and CXX

* Sun Jul 20 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt3
- BuildRequires on gcc-c++.

* Wed Jul 16 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt2
- fixed guile guile dependence.
- let ./configure automatically determine required optimization
  to prevent segfaults with gcc 3.*.

* Fri Jan 03 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt1
- TeXmacs 1.0.1 

* Wed Oct 23 2002 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.0.19-alt1
- Spec cleanup
- Build with gcc 3.2

* Sat Aug 17 2002 ZW <vvzhy@mail.ru>
- Russian transliteration is removed since it
  practically useless and even confusing in
  Russian language environment (BTS #0000927)

* Sat Jul 20 2002 ZW <vvzhy@mail.ru>
- Now TeXmacs works well with new Maxima 5.9.0.
  Default lisp can be chosen via TEXMACS_MAXIMA_LISP
  environment variable.  Available options are
  gcl or clisp (cmucl doesn't work well yet).

* Wed Mar 27 2002 ZW <vvzhy@mail.ru>
- fixed spurious automatic dependence on maxima

* Wed Mar 20 2002 ZW <vvzhy@mail.ru>
- TeXmacs 1.0
- it seems that we no longer need compat-gcc

* Wed Mar 21 2001 AEN <aen@logic.ru>
- guile-devel in requires

* Tue Jan 30 2001 AEN <aen@logic.ru>
- jcuken keyboard by default

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation
- build w/o cyrillic patch
* Thu Jan 09 2001 AEN <aen@loigc.ru>
- first build for RE
- cyrillic patch

