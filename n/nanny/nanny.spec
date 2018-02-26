%define ver_major 2.30

Name: nanny
Version: %ver_major.0
Release: alt1.1

Summary: Gnome-Nanny is a parental control system designed for Gnome
License: GPLv2
Group: Graphical desktop/GNOME
Url: http://projects.gnome.org/nanny/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://download.gnome.org/sources/nanny/%ver_major/%name-%version.tar
Patch: %name-%version.patch

BuildRequires: rpm-build-gnome glib2-devel gnome-common gnome-doc-utils intltool 
BuildRequires: python-devel python-module-dbus-devel python-module-pygtk-devel
BuildRequires: python-module-imaging python-module-twisted-web python-module-hachoir-regex
# gtop
BuildRequires: /proc python-module-pygnome-desktop-devel

%description
Nanny is an easy way to control what your kids are doing in the computer.
You can limit how much time a day each one of them is browsing the web,
chatting or doing email. You can also decide at which times of the day the
can do this things.

%prep
%setup
%patch -p1
find -name Makefile.am -print0 |xargs -r0 subst 's,pythondir,pyexecdir,' --

%build
NOCONFIGURE=1 ./autogen.sh
%configure --with-init-scripts=altlinux --disable-static

%make_build

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_localstatedir/%name

%find_lang --with-gnome %name

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%doc README AUTHORS COPYING NEWS ChangeLog
%config %_initdir/%name
%config(noreplace) %_sysconfdir/xdg/autostart/%name-systray.desktop
%config %_sysconfdir/dbus-1/system.d/%name-daemon.conf
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/applists
%config(noreplace) %_sysconfdir/%name/applists/*
%_bindir/*
%_sbindir/*
%python_sitelibdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/polkit-1/actions/*.policy
%_datadir/%name
%ghost %_localstatedir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.30.0-alt1.1
- Rebuild with Python-2.7

* Mon Sep 13 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt1
- initial build for ALTLinux
- thx to aris@
