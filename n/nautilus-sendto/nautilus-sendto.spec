%define ver_major 3.0

%def_enable gtk_doc
%def_with gupnp
%def_without gajim

Name: nautilus-sendto
Version: %ver_major.3
Release: alt1

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Summary: Nautilus Sendto menu item
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.gnome.org

Obsoletes: %name-thunderbird
Obsoletes: %name-sylpheed
Obsoletes: %name-balsa

Source: %name-%version.tar.xz

BuildPreReq: rpm-build-gnome
BuildRequires: intltool glib2-devel libgio-devel libgtk+3-devel pidgin-devel libpurple-devel libnautilus-devel
BuildRequires: libdbus-glib-devel libdbus-devel gtk-doc evolution-data-server-devel gcc-c++ gnome-common
%{?_with_gajim:BuildRequires: gajim}
%{?_with_gupnp:BuildRequires: libgupnp-devel}

%description
This application provides integration between nautilus and other.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package evolution
Summary: Send files from nautilus to evolution
Group: Graphical desktop/GNOME
Requires: evolution
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description evolution
This application provides integration between nautilus and evolution.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package pidgin
Summary: Send files from nautilus to pidgin
Group: Graphical desktop/GNOME
Requires: pidgin
Requires: %name = %version
Provides: %name-plugin = %version-%release
Provides: nautilus-sendto-gaim
Obsoletes: nautilus-sendto-gaim

%description pidgin
This application provides integration between nautilus and pidgin.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package gajim
Summary: Send files from nautilus to gajim
Group: Graphical desktop/GNOME
Requires: gajim
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description gajim
This application provides integration between nautilus and gajim.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package removable-devices
Summary: Send files from nautilus to removable devices
Group: Graphical desktop/GNOME
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description removable-devices
This application provides ability for nautilus to send files to
removable devices and shares.

%package nautilus-burn
Summary: Send files to from nautilus to nautilus-cd-burner
Group: Graphical desktop/GNOME
Requires: %name = %version
Provides: %name-plugin = %version-%release
Requires: brasero-nautilus

%description nautilus-burn
This application provides integration between nautilus and Nautilus CD Burner.

%package upnp
Summary: Send files to to UPNP Media Servers
Group: Graphical desktop/GNOME
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description upnp
Plugin to allow sending files to UPNP Media Servers

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
The %name-devel package contains header files for developing
applications that use %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
The %name-devel-doc package contains documentation needed for developing
applications that use %name

%prep
%setup -q

%build
%autoreconf
%configure \
	--with-plugins="evolution %{?_with_gajim:gajim} nautilus-burn pidgin removable-devices upnp" \
	--disable-schemas-compile \
	%{subst_enable gtk_doc} \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %name

%files -f %name.lang
%doc NEWS AUTHORS COPYING ChangeLog*
%_bindir/*
# in nautilus now
%exclude %_libdir/nautilus/extensions-3.0/libnautilus-sendto.so
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%_datadir/%name
%_datadir/GConf/gsettings/nautilus-sendto-convert
%_datadir/glib-2.0/schemas/*.xml
%_man1dir/*.1*

%files pidgin
%_libdir/%name/plugins/libnstpidgin.so

%if_with gajim
%files gajim
%_libdir/%name/plugins/libnstgajim.so
%endif

%files evolution
%_libdir/%name/plugins/libnstevolution.so

%files nautilus-burn
%_libdir/%name/plugins/libnstburn.so

%files removable-devices
%_libdir/%name/plugins/libnstremovable_devices.so

%if_with gupnp
%files upnp
%_libdir/%name/plugins/libnstupnp.so
%endif

%files devel
%_includedir/%name
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%else
%exclude %_datadir/gtk-doc/html/*
%endif

%changelog
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
