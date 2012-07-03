Name: xkeyboard-config
Summary: XML-based XKB configuration registry
Version: 2.6
Release: alt1
Epoch: 1
License: X11/MIT
Group: System/X11
Url: http://gswitchit.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: libX11 >= 1.4.3

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: intltool xkbcomp glib2-devel libX11-devel xorg-util-macros xsltproc

%description
Just XML stuff. Later hopefully will be part of Xorg

%package devel
Summary: XML-based XKB configuration registry development package
Group: Development/Other
Requires: %name = %version-%release

%description devel
XML-based XKB configuration registry development package

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--with-xkb-base=%_datadir/X11/xkb \
	--enable-compat-rules \
	--with-xkb-rules-symlink=xorg
%make

for d in compat geometry keycodes symbols types; do
	cd $d
	xkbcomp -lfhlpR -o $d.dir '*'
	cd ../
done

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%_datadir/X11/xkb/compiled

%find_lang %name

%pre
[ ! -d %_datadir/X11/xkb/symbols/pc ] || rm -fr %_datadir/X11/xkb/symbols/pc

%files -f %name.lang
%doc AUTHORS CREDITS NEWS README COPYING docs/HOWTO.testing docs/HOWTO.transition
%doc docs/README.config docs/README.enhancing docs/README.symbols
%_datadir/X11/xkb
%_man7dir/*.7*

%files devel
%_datadir/pkgconfig/*.pc

%changelog
* Sun Jun 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.6-alt1
- 2.6

* Wed May 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.5.1-alt1
- 2.5.1

* Mon Jan 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.5-alt1
- 2.5

* Tue Jan 03 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3-alt2
- 2.3

* Thu Oct 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Thu Jun 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- 2.3

* Wed Apr 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Feb 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.1-alt1
- 2.1

* Fri Oct 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- 2.0

* Thu May 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9-alt1
- 1.9

* Wed Jan 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.8-alt1
- 1.8

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt3
- added FK22 as XF86TouchpadToggle to standard inet symbols

* Thu Oct 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt2
- added grp:rctrl_rshift_toggle option

* Wed Sep 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.7-alt1
- 1.7

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt4
- added ru(bak) (closes: #20332)

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt3
- 1.6 release

* Sat May 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt2
- fixed symbols/ua

* Thu May 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt1
- 1.6

* Wed Jan 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt1
- 1.5

* Wed Oct 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4-alt1
- 1.4

* Mon Sep 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt2.M41.1
- build for branch 4.1

* Wed Aug 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt3
- updated russian translate

* Wed Aug 06 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt2
- added support Logitech diNovo Media Desktop Laser Keyboard

* Thu May 29 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.3-alt1
- 1.3

* Thu Apr 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt3
- final variant yakut language layout

* Thu Apr 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt2
- added yakut language layout

* Wed Jan 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Tue Jan 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt5
- CVS snapshot 2008-01-07:
  + added logiultrax, BTC 6301URF, thinkpad60 models
  + small OLPC fixes

* Sun Oct 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt4
- CVS snapshot 2007-10-28:
  + OLPC fixlets

* Mon Oct 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt3
- CVS snapshot 2007-10-13

* Thu Oct 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt2
- drop Slovenian translation

* Wed Sep 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.1-alt1
- 1.1

* Sun Sep 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt5
- CVS snapshot 2007-09-14

* Sat Aug 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt4
- CVS snapshot 2007-08-24

* Sun Aug 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt3
- CVS snapshot 2007-08-18

* Sat Jul 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt2
- updated/new translations

* Fri Jun 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0-alt1
- 1.0

* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt8
- CVS snapshot 2007-06-18:
- fixed symbols in chuvash keyboard layout

* Fri Jun 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt7
- CVS snapshot 2007-06-13:
  + chuvash and udmurt keyboard layout

* Tue Jun 05 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt6
- CVS snapshot 2007-05-26

* Thu May 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt5
- CVS snapshot 2007-05-14

* Sun Feb 04 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt4
- CVS snapshot 2007-02-03:
  + added (model, layout->geometry) section for thinkpad

* Sat Jan 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt3
- CVS snapshot 2007-01-27
- closed #10720

* Wed Dec 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt2
- CVS snapshot 2006-11-20
- added support BTC 9116U Mini Wireless Internet and Gaming keyboard

* Mon Oct 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt1
- 0.9

* Mon Oct 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt7
- CVS snaphot 2006-10-01

* Thu May 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt6
- added support BTC 9019U

* Sun May 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt5
- CVS snapshot 2006-05-05

* Sun Apr 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt4
- CVS snapshot 2006-04-20
- Obsoletes xorg-x11-xkbdata

* Mon Apr 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt3
- added support Genius KB-19e NB

* Sun Mar 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt2
- CVS snapshot 2006-03-25

* Mon Mar 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8-alt1
- initial release

