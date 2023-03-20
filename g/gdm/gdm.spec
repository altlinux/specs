%def_disable snapshot

%define ver_major 44
%define beta %nil
%define api_ver 1.0

%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%define default_pam_config redhat
# Initial virtual terminal to use
%define vt_nr 1

%def_disable static
%def_disable debug
%def_enable ipv6
%def_with xdmcp
%def_with selinux
%def_with libaudit
%def_without plymouth
%def_enable wayland
%def_enable xsession
#Enable running X server as user
%def_enable user_display_server
%def_enable check

Name: gdm
Version: %ver_major.0
Release: alt1%beta

Summary: The GNOME Display Manager
License: GPL-2.0
URL: http://wiki.gnome.org/Projects/GDM
Group: Graphical desktop/GNOME

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

Source1: gdm_xdmcp.control
Source2: gdm.wms-method
Source3: default.pa-for-gdm

# PAM config files
Source10: gdm.pam
Source11: gdm-autologin.pam
Source12: gdm-password.pam
Source13: gdm-launch-environment.pam
Source14: gdm-smartcard.pam
Source15: gdm-fingerprint.pam

Patch2: gdm-40.beta-alt-Xsession.patch
Patch7: gdm-40.beta-alt-Init.patch

Obsoletes: %name-gnome
Provides: %name-gnome = %version-%release
Provides: gnome-dm

# from meson.build
%define glib_ver 2.56.0
%define gtk_ver 3.16.0
%define shell_ver %ver_major
%define libcanberra_ver 0.4
%define accountsservice_ver 0.6.35
%define check_ver 0.9.4
%define session_ver 40
%define gudev_ver 232

Provides: %name-user-switch-applet = %version-%release
Obsoletes: %name-user-switch-applet

Requires(pre): %_rpmlibdir/update-dconf-database.filetrigger
Requires(pre): %name-libs = %version-%release
Requires(pre): %name-data = %version-%release
Requires: gnome-shell >= %shell_ver
Requires: accountsservice >= %accountsservice_ver
Requires: coreutils xinitrc iso-codes lsb-release shadow-utils
Requires: gnome-session >= %session_ver
Requires: gnome-session-wayland
Requires: /bin/dbus-run-session

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires(pre): rpm-build-gir rpm-macros-pam0 rpm-build-systemd
BuildRequires: meson gcc-c++ desktop-file-utils gnome-common yelp-tools
BuildRequires: iso-codes-devel
BuildRequires: glib2-devel >= %glib_ver libgio-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libaccountsservice-devel >= %accountsservice_ver
BuildRequires: libgudev-devel >= %gudev_ver
BuildRequires: dconf pkgconfig(systemd) libpam-devel
%{?_with_selinux:BuildPreReq: libselinux-devel libattr-devel}
%{?_with_libaudit:BuildPreReq: libaudit-devel}
%{?_with_plymouth:BuildPreReq: plymouth-devel}
BuildRequires: libcanberra-devel >= %libcanberra_ver libcanberra-gtk3-devel
BuildRequires: libXdmcp-devel

BuildRequires: libX11-devel libXau-devel libXrandr-devel libXext-devel libXft-devel libSM-devel
BuildRequires: libXi-devel xorg-proto-devel libXinerama-devel
BuildRequires: xorg-xephyr xorg-server
BuildRequires: libkeyutils-devel
BuildRequires: libcheck-devel >= %check_ver

BuildRequires: libdmx-devel
BuildRequires: librsvg-devel perl-XML-Parser docbook-dtds xsltproc zenity
BuildRequires: gobject-introspection-devel
BuildRequires: libdaemon-devel libudev-devel
%{?_enable_check:BuildRequires: /proc dbus-tools-gui}

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%package data
Summary: Arch independent files for GDM
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: gdm2.20

%description data
This package provides noarch data needed for GDM to work.

%package libs
Summary: GDM libraries
Group: System/Libraries

%description -n %name-libs
This package contains shared libraries needed for GNOME Display Manager
to work.

%package libs-devel
Summary: Development files for GDM libraries
Group: Development/C
Requires: %name-libs = %version-%release

%description libs-devel
This package contains headers and development libraries for GNOME
Display Manager.

%package libs-gir
Summary: GObject introspection data for the GDM
Group: System/Libraries
Requires: %name-libs = %version-%release

%description libs-gir
GObject introspection data for the GDM libraries.

%package libs-gir-devel
Summary: GObject introspection devel data for the GDM
Group: Development/Other
BuildArch: noarch
Requires: %name-libs-gir = %version-%release
Requires: %name-libs-devel = %version-%release

%description libs-gir-devel
GObject introspection devel data for the GDM libraries.

%package help
Summary: User documentation for Gdm
Group: Graphical desktop/GNOME
BuildArch: noarch
Conflicts: %name < %version-%release

%description help
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

This package contains user documentation for Gdm.

%prep
%setup -n %name-%version%beta
sed -i 's|/usr\(/bin/touch\)|\1|' data/61-gdm.rules.in
%patch2 -p1 -b .XSession
%patch7 -p1 -b .Init

# just copy our PAM config files to %default_pam_config directory
cp %SOURCE10 %SOURCE11 %SOURCE12 %SOURCE13 %SOURCE14 %SOURCE15  data/pam-%default_pam_config/

%build
%meson \
	%{?_enable_ipv6:-Dipv6=true} \
	-Dinitial-vt='%vt_nr' \
	-Ddefault-path='/bin:/usr/bin:/usr/local/bin' \
	-Dsysconfsubdir='X11/gdm' \
	-Dpam-prefix='%_sysconfdir' \
	-Dpam-mod-dir='%_pam_modules_dir' \
	-Ddefault-pam-config='%default_pam_config' \
	-Ddmconfdir='%_sysconfdir/X11/sessions' \
	-Dudev-dir='%_udevrulesdir' \
	%{?_without_xdmcp:-Dxdmcp=disabled} \
	%{?_without_libaudit:-Dlibaudit=disabled} \
	%{?_without plymouth:-Dplymouth=disabled} \
	%{?_disable_wayland:-Dwayland-support=false} \
	%{?_enable_xsession:-Dgdm-xsession=true} \
	%{?_disable_user_display_server:-Duser-display-server=false}
%nil
%meson_build

%install
mkdir -p %buildroot%_sysconfdir/X11/sessions
mkdir -p %buildroot%_sysconfdir/X11/wms-methods.d

%meson_install
rm -f %buildroot%_sysconfdir/pam.d/gdm

# env.d directories
mkdir -p %buildroot{%_sysconfdir/X11,%_datadir}/gdm/env.d

# install external hook for update_wms
install -m755 %SOURCE2 %buildroot%_sysconfdir/X11/wms-methods.d/%name

# control gdm/xdmcp
install -pDm755 %SOURCE1 %buildroot%_controldir/gdm_xdmcp

# default.pa for gdm
install -p -m644 -D %SOURCE3 %buildroot%_localstatedir/lib/gdm/.config/pulse/default.pa

%find_lang %name
%find_lang --output=%name-help.lang --without-mo --with-gnome %name

%check
dbus-run-session %__meson_test

%pre
%pre_control gdm_xdmcp

%post
%post_control -s disabled gdm_xdmcp

%files
%_sbindir/gdm
%_bindir/gdm-screenshot
%_bindir/gdmflexiserver
%_libexecdir/gdm-host-chooser
%_libexecdir/gdm-session-worker
%_libexecdir/gdm-simple-chooser
%_libexecdir/gdm-wayland-session
%_libexecdir/gdm-x-session
%_libexecdir/gdm-runtime-config
%_pam_modules_dir/pam_gdm.so
%_unitdir/gdm.service
%_userunitdir/gnome-session@gnome-login.target.d/session.conf
%doc AUTHORS NEWS README*

%files data -f %name.lang
%config %_sysconfdir/pam.d/gdm-autologin
%config %_sysconfdir/pam.d/gdm-password
%config %_sysconfdir/pam.d/gdm-launch-environment
%config %_sysconfdir/pam.d/gdm-smartcard
%config %_sysconfdir/pam.d/gdm-fingerprint
%_udevrulesdir/61-%name.rules
%config %_sysconfdir/dbus-1/system.d/%name.conf
%config %_datadir/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
%config(noreplace) %_sysconfdir/X11/%name
%dir %_sysconfdir/X11/sessions
%config %_controldir/gdm_xdmcp
%_sysconfdir/X11/wms-methods.d/%name
%dir %_datadir/%name
%_datadir/%name/locale.alias
%_datadir/%name/gdb-cmd
%_datadir/%name/%name.schemas
%dir %_datadir/%name/greeter
%dir %_datadir/%name/greeter/applications
%_datadir/%name/greeter-dconf-defaults
%_datadir/gnome-session/sessions/gnome-login.session
%_datadir/dconf/profile/%name
%attr(1770, gdm, gdm) %dir %_localstatedir/lib/gdm
%attr(1750, gdm, gdm) %dir %_localstatedir/lib/gdm/.config
%attr(1750, gdm, gdm) %dir %_localstatedir/lib/gdm/.config/pulse
%attr(0600, gdm, gdm) %_localstatedir/lib/gdm/.config/pulse/default.pa
%_datadir/gdm/greeter/applications/mime-dummy-handler.desktop
%_datadir/gdm/greeter/applications/mimeapps.list
%dir %_datadir/%name/greeter/autostart
%exclude %_datadir/gdm/greeter/autostart/orca-autostart.desktop

%files help -f %name-help.lang

%files libs
%_libdir/libgdm.so.*

%files libs-devel
%_includedir/gdm/
%_libdir/libgdm.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-pam-extensions.pc

%files libs-gir
%_typelibdir/Gdm-%api_ver.typelib

%files libs-gir-devel
%_girdir/Gdm-%api_ver.gir


%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Fri Oct 07 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt2
- data/61-gdm.rules.in: /usr/bin/touch -> /bin/touch (reported by shaba@)

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1.1
- Requires(pre): -libs, -data subpakages

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Mon Sep 06 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.9.rc
- 41

* Fri Jul 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Tue Dec 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2.1-alt1
- 3.38.2.1 (fixed CVE-2020-27837)

* Tue Nov 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0 (ported to Meson build system)

* Tue Jul 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sun May 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt2
- updated to 3.36.2-real-1-g38fc7ef8 (fixed user switching)

* Tue May 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Feb 27 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3 (fixed CVE-2019-3825)

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Fri Sep 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt2
- updated to 3.30.0-4-g839c9501
- reverted "gdm-wayland-session,gdm-x-session: register after delay"
  (https://gitlab.gnome.org/GNOME/gdm/issues/419)
- temporarily disabled plymouth support

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt2
- rebuilt without tcp_wrappers

* Wed Aug 29 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.4-alt1
- 3.28.4

* Sun Aug 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt2
- removed obsolete deps on caribou

* Mon Aug 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3 (fixed CVE-2018-14424)
- disabled parallel build on aarch64

* Wed Jun 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- updated to 3.28.2-15-g909d417

* Sat May 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2.1-alt1
- 3.26.2.1

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3 (fixed CVE-2017-12164)

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Mar 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Nov 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Thu Oct 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt2
- 3.18.0_76e2a54a (fixed BGO #754814)

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1.1
- temporarily disabled default wayland session before new Mesa and Xorg

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Sep 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.3-alt1
- 3.16.3

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon May 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1.1-alt2
- explicitly enabled wayland support

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1.1-alt1
- 3.16.1.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0.1-alt1
- 3.16.0.1

* Fri Oct 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Tue Sep 16 2014 Alexey Shabalin <shaba@altlinux.ru> 3.13.91-alt1
- 3.13.91

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt2
- add post_script for enable gdm.service

* Wed Jun 11 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt1
- 3.12.2

* Wed Apr 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt4
- remove compatibility "-nodaemon" option patch
- add upstream 0001-Revert-"worker:-get-PATH-from-parent-instead-of-#define".patch
- update pam configs
- cleanup spec

* Thu Apr 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt3
- set initial vt number to 1 for "flicker-free plymouth transition"

* Thu Apr 17 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt2
- add compatibility with xdm "-nodaemon" option

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0
- removed ConsoleKit support

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3.1-alt1
- 3.8.3.1

* Fri Jun 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3
- obsoleted gnome subpackage

* Sat Apr 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1.1-alt1.1
- removed %%_datadir/gdm/greeter/autostart/orca-autostart.desktop

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1.1-alt1
- 3.8.1.1

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Fri Apr 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- after 3.8.0 snapshot (7a040a9)
- updated buildreqs
- disabled fallback greeter (gnome-shell required)

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- 3.7.92
- disabled console-kit support

* Sun Feb 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt5
- fixed relogin if autologin enabled (ALT #28475)(BGO 682467)
  patch: http://git.gnome.org/browse/gdm/commit/?h=gnome-3-6&id=12ba97b9741a9f1691f2ef7417871c148dd9fa09

* Wed Feb 13 2013 Michael Shigorin <mike@altlinux.org> 3.6.2-alt4
- NMU: fixed /var/run/gdm permissions which were blocking
  proper pam_xauth execution; thanks ldv@ (closes: #28549)

* Sun Dec 23 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt3
- reverted http://git.gnome.org/browse/gdm/commit/?h=gnome-3-6&id=affb42aff901f407502e4d2c0eb65b4f30a1275d (ALT #28231)

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt2
- after 3.6.2 snapshot (b60452d12)
- %%check section

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Oct 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to 571ea34

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Jul 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt0.1
- 3.4.2 snapshot
- plymouth support enabled

* Sun Apr 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Sun Dec 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1.1-alt2
- fix to skip users with invalid shells (such as "hasher sitellite")

* Thu Nov 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1.1-alt1
- 3.2.1.1
- packaged automatically updated from dconf posttrans filetrigger
  %%_sysconfdir/dconf/db/gdm as %%ghost

* Tue Oct 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt4
- aditional fix for https://bugzilla.gnome.org/show_bug.cgi?id=658451 from upstream

* Thu Oct 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt3
- fixed https://bugzilla.gnome.org/show_bug.cgi?id=658451 from upstream

* Sat Oct 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git
- adapted pam/gdm-welcome

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Sep 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92
- removed gdm-alt-polkit.patch, gdm-alt-dconf.patch (obsolete)
- updated gdm-alt-Init.patch
- fixed link (gdm-3.1.92-alt-link.patch)
- introspection support, new -libs* subpackages
- TODO: inspect extensions, especially its pam configurations
- disabled split authentication

* Wed Jun 01 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.4-alt1
- 3.0.4 (fixed CVE-2011-1709)

* Fri May 27 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt3
- 3.0.2

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt3
- cas@:
  Update Russian tranaslation for translated `Cancel` button

* Sun May 22 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt2
- Mark the Cancel button for translation (ALT #20988)
- Correctly give focus to the user chooser on startup (Gnome #629310)

* Wed Mar 30 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt1
- fixed CVE-2011-0727 - change to user before copying user files

* Fri Dec 10 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt3
- update gdm Init

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt2
- disable a11y by default
- add path(/var/lib/gdm/.gconf.defaults) for distribution default values
- add default settings

* Tue Sep 28 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt1
- 2.32.0
- build with SELinux

* Thu Aug 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.5-alt1
- 2.30.5
- Don’t use dbus-launch --exit-with-session for the login session (Gnome #624373)
- Port to upower (Gnome #626176)

* Fri Jul 02 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt3
- rebuild with new libaudit

* Fri Jun 25 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt2
- 2.30.2 release (without snapshot of branch 2-30)
- ldv@:
  + pam.d/gdm-autologin: rewrite using common-login, drop pam_env
  + pam.d/gdm: rewrite using common-login, drop pam_env and nopasswdlogin check

* Tue Jun 22 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt1
- 2.30.2
- ldv@: /etc/pam.d/gdm: Added pam_shells to auth stack (closes: #23643).

* Tue Apr 27 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.1-alt1
- 2.30.1 + snapshot (= 2.30.2)

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.92-alt1
- 2.29.92

* Thu Jan 28 2010 Alexey Shabalin <shaba@altlinux.ru> 2.29.6-alt1
- 2.29.6
- build without any patches, only altlinux specific

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt1
- 2.28.2
- fixed permissions for /var/cache/gdm

* Mon Dec 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt3
- fixed spurious requires (closes: #17047)

* Fri Dec 11 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.1-alt2
- mike@:
  + added XDMCP control support by ktirf@ (closes: #17047)
  + applied patch from RH#496882 to fix cookies when using XDMCP
- add --with-default-path="/bin:/usr/bin:/usr/local/bin" (ALT #21897)

* Thu Oct 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt2
- new subpackage %name-gnome
- fixed polkit-gnome-authentication-agent-1 path

* Tue Sep 22 2009 Alexey Shabalin <shaba@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.91-alt0.2
- git version 20090914

* Thu Sep 10 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.91-alt0.1
- 2.27.91 snapshot
- remove pam_ck_connector.so from pam config files (import from 2.26.1-alt3)
- improper work with XKB (import from 2.26.1-alt2)

* Wed Aug 26 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.90-alt2
- update buildreq

* Tue Aug 25 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.90-alt1
- 2.27.90

* Fri Aug 21 2009 Alexey Shabalin <shaba@altlinux.ru> 2.27.4-alt0.1
- 2.27.4 + git 20090821

* Mon May 04 2009 Alexey Shabalin <shaba@altlinux.ru> 2.26.1-alt1
- remove hack for strip unneeded translations from .mo files
- add external hook for update_wms (ALT#19288)
- thx rider@ :
  + new version, build from git
  + temporary removed multi-stack patch

* Wed Apr 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.26.0-alt1
- 2.26.0
- applay patch from multi-stack branch (http://git.gnome.org/cgit/preview/gdm/?h=multi-stack)
- TODO: plugin-fingerprint and plugin-smartcard subpackage
- add patches from fedora
- move patch2 to Source2
- strip unneeded translations from .mo files

* Fri Mar 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Wed Dec 17 2008 Yuri N. Sedunov <aris@altlinux.org> 2.25.2-alt1
- 2.25.2
- replaced trivial gdm-2.24.0-alt-grep.patch by subst expression
- removed other useless and upstreamed patches

* Thu Dec 04 2008 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- new unstable release

* Thu Dec 04 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt3
- provides gnome-dm
- requires GConf-sanity-check
- removed patch6 implemeted in previous release, --
  /etc/gconf/gconf.xml.system directory packaged in GConf now
- build gdm-help as noarch

* Tue Dec 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.1-alt2
- fix warning gconf-sanity-check-2 on startup(patch6)

* Wed Nov 19 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- remove upstreamed patches
- remove {update,clean}_{scrollkeeper,wms} calls from %%post{,un}

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt2
- fix path  to su for in /usr/sbin/gdm

* Tue Sep 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- 2.24.0
- add patches from fedora cvs

* Thu Sep 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.8-alt1
- 2.20.8
- hard disabled xdmcp in custom.conf

* Tue Aug 19 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.7-alt2
- update custom config (selected default theme "Happy GNOME with Browser")

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.7-alt1
- 2.20.7

* Mon Jun 16 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.6-alt1
- 2.20.6

* Wed Apr 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.5-alt1
- 2.20.5

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.4-alt1
- 2.20.4

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.3-alt1
- 2.20.3

* Tue Dec 25 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt4
- Correct buildreq

* Mon Dec 24 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt3
- Thanks to Alexey Shabalin <shaba@altlinux.ru>
-     build with ConsoleKit support
-     add some RH patches

* Tue Nov 27 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Fri Oct 19 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.1-alt1
- 2.20.1 (WARNING: PAM files changed)

* Tue Sep 18 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.20.0-alt1
- 2.20.0 (this virsion crashes on startup)

* Wed Aug 08 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt1
- new version (2.18.4), includes the fix for CVE-2007-3381.
- more macros usage in the spec
- removed most of %%__ macros
- removed some excess buildreqs
- added --disable-static and %%excluded .la files to get rid of rpmbuild warning

* Wed May 30 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.2-alt1
- 2.18.2

* Mon Apr 09 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.1-alt1
- 2.18.1

* Mon Mar 12 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.18.0-alt0.1
- 2.18.0

* Wed Mar 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.17.8-alt0.1
- 2.17.8 (!!WARNING!! this is an experimental build)

* Mon Jan 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.5-alt1
- 2.16.5

* Wed Dec 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.4-alt1
- 2.16.4

* Mon Nov 27 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.3-alt1
- 2.16.3

* Wed Nov 01 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.2-alt1
- 2.16.2

* Wed Oct 25 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt2
- Run system Xsession script instead gdm specific

* Mon Oct 09 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.1-alt1
- 2.16.1

* Fri Sep 08 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.16.0-alt1
- 2.16.0

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.10-alt1
- 2.14.10

* Tue Jun 13 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.9-alt1
- 2.14.9 (security fix!!!)

* Thu May 25 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.7-alt1
- 2.14.7

* Wed May 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.6-alt1
- 2.14.6

* Tue May 02 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.4-alt1
- 2.14.4

* Sun Apr 16 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.2-alt1
- 2.14.2

* Tue Apr 11 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.1-alt1
- 2.14.1

* Mon Mar 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt2
- Add patch for successfull build with --as-needed (by D.Levin)

* Fri Mar 17 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Tue Mar 14 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.10-alt2
- ChangeLog corrected

* Fri Mar 10 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.10-alt1
- 2.13.0.10

* Tue Mar 07 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.8-alt2
- Disable --as-needed flag for linker

* Wed Feb 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.8-alt1
- 2.13.0.8

* Fri Feb 03 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.7-alt1
- 2.13.0.7

* Mon Jan 23 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.5-alt2
- auto BuildReq regeneration

* Thu Jan 19 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.13.0.5-alt1
- 2.13.0.5

* Fri Dec 02 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.7-alt1
- 2.8.0.7

* Mon Oct 10 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.5-alt1
- 2.8.0.5

* Sat Sep 17 2005 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.8.0.4-alt3
- 2.8.0.4

* Mon Apr 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.9-alt1
- 2.6.0.9

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.8-alt1
- 2.6.0.8

* Wed Feb 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.7-alt1
- 2.6.0.7

* Sat Dec 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.6-alt2
- user help moved to gdm-help subpackage.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.6-alt1
- 2.6.0.6

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.3-alt1
- 2.6.0.3

* Thu Jun 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt2.1
- comment out BaseXsession (requires updated update_wms)
- partially merge /usr/X11R6/lib/X11/locale/locale.alias
  and /etc/X11/gdm/locale.alias for ru_RU, uk_UA, be_BY.

* Wed Jun 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt2
- fix #1572.
- apply BaseXsession=/etc/X11/Xsession in gdm.conf
- requires newest xinitrc.

* Wed May 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.2-alt1
- 2.6.0.2

* Mon Apr 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.0-alt1
- 2.6.0.0

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90.2-alt1
- 2.5.90.2

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90.1-alt1
- 2.5.90.1

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.7-alt1
- 2.4.4.7

* Sat Oct 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.5-alt1
- 2.4.4.5

* Fri Oct 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.4-alt1
- 2.4.4.4

* Sat Oct 04 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.4.3-alt2
- Updated package dependencies.
- Updated package build dependencies.

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.3-alt1
- 2.4.4.3

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.2-alt2
- fix /etc/X11/gdm/Xsession.

* Thu Sep 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.2-alt1
- 2.4.4.2

* Fri Sep 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.4.0-alt1
- 2.4.4.0

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.97-alt1
- 2.4.2.97

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.96-alt2
- build process fixed
- fixed %%files section.

* Sat Jun 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.96-alt1
- 2.4.2.96

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2.95-alt1
- 2.4.2.95

* Mon Jun 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.4-alt2
- /etc/pam.d/{gdm-autologin,gdmsetup} adopted for new PAM configuration
  policy (requires pam >= 0.75-alt20).

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.4-alt1
- 2.4.1.4
- Modify /usr/bin/gdm to avoid root (POSIX) locale setting
  (Alexey Morozov <morozov@novosoft.ru>)

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.3-alt1
- 2.4.1.3

* Sun Jan 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.2-alt1
- 2.4.1.2

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt2
- removed not useful dependence on mandrake_desk.

* Tue Jan 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.1-alt1
- 2.4.1.1

* Fri Jan 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1.0-alt1
- 2.4.1.0

* Thu Nov 21 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.12-alt1
- 2.4.0.12

* Mon Nov 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt3
- Precached consolehelper for %%configure.
- %%files section fixed.
- Rebuilt with new libwrap.
- Updated buildrequires.

* Sun Oct 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt2
- rebuild with new pango, gtk+.
- Some changes in default configuration.

* Sat Sep 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0.11-alt1
- 2.4.0.11 (GNOME-2.0.2)

* Thu Mar 21 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.5-alt2
- fixed buildreqs

* Thu Mar 14 2002 Sergey N. Yatskevich <syatskevich@mail.ru> 2.2.5.5-alt1
- update

* Mon Feb 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.4-alt1
- update

* Thu Jan 31 2002 Sergey N. Yatskevich <syatskevich@mail.ru> 2.2.5.2-alt3
- fix filesystem and pam directory conflicts

* Wed Jan 09 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2.5.2-alt2
- fix locale files
- clear /etc/X11/gdm/Sessions directory

* Sat Nov 24 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.5.2

* Fri Sep 07 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.4.1

* Sat Jun 09 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
- release 2.2.2.1

* Tue Mar 20 2001 AEN <aen@logic.ru>
- useradd removed

* Thu Jan 04 2001 AEN <aen@logic.ru>
- adopted for RE

* Thu Nov 23 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.0beta4-23mdk
- Chinese fix. (Andrew Lee @ CLE)

* Mon Oct  9 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-22mdk
- Really apply faces patch

* Mon Oct  2 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-21mdk
- Correct pam dependancy

* Tue Sep 26 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-20mdk
- Add apache and zope as non-visible users in browser
- bziped pam file

* Mon Sep 25 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0beta4-19mdk
- pam uses pam_stack.

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-18mdk
- New login screen

* Thu Sep 14 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-17mdk
- Prevent respawn

* Tue Sep  5 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-16mdk
- Check faces with .png extension

* Wed Aug 30 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-15mdk
- /var/state -> /var/lib (FHS 2.1)

* Tue Aug 22 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-14mdk
- Clean spec
- merge from helix (3mdk_helix_2)
- update i18n from cvs
- decompress manual before installing it
- disable language menu
- change location of user icons

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0beta4-13mdk
- automatically added BuildRequires

* Tue Jul 25 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-12mdk
- Correct location of icon used by gdm
- use more macros

* Mon Jul 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-11mdk
- Recompile with new rpm version
- Correct gdm.conf to reflect BM

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 2.0beta4-10mdk
- macrozification.

* Thu Jul 20 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0beta4-9mdk
- BM

* Mon Jul 17 2000 dam's <damien@mandrakesoft.com> 2.0beta4-8mdk
- added fndsession call in post/postun

* Wed Jul  5 2000 dam's <damien@mandrakesoft.com> 2.0beta4-7mdk
- spec. cleanup

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 2.0beta4-6mdk
- bziped source 2 5 11 12.

* Tue Jul  4 2000 dam's <damien@mandrakesoft.com> 2.0beta4-5mdk
- updated from helix.

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.0beta4-4mdk
- Use tmppath macros.
- BuildRequires: pam-devel

* Wed May 17 2000 dam's <damien@mandrakesoft.com> 2.0beta4-3mdk
- corrected exclude list

* Fri May 05 2000 dam's <damien@mandrakesoft.com> 2.0beta4-2mdk
- Changed again background color.

* Fri Apr 21 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0beta4-1mdk
- release 2.0beta4
- add some nice users and mandrake logo! looks great !
- remove unnecessary patches.

* Sat Apr 15 2000 Daouda Lo <daouda@mandrakesoft.com> 2.0beta2-11mdk
- fixed gdmlogin bug .
- merge with helix stuffs .
- add /sbin/ldconfig in post to load shared libraries

* Tue Apr 04 2000 dam's <damin@mandrakesoft.com> 2.0beta2-10mdk
- fixed logo & background locations.

* Mon Apr 03 2000 Jerome Martin <jerome@mandrakesoft.com> 2.0beta2-9mdk
- spec-helper issues cleanup
- fixed group

* Wed Jan 12 2000 Pixel <pixel@mandrakesoft.com>
- libtoolize --force

* Fri Jan  7 2000 Pixel <pixel@mandrakesoft.com>
- remove the Language menu (doesn't work and made gnome fail to load the right font)

* Wed Dec 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Require mandrake_desk and put a new image at startup.

* Wed Dec 15 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- add a post to make sure Xsession is executable.

* Mon Nov 01 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Add docs (r)

* Sun Oct 31 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- Adapt for Linux-Mandrake from Redhat spec (13):
	- SMP building
	- bzip2 man/info (don't think it has any (yet))

* Sun Sep 26 1999 Elliot Lee <sopwith@redhat.com>
- Fixed pipewrite bug (found by mkj & ewt).
