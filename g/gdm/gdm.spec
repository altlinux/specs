%define ver_major 3.4

%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%define authentication_scheme pam
%def_disable static
%def_disable debug
%def_enable ipv6
%def_with xinerama
%def_with xdmcp
%def_with tcp_wrappers
%def_with selinux
%def_with consolekit
%def_with systemd
%def_with libaudit
%def_without xevie
%def_disable split_authentication

Name: gdm
Version: %ver_major.1
Release: alt1

Summary: The GNOME Display Manager
License: GPLv2+
URL: ftp://ftp.gnome.org/
Group: Graphical desktop/GNOME
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar.xz
Source1: gdm_xdmcp.control
Source2: gdm.wms-method

Patch0: gdm-snapshot.patch
Patch2: gdm-3.2.1.1-alt-Xsession.patch
Patch3: gdm-3.1.92-alt-pam.patch
Patch7: gdm-3.1.92-alt-Init.patch
Patch9: gdm-3.2.2-alt-link.patch
Patch10: gdm-3.2.1.1-alt-invalid_user_shell.patch

# from configure.ac
%define dbus_glib_ver 0.74
%define glib_ver 2.29.3
%define gtk_ver 2.91.1
%define pango_ver 1.3.0
%define scrollkeeper_ver 0.1.4
%define libxklavier_ver 4.0
%define libcanberra_ver 0.4
%define fontconfig_ver 2.5.0
%define upower_ver 0.9.0
%define accountsservice_ver 0.6.12

Provides: %name-user-switch-applet = %version-%release
Obsoletes: %name-user-switch-applet

PreReq: %_rpmlibdir/update-dconf-database.filetrigger
Requires: %name-libs = %version-%release
%{?_with_consolekit:Requires: ConsoleKit-x11}
Requires: coreutils consolehelper zenity xinitrc iso-codes lsb-release

BuildPreReq: desktop-file-utils gnome-common gnome-doc-utils rpm-build-gnome
BuildPreReq: intltool >= 0.40.0
BuildPreReq: libdbus-glib-devel >= %dbus_glib_ver
BuildPreReq: iso-codes-devel
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: librarian
BuildPreReq: libupower-devel >= %upower_ver
BuildPreReq: libaccountsservice-devel >= %accountsservice_ver
%{?_with_consolekit:BuildPreReq: libConsoleKit-devel}
%{?_with_systemd:BuildRequires: systemd-devel}
%{?_with_selinux:BuildPreReq: libselinux-devel libattr-devel}
%{?_with_libaudit:BuildPreReq: libaudit-devel}
BuildPreReq: libpam-devel
%{?_with_tcp_wrappers:BuildPreReq: libwrap-devel}
BuildPreReq: libgnome-panel-devel >= 2.0.0
BuildPreReq: libxklavier-devel >= %libxklavier_ver
BuildPreReq: libcanberra-devel >= %libcanberra_ver libcanberra-gtk3-devel
BuildPreReq: fontconfig-devel >= %fontconfig_ver
BuildPreReq: libX11-devel libXau-devel libXrandr-devel libXext-devel libXdmcp-devel libXft-devel libSM-devel
BuildPreReq: libXi-devel xorg-inputproto-devel libXinerama-devel xorg-xineramaproto-devel libXevie-devel
BuildPreReq: xorg-xephyr xorg-server
BuildPreReq: libcheck-devel >= 0.9.4
BuildPreReq: libnss-devel >= 3.11.1

BuildRequires: docbook-dtds gcc-c++ gnome-doc-utils-xslt libdmx-devel
BuildRequires: libpopt-devel librsvg-devel perl-XML-Parser xsltproc zenity
BuildRequires: gobject-introspection-devel
#BuildRequires: libhal-devel

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

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

%package extension-fingerprint
Summary: Fingerprint extension for Gdm
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: %_libdir/gdm/simple-greeter/extensions

%description extension-fingerprint
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

This package contains Fingerprint extension for Gdm.

%package extension-smartcard
Summary: Smartcard extension for Gdm
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: %_libdir/gdm/simple-greeter/extensions

%description extension-smartcard
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

This package contains Smartcard extension for Gdm.

%package gnome
Summary: GNOME-specific part of Gdm
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %version-%release
Provides: gnome-dm
Conflicts: %name < 2.28.0-alt1
Requires: gnome-session >= 3.2.1
Requires: polkit-gnome gnome-settings-daemon >= 3.2.1

%description gnome
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

Install this package for use with GNOME desktop.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1 -b .altpam
%patch7 -p1
%patch9 -p1 -b .link
%patch10 -p1 -b .shells

%build
mkdir -p m4
gnome-doc-prepare -f
%autoreconf
%configure \
	%{subst_enable static} \
	--disable-scrollkeeper \
	--disable-schemas-compile \
	--enable-console-helper \
	--enable-authentication-scheme=%authentication_scheme \
	%{subst_enable ipv6} \
	%{subst_enable debug} \
	--with-sysconfsubdir=X11/gdm \
	%{subst_with xinerama} \
	%{subst_with xdmcp} \
	%{?_with_tcp_wrappers:--with-tcp-wrappers} \
	%{subst_with selinux} \
	%{?_with_consolekit:--with-console-kit} \
	%{subst_with systemd} \
	--with-pam-prefix=%_sysconfdir \
	%{subst_with xevie} \
	%{subst_with libaudit} \
	--disable-dependency-tracking \
	--with-default-path="/bin:/usr/bin:/usr/local/bin" \
	%{?_disable_split_authentication:--disable-split-authentication}

%make_build

%install
mkdir -p %buildroot%_sysconfdir/X11/sessions
mkdir -p %buildroot%_sysconfdir/X11/wms-methods.d

%make DESTDIR=%buildroot install

# create empty default dconf database updated from dconf posttrans filetrigger
touch %buildroot/%_sysconfdir/dconf/db/gdm

# install external hook for update_wms
install -m755 %SOURCE2 %buildroot%_sysconfdir/X11/wms-methods.d/%name

find %buildroot -name '*.a' -delete
find %buildroot -name '*.la' -delete

# control gdm/xdmcp
install -pDm755 %SOURCE1 %buildroot%_controldir/gdm_xdmcp

%find_lang %name
%find_lang --output=%name-help.lang --without-mo --with-gnome %name

%pre
%pre_control gdm_xdmcp

%post
%post_control -s disabled gdm_xdmcp

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%config %_sysconfdir/pam.d/gdm
%config %_sysconfdir/pam.d/gdm-autologin
%config %_sysconfdir/dbus-1/system.d/%name.conf
%config %_datadir/glib-2.0/schemas/org.gnome.login-screen.gschema.xml
%config(noreplace) %_sysconfdir/X11/%name
%config %_sysconfdir/dconf/profile/gdm
%ghost %_sysconfdir/dconf/db/gdm
%dir %_sysconfdir/dconf/db/gdm.d
%_sysconfdir/dconf/db/gdm.d/00-upstream-settings
%dir %_sysconfdir/dconf/db/gdm.d/locks
%_sysconfdir/dconf/db/gdm.d/locks/00-upstream-settings-locks
%dir %_sysconfdir/X11/sessions
%config %_controldir/gdm_xdmcp
%_sysconfdir/X11/wms-methods.d/%name
%_bindir/*
%_sbindir/*
%_libexecdir/*
%dir %_datadir/%name
%_datadir/%name/*.ui
%_datadir/%name/locale.alias
%_datadir/%name/gdb-cmd
%_datadir/%name/gdm.schemas
%_pixmapsdir/*
%_datadir/icons/*/*/*/*.*
%dir %_localstatedir/log/gdm
%attr(775, gdm, gdm) %dir %_localstatedir/cache/gdm
%attr(1770, gdm, gdm) %dir %_localstatedir/lib/gdm
%attr(1750, gdm, gdm) %dir %_localstatedir/lib/gdm/.local
%attr(1750, gdm, gdm) %dir %_localstatedir/lib/gdm/.local/share
%attr(1777, root, gdm) %dir %_localstatedir/run/gdm

%dir %_datadir/gdm/simple-greeter/extensions
%dir %_datadir/gdm/simple-greeter

%_sysconfdir/pam.d/gdm-welcome
%dir %_datadir/gdm/simple-greeter/extensions/unified
%_datadir/gdm/simple-greeter/extensions/unified/page.ui

%if_enabled split_authentication
%_sysconfdir/pam.d/gdm-password
%_libdir/gdm/simple-greeter/extensions/libpassword.so
%dir %_datadir/gdm/simple-greeter/extensions/password
%_datadir/gdm/simple-greeter/extensions/password/page.ui
%endif

%files help -f %name-help.lang

%files gnome
%_datadir/gdm/greeter/applications/gdm-simple-greeter.desktop
%_datadir/gdm/greeter/applications/gnome-mag.desktop
%_datadir/gdm/greeter/applications/gnome-shell.desktop
%_datadir/gdm/greeter/applications/gok.desktop
%_datadir/gdm/greeter/applications/mime-dummy-handler.desktop
%_datadir/gdm/greeter/applications/mimeapps.list
%_datadir/gdm/greeter/applications/orca-screen-reader.desktop
%_datadir/gnome-session/sessions/gdm-fallback.session
%_datadir/gnome-session/sessions/gdm-shell.session

%files libs
%_libdir/libgdmgreeter.so.*
%_libdir/libgdmsimplegreeter.so.*

%files libs-devel
%_includedir/gdm/
%_libdir/libgdmgreeter.so
%_libdir/libgdmsimplegreeter.so
%_libdir/pkgconfig/gdmgreeter.pc
%_libdir/pkgconfig/gdmsimplegreeter.pc

%files libs-gir
%_typelibdir/GdmGreeter-1.0.typelib

%files libs-gir-devel
%_girdir/GdmGreeter-1.0.gir

# TODO
%if_enabled split_authentication
%files extension-fingerprint
%_sysconfdir/pam.d/gdm-fingerprint
%_libdir/gdm/simple-greeter/extensions/libfingerprint.so
%dir %_datadir/gdm/simple-greeter/extensions/fingerprint
%_datadir/gdm/simple-greeter/extensions/fingerprint/page.ui

%files extension-smartcard
%_sysconfdir/pam.d/gdm-smartcard
%_libdir/gdm/simple-greeter/extensions/libsmartcard.so
%dir %_datadir/gdm/simple-greeter/extensions/smartcard
%_datadir/gdm/simple-greeter/extensions/smartcard/page.ui
%endif

%changelog
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

* Fri Nov 24 2001 Sergey N. Yatskevich <syatskevich@mail.ru>
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

* Fri Sep 26 1999 Elliot Lee <sopwith@redhat.com>
- Fixed pipewrite bug (found by mkj & ewt).
