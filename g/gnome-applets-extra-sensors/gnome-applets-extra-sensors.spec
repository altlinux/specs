%define _name sensors-applet
%define ver_major 3.0
%define panel_api_ver 4.0

# disabled due the relocation error on x86_64
%def_without nvidia
%{?_with_nvidia:%set_verify_elf_method textrel=relaxed}
%def_with aticonfig
%def_enable udisks

Name: gnome-applets-extra-sensors
Version: %ver_major.0
Release: alt1

Summary: GNOME Sensors Applet
Group: Graphical desktop/GNOME
License: %gpl2plus
Url: http://%_name.sourceforge.net

Source: http://downloads.sourceforge.net/%_name/%_name-%version.tar.gz
Patch: %_name-2.2.1-alt-fix-plugin_name-linkage.patch

%{?_enable_devicekit:Requires: udisks}

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: glib2-devel >= 2.30.0
BuildPreReq: libgtk+3-devel >= 3.0.0
BuildPreReq: libgnome-panel-devel >= 3.0.0
BuildPreReq: libnotify-devel >= 0.3.0
BuildPreReq: libcairo-devel >= 1.0.4
BuildRequires: libsensors3-devel
BuildRequires: gnome-common gnome-doc-utils intltool gnome-common
BuildRequires: libSM-devel libXext-devel
%{?_enable_udisks:BuildRequires: libdbus-glib-devel libatasmart-devel >= 0.16}
%{?_with_nvidia:BuildRequires: nvidia-settings-devel}

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display
readings from hardware sensors, including CPU and system temperatures,
fan speeds and voltage readings under Linux.

%package plugin-nvidia
Summary: NVIDIA GPUs plugin for GNOME Sensors Applet
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description plugin-nvidia
GNOME Sensors Applet is an applet for the GNOME Panel to display
readings from hardware sensors, including CPU and system temperatures,
fan speeds and voltage readings under Linux.

This package provides plugin for NVIDIA GPUs.

%package plugin-ati
Summary: ATI/AMD GPUs plugin for GNOME Sensors Applet
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: fglrx-tools

%description plugin-ati
GNOME Sensors Applet is an applet for the GNOME Panel to display
readings from hardware sensors, including CPU and system temperatures,
fan speeds and voltage readings under Linux.

This package provides plugin for ATI/AMD GPUs.

%package devel
Summary: Development files for GNOME Sensors Applet
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package provides development files and libraries needed to write more
plugins and sensors for GNOME Sensors Applet.

%define _appletdir %gnome_appletsdir
# FIXME: For some reason, it put the applet to plain %_libexecdir/ anyway.

%prep
%setup -q -n %_name-%version
%patch

%build
%autoreconf
%configure \
    --enable-libnotify \
    %{subst_enable udisks} \
    %{subst_with nvidia} \
    %{?_with_aticonfig:--with-aticonfig=%_bindir/aticonfig} \
    --libexecdir=%gnome_appletsdir \
    --disable-static \
    --disable-scrollkeeper

%make_build

%install
%make_install install libexecdir=%gnome_appletsdir DESTDIR=%buildroot

%find_lang --with-gnome %_name

%files -f %_name.lang
%gnome_appletsdir/%_name
%_libdir/lib%_name-plugin.so.*
%dir %_libdir/%_name/plugins
%_libdir/%_name/plugins/*.so

%exclude %_libdir/%_name/plugins/*.la
%if_with aticonfig
%exclude %_libdir/%_name/plugins/libaticonfig.so
%endif
%if_with nvidia
%exclude %_libdir/%_name/plugins/libnvidia.so
%endif

%_datadir/dbus-1/services/org.gnome.panel.applet.SensorsAppletFactory.service
%_datadir/gnome-panel/%panel_api_ver/applets/org.gnome.applets.SensorsApplet.panel-applet
%_datadir/%_name/
%_pixmapsdir/%_name/
%_iconsdir/hicolor/22x22/devices/%_name-*.png
%_liconsdir/%_name.png
%doc AUTHORS README ChangeLog

%if_with nvidia
%files plugin-nvidia
%_libdir/%_name/plugins/libnvidia.so
%endif

%if_with aticonfig
%files plugin-ati
%_libdir/%_name/plugins/libaticonfig.so
%endif

%files devel
%_includedir/%_name/
%_libdir/lib%_name-plugin.so

%changelog
* Sat Apr 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Apr 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.2.7-alt1
- 2.2.7

* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt2
- updated buildreqs

* Thu Feb 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- new version
- build against libsensors3
- nvidia/ati plugins moved to separate subpackages

* Mon Sep 08 2008 Alexey Rusakov <ktirf@altlinux.org> 2.2.1-alt2
- Added libXext-devel to explicit buildreqs.

* Sat Dec 29 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.1-alt1
- New version (2.2.1).
- Fixed wicked linkage.
- Use macros from rpm-build-gnome.

* Sun Apr 29 2007 Alexey Rusakov <ktirf@altlinux.org> 1.7.12-alt1
- new version 1.7.12 (with rpmrb script)

* Sat Apr 21 2007 Alexey Rusakov <ktirf@altlinux.org> 1.7.11-alt1
- new version (1.7.11)

* Mon Jan 29 2007 Alexey Rusakov <ktirf@altlinux.org> 1.7.10-alt1
- new version (1.7.10)

* Wed Jun 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.1-alt2
- fixed packaging mistakes.

* Wed Jun 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 1.6.1-alt1
- new version (1.6.1)
- updated dependencies
- cleaned up the spec
- the applet now resides in %_libdir/gnome-applets.

* Mon Mar 14 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Mon Jan 31 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0
- Thanks to voldar@ for russian translation.

* Tue Jan 25 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.2.2-alt1
- First build for Sisyphus.

