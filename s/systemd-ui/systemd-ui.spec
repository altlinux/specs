
Name: systemd-ui
Url: http://www.freedesktop.org/wiki/Software/systemd
Version: 2
Release: alt1
License: GPLv2+
Group: System/Configuration/Other
Summary: Graphical front-end for systemd
Source: %name-%version.tar
BuildRequires: pkgconfig(dbus-1) >= 1.3.2
BuildRequires: pkgconfig(gtk+-3.0) pkgconfig(glib-2.0) > 2.26 pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libnotify)
BuildRequires: vala >= 0.10
BuildRequires: desktop-file-utils
BuildRequires: xsltproc docbook-style-xsl docbook-dtds
Requires: systemd >= 183-alt1
Obsoletes: systemd-gtk < 45
Provides: systemd-gtk = 45-alt1

%description
Graphical front-end for systemd. It provides a simple user interface to manage
services, and a graphical agent to request passwords from the user.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/systemadm
%_bindir/systemd-gnome-ask-password-agent
%_desktopdir/systemadm.desktop
%_man1dir/systemadm.*

%changelog
* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 2-alt1
- version 2

* Mon Jun 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1-alt1
- initial release after split-off from systemd package
