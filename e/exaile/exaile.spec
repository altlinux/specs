Name: exaile
Version: 0.3.2.2
Release: alt1.1

Summary: a music player aiming to be similar to KDE's Amarok, but for GTK+ and written in Python
License: GPL
Group: Sound
Url: http://www.exaile.org

BuildArch: noarch
Source: http://www.launchpad.net/%name/0.3.2/%version/+download/%name-%version.tar
Patch0: %name-%version-%release.patch

%add_python_req_skip xl
%add_python_req_skip xlgui

BuildRequires: help2man python-module-pygobject python-devel

%description
Exaile is a music player aiming to be similar to KDE's Amarok, but for
GTK+ and written in Python. It incorporates many of the cool things from
Amarok (and other media players) like automatic fetching of album art,
handling of large libraries, lyrics fetching, artist/album information
via Wikipedia, Last.fm submission support, and optional iPod support via
a plugin.
In addition, Exaile also includes a built-in SHOUTcast directory
browser, tabbed playlists (so you can have more than one playlist open
at a time), blacklisting of tracks (so they don't get scanned into your
library), downloading of guitar tablature from fretplay.com, and
submitting played tracks on your iPod to Last.fm.

%package plugin-ipod
Group: Sound
Summary: Ipod plugin for exaile
Requires: %name = %version-%release

%description plugin-ipod
%summary

%package plugin-exfalso
Group: Sound
Summary: Ex Falso tag editor for exaile
Requires: %name = %version-%release

%description plugin-exfalso
%summary

%prep
%setup -q
%patch -p1

%build
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=%_prefix install
mkdir -p %buildroot{%_liconsdir,%_niconsdir,%_miconsdir}
cp %buildroot%_datadir/%name/data/images/16x16/%name.png %buildroot%_miconsdir/
cp %buildroot%_datadir/%name/data/images/32x32/%name.png %buildroot%_niconsdir/
cp %buildroot%_datadir/%name/data/images/48x48/%name.png %buildroot%_liconsdir/

%find_lang %name

%files -f %name.lang
%_sysconfdir/xdg/%name
%_bindir/%name
%_desktopdir/%name.desktop
%_prefix/lib/%name
%exclude %_datadir/%name/plugins/ipod
%exclude %_datadir/%name/plugins/exfalso
%_datadir/%name
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_man1dir/%name.*
%doc COPYING

%files plugin-ipod
%_datadir/%name/plugins/ipod

%files plugin-exfalso
%_datadir/%name/plugins/exfalso

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2.2-alt1.1
- Rebuild with Python-2.7

* Fri Oct 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.2.2-alt1
- New version 0.3.2.2

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.2.1-alt1
- New version 0.3.2.1

* Wed Sep 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2.0-alt3
- Cleaning dependencies (Closes: #24143)

* Mon Aug 23 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2.0-alt2
- Fixed jamendo plugin (Closes: #23925)

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2.0-alt1
- New version 0.3.2.0

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.1.2-alt1
- New version 0.3.1.2

* Sat Apr 10 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.1.1-alt1
- New version 0.3.1.1

* Wed Mar 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.1.0-alt1
- New version 0.3.1.0
- Separate ipod plugin and new exfalso plugin

* Fri Mar 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.0.2-alt1.r2473
- Updated source from stable branch 0.3.0

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0.1-alt1.1
- Rebuilt with python 2.6

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.3.0.1-alt1
- bugfix release

* Mon Aug 31 2009 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- new version

* Sat Oct 11 2008 Vladimir Lettiev <crux@altlinux.ru> 0.2.14-alt1
- Initial build for Sisyphus

