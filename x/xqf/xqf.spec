Name:    xqf
Version: 1.0.6.2
Release: alt2
Summary: X11 QStat Frontend
Packager: Andrey Cherepanov <cas@altlinux.org>
License: GPL
Group:   Networking/Other
URL:     https://xqf.github.io/en/
# VCS:   https://github.com/XQF/xqf

Requires: qstat >= 2.11
Requires: gzip
Requires: wget

Source: %name-%version.tar
Patch:  %name-%version.patch

BuildRequires: fontconfig-devel freetype2-devel glib2-devel libGeoIP-devel
BuildRequires: libatk-devel libcairo-devel libglitz-devel libgtk+2-devel
BuildRequires: libpango-devel libpng-devel perl-XML-Parser pkg-config qstat
BuildRequires: zlib-devel intltool

%description
XQF is a 3D action game (such as Quake, sequels and derivatives) server
browser. It uses X and is written using the GIMP Tool Kit. XQF is a
front-end to QStat, a program by Steve Jankowsk which is used to
retrieve server info.

%prep
%setup
%patch -p1

%build
sh autogen.sh
%autoreconf
%configure \
		--enable-bzip2 \
		--disable-gtk \
		--enable-gtk2 \
		--enable-geoip \
		--with-qstat=/usr/bin/qstat \
		%{subst_enable debug}

%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README.md AUTHORS.md BUGS ChangeLog NEWS.md TODO GUIDELINES.md docs/xqfdocs.html
%_bindir/%name
%_datadir/%name
%_pixmapsdir/*
%_desktopdir/%name.desktop
%_man6dir/%name.6*

%changelog
* Thu Feb 07 2019 Konstantin Rybakov <kastet@altlinux.org> 1.0.6.2-alt2
- NMU: update runtime dependencies

* Wed Oct 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.6.2-alt1
- New version from upstream Git repository
- Spec cleanup

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.5-alt2.1.qa1
- NMU: rebuilt for updated dependencies.

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


