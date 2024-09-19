%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.44
%define api_ver 2.8
%def_enable external_plugin
%def_enable mpris_plugin
%def_enable tracker3_plugin
%def_enable gtk
%define media_engine gstreamer

%if %media_engine == gstreamer
%def_enable playbin_plugin
%def_enable media_export_plugin
%def_enable gst_launch_plugin
%else
%def_disable playbin_plugin
%def_disable media_export_plugin
%def_disable gst_launch_plugin
%endif

Name: rygel
Version: %ver_major.0
Release: alt1

Summary: A UPnP v2 Media Server
Group: System/Servers
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/Rygel

Vcs: https://gitlab.gnome.org/GNOME/rygel.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define libxml_ver 2.7
%define vala_ver 0.36.0
%define gi_ver 1.33.4
%define gssdp_api_ver 1.6
%define gssdp_ver 1.6.0
%define gupnp_api_ver 1.6
%define gupnp_ver 1.6.0
%define gupnp_av_ver 0.12.8
%define gupnp_dlna_ver 0.9.4
%define gstreamer_ver 1.0
%define gst_api_ver 1.0
%define gst_ver 1.12
%define gst_pbu_ver 1.12
%define gst_tag_ver 1.12
%define gst_app_ver 1.12
%define gst_audio_ver 1.12
%define gst_ges_ver 1.16
%define gio_ver 2.62
%define gee_ver 0.8.0
%define uuid_ver 1.41.3
%define libsoup_ver 3.2
%define gtk_ver 3.22
%define libsqlite3_ver 3.5
%define mediaart_ver 1.9
%define tracker_ver 3.0

Requires: gstreamer%gst_api_ver >= %gst_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gstreamer-editing-services
Requires: gst-libav
Requires: lsdvd

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: gobject-introspection-devel >= %gi_ver
BuildRequires: pkgconfig(gssdp-%gssdp_api_ver) >= %gssdp_ver
BuildRequires: pkgconfig(gupnp-%gupnp_api_ver) >= %gupnp_ver
BuildRequires: pkgconfig(gupnp-av-1.0) >= %gupnp_av_ver
BuildRequires: pkgconfig(gio-2.0) >= %gio_ver
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gee-0.8) >= %gee_ver
BuildRequires: pkgconfig(uuid) >= %uuid_ver
BuildRequires: pkgconfig(libsoup-3.0) >= %libsoup_ver
BuildRequires: pkgconfig(libxml-2.0) >= %libxml_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gstreamer_ver
BuildRequires: pkgconfig(gstreamer-base-1.0) >= %gstreamer_ver
BuildRequires: pkgconfig(libmediaart-2.0) >= %mediaart_ver
BuildRequires: libunistring-devel
%if %media_engine == gstreamer
BuildRequires: pkgconfig(gstreamer-pbutils-1.0) >= %gst_pbu_ver
BuildRequires: pkgconfig(gstreamer-app-1.0) >= %gst_app_ver
BuildRequires: pkgconfig(gstreamer-audio-1.0) >= %gst_audio_ver
BuildRequires: pkgconfig(gst-editing-services-%gst_api_ver) >= %gst_ges_ver
BuildRequires: pkgconfig(gupnp-dlna-2.0) >= %gupnp_dlna_ver
BuildRequires: pkgconfig(gio-2.0) >= %gio_ver
BuildRequires: gir(Gst) = 1.0
%endif
%{?_enable_api_docs:BuildRequires: gtk-doc valadoc}
%{?_enable_tracker3_plugin:BuildRequires: pkgconfig(tracker-sparql-3.0) >= %tracker_ver}
%{?_enable_media_export_plugin:BuildRequires: pkgconfig(sqlite3) >= %libsqlite3_ver pkgconfig(gstreamer-tag-1.0) >= %gst_tag_ver pkgconfig(gstreamer-app-1.0) >= %gst_app_ver pkgconfig(gupnp-dlna-2.0) >= %gupnp_dlna_ver pkgconfig(gupnp-dlna-gst-2.0) >= %gupnp_dlna_ver }
BuildRequires: libvala-devel >= %vala_ver vala >= %vala_ver
BuildRequires: vapi(gupnp-1.6) vapi(gupnp-av-1.0) vapi(gio-2.0) vapi(gee-0.8) vapi(posix)
BuildRequires: gir(GUPnP) = 1.6 gir(GUPnPAV) = 1.0 gir(GObject) = 2.0 gir(Gee) = 0.8 gir(Gio) = 2.0 gir(GLib) = 2.0
%{?_enable_gtk:BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver}
BuildRequires: xsltproc docbook-style-xsl docbook-dtds
BuildRequires: pkgconfig(systemd)

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is
specifically designed for GNOME. It is based on GUPnP and is written (mostly)
in Vala language. The project was previously known as gupnp-media-server.

%package devel
Summary: Development package for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Files for development with %name.

%package devel-doc
Summary: Development documentation for Rygel libraries
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is
specifically designed for GNOME. It is based on GUPnP and is written (mostly)
in Vala language. The project was previously known as gupnp-media-server.

This package contains documentation needed to develop applications using Rygel
libraries.

%package tracker
Summary: Tracker3 plugin for %name
Group: System/Servers
Requires: %name = %EVR
Requires: localsearch

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %name

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool api_docs api-docs}
%nil
%meson_build

%install
%meson_install
# fix *.gir
sed -E -i 's|(/>)(<)|\1\n\2|g' %buildroot%_girdir/*.gir
%find_lang --with-gnome %name

%files -f %name.lang
%config(noreplace) %_sysconfdir/%name.conf
%_bindir/%name
%_bindir/%name-preferences
%_libexecdir/%name/
%_libdir/lib%name-*.so.*
%_libdir/%name-%api_ver/

%exclude %_libdir/%name-%api_ver/plugins/lib%name-tracker3.so
%exclude %_libdir/%name-%api_ver/plugins/tracker3.plugin

%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_prefix/lib/systemd/user/%name.service
%_datadir/dbus-1/services/*.service
%_man1dir/*
%_man5dir/*
%doc AUTHORS NEWS README*

%files tracker
%_libdir/%name-%api_ver/plugins/librygel-tracker3.so
%_libdir/%name-%api_ver/plugins/tracker3.plugin

%files devel
%_libdir/lib%name-*.so
%_includedir/%name-*
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*

%if_enabled api-docs
%files devel-doc
%_datadir/gtk-doc/html/lib%name-*/
%endif

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%changelog
* Sun Sep 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.44.0-alt1
- 0.44.0

* Tue May 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.6-alt1
- 0.42.6

* Sun Jan 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.42.5-alt1
- 0.42.5

* Thu Sep 07 2023 Yuri N. Sedunov <aris@altlinux.org> 0.42.4-alt1.1
- disabled lms plugin, unmantained lightmediascanner don't supports ffmpeg > 5

* Wed Aug 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.42.4-alt1
- 0.42.4

* Sat Apr 22 2023 Yuri N. Sedunov <aris@altlinux.org> 0.42.3-alt1
- 0.42.3

* Sat Apr 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.42.2-alt1
- 0.42.2

* Sat Feb 11 2023 Yuri N. Sedunov <aris@altlinux.org> 0.42.1-alt1
- 0.42.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.42.0-alt1
- 0.42.0

* Fri Jun 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.40.4-alt1
- 0.40.4

* Sun Jan 09 2022 Yuri N. Sedunov <aris@altlinux.org> 0.40.3-alt1
- 0.40.3

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 0.40.2-alt1
- 0.40.2

* Tue Jul 06 2021 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1.1
- fixed build

* Sat Feb 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0 (ported to Meson build system)

* Fri Jul 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.38.4-alt1
- 0.38.4

* Wed Nov 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.38.3-alt1
- 0.38.3

* Sun Oct 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.38.2-alt1
- 0.38.2

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 0.38.1-alt1
- 0.38.1

* Mon Mar 18 2019 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.36.2-alt1
- 0.36.2

* Mon Feb 05 2018 Yuri N. Sedunov <aris@altlinux.org> 0.36.1-alt1
- 0.36.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt1
- 0.34.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 0.32.1-alt1
- 0.32.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.30.3-alt1
- 0.30.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 0.30.2-alt1
- 0.30.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.30.1-alt1
- 0.30.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0

* Wed Mar 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.28.3-alt1
- 0.28.3

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.28.2-alt1
- 0.28.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- 0.28.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- 0.28.0

* Sun May 10 2015 Yuri N. Sedunov <aris@altlinux.org> 0.26.1-alt1
- 0.26.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sat Jan 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.24.3-alt1
- 0.24.3

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.2-alt1
- 0.24.2

* Wed Nov 05 2014 Yuri N. Sedunov <aris@altlinux.org> 0.24.1-alt1
- 0.24.1

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 0.24.0-alt1
- 0.24.0

* Mon Jul 28 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.3-alt1
- 0.22.3

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.2-alt1
- 0.22.2

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.1-alt1
- 0.22.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.22.0-alt1
- 0.22.0

* Wed Jan 15 2014 Alexey Shabalin <shaba@altlinux.ru> 0.20.3-alt1
- 0.20.3

* Thu Nov 14 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.2-alt1
- 0.20.2

* Thu Oct 17 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Wed Sep 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Mon Aug 12 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.4-alt1
- 0.18.4

* Tue Jul 30 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.3-alt1
- 0.18.3

* Mon May 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.2-alt1
- 0.18.2

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.1-alt1
- 0.18.1

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.17.9-alt1
- 0.17.9

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.17.8-alt1
- 0.17.8

* Mon Dec 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.5.1-alt1
- 0.17.5.1

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.17.4-alt1
- 0.17.4

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.3-alt1
- 0.16.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Fri Oct 12 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Tue Sep 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.3-alt1
- 0.14.3

* Mon Jul 30 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Tue May 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.13.3-alt1
- 0.13.3

* Wed Feb 08 2012 Alexey Shabalin <shaba@altlinux.ru> 0.12.7-alt1
- 0.12.7

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.6-alt1
- 0.12.6

* Mon Nov 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.5-alt1
- 0.12.5

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.4-alt1
- 0.12.4

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.3-alt1
- 0.12.3

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.2-alt1
- 0.12.2

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Thu Oct 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun May 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1.ba17eba
- git version with port to tracker 0.7 API

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- Initial release
