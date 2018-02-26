# vim: set ft=spec: -*- mode: rpm-spec; -*-
# $Id: xqf,v 1.2 2003/09/21 21:23:04 raorn Exp $

%def_disable debug

%if_enabled debug
%set_strip_method none
%endif

Name: xqf
Version: 1.0.5
Release: alt2.1
Summary: X11 QStat Frontend
Packager: Pavlov Konstantin <thresh@altlinux.ru>
License: GPL
Group: Networking/Other
URL: http://www.linuxgames.com/xqf/

Requires: qstat = 2.11
Requires: gzip
Requires: wget

Source: %name-%version.tar.gz
Patch: %name-1.0.5-alt-DSO.patch

# Automatically added by buildreq on Sun Nov 06 2005
BuildRequires: fontconfig-devel freetype2-devel glib2-devel libGeoIP-devel libatk-devel libcairo-devel libglitz-devel libgtk+2-devel libpango-devel libpng-devel perl-XML-Parser pkg-config qstat zlib-devel

%description
XQF is a 3D action game (such as Quake, sequels and derivatives)
server browser. It uses X and is written using the GIMP Tool Kit.                                       
XQF is a front-end to QStat, a program by Steve Jankowsk which
is used to retrieve server info.

%prep
%setup
%patch -p2

%build
#./autogen.sh
export CPPFLAGS=-I/usr/include/GeoIP

%configure \
		--enable-bzip2 \
		--disable-gtk \
		--enable-gtk2 \
		--enable-geoip \
		--with-qstat=/usr/bin/qstat \
		%{subst_enable debug}

%make_build

%install
#%__mkdir -p %buildroot%_menudir
%make_install DESTDIR=%buildroot install

#cat <<EOF > %%buildroot%%_menudir/%%name
#?package(%%name): needs=x11 \
#        command="xqf" \
#        section="Networking/Other" \
#        title="X11 Quake Frontend"
#EOF

%find_lang %name

%files -f %name.lang
%doc README AUTHORS BUGS ChangeLog INSTALL NEWS TODO docs/xqfdocs.html
%_bindir/xqf
%_mandir/man6/xqf.6*
%_datadir/pixmaps/*
%_datadir/applications/xqf.desktop
%_datadir/%name
#%%_menudir/%name

%changelog
* Sat Jun 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt2.1
- Fixed build

* Wed Apr 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.5-alt2
- fix build

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1
- NMU (by repocop): the following fixes applied:
  * update_menus for xqf

* Mon Nov 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5-alt1
- 1.0.5.
- Removed patch1 for xpms.

* Fri Jun 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.0.4-alt2
- Woops, xpms were not packaged.
- Removed support for .menu file.

* Sun Nov 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.0.4-alt1
- 1.0.4 release.
- gtk1 version seems to be b0rken, let's build gtk2.
- requires qstat >= 2.10 due to q4 support.

* Tue Apr 05 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.0.3-alt1
- 1.0.3 release

* Thu Jan 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.0.2-alt1
- 1.0.2 release

* Mon Sep 22 2003 Sir Raorn <raorn@altlinux.ru> 0.9.12-alt1.1
- Fixed buildrequires

* Wed Jun 18 2003 Sir Raorn <raorn@altlinux.ru> 0.9.12-alt1
- [0.9.12]

* Sun Oct 20 2002 Sir Raorn <raorn@altlinux.ru> 0.9.9-alt1
- [0.9.9]

* Wed Mar 06 2002 Sir Raorn <raorn@altlinux.ru> 0.9.8-alt1
- Built for Sisyphus


