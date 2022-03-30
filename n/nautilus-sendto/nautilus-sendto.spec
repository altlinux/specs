%def_enable snapshot
%define ver_major 3.8

Name: nautilus-sendto
Version: %ver_major.6
Release: alt2

Summary: Nautilus Sendto menu item
License: GPLv2
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.26

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson intltool libgio-devel >= %glib_ver gobject-introspection-devel
BuildRequires: %_bindir/appstream-util

%description
This application provides integration between nautilus and e-mail agents.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email which you want to send the file/files.

%prep
%setup
sed -i "s/'appdata'\,//" src/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_man1dir/%name.1*
%_datadir/metainfo/*.xml
%doc NEWS AUTHORS

%changelog
* Wed Mar 30 2022 Yuri N. Sedunov <aris@altlinux.org> 3.8.6-alt2
- updated to 3_8_6-28-gc87aac4
- fixed build with meson >= 0.61

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.8.6-alt1
- 3.8.6

* Thu Jun 22 2017 Yuri N. Sedunov <aris@altlinux.org> 3.8.5-alt1
- 3.8.5

* Fri Sep 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt3
- rebuilt against e-d-s-3.10 libraries

* Wed Mar 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- rebuilt against e-d-s-3.8 libraries

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- rebuilt against newest e-d-s

* Wed Mar 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2
- gajim support disabled

* Thu Oct 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt2
- rebuilt against libebook-1.2.so.12

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- rebuilt against libgupnp-1.0.so.4 (gupnp-0.17)

* Sun May 29 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Mon Jun 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.28.4-alt2
- rebuild with libedataserver-1.2.so.13

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.28.4-alt1
- 2.28.4

* Sat Mar 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt3
- disabled bluetooth/empathy

* Mon Nov 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt2
- new subpackage devel

* Thu Nov 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt1
- 2.28.2
- enabled empathy/upnp

* Wed Nov 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt4
- disabled empathy/upnp

* Sat Oct 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt3
- 2.28.0

* Fri Oct 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt2
- nautilus-sendto-nautilus-burn: fixed requires (closes: #21768)

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.5-alt1
- 1.1.5
- add -upnp package

* Thu Apr 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.4.1-alt1
- 1.1.4.1

* Sat Apr 18 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sun Apr 05 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.3-alt1
- 1.1.3
- aris@
    removed obsolete patch for balsa
    updated buildreqs
    removed obsolete -thunderbird, -sylpheed, -balsa plugins
    new -empathy, -burn, -removable-devices plugins

* Tue Feb 10 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt3
- changed requires from bluez-utils to bluez for bluetooth package(need for bluez-4)

* Tue Oct 28 2008 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- rebuild

* Mon Oct 06 2008 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Aug 21 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Jul 08 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt3
- change requires for bluetooth from gnome-bluetooth to bluez-gnome

* Tue Jun 24 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt2
- fix requires for thunderbird plugin
- remove requires for sylpheed plugin
- add provides %name-claws-mail for sylpheed plugin
- build balsa plugin
- fix sending files with balsa (patch1, thx Nick Butorin)

* Fri Jun 20 2008 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0
- revoke from orphaned
- rewrite spec, based on mandriva (thx Andrey Novoselov)

* Sat Sep 03 2005 Vital Khilko <vk@altlinux.ru> 0.4-alt1
- 0.4
- added bluetooth subpackage

* Mon Jan 31 2005 Vital Khilko <vk@altlinux.ru> 0.3-alt1
- initial build for ALT Linux Sisyphus
- added belarusian translation
