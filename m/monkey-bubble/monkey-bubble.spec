Name: monkey-bubble
Version: 0.4.0
Release: alt5

Summary: Monkey Bubble - the gnome bust'a'move clone

License: GPL
Group: Games/Arcade
Url: http://home.gna.org/monkeybubble/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://home.gna.org/monkeybubble/downloads/%name-%version.tar.bz2
Patch: %name-%version.patch
Patch1: %name-%version-help-disable.patch
Patch2: %name-%version-help.patch
Patch3: %name-%version-format-strings.patch

# Automatically added by buildreq on Sun Jun 27 2010
BuildRequires: glibc-devel gstreamer-devel libglade-devel libgnomeui-devel librsvg-devel

BuildPreReq: libesd-devel

BuildPreReq: intltool

# Typical environment for GNOME program
Requires(post): GConf2
Requires(post,postun): scrollkeeper
Requires(post,postun): desktop-file-utils
BuildPreReq: libGConf2-devel
BuildPreReq: desktop-file-utils

%description
Monkey Bubble - the gnome bust'a'move clone.

%prep
%setup -q
%patch
%patch1
%patch3 -p1

%__subst "s|-Werror||g" */*/Makefile.*

# do not include glib/*.h directly
%__subst "s|#include <glib/.*||g" src/*/*.[ch]

%build
%undefine __libtoolize
%autoreconf
%configure --disable-schemas-install --disable-scrollkeeper
%make_build

%install
%makeinstall_std

%find_lang %name --with-gnome
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=ArcadeGame \
	%buildroot%_desktopdir/monkey-bubble.desktop

%files -f %name.lang
%doc AUTHORS ChangeLog
%_bindir/%name
%_bindir/monkey-srv
%_datadir/%name/
%_desktopdir/*
%_pixmapsdir/*
%config %_sysconfdir/gconf/schemas/*

%changelog
* Wed Apr 18 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt5
- # do not include glib/*.h directly

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0-alt4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for monkey-bubble
  * freedesktop-desktop-file-proposed-patch for monkey-bubble
  * postclean-03-private-rpm-macros for the spec file

* Sun Jun 27 2010 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt4
- update buildreqs

* Mon Jul 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt3
- remove -Werror

* Mon Jan 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt2
- cleanup spec, update buildreq
- disable help in configure

* Sun Jul 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- add libSM-devel buildreq
- disable help at all

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version 0.4.0, add Source URL
- remove Debian menu, cleanup spec
- update buildreq, add fixes for --as-needed

* Sat Jan 22 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt2
- patch for gcc3.4

* Sun Dec 05 2004 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- first build for ALT Linux Sisyphus
