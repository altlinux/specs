%define ver_major 3.4
%def_disable static
%def_enable sendto
%def_enable map
%def_enable goa
%if_enabled goa
%define mcp_dir %(pkg-config --variable=plugindir mission-control-plugins)
%endif
%def_enable geocode
%def_enable gudev
%def_with cheese

Name: empathy
Version: %ver_major.2.2
Release: alt1

Summary: Instant Messaging Client for GNOME
License: GPL/LGPL
Group: Networking/Instant messaging
Url: http://live.gnome.org/Empathy

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Conflicts: telepathy-haze-aim
Obsoletes: libempathy libempathy-gtk python-module-empathy

Requires: %name-data = %version-%release

%define intltool_ver 0.35.0
%define glib_ver 2.31.10
%define gtk_ver 3.3.6
%define clutter_ver 1.1.2
%define clutter_gst_ver 1.5.2
%define tp_glib_ver 0.18.0
%define tp_logger_ver 0.2.13
%define tp_gabble_ver 0.16.0
%define tp_haze_ver 0.6.0
%define tp_salut_ver 0.8.0
%define mission_control_ver 5.12.0
%define enchant_ver 1.2.0
%define check_ver 0.9.4
%define iso_codes_ver 0.35
%define notify_ver 0.7.3
%define canberra_ver 0.26
%define webkit_ver 1.3.13
%define geoclue_ver 0.12
%define keyring_ver 2.32.0
%define gcr_ver 3.3.90
%define champlain_ver 0.12.0
%define gnutls_ver 2.8.5
%define folks_ver 0.6.4
%define nst_ver 2.91.6
%define farstream_ver 0.1.1
%define nm_ver 0.8.995
%define goa_ver 3.3.0

Requires: telepathy-gabble >= %tp_gabble_ver
Requires: telepathy-salut >= %tp_salut_ver
Requires: telepathy-haze >= %tp_haze_ver
Requires: libtelepathy-mission-control >= %mission_control_ver
Requires: gst-plugins-gconf
Requires: telepathy-logger >= %tp_logger_ver

BuildPreReq: intltool >= %intltool_ver gnome-common itstool
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libclutter-gtk3-devel >= %clutter_ver
BuildPreReq: libclutter-gst-devel >= %clutter_gst_ver
BuildPreReq: libtelepathy-glib-devel >= %tp_glib_ver
BuildPreReq: libfolks-devel >= %folks_ver
BuildPreReq: libenchant-devel >= %enchant_ver
BuildPreReq: libcheck-devel >= %check_ver
BuildPreReq: iso-codes-devel >= %iso_codes_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: libcanberra-gtk3-devel >= %canberra_ver
BuildPreReq: libgeoclue-devel >= %geoclue_ver
BuildPreReq: libwebkitgtk3-devel >= %webkit_ver
BuildPreReq: libgnome-keyring-devel >= %keyring_ver
BuildPreReq: gcr-libs-devel >= %gcr_ver
BuildPreReq: libtelepathy-logger-devel >= %tp_logger_ver
BuildPreReq: libgnutls-devel >= %gnutls_ver
# for gnome-control-center-3.0.x
# BuildPreReq: gnome-control-center-devel
BuildPreReq: NetworkManager-glib-devel >= %nm_ver libtelepathy-farstream-devel >= %farstream_ver
%{?_enable_sendto:BuildRequires: nautilus-sendto-devel >= %nst_ver}
%{?_enable_map:BuildPreReq: libchamplain-devel >= %champlain_ver  libchamplain-gtk3-devel >= %champlain_ver}
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver libtelepathy-mission-control-devel}
%{?_enable_geocode:BuildRequires: libgeocode-glib-devel}
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_with_cheese:BuildRequires: libcheese-devel}
BuildRequires: libcheck-devel gsettings-desktop-schemas-devel xsltproc
BuildRequires: yelp-tools itstool
BuildRequires: libpulseaudio-devel gstreamer-devel gst-plugins-devel
BuildRequires: db2latex-xsl evolution-data-server-devel gtk-doc
BuildRequires: xorg-cf-files libICE-devel libSM-devel

%description
Telepathy-based multi-protocol instant messaging client for GNOME
which supports Jabber, GTalk, MSN, IRC, Salut, and other protocols.

%package data
Summary: Arch independent files for Empathy
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for Empathy to work.

%package -n nautilus-sendto-empathy
Summary: Send files to from nautilus to Empathy
Group: Graphical desktop/GNOME
Requires: nautilus-sendto >= 2.28.2
Requires: %name = %version-%release
Provides: nautilus-sendto-plugin = %version-%release

%description -n nautilus-sendto-empathy
This application provides integration between nautilus and Empathy.

%prep
%setup -q

rm -f data/%name.desktop

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-schemas-compile \
	%{subst_enable static} \
	%{?_enable_goa:--enable-goa=yes} \
	%{?_enable_geocode:--enable-geocode=yes} \
	%{?_enable_gudev:--enable-gudev=yes} \
	%{subst_with cheese} \
	%{?_enable_sendto:--enable-nautilus-sendto=yes} \
	%{?_disable_sendto:--enable-nautilus-sendto=no}

# SMP-incompatible build
%make

%install
%make_install DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files
%_bindir/*
%_libexecdir/empathy-auth-client
%_libexecdir/empathy-call
%_libexecdir/empathy-chat
%if_enabled goa
%mcp_dir/mcp-account-manager-goa.so
%exclude %mcp_dir/mcp-account-manager-goa.la
%endif

%files data -f %name.lang
%_datadir/applications/empathy.desktop
%_datadir/applications/empathy-accounts.desktop
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service
%dir %_datadir/empathy
%_datadir/empathy/*.ui
%_datadir/empathy/*.dtd
%_datadir/empathy/irc-networks.xml
%_datadir/empathy/Template.html
%_datadir/telepathy/clients/Empathy.Chat.client
%_datadir/telepathy/clients/Empathy.Call.client
%_datadir/telepathy/clients/Empathy.Auth.client
%_datadir/telepathy/clients/Empathy.FileTransfer.client
%_datadir/empathy/icons/
%_datadir/empathy/empathy-log-window.html
%_datadir/icons/hicolor/*/apps/*
%_man1dir/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/%name.convert
%doc AUTHORS CONTRIBUTORS NEWS README TODO

%if_enabled sendto
%files -n nautilus-sendto-empathy
%_libdir/nautilus-sendto/plugins/libnstempathy.so
%exclude %_libdir/nautilus-sendto/plugins/libnstempathy.la
%endif


%changelog
* Wed Jun 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2.2-alt1
- 3.4.2.2

* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2.1-alt1
- 3.4.2.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Apr 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.2-alt1
- 3.4.0.2

* Thu Apr 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0.1-alt1
- 3.4.0.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt2
- rebuild against newest telepathy-farstream

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt3
- temporarily removed dependency on telepathy-haze (ALT #27058)

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- some fixes from upstream git (GNOME bugs ##664795,664564)
- split up noarch data in separate -data subpackage

* Mon Nov 14 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1.2-alt1
- 3.2.1.2

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt3
- rebuilt against folks-0.6.4.1

* Tue Oct 18 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- rebuilt against folks-0.6.4

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Tue Oct 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- rebuild against libchamplain-0.12

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Mon Aug 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- updated from git

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Mon Nov 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0.1-alt1
- 2.32.0.1

* Tue Aug 24 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.1-alt1
- 2.30.1.1
- gst-plugins-gconf added to requires (closes #23542)

* Mon Apr 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Apr 20 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0.2-alt1
- 2.30.0.2

* Fri Apr 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0.1-alt1
- 2.30.0.1

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.93-alt1
- 2.29.93

* Tue Jan 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5.1-alt2
- Add patch to fix crasher due to misuse of xmlCleanParser

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5.1-alt1
- 2.29.5.1

* Mon Dec 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Mon Dec 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- fixed build with new gtk-doc

* Mon Nov 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Fri Nov 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1.2-alt2
- NM support enabled again (patched to build against libnm-glib)

* Thu Nov 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1.2-alt1.1
- NM support temporarily disabled

* Thu Nov 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1.2-alt1
- 2.28.1.2

* Sat Oct 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1.1-alt1
- 2.28.1.1

* Mon Oct 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Fri Oct 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0.1-alt1
- 2.28.0.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Fri Sep 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt2
- updated to current git 

* Mon Sep 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Mon May 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2
- updated buldreqs

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0.1-alt1
- 2.26.0.1

* Fri Mar 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete %%post{,un} scripts
- updated {build,}reqs

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Fri Oct 03 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- updated {build,}reqs

* Sun Jul 20 2008 Igor Zubkov <icesik@altlinux.org> 0.23.4-alt1
- 0.23.4 -> 0.23.4

* Thu Jun 05 2008 Igor Zubkov <icesik@altlinux.org> 0.23.3-alt2
- fix for repocop

* Tue Jun 03 2008 Igor Zubkov <icesik@altlinux.org> 0.23.3-alt1
- 0.23.2 -> 0.23.3

* Mon May 26 2008 Igor Zubkov <icesik@altlinux.org> 0.23.2-alt2
- enable python module build

* Sun May 25 2008 Igor Zubkov <icesik@altlinux.org> 0.23.2-alt1
- 0.23.1 -> 0.23.2

* Sat May 24 2008 Igor Zubkov <icesik@altlinux.org> 0.23.1-alt1
- 0.22.1 -> 0.23.1

* Sun May 04 2008 Igor Zubkov <icesik@altlinux.org> 0.22.1-alt2
- fix for fresh sisyphus_check

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 0.22.1-alt1
- 0.22.0 -> 0.22.1

* Thu Apr 24 2008 Igor Zubkov <icesik@altlinux.org> 0.22.0-alt1
- 0.21.91 -> 0.22.0

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.21.91-alt1
- 0.21.90 -> 0.21.91

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.21.90-alt1
- 0.21.5.2 -> 0.21.90

* Thu Jan 24 2008 Igor Zubkov <icesik@altlinux.org> 0.21.5.2-alt1
- 0.21.5.1 -> 0.21.5.2

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 0.21.5.1-alt1
- 0.21.5 -> 0.21.5.1

* Tue Jan 15 2008 Igor Zubkov <icesik@altlinux.org> 0.21.5-alt1
- 0.21.4 -> 0.21.5
- buildreq

* Wed Jan 09 2008 Igor Zubkov <icesik@altlinux.org> 0.21.4-alt3
- move libempathy library to libempathy subpackage (#12567)
- move libempathy-gtk library to libempathy-gtk subpackage (#12567)
- move libempathy devel files to libempathy-devel subpackage (#12567)
- move libempathy-gtk devel files to libempathy-gtk-devel subpackage (#12567)

* Sat Jan 05 2008 Igor Zubkov <icesik@altlinux.org> 0.21.4-alt2
- add Conflicts: telepathy-haze-aim (it's don't needed anymore)

* Tue Dec 18 2007 Igor Zubkov <icesik@altlinux.org> 0.21.4-alt1
- 0.21.3 -> 0.21.4
- build with --enable-voip=yes

* Sun Dec 16 2007 Igor Zubkov <icesik@altlinux.org> 0.21.3-alt2
- bump release

* Tue Dec 04 2007 Igor Zubkov <icesik@altlinux.org> 0.21.3-alt1
- 0.21.2 -> 0.21.3
- build with --enable-voip=no (it's broken now)
- buildreq

* Mon Nov 12 2007 Igor Zubkov <icesik@altlinux.org> 0.21.2-alt1
- 0.21.1 -> 0.21.2

* Thu Nov 01 2007 Igor Zubkov <icesik@altlinux.org> 0.21.1-alt1
- 0.14 -> 0.21.1
- update License tag, some code from now is LGPL

* Fri Oct 12 2007 Igor Zubkov <icesik@altlinux.org> 0.14-alt1
- 0.13 -> 0.14
- build with --enable-voip=yes

* Fri Oct 12 2007 Igor Zubkov <icesik@altlinux.org> 0.13-alt2
- fix build on x86_64

* Sat Sep 29 2007 Igor Zubkov <icesik@altlinux.org> 0.13-alt1
- 0.12 -> 0.13

* Fri Sep 07 2007 Igor Zubkov <icesik@altlinux.org> 0.12-alt2
- rebuild with telepathy-mission-control-4.37-alt1

* Sat Aug 25 2007 Igor Zubkov <icesik@altlinux.org> 0.12-alt1
- 0.11 -> 0.12

* Wed Aug 15 2007 Igor Zubkov <icesik@altlinux.org> 0.11-alt2
- rebuild with telepathy-mission-control-4.34-alt1

* Mon Aug 13 2007 Igor Zubkov <icesik@altlinux.org> 0.11-alt1
- 0.10 -> 0.11

* Thu Aug 02 2007 Igor Zubkov <icesik@altlinux.org> 0.10-alt1
- 0.8 -> 0.10

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 0.8-alt1
- build for Sisyphus

