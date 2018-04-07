%def_enable snapshot

%define _libexecdir %_prefix/libexec/polkit-1
%define oldname PolicyKit-gnome

Name: polkit-gnome
Version: 0.106
Release: alt0.1

Summary: polkit integration tool for the GNOME 3 desktop
License: GPLv2+
Group: System/Libraries
Url: http://git.gnome.org/cgit/PolicyKit-gnome/

Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Requires: polkit
Provides: %oldname = %version-%release
Obsoletes: %oldname < %version
Obsoletes: lib%name

%if_disabled snapshot
Source: http://ftp.gnome.org/pub/gnome/sources/%name/%version/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-0.106-alt-desktop.patch

BuildRequires(pre): rpm-build-xdg
BuildRequires: gnome-common intltool libpolkit-devel libgtk+3-devel libcairo-gobject-devel

%description
%name provides a GNOME Authentication Agent for polkit that matches the
look and feel of the GNOME desktop.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure  \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang %name-1

%files -f %name-1.lang
%doc README AUTHORS NEWS HACKING
%_libexecdir/%name-authentication-agent-1
%_xdgconfigdir/autostart/%name-authentication-agent-1.desktop

%changelog
* Sat Apr 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.106-alt0.1
- updated to 0.105-66-ga0763a2
- restored /etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
  for DEs that do not provide its own polkit-agent

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 0.105-alt1
- updated to 0.105
- removed harmful for gnome-3.6 /etc/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

* Tue Mar 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.101-alt1
- 0.101

* Tue Feb 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.100-alt1
- 0.100

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.99-alt1
- 0.99

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt3
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt2
- rebuild

* Sat Jan 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.96-alt1
- 0.96

* Sat Nov 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt2
- obsoletes PolicyKit-gnome

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.95-alt1
- 0.95

* Thu Aug 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.94-alt1
- 0.94

* Thu Jul 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt2
- fixes for dbus-glib-0.82

* Wed Jul 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.9-alt2
- apply a patch to fix applications using PolicyKit-gnome with widgets that only email clicked events

* Sun Aug 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.9-alt1
- release 0.9

* Mon Apr 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- release 0.8
- show the menu item in other desktops too
- fix i18n (fedora patch1)
- drop other patches(upsteam fixed)

* Thu Apr 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt2
- add requires PolicyKit (#15132, #15133)
- define dir libexecdir as %%_prefix/libexec/PolicyKit

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 0.7-alt1
- initial build for ALTLinux

