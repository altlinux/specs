%def_with xft
%def_with gpm

%def_with pdump
%def_with newgc
%def_with kkcc

%def_without ldap
%def_without postgresql
%def_without alsa

Name: xemacs
Version: 21.5.31
Release: alt1

%add_findreq_skiplist %_xemacs_etcdir/*

Summary: Things needed to run the XEmacs text editor
License: GPLv3
Group: Editors
Url: http://www.xemacs.org/

Source: %name-%version-%release.tar

BuildPreReq: alternatives >= 0.2 xemacsen >= 0.5-alt1
BuildRequires: libcompface-devel libdb4-devel libjpeg-devel libncurses-devel
BuildRequires: libpng-devel libtiff-devel libXau-devel libXaw3d-devel
BuildRequires: libXext-devel libXmu-devel libXpm-devel xorg-bitmaps zlib-devel
%{?_with_gpm:BuildRequires: libgpm-devel}
%{?_with_ldap:BuildRequires: libldap-devel}
%{?_with_postgresql:BuildRequires: postgresql-devel}
%{?_with_alsa:BuildRequires: libalsa-devel}
%{?_with_xft:BuildRequires: libXft-devel fontconfig-devel >= 2.5.0-alt1}

%package minimal
Summary: Minimal set needed to run the XEmacs
Group: Editors
Requires: xemacsen >= 0.5-alt1 %name = %version-%release
Provides: xemacs-mule-minimal = %version-%version
Obsoletes: xemacs-mule-minimal

%package x11
Summary: The XEmacs text editor for X
Group: Editors
PreReq: xemacsen >= 0.5-alt1
Requires: %name-minimal = %version-%release
Provides: %name = %version-%release
Provides: %name-mule  = %version-%release
Conflicts: app-defaults < 0.2.1-alt1

%package nox
Summary: The XEmacs text editor without X support
Group: Editors
PreReq: xemacsen >= 0.5-alt1
Requires: %name-minimal = %version-%release
Provides: %name = %version-%release
Provides: %name-mule = %version-%release %name-nox-mule = %version-%release

%package extras
Summary: Files that XEmacs has in common with GNU Emacs
Group: Editors
Requires: %name = %version-%release
Conflicts: emacs-common
Provides: /usr/bin/b2m, /usr/bin/etags

%package devel
Summary: Header files for XEmacs
Group: Development/C
Requires: %name = %version-%release

%description
XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
extensible, real-time display editor.  XEmacs is self-documenting
because at any time you can type in control-h to find out what your
options are or to find out what a command does.  XEmacs is customizable
because you can change the definitions of XEmacs commands to anything
you want.  XEmacs is extensible because you can write entirely new
commands--programs in the Lisp language to be run by Emacs' own Lisp
interpreter.  XEmacs includes a real-time display, which means that the
text being edited is visible on the screen and is updated very
frequently (usually after every character or pair of characters) as you
type.

%description minimal
XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
extensible, real-time display editor.  XEmacs is self-documenting
because at any time you can type in control-h to find out what your
options are or to find out what a command does.  XEmacs is customizable
because you can change the definitions of XEmacs commands to anything
you want.  XEmacs is extensible because you can write entirely new
commands--programs in the Lisp language to be run by Emacs' own Lisp
interpreter.  XEmacs includes a real-time display, which means that the
text being edited is visible on the screen and is updated very
frequently (usually after every character or pair of characters) as you
type.

This package contains minimal set you need to run the XEmacs editor, so you
need to install this package if you intend to use XEmacs.  You also need
to install the actual XEmacs program package (%name-x11 or %name-nox).

%description x11
XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
extensible, real-time display editor.  XEmacs is self-documenting
because at any time you can type in control-h to find out what your
options are or to find out what a command does.  XEmacs is customizable
because you can change the definitions of XEmacs commands to anything
you want.  XEmacs is extensible because you can write entirely new
commands--programs in the Lisp language to be run by Emacs' own Lisp
interpreter.  XEmacs includes a real-time display, which means that the
text being edited is visible on the screen and is updated very
frequently (usually after every character or pair of characters) as you
type.

This package contains the XEmacs binary for X Window System.

%description nox
XEmacs (and regular GNU Emacs, too) is a self-documenting, customizable,
extensible, real-time display editor.  XEmacs is self-documenting
because at any time you can type in control-h to find out what your
options are or to find out what a command does.  XEmacs is customizable
because you can change the definitions of XEmacs commands to anything
you want.  XEmacs is extensible because you can write entirely new
commands--programs in the Lisp language to be run by Emacs' own Lisp
interpreter.  XEmacs includes a real-time display, which means that the
text being edited is visible on the screen and is updated very
frequently (usually after every character or pair of characters) as you
type.

This package contains the XEmacs binary without X Window System support

%description devel
Contains all the header files needed for XEmacs development.

%description extras
XEmacs-extras includes files which are used by both GNU Emacs
and XEmacs. If you don't have GNU Emacs installed, be sure to also
install this package when you install the XEmacs text editor.

%prep
%setup

%build
XEMACS_CONFIG="\
       --with-etcdir=%_xemacs_etcdir \
       --with-archlibdir=%_xemacs_archlibdir \
       --with-lispdir=%_xemacs_lispdir \
	--infodir=%_xemacs_infodir \
	--with-late-packages=%_datadir/%name \
	--with-infopath=%_xemacs_infodir:%_infodir \
	--without-debug \
	--without-error-checking \
	--without-assertions \
	%{subst_with pdump} \
	%{subst_with kkcc} \
	%{subst_with newgc} \
	--with-rel-alloc \
	--without-clash-detection \
	--with-pop \
	--with-mail-locking=lockf \
	--with-sound=none%{?_with_alsa:,alsa} \
	--with-mule \
	--with-file-coding \
	--with-zlib \
	%{subst_with ldap} \
	%{subst_with postgresql}"

XEMACS_nox_CONFIG="\
	--with-docdir=%_xemacs_docdir-nox \
	--without-x11 \
	--with-tty=yes \
	--with-ncurses \
	%{subst_with gpm}"

XEMACS_x11_CONFIG="\
	--with-docdir=%_xemacs_docdir-x11 \
	--with-x11 \
	--with-athena=3d \
	--with-scrollbars=lucid \
	--with-menubars=lucid \
	--with-dialogs=athena \
	--with-widgets=athena \
	--with-xim=xlib \
	--with-xpm \
	--with-xface \
	%{?_with_xft:--with-xft=emacs,menubars,tabs,gauges} \
	--without-tty"

%undefine __libtoolize
%define _configure_script ../configure

rm -rf %_target_platform-x11 %_target_platform-nox
mkdir %_target_platform-x11 %_target_platform-nox

cd %_target_platform-x11
%configure $XEMACS_CONFIG $XEMACS_x11_CONFIG
%make_build
cd ..

cd %_target_platform-nox
%configure $XEMACS_CONFIG $XEMACS_nox_CONFIG
%make_build
cd ..

%install
%makeinstall -C %_target_platform-x11 \
    etcdir=%buildroot%_xemacs_etcdir \
    archlibdir=%buildroot%_xemacs_archlibdir \
    lispdir=%buildroot%_xemacs_lispdir \
    infodir=%buildroot%_xemacs_infodir \
    docdir=%buildroot%_xemacs_docdir-x11 \
    mandir=%buildroot%_man1dir \

# binaries
for v in x11 nox; do
dumpid=`%_target_platform-$v/src/%name -sd`
install -m0755 %_target_platform-$v/src/%name %buildroot%_bindir/%name-$v
install -m0644 %_target_platform-$v/src/%name.dmp \
    %buildroot%_xemacs_archlibdir/%name-$dumpid.dmp
echo %_bindir/%name-$v > %name-$v-files
echo %_xemacs_archlibdir/%name-$dumpid.dmp >> %name-$v-files
echo %_desktopdir/%name-$v.desktop >> %name-$v-files
echo %_xemacs_docdir-$v >> %name-$v-files

%_target_platform-$v/src/%name -batch -no-site-file --eval \
    '(princ (mapconcat
	(function (lambda (s)
	    (format "%%s/%%s.elc" "%buildroot%_xemacs_lispdir" s)))
	preloaded-file-list "\n"))' > %name-$v-dumped-lisp
done

# DOC etc for rest of variants
for v in nox; do
install -p -m0644 -D %_target_platform-$v/lib-src/DOC %buildroot%_xemacs_docdir-$v/DOC
install -p -m0644 %_target_platform-$v/lib-src/config.values %buildroot%_xemacs_docdir-$v
done

# link site-start file
ln -s ../../../..%_xemacs_confdir/site-start.el %buildroot%_xemacs_lispdir/site-start.el
# link package index file
ln -sf ../../xemacs/package-index %buildroot%_xemacs_etcdir/package-index.LATEST.gpg

# icons, desktop entries
(cd altlinux && find . -type f |cpio -pmd %buildroot)

# cleanups
# these already in %_man1dir
rm -f %buildroot%_xemacs_etcdir/*.1
# these shouldn't be in xemacs package
rm -f %buildroot%_xemacs_infodir/{info,standards,termcap,texinfo}.info*
# win-specific files
rm -f %buildroot%_xemacs_lispdir/msw-*
# obsolete gtk1 stuff
rm -f %buildroot%_xemacs_lispdir/gtk-* 
# already dumped with every xemacs binary
num=`ls -1 %name-*-dumped-lisp|wc -l`
cat %name-*-dumped-lisp |sort |uniq -c |grep "^ \\+$num" |cut -d\  -f8 |xargs rm -vf --

#===============================================================================
%files minimal
%doc CHANGES-beta ChangeLog README PROBLEMS

%_bindir/gnuattach
%_bindir/gnuclient
%_bindir/gnudoit

%dir %_xemacs_libdir
%dir %_xemacs_archlibdir
%_xemacs_archlibdir/modules
%_xemacs_archlibdir/gnuserv
%_xemacs_archlibdir/fakemail
%_xemacs_archlibdir/profile
%_xemacs_archlibdir/make-docfile
%_xemacs_archlibdir/digest-doc
%_xemacs_archlibdir/sorted-doc
%_xemacs_archlibdir/movemail
%_xemacs_archlibdir/hexl
%_xemacs_archlibdir/mmencode
%_xemacs_archlibdir/rcs2log
%_xemacs_archlibdir/vcdiff

%dir %_xemacs_datadir
%dir %_xemacs_etcdir
%_xemacs_etcdir/package-index.LATEST.gpg
%_xemacs_etcdir/custom
%_xemacs_etcdir/eos
%_xemacs_etcdir/photos
%_xemacs_etcdir/toolbar
%_xemacs_etcdir/unicode
%_xemacs_etcdir/*.xpm
%_xemacs_etcdir/*.xbm
%_xemacs_etcdir/*.png

%_xemacs_etcdir/TUTORIAL
%lang(cs) %_xemacs_etcdir/TUTORIAL.cs
%lang(de) %_xemacs_etcdir/TUTORIAL.de
%lang(es) %_xemacs_etcdir/TUTORIAL.es
%lang(fr) %_xemacs_etcdir/TUTORIAL.fr
%lang(hr) %_xemacs_etcdir/TUTORIAL.hr
%lang(ja) %_xemacs_etcdir/TUTORIAL.ja
%lang(ko) %_xemacs_etcdir/TUTORIAL.ko
%lang(nl) %_xemacs_etcdir/TUTORIAL.nl
%lang(no) %_xemacs_etcdir/TUTORIAL.no
%lang(pl) %_xemacs_etcdir/TUTORIAL.pl
%lang(ro) %_xemacs_etcdir/TUTORIAL.ro
%lang(ru) %_xemacs_etcdir/TUTORIAL.ru
%lang(se) %_xemacs_etcdir/TUTORIAL.se
%lang(sk) %_xemacs_etcdir/TUTORIAL.sk
%lang(sl) %_xemacs_etcdir/TUTORIAL.sl
%lang(th) %_xemacs_etcdir/TUTORIAL.th

%_xemacs_etcdir/Emacs.ad
%_xemacs_etcdir/XKeysymDB
%_xemacs_etcdir/sample.*
%_xemacs_etcdir/refcard.*

%dir %_xemacs_lispdir
%_xemacs_lispdir/site-start.el
%_xemacs_lispdir/term
%_xemacs_lispdir/*.elc

%_iconsdir/*.xpm
%_iconsdir/large/*.xpm
%_iconsdir/mini/*.xpm

%_xemacs_infodir/*.info*

%_man1dir/xemacs.1*
%_man1dir/gnuserv.1*
%_man1dir/gnuclient.1*
%_man1dir/gnuattach.1*
%_man1dir/gnudoit.1*

%_xemacs_etcdir/HELLO
%dir %_xemacs_lispdir/mule
%_xemacs_lispdir/mule/*.elc

%files x11 -f %name-x11-files
%_altdir/xemacs-x11

%files nox -f %name-nox-files
%_altdir/xemacs-nox

%files devel
%_bindir/ellcc
%_xemacs_archlibdir/include

%files extras
%_bindir/b2m
%_bindir/etags
%_bindir/ootags
%_man1dir/etags.1*

%changelog
* Tue May 03 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.31-alt1
- 21.5.31 released

* Tue Jun 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.29-alt2
- rebuilt due libpng ABI change

* Fri May 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.29-alt1
- 21.5.29 released

* Mon Jun 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.28-alt3
- rebuilt with db4.7

* Sat Nov 10 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.28-alt2
- CVS snapshot @20071109

* Sat May 26 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.28-alt1
- XEmacs 21.5.28 'fuki' released

* Sat Nov 18 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.27-alt3
- sync'd with XE CVS, including:
  + font-lock-add-keywords et al from GNU Emacs
  + minibuffer resizing based on echo area size
  + added support for some non-ISO-8859-5 Cyrillic keysyms in X11

* Fri Oct 13 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.27-alt2
- fixed event handling on tty builds (b'ported from XE CVS)
- gpm support enabled for nox variant

* Mon Sep 25 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.5.27-alt1
- initial beta build

* Mon Mar 27 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.19-alt2
- rebuilt against recent db4

* Sat Feb  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.19-alt1
- 21.4.19 released

* Sat Dec 10 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.18-alt1
- 21.4.18 released

* Sat Aug 20 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.17-alt2
- applied x86_64-related patch (closes #6091)

* Thu Feb 10 2005 ALT QA Team Robot <qa-robot@altlinux.org> 21.4.17-alt1.1
- Updated libdb4 build dependencies.
- Rebuilt with libdb4.3.

* Mon Feb  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.17-alt1
- 21.4.17

* Sun Dec 19 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.16-alt1
- 21.4.16
- use portable dumper from now
- tty-only xemacs binaries appeared
- tty support in rest of variants dropped

* Sat Jun 19 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.15-alt3
- added support for uk & be in cp1251
- fixed package index file name

* Tue Jun  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.15-alt2
- rebuilt against new libcompface

* Wed Mar 10 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.15-alt1
- 21.4.15

* Thu Feb 19 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.14-alt3
- sound support dropped by default, see #3718

* Fri Feb 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.14-alt2
- rebuilt against recent Berkeley DB

* Sat Oct  4 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 21.4.14-alt1
- 21.4.14

* Sat Jun 14 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 21.4.12-alt3
- new alternatives
- added sound support (native and NAS)

* Sat May 17 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 21.4.12-alt2
- tty supported in all flavours
- koi8-u support added

* Tue Jan 21 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 21.4.12-alt1
- 21.4.12

* Tue Nov 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 21.4.10-alt2
- cleanups in menu/icon area

* Mon Nov 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 21.4.10-alt1
- 21.4.10

* Tue Oct 29 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 21.4.9-alt3
- neXtaw variants appeared

* Sat Sep 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 21.4.9-alt2
- rebuilt in new env

* Sat Aug 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 21.4.9-alt1
- basic lisp code moved to %_datadir/%name-%version
- xemacs lisp packages separated
- gtk/gnome variants temporarilly dropped
- movemail fixed to use lockf

* Thu Oct 11 2001 AEN <aen@logic.ru> 21.4.3-alt6
- rebuilt with libpng.so.3

* Thu Sep 20 2001 Dmitry V. Levin <ldv@altlinux.ru> 21.4.3-alt5
- Rebuilt with db3-3.3.11.

* Sat Jul 28 2001 Sergey Vlasov <vsu@altlinux.ru> 21.4.3-alt4
- generate separate DOC files for different variants (they are not compatible)
- added switch WITH_XAW3D to build with Xaw3d (plain Xaw sucks)

* Mon Jul  9 2001 Sergey Vlasov <vsu@altlinux.ru> 21.4.3-alt3
- file lists fixed
- info scripts fixed again
- general spec file cleanup
- moved common %name stuff to %name-common subpackage
- moved common mule stuff to %name-mule-common subpackage
- used update-alternatives for nomule, mule, gtk, gtk-gnome subpackages
- added nosource conditional
- fixed leim problem (leim-list.el must not be compiled)

* Fri Jun 1 2001 AEN <aen@logic.ru> 21.4.3-alt2
- info scripts fixed

* Fri Jun 1 2001 AEN <aen@logic.ru> 21.4.3-alt1
- build new version
- gtk & gnome build with mule

* Sat Mar 17  2001  AEN <aen@logic.ru> 21.1.14-ipl1mdk
- new version
- new sumo
- sync with MDK
- update-alternatives

* Wed Jan 03 2001 AEN <aen@logic.ru>
- adopted for RE
