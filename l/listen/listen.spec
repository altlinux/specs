Name: listen
Version: 0.6.5
Release: alt1.1

Summary: Listen is an audio player written in Python. 
Summary(ru_RU.UTF8): Listen - музыкальный проигрыватель написаный на Python.
License: GPLv2
Group: Sound
Url: http://www.listen-project.org/

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

BuildRequires: python-devel >= 2.4 python-module-pygtk-devel python-module-gst
BuildRequires: python-module-pyinotify python-module-pywebkitgtk python-module-sexy python-module-dbus-devel
# may be change it ot python-eggtrayicon ?
BuildRequires: python-module-xlib

BuildRequires: libgtk+2-devel intltool

# optional
BuildRequires: libtunepimp-devel python-module-gpod python-module-pygnome
BuildRequires: python-module-musicbrainz2 python-module-tunepimp python-module-daap

%add_python_req_skip gst_daap gtkmozembed

Requires(post,postun): desktop-file-utils
Requires: python-module-pygtk-libglade notification-daemon python-module-sexy python-module-musicbrainz2 python-module-tunepimp python-module-pywebkitgtk python-module-gpod  python-module-pyinotify python-module-pygnome python-module-gst python-module-dbus python-module-daap

%description
Listen is an audio player written in Python. Thanks to it, you can
easily organize your music collections.
It supports many features such as Podcasts management, browse
Shoutcast directory.
It provides a direct access to lyrics, lastfm and wikipedia
informations.
It intuitively creates playlists for you by retrieving informations
from lastfm and what you most frequently listen to.


%prep
%setup -q
sed -i 's|LIBDIR  ?= $(PREFIX)/lib|LIBDIR  ?= $(PREFIX)/%_lib|g' Makefile

%build
%make clean
%make_build
%make po-data

%install
mkdir -p %buildroot
export DESTDIR=%{buildroot}
make install

%files
%doc README TODO
%_bindir/*
%_libdir/%name/*
%_desktopdir/*
%_datadir/dbus-1/services/*
%_datadir/%name/*
%_datadir/locale/*/LC_MESSAGES/%{name}.mo
%_man1dir/*
%_pixmapsdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1
- Rebuild with Python-2.7

* Sat Jul 03 2010 Alexey Morsov <swi@altlinux.ru> 0.6.5-alt1
- new version

* Sun Oct 04 2009 Alexey Morsov <swi@altlinux.ru> 0.6.3-alt2
- fix requires
- add python-tunepimp, python-musicbrainz2, python-daap

* Thu Oct 01 2009 Alexey Morsov <swi@altlinux.ru> 0.6.3-alt1
- initial build for Sisyphus


