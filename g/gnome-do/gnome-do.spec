
Name: gnome-do
Version: 0.8.5
Release: alt1
Summary: Quick launch and search

License: %gpl3plus
Group: Graphical desktop/GNOME
Url: http://do.davebsd.com/
Source: http://launchpad.net/do/trunk/%version/+download/%name-%version.tar
Patch1: gnome-do-0.8.1-alt-mono-nunit.patch

Provides: mono(Do.Platform) = 0.10.0.0
Provides: mono(Do.Platform.Linux) = 0.10.0.0
Provides: mono(Do.Universe) = 0.10.0.0
Provides: mono(Do.Interface.Linux) = 0.10.0.0
Provides: mono(Do.Interface.Linux.Classic) = 0.10.0.0
Provides: mono(Do.Interface.Linux.AnimationBase) = 0.10.0.0
Provides: mono(Do.Interface.Linux.GlassFrame) = 0.10.0.0
Provides: mono(Do.Interface.Linux.HUD) = 0.10.0.0
Provides: mono(Do.Interface.Linux.Mini) = 0.10.0.0

BuildRequires: GConf libGConf-devel gcc-c++ intltool libgtk+2-devel
BuildRequires: mono-addins-devel
BuildRequires: ndesk-dbus-devel
BuildRequires: ndesk-dbus-glib-devel
BuildRequires: libgtk-sharp2-devel
BuildRequires: libnotify-sharp-devel
BuildRequires: libgnome-sharp-devel libgnome-desktop-sharp-devel
BuildRequires: libgnome-keyring-sharp-devel
BuildRequires: mono-nunit-devel

BuildPreReq: rpm-build-mono mono-mcs mono-devel
BuildPreReq: rpm-build-licenses desktop-file-utils
BuildRequires: /proc

%description
Allows you to quickly search for many objects present in your
GNOME desktop environment and perform commonly used commands
on those objects

%package devel
Summary: Develpment files for GNOME Do
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for GNOME Do

%prep
%setup -q
%patch1 -p1

%build
rm -f *.m4
ACLOCAL="aclocal -I m4/shamrock"  %autoreconf
%configure --disable-schemas-install
%make_build

%install
%make_install install DESTDIR=%buildroot

install -m 644 data/%name.desktop %buildroot%_desktopdir/%name.desktop

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS COPYING COPYRIGHT
%_bindir/*
%_libdir/%name
%config(noreplace) %_sysconfdir/xdg/autostart/%name.desktop
%config %_sysconfdir/gconf/*/*
%_iconsdir/hicolor/*/apps/%name.*
%_desktopdir/%name.desktop

%files devel
%_pkgconfigdir/*

%changelog
* Mon Feb 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Wed Dec 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3.1-alt2
- fix build with new gtk+

* Tue Jan 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3.1-alt1
- 0.8.3.1

* Mon Jul 13 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt2
- update buildreq

* Fri Jul 03 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Jun 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.1.3-alt1
- 0.8.1.3
- build with mono-nunit support

* Sat Jan 31 2009 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- initial package for ALTLinux

