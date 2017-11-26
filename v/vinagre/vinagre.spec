%def_enable snapshot

%define ver_major 3.22
%define api_ver 3.0
%define _libexecdir %_prefix/libexec

# freerdp >= 2.0.0-alt0.git20160331 required
%def_enable rdp
%def_enable spice
%def_enable telepathy
%def_enable ssh

Name: vinagre
Version: %ver_major.0
Release: alt3

Summary: Remote desktop viewer for the GNOME Desktop
License: GPLv2
Group: Networking/Remote access
URL: https://wiki.gnome.org/Apps/Vinagre

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

#Patches from opensuse
Patch1:         vinagre-freerdp2.patch
Patch2:         vinagre-cert-validation-api.patch

Requires: dconf gnome-icon-theme-symbolic
%{?_enable_rdp:Requires: freerdp >= 2.0.0-alt0.git20160331}

BuildPreReq: rpm-build-gnome gnome-common desktop-file-utils
BuildPreReq: libappstream-glib-devel
BuildPreReq: intltool >= 0.35 glib2-devel >= 2.28.0
BuildPreReq: libgtk+3-devel >= 3.9.6 libgtk3vnc-devel >= 0.4.3-alt2
BuildRequires: libavahi-gobject-devel libavahi-ui-gtk3-devel libsecret-devel
BuildRequires: yelp-tools itstool xmllint
%{?_enable_ssh:BuildRequires: libvte3-devel >= 0.37 libxml2-devel}
%{?_enable_telepathy:BuildRequires: libtelepathy-glib-devel >= 0.11.6 libdbus-glib-devel}
%{?_enable_spice:BuildRequires: libspice-gtk3-devel}
%{?_enable_rdp:BuildRequires: libfreerdp-devel >= 1.1}
BuildRequires: gcc-c++

%description
Vinagre is a remote desktop viewer for GNOME, that uses Virtual Network
Computing (VNC) to remotely control another desktop. Additional
protocols, such as RDP and SSH, are also supported.

%prep
%setup
%patch1 -p1
%patch2 -p1
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
# for SSH plugin
export LIBS="$LIBS `pkg-config --libs libxml-2.0`"
%configure \
	--enable-ssh \
	%{subst_enable spice} \
	%{subst_enable ssh} \
	%{subst_enable rdp} \
	%{?_disable_introspection:--enable-introspection=no} \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std

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
%_datadir/metainfo/%name.appdata.xml
%_man1dir/vinagre.*
%doc AUTHORS NEWS README

%changelog
* Sun Nov 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt3
- updated to latest snapshot (fixed BGO #783517)
- fixed %%files section

* Wed Jul 26 2017 Alexey Shabalin <shaba@altlinux.ru> 3.22.0-alt2
- add patches from opensuse for build with freerdp-2.0.0-RC0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.2-alt2
- rebuild with spice-gtk-0.32-alt1

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1
- enabled RDP support, required freerdp >= 2.0.0-alt0.git20160331

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0
- disabled RDP support, our freerdp is too old again

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Apr 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2
- enabled rdp support via libfreerdp-1.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.90-alt1
- 3.5.90

* Tue Sep 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1.1
- rebuild with new libspice-client-glib-2.0.so.1, libspice-client-gtk-3.0.so.1

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
