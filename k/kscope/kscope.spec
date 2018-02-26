Name: kscope
Version: 1.6.2
Release: alt3.1

Summary: KDE front-end to Cscope

License: BSD
Group: Development/Other
Url: http://kscope.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/kscope/%name-%version.tar.bz2
Patch: %name-desktop.patch
Patch1: %name-1.6.2-alt-DSO.patch

# manually removed: qt3-designer gcc-java imake kde-i18n-ru qt3-designer  xorg-cf-files
# Automatically added by buildreq on Tue Oct 14 2008
BuildRequires: flex gcc-c++ kdepim-devel libXt-devel libjpeg-devel xml-utils

Requires: cscope ctags graphviz

%description
KScope is a KDE front-end to Cscope. It provides a source-editing
environment for large C projects, such as the Linux kernel. KScope is
by no means intended to be a replacement to any of the leading
Linux/KDE IDEs, such as KDevelop. However, these IDEs, often targeted
at Object-Oriented, user-space programming, are usually unsuitable for
maintaining large projects, using functional programming. For
instance, using a "Classes" window to display the thousands of
functions in the Linux kernel code, would be impractical, and thus
will prevent any useful navigation throughout the code. KScope, on the
other hand, provides a rather useful mechanism for code-navigation, by
allowing the user to run queries on the code.

%prep
%setup -q
#%patch0 -p1
%patch1 -p2

%build
#cp -f %_datadir/automake/config.sub admin
# TODO: where is error?
%add_optflags -I%_includedir/tqtinterface
%__subst "s|-lkateinterfaces|-lkatepartinterfaces|g" src/Makefile.in
%K3configure
%make_build

%install
%K3install

%K3find_lang %name --with-kde

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO COPYING
%_K3bindir/%name
%_K3datadir/apps/%name/
#%_liconsdir/*.png
#%_niconsdir/*.png
#%_miconsdir/*.png
%_kde3_iconsdir/hicolor/*/apps/%name.png
%_kde3_iconsdir/locolor/*/apps/%name.png
/usr/share/kde/applnk/Development/*.desktop

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt3.1
- Fixed build

* Wed Mar 02 2011 Timur Aitov <timonbl4@altlinux.org> 1.6.2-alt3
- move to alternate place

* Fri Dec 17 2010 Ilya Shpigor <elly@altlinux.org> 1.6.2-alt2
- fix bug with symbol links adding

* Tue Oct 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version 1.6.2 (with rpmrb script)
- update buildreqs

* Sun May 25 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt2
- move desktop file to desktopdir
- cleanup spec, update buildreq
- add require graphviz (fix bug #15756)

* Sat Feb 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- new version 1.6.1 (with rpmrb script)

* Mon Jul 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0 (with rpmrb script)

* Tue May 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Mon Apr 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.1
- new version 1.4.1
- cleanup spec, fix license, fix icons
- remove obsoleted desktop patch

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1
- new version 1.4.0 (with rpmrb script)

* Mon May 01 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt0.1
- new version 1.3.4 (with rpmrb script)

* Mon Mar 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD Team)
- fix kate lib
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: kscope.spec,v $
Revision 1.13  2005/12/12 16:39:34  charles
- BR graphviz-devel >= 2.6-3

Revision 1.12  2005/12/12 04:41:17  charles
- updated to 1.3.2
- updated BRs (libsvg-cairo-devel is not needed)

Revision 1.11  2005/08/04 10:22:26  blekot
- up to 1.3.0
- BR: graphviz-devel, libsvg-cairo-devel

Revision 1.10  2005/02/02 03:42:42  charles
- updated to 1.1.0

Revision 1.9  2005/01/15 16:31:01  charles
- only _iconsdir/hicolor
- proper Licence
- rel 3, STBR

Revision 1.8  2004/12/21 06:16:23  adamg
- small fix in pl description (by Karol "Charles" Krenski  charles (at) os.pl)

Revision 1.7  2004/12/21 01:06:53  adamg
- release 2

Revision 1.6  2004/12/21 01:01:51  adamg
- referesh config.sub (fixes build on amd64)

Revision 1.5  2004/12/07 12:02:09  snurf
- up to 1.0

Revision 1.4  2004/11/13 10:42:41  kolodko
- up to 0.9 by Charles <charles (at) os.pl>

Revision 1.3  2004/05/31 20:04:12  twittner
- added .desktop patch

Revision 1.2  2004/05/31 16:44:23  qboosh
- pl, use proper dirs for *.desktop and html

Revision 1.1  2004/05/30 22:37:40  arekm
- initial pld release
