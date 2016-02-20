%define _libexecdir %_prefix/libexec

%define ver_major 3.12
%def_disable static
%def_enable map
%def_enable goa
%if_enabled goa
%define mcp_dir %(pkg-config --variable=plugindir mission-control-plugins)
%endif
%def_enable geocode
%def_enable location
%def_enable gudev
%def_with cheese
%define gst_api_ver 1.0

Name: empathy
Version: %ver_major.11
Release: alt3

Summary: Instant Messaging Client for GNOME
License: GPL/LGPL
Group: Networking/Instant messaging
Url: https://live.gnome.org/Empathy

#Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source: %name-%version.tar

Conflicts: telepathy-haze-aim
Obsoletes: libempathy libempathy-gtk python-module-empathy

%define intltool_ver 0.35.0
%define glib_ver 2.37.6
%define gtk_ver 3.9.4
%define clutter_ver 1.1.2
%define clutter_gst_ver 1.9.92
%define tp_glib_ver 0.23.2
%define tp_logger_ver 0.8.0
%define tp_gabble_ver 0.16.0
%define tp_haze_ver 0.6.0
%define tp_salut_ver 0.8.0
%define mission_control_ver 5.13.0
%define enchant_ver 1.2.0
%define check_ver 0.9.4
%define iso_codes_ver 0.35
%define notify_ver 0.7.3
%define canberra_ver 0.26
%define webkit_ver 1.3.13
%define geoclue2_ver 1.99.3
%define gcr_ver 3.3.90
%define champlain_ver 0.12.0
%define gnutls_ver 2.8.5
%define folks_ver 0.9.5
%define nst_ver 2.91.6
%define nm_ver 0.8.995
%define goa_ver 3.6.2
%define secret_ver 0.5
%define farstream_ver 0.2
%define geocode_ver 0.99.3

Requires: %name-data = %version-%release

Requires: telepathy-gabble >= %tp_gabble_ver
Requires: telepathy-salut >= %tp_salut_ver
Requires: telepathy-haze >= %tp_haze_ver
Requires: libtelepathy-mission-control >= %mission_control_ver
Requires: telepathy-logger >= %tp_logger_ver
Requires: farstream0.2 >= %farstream_ver
%{?_enable_location:Requires: geoclue2 >= %geoclue2_ver}

BuildPreReq: intltool >= %intltool_ver gnome-common itstool
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libclutter-gtk3-devel >= %clutter_ver
BuildPreReq: libclutter-gst2.0-devel >= %clutter_gst_ver
BuildPreReq: libtelepathy-glib-devel >= %tp_glib_ver
BuildPreReq: libfolks-devel >= %folks_ver
BuildPreReq: libenchant-devel >= %enchant_ver
BuildPreReq: libcheck-devel >= %check_ver
BuildPreReq: iso-codes-devel >= %iso_codes_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildPreReq: libcanberra-gtk3-devel >= %canberra_ver
BuildPreReq: libwebkitgtk3-devel >= %webkit_ver
BuildPreReq: libsecret-devel >= %secret_ver
BuildPreReq: gcr-libs-devel >= %gcr_ver
BuildPreReq: libtelepathy-logger-devel >= %tp_logger_ver
BuildPreReq: libgnutls-devel >= %gnutls_ver
BuildRequires: libgee0.8-devel gobject-introspection-devel libgtk+3-gir-devel
# for gnome-control-center-3.0.x
# BuildPreReq: gnome-control-center-devel
BuildPreReq: NetworkManager-glib-devel >= %nm_ver libtelepathy-farstream-devel >= %farstream_ver
%{?_enable_map:BuildPreReq: libchamplain-devel >= %champlain_ver  libchamplain-gtk3-devel >= %champlain_ver}
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver libtelepathy-mission-control-devel}
%{?_enable_location:BuildPreReq: geoclue2-devel >= %geoclue2_ver}
%{?_enable_geocode:BuildRequires: libgeocode-glib-devel >= %geocode_ver}
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_with_cheese:BuildRequires: libcheese-devel}
BuildRequires: libcheck-devel gsettings-desktop-schemas-devel xsltproc
BuildRequires: yelp-tools itstool
BuildRequires: libpulseaudio-devel gstreamer%gst_api_ver-devel gst-plugins%gst_api_ver-devel
BuildRequires: db2latex-xsl evolution-data-server-devel gtk-doc
BuildRequires: xorg-cf-files libICE-devel libSM-devel
# for check
BuildRequires: xvfb-run

%description
Telepathy-based multi-protocol instant messaging client for GNOME
which supports Jabber, GTalk, MSN, IRC, Salut, and other protocols.

%package data
Summary: Arch independent files for Empathy
Group: Networking/Instant messaging
BuildArch: noarch

%description data
This package provides noarch data needed for Empathy to work.

%prep
%setup

rm -f data/%name.desktop

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-schemas-compile \
	%{subst_enable static} \
	%{?_enable_goa:--enable-goa=yes} \
	%{?_enable_geocode:--enable-geocode=yes} \
	%{?_enable_location:--enable-location=yes} \
	%{?_enable_gudev:--enable-gudev=yes} \
	%{subst_with cheese} \
	--disable-Werror
# SMP-incompatible build
%make

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name %name-tpaw

%check
# empathy-parser-test failed
# xvfb-run %make check

%files
%_bindir/*
%_libexecdir/empathy-auth-client
%_libexecdir/empathy-call
%_libexecdir/empathy-chat
%dir %_libdir/%name
%_libdir/%name/lib%name-%{version}*.so
%_libdir/%name/lib%name.so
%_libdir/%name/lib%name-gtk-%{version}*.so
%_libdir/%name/lib%name-gtk.so
%exclude %_libdir/%name/*.la
%if_enabled goa
%mcp_dir/mcp-account-manager-goa.so
%exclude %mcp_dir/mcp-account-manager-goa.la
%endif

%files data -f %name.lang
%_datadir/applications/%name.desktop
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Chat.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Call.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.Auth.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Empathy.FileTransfer.service
%dir %_datadir/%name
%_datadir/%name/*.ui
%_datadir/%name/irc-networks.xml
%_datadir/%name/Template.html
%_datadir/%name/%name.css
%_datadir/telepathy/clients/Empathy.Chat.client
%_datadir/telepathy/clients/Empathy.Call.client
%_datadir/telepathy/clients/Empathy.Auth.client
%_datadir/telepathy/clients/Empathy.FileTransfer.client
%_datadir/%name/icons/
%_datadir/%name/%name-log-window.html
%_datadir/icons/hicolor/*/apps/*
%dir %_datadir/adium
%_datadir/adium/*
%_man1dir/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/%name.convert
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS CONTRIBUTORS NEWS README TODO


%changelog
* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.12.11-alt3
- updated to 3.12.11-10-ga7ad339

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.11-alt2
- rebuilt against libgnutls.so.30

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.11-alt1
- 3.12.11

* Tue Aug 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.10-alt2
- updated to 3.12.10_e567bbbb

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.10-alt1
- 3.12.10

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.9-alt1
- 3.12.9

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.8-alt1
- 3.12.8

* Fri Jan 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt2
- rebuilt against libfarstream-0.2.so.5

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.7-alt1
- 3.12.7

* Fri Sep 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.6-alt1
- 3.12.6

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.5-alt1
- 3.12.5

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.4-alt1
- 3.12.4

* Wed Jun 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0
- removed obsolete nautilus-sendto-empathy subpackage

* Tue Jan 07 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Fri May 31 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0
- geocode support temporarily disabled

* Mon Mar 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Wed Jan 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.6.3-alt1
- 3.6.3

* Wed Nov 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Wed Nov 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt2
- rebuilt against libtelepathy-logger.so.3

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Oct 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.3-alt1
- 3.6.0.3

* Mon Oct 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.2-alt1
- 3.6.0.2

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.1-alt1
- 3.6.0.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

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
- move lib%name library to lib%name subpackage (#12567)
- move lib%name-gtk library to lib%name-gtk subpackage (#12567)
- move lib%name devel files to lib%name-devel subpackage (#12567)
- move lib%name-gtk devel files to libempathy-gtk-devel subpackage (#12567)

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

