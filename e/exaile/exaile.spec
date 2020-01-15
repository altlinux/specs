%def_enable snapshot
%define beta %nil
%define gst_api_ver 1.0

# no more these plugins
%def_disable exfalso
%def_disable ipod

Name: exaile
Version: 4.0.2
Release: alt1

Summary: a music player aiming to be similar to KDE's Amarok, but for GTK+ and written in Python
License: GPL-2.0
Group: Sound
Url: http://www.exaile.org

BuildArch: noarch

%if_disabled snapshot
Source: https://github.com/exaile/%name/releases/download/%version/%name-%version%beta.tar.gz
%else
Source: %name-%version.tar
%endif
#Patch: %name-%version-%release.patch

# python-2.x supported only
#%%define __python %nil
#BuildRequires(pre): rpm-build-python3

# remove ubuntu and Mac-specific dependency
%add_typelib_req_skiplist typelib(GtkosxApplication)

BuildRequires(pre): rpm-build-gir rpm-build-python
BuildRequires: python-devel python-module-pygobject3
BuildRequires: help2man bash-completion

# explicitly required gtk+3
Requires: typelib(Gtk) = 3.0
Requires: dbus dconf
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver

%description
Exaile is a music player with a simple interface and powerful music
management capabilities. Features include automatic fetching of album
art, lyrics fetching, streaming internet radio, tabbed playlists, smart
playlists with extensive filtering/search capabilities, and much more.

Exaile is written using Python and GTK+ and is easily extensible via
plugins. There are over 50 plugins distributed with Exaile that include
advanced track tagging, last.fm scrobbling, support for portable media
players, podcasts, internet radio such as icecast and Soma.FM,
ReplayGain, output via a secondary output device (great for DJs!), and
much more.

For more information see http://exaile.readthedocs.io/


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
%setup
#%patch -p1
subst 's@\(\$(DATADIR)\/\)appdata@\1metainfo@' Makefile

%build
%make_build EPREFIX=%_prefix

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
%{?_enable_ipod:%exclude %_datadir/%name/plugins/ipod}
%{?_enable_exfalso:%exclude %_datadir/%name/plugins/exfalso}
%_datadir/%name
%_datadir/metainfo/exaile.appdata.xml
%_datadir/dbus-1/services/org.exaile.Exaile.service
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_man1dir/%name.*
%_datadir/bash-completion/completions/%name
%doc README.md

%if_enabled ipod
%files plugin-ipod
%_datadir/%name/plugins/ipod
%endif

%if_enabled exfalso
%files plugin-exfalso
%_datadir/%name/plugins/exfalso
%endif

%changelog
* Tue Jan 14 2020 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2 release

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt0.2
- updated to 4.0.0-rc1-14-g15b337f

* Thu Mar 22 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt0.1
- updated to 4.0.0-beta3-7-g6c83c2a (ported to GTK+3, GStreamer-1.0)

* Thu Nov 19 2015 Vladimir Lettiev <crux@altlinux.ru> 3.4.5-alt1
- New version 3.4.5
- Dependency on gst-plugins-base (Closes: #31517)

* Mon Dec 16 2013 Vladimir Lettiev <crux@altlinux.ru> 3.3.2-alt1
- New version 3.3.2

* Tue Apr 09 2013 Vladimir Lettiev <crux@altlinux.ru> 3.3.1-alt1
- New version 3.3.1

* Fri Oct 05 2012 Vladimir Lettiev <crux@altlinux.ru> 3.3.0-alt1
- New version 3.3.0

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

