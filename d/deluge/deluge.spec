Name: deluge
Version: 1.3.5
Release: alt2

Summary: full-featured BitTorrent client
License: GPL
Group: Networking/File transfer

Url: http://deluge-torrent.org
# http://git.deluge-torrent.org/deluge/

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildArch: noarch

BuildRequires: python-module-dbus-devel python-module-pygtk-devel
BuildRequires: python-module-notify librsvg-devel python-module-pyxdg
BuildRequires: python-module-setuptools python-module-libtorrent-rasterbar
BuildRequires: python-module-simplejson intltool

Requires: deluge-gtk = %version-%release

%description
Deluge is a full-featured  BitTorrent client for Linux, OS X, Unix and
Windows. It uses  libtorrent in it's backend and features multiple
user-interfaces including: GTK+, web and console. It has been designed
using the client server model with a daemon process that handles all the
bittorrent activity. The Deluge daemon is able to run on headless
machines with the user-interfaces being able to connect remotely from
any platform.

Deluge features a rich plugin collection; in fact, most of Deluge's
functionality is available in the form of plugins.

Deluge was created with the intention of being lightweight and
unobtrusive. It is our belief that downloading shouldn't be the primary
task on your computer and therefore shouldn't monopolize system
resources.

Deluge is not designed for any one desktop environment and will work
just fine in GNOME, KDE, XFCE and others. We do our best to adhere to
the  freedesktop standards.

Deluge is  Free Software and is licensed under the  GNU General Public
License.

%package -n python-module-deluge
Group: Networking/File transfer
Summary: full-featured BitTorrent client (common files)
Requires: python-module-simplejson python-module-pyxdg python-module-libtorrent-rasterbar python-module-twisted-web

%description -n python-module-deluge
This package contains data files commons to both the deluge daemon and
the user-interfaces.

%package console
Group: Networking/File transfer
Summary: full-featured BitTorrent client (console UI)
Requires: python-module-deluge = %version-%release

%description console
This package contains the console user-interface.

%package -n deluged
Group: Networking/File transfer
Summary: full-featured BitTorrent client (deluge daemon)
Requires: python-module-deluge = %version-%release

%description -n deluged
Deluge daemon process handles all the bittorrent activity.
The Deluge daemon is able to run on headless machines with the
user-interfaces being able to connect remotely from any platform.

%package gtk
Group: Networking/File transfer
Summary: full-featured BitTorrent client (GTK UI)
Requires: python-module-deluge = %version-%release python-module-twisted-core-gui python-module-pygtk-libglade

%description gtk
This package contains the GTK user-interface.

%package web
Group: Networking/File transfer
Summary: full-featured BitTorrent client (web UI)
Requires: python-module-deluge = %version-%release

%description web
This package contains the web user-interface.

%prep
%setup -q
%patch0 -p1

%build
%python_build

%install
%python_install
rm -f %buildroot%_datadir/pixmaps/*
rm -f %buildroot%python_sitelibdir/%name/ui/webui/scripts/build_webui_tarball.sh
mkdir -p %buildroot{%_initdir,%_sysconfdir/sysconfig,%_spooldir/deluged}
cp altlinux/deluged.init %buildroot%_initdir/deluged
cp altlinux/deluged.sys %buildroot%_sysconfdir/sysconfig/deluged

%pre -n deluged
%_sbindir/groupadd -r -f _deluge
%_sbindir/useradd -r -n -g _deluge -d %_spooldir/deluged -s /dev/null -c "deluge bittorrent daemon" _deluge >/dev/null 2>&1 ||:

%post -n deluged
%post_service deluged

%preun -n deluged
%preun_service deluged

%files
%_bindir/%name
%_man1dir/%name.1*
%doc LICENSE ChangeLog README

%files -n python-module-deluge
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/*.py*
%python_sitelibdir/%name/core
%python_sitelibdir/%name/data
%python_sitelibdir/%name/i18n
%python_sitelibdir/%name/plugins
%dir %python_sitelibdir/%name/ui
%python_sitelibdir/%name/ui/*.py*
%python_sitelibdir/*.egg-info

%files console
%_bindir/%name-console
%_man1dir/%name-console.1*
%python_sitelibdir/%name/ui/console

%files -n deluged
%attr(0755,root,root) %_initdir/deluged
%config(noreplace) %_sysconfdir/sysconfig/deluged
%_bindir/deluged
%_man1dir/deluged.1*
%attr(0775,root,_deluge) %dir %_spooldir/deluged

%files gtk
%_bindir/%name-gtk
%_man1dir/%name-gtk.1*
%python_sitelibdir/%name/ui/gtkui
%_iconsdir/hicolor/*/apps/*
%_iconsdir/scalable/apps/*
%_desktopdir/%name.desktop

%files web
%_bindir/%name-web
%_man1dir/%name-web.1*
%python_sitelibdir/%name/ui/web

%changelog
* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.5-alt2
- Fixed subpackages dependencies (Closed: #27388)

* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.5-alt1
- New version 1.3.5

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.4-alt1
- New version 1.3.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt3.1
- Rebuild with Python-2.7

* Tue Aug 16 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt3
- Fixed default port of WebUI - 8112

* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt2
- Fixed _deluge home dir

* Thu Aug 11 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt1
- New version 1.3.3
- split up package: deluge, python-module-deluge, deluge-console,
  deluge-web, deluge-gtk, deluged
- added initscript for deluged and deluge-web

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.3.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for deluge

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.1-alt1
- New version 1.3.1

* Wed Sep 22 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt2
- Added python-module-pyxdg to requires (Closes: #24132)
- Added librsvg to requires (loading svg logo)

* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt1
- New version 1.3.0

* Sun Sep 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.0-alt0.rc2
- New version 1.3.0_rc2

* Thu Aug 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt2
- Add python-module-twisted-core-gui to requires (Closes: #23854)

* Sun Mar 28 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt1
- New version 1.2.3

* Wed Mar 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- New version 1.2.1

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt3
- Fixed deluged failure with new libtorrent-rasterbar0.15 (Closes: #22849)

* Sun Jan 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt2
- New version 1.2.0

* Tue Dec 29 2009 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1.rc5
- YARC

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.rc3.1
- Rebuilt with python 2.6

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1.rc3
- another RC

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1.rc2
- new RC

* Sat Oct 17 2009 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1.rc1
- new version
- do not check new version by default (Closes: #21908)

* Tue Jun 16 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.9-alt1
- new version

* Sun Jun 14 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.8-alt2
- build with system libtorrent-rasterbar (Closes: 20387)
- dropped libtorrent patches and buildreqs
- noarch

* Sun May 31 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.8-alt1
- new version

* Sun Apr 26 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.7-alt1
- new version
- patch2 moved to upstream

* Thu Apr 09 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt2
- fix bug #18929

* Tue Apr 07 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.6-alt1
- new version

* Sun Feb 22 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.3-alt1
- new version

* Mon Jan 26 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt1
- new version

* Thu Jan 15 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.0-alt1
- new version
- cleared deprecated macroses
- fixed #18201

* Mon Oct 13 2008 Vladimir Lettiev <crux@altlinux.ru> 1.0.2-alt1
- new version
- applied patch from Ivan A. Melnikov (iv@) to fix build with new
  boost and old gcc (workaround gcc-c++ bug #33094)
- removed patch for boost lib detection logic (merged in upstream)
- updated bosts's dependencies
- removed icon from pixmaps dir

* Tue Sep 23 2008 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt2
- Fix build on x86_64 (patch from deluge trac ticket #503)

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- Initial build for Sisyphus

