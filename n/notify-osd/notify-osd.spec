#
# spec file for package notify-osd
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.altlinux.org/

Name: notify-osd
Version: 0.9.30
Release: alt1

Summary: Streamlined Desktop Notifications
License: GPLv3+
Group: Graphical desktop/GNOME

Url: https://launchpad.net/notify-osd
Source: %name-%version.tar.gz
# PATCH-FIX-UPSTREAM notify-osd-link-libm.patch lp#853871 vuntz@opensuse.org
# ALT: relevant for 0.9.32 (gtk+3)
#Patch: notify-osd-link-libm.patch
# PATCH-FIX-UPSTREAM notify-osd-libnotify-0.7.patch lp#785452 dimstar@opensuse.org -- Fix build with libnotify 0.7
Patch: notify-osd-libnotify-0.7.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Oct 12 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libpango-devel libstartup-notification pkg-config xorg-xproto-devel
BuildRequires: libGConf-devel libdbus-glib-devel libnotify-devel libpixman-devel libwnck-devel

BuildRequires: pkgconfig(glib-2.0) >= 2.16
#BuildRequires: pkgconfig(gtk+-3.0) >= 3.1.6
BuildRequires: pkgconfig(gtk+-2.0) >= 2.14
BuildRequires: pkgconfig(libnotify) >= 0.4.5
BuildRequires: pkgconfig(dbus-glib-1) >= 0.76

# both packages provide {_datadir}/dbus-1/services/org.freedesktop.Notifications.service
Conflicts: notification-daemon xfce4-notifyd

%description
This notification service is an alternative to the notification-daemon
package. It follows the freedesktop notification specification and
introduces some new policies for streamlining the user-experience by
discouraging the use of actions and timeouts.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README TODO
%_datadir/%name/
%_datadir/dbus-1/services/org.freedesktop.Notifications.service
# ALT: 0.9.32
#_datadir/glib-2.0/schemas/com.canonical.NotifyOSD.gschema.xml
%_libexecdir/%name

# dropped pre-ALT changelog, for the reference see this one:
# https://api.opensuse.org/public/source/openSUSE:Factory/notify-osd/notify-osd.spec?rev=7c5fe51a51d63d4581743444b54df419

%changelog
* Wed Oct 12 2011 Michael Shigorin <mike@altlinux.org> 0.9.30-alt1
- rollback to 0.9.30 (gtk+3-3.2.0 not yet moved to Sisyphus)
- picked up a patch from opensuse 0.9.30-1 package
- buildreq

* Wed Oct 12 2011 Michael Shigorin <mike@altlinux.org> 0.9.32-alt1
- built for ALT Linux (based on opensuse 0.9.32-1.1 package)
- dropped leolik patch (declined upstream)
- spec cleanup

