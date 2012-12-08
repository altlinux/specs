Name: xpra
Version: 0.7.5
Release: alt1

Summary: X Persistent Remote Applications

Group: Networking/Remote access
License: GPLv2
Url: http://xpra.org/

Source: http://xpra.org/src/%name-%version.tar

# Automatically added by buildreq on Sat Dec 08 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libXfixes-devel libXi-devel libXrender-devel libatk-devel libavutil-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel pkg-config python-base python-devel python-module-distribute python-module-peak python-module-pygobject-devel python-module-zope python-modules python-modules-compiler python-modules-email python-modules-encodings xorg-compositeproto-devel xorg-damageproto-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXcomposite-devel libXdamage-devel libXrandr-devel libXtst-devel libavcodec-devel libswscale-devel libvpx-devel libx264-devel python-module-Cython python-module-mwlib python-module-paste python-module-pygtk-devel subversion

Requires: libwebp xorg-xvfb setxkbmap

%description
Xpra is 'screen for X': it allows you to run X programs,
usually on a remote host, direct their display to your local machine,
and then to disconnect from these programs and reconnect
from the same or another machine, without losing any state.
It gives you remote access to individual applications.
Xpra is "rootless" or "seamless": programs you run under
it show up on your desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt
to changing network bandwidth limits. (see also adaptive JPEG mode)
Xpra is open-source (GPLv2+), multi-platform and multi-language,
with current clients written in Python and Java. 

%prep
%setup
%__subst "s|pygtk-2.0/pygobject.h|pygtk/pygobject.h|g" wimpiggy/lowlevel/bindings.pyx
%__subst "s|pygtk-2.0/pygtk/pygtk.h|pygtk/pygtk.h|g" wimpiggy/gdk/gdk_atoms.pyx

%build
%python_build

%install
%python_install

%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/*
%_bindir/*
%python_sitelibdir/*
%_desktopdir/*
%_iconsdir/*
%_man1dir/*
%_datadir/parti/
%_datadir/wimpiggy/
%_datadir/xpra/

%changelog
* Sat Dec 08 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- initial build for Sisyphus

