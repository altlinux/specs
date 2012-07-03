%define ver_major 3.4
%define api_ver 3.0
%define panel_api_ver 4.0

%def_enable rdp
%def_enable spice
%def_enable telepathy
%def_enable ssh

Name: vinagre
Version: %ver_major.2
Release: alt1

Summary: VNC client for the GNOME Desktop
License: GPLv2
Group: Networking/Remote access
URL: http://www.gnome.org/projects/vinagre
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%{?_enable_rdp:Requires: rdesktop}

BuildPreReq: rpm-build-gnome gnome-common gnome-icon-theme
BuildPreReq: intltool >= 0.35 glib2-devel >= 2.28.0
BuildPreReq: libgtk3vnc-devel >= 0.4.3-alt2
BuildRequires: libavahi-gobject-devel libavahi-ui-gtk3-devel libgnome-keyring-devel
BuildRequires: yelp-tools itstool xmllint
%{?_enable_ssh:BuildRequires: libvte3-devel libxml2-devel}
%{?_enable_telepathy:BuildRequires: libtelepathy-glib-devel >= 0.11.6 libdbus-glib-devel}
%{?_enable_spice:BuildRequires: libspice-gtk3-devel}
BuildRequires: gcc-c++

%description
This is vinagre, a VNC client for the GNOME Desktop.

%package -n gnome-applets-extra-vinagre
Summary: Vinagre applet for GNOME panel
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description -n gnome-applets-extra-vinagre
This package contains panel applet for Vinagre - VNC client for the
GNOME Desktop

%define _libexecdir %gnome_appletsdir

%prep
%setup -q

%build
%autoreconf
# for SSH plugin
export LIBS="$LIBS `pkg-config --libs libxml-2.0`"
export ac_cv_path_RDESKTOP_PROGRAM=%_bindir/rdesktop
%configure \
	--enable-ssh \
	%{subst_enable spice} \
	%{subst_enable ssh} \
	%{subst_enable rdp} \
	%{?_disable_introspection:--enable-introspection=no} \
	--disable-schemas-compile

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

rm -rf %buildroot%_datadir/doc

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/telepathy/clients/Vinagre.client
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*
%_datadir/mime/packages/vinagre-mime.xml
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%config %_datadir/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%_datadir/GConf/gsettings/org.gnome.Vinagre.convert
%_man1dir/vinagre.*
%doc AUTHORS NEWS README

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Oct 30 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- broken RDP plugin temporarily disabled

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Aug 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- requires %%name-gir to work (ALT #26028)

* Wed Aug 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2
- enabled spice support

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Fri Apr 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Mar 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- fixed linking of ssh plugin

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Fri Feb 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0.1-alt1
- 2.28.0.1
- new -devel package

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Mon Aug 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- updated buildreqs

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Thu Mar 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- upated buildreqs

* Mon Dec 29 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- updated buildreqs

* Fri Dec 05 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- new subpackage -- gnome-applets-extra-vinagre
- updated buildreqs

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.5.1-alt2
- apply patch from repocop
- buildreq

* Tue Apr 15 2008 Igor Zubkov <icesik@altlinux.org> 0.5.1-alt1
- build for Sisyphus

* Thu Apr 03 2008 TABUCHI Takaaki <tab@momonga-linux.org>
- (0.5.0-2m)
- rebuild against gcc43

* Wed Mar 12 2008 Nishio Futoshi <futoshi@momonga-linux.org>
- (0.5.0-1)
- initial build
