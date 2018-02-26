%define ver_major 0.14
%def_enable vala
%def_enable tracker_plugin
%def_enable media_export_plugin
%def_enable external_plugin
%def_enable mpris_plugin
%def_enable playbin_plugin
%def_enable mediathek_plugin
%def_enable gst_launch_plugin
%def_with ui

Name: rygel
Version: %ver_major.1
Release: alt1
Summary: A UPnP v2 Media Server

Group: System/Servers
License: LGPLv2+
Url: http://live.gnome.org/Rygel
Packager: GNOME Maintainers Team <gnome at packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%ver_major/%name-%version.tar

%define vala_ver 0.14.1
%define gssdp_ver 0.11.0
%define gupnp_ver 0.17.1
%define gupnp_av_ver 0.9.0
%define gupnp_dlna_ver 0.5.0
%define gupnp_vala_ver 0.10.2
%define gstreamer_ver 0.10.35
%define gstreamer_plugins_ver 0.10.35
%define gio_ver 2.26
%define gee_ver 0.5.2
%define uuid_ver 1.41.3
%define libsoup_ver 2.34.0
%define gtk_ver 2.90.3
%define libsqlite3_ver 3.5

BuildRequires: intltool gnome-common
BuildRequires: libgssdp-devel >= %gssdp_ver
BuildRequires: libgupnp-devel >= %gupnp_ver
BuildRequires: libgupnp-av-devel >= %gupnp_av_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_dlna_ver
BuildRequires: gstreamer-devel >= %gstreamer_ver
BuildRequires: libgio-devel >= %gio_ver
BuildRequires: libgee-devel >= %gee_ver
BuildRequires: libuuid-devel >= %uuid_ver
BuildRequires: libsoup-devel >= %libsoup_ver
%{?_enable_media_export_plugin:BuildRequires: libsqlite3-devel >= %libsqlite3_ver gst-plugins-devel >= %gstreamer_plugins_ver}
%{?_enable_vala:BuildRequires: libvala-devel >= %vala_ver vala >= %vala_ver libgupnp-vala >= %gupnp_vala_ver}
%{?_with_ui:BuildRequires: libgtk+3-devel >= %gtk_ver}
BuildRequires: xsltproc docbook-style-xsl docbook-dtds
# ? gconf-2.0.pc in rygel-1.0.pc
BuildRequires: libGConf-devel

%description
Rygel is an implementation of the UPnP MediaServer V 2.0 specification that is
specifically designed for GNOME. It is based on GUPnP and is written (mostly)
in Vala language. The project was previously known as gupnp-media-server.

%package devel
Summary: Development package for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Files for development with %name.

%package tracker
Summary: Tracker plugin for %name
Group: System/Servers
Requires: %name = %version-%release
Requires: tracker

%description tracker
A plugin for rygel to use tracker to locate media on the local machine.

%prep
%setup -q
echo %version > .tarball-version

%build
%autoreconf
# glib-gettextize --force --copy
# ./autogen.sh
%configure \
	%{subst_enable vala} \
	%{subst_with ui} \
	%{?_enable_tracker_plugin:--enable-tracker-plugin} \
	%{?_enable_media_export_plugin:--enable-media-export-plugin} \
	%{?_enable_external_plugin:--enable-external-plugin} \
	%{?_enable_mpris_plugin:--enable-mpris-plugin} \
	%{subst_enable playbin_plugin} \
	%{?_enable_mediathek_plugin:--enable-mediathek-plugin} \
	%{?_enable_gst_launch_plugin:--enable-gst-launch-plugin}


%make_build

%install

%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS COPYING README TODO NEWS
%config(noreplace) %_sysconfdir/rygel.conf
%_bindir/*
%_libdir/%name-1.0/*.so
%exclude %_libdir/%name-1.0/librygel-tracker.so
%_datadir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%_datadir/dbus-1/services/*.service
%_man1dir/*
%_man5dir/*
%exclude %_libdir/%name-1.0/*.la

%files tracker
%_libdir/%name-1.0/librygel-tracker.so

%files devel
%_includedir/%name-*
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*

%changelog
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
