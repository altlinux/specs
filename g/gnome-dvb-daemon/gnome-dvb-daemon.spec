%def_enable totem

Name: gnome-dvb-daemon
Version: 0.2.9
Release: alt1

Summary: DVB Daemon for GNOME 3
Group: Video
License: GPLv3
Url: http://live.gnome.org/DVBDaemon

Source: http://launchpad.net/%name/trunk/%version/+download/%name-%version.tar.xz

%setup_python_module gnomedvb

%define totem_ver 3.0.0

Requires: gst-plugins-good
Requires: gst-plugins-bad >= 0.10.20
Requires: linuxtv-dvb-apps

BuildRequires: gstreamer-devel >= 0.10.29
BuildRequires: gst-plugins-devel
BuildRequires: libgst-rtsp-devel >= 0.10.7
BuildRequires: libgee-devel >= 0.5
BuildRequires: libsqlite3-devel >= 3.4
BuildRequires: glib2-devel >= 2.32 libgio-devel libgudev-devel
BuildRequires: gst-plugins-bad >= 0.10.9
BuildRequires: libvala-devel >= 0.14
BuildRequires: gst-plugins-good gstreamer-utils
BuildRequires: python-module-pygobject3-devel >= 3.2.1
BuildRequires: intltool

%description
DVB Daemon is a daemon written in Vala to setup your DVB devices,
record TV shows and browse EPG. It can be controlled via its D-Bus interface.

%add_python_lib_path %_libdir/totem/plugins/dvb-daemon

%package -n totem-plugins-dvb
Summary: DVB plugin for Totem
Group: Video
Requires: totem >= %totem_ver
Requires: %name = %version-%release

%description -n totem-plugins-dvb
A plugin for Totem media palyer that allows to watch live TV and
recorded shows.

%prep
%setup -q

subst 's/\$(pythondir)/\$(pyexecdir)/g' client/gnomedvb/Makefile*

%build
%configure %{?_enable_totem:--enable-totem-plugin} \
	--with-totem-plugin-dir=%_libdir/totem/plugins
%make_build

%install
%make DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/dbus-1/services/*.service
%_iconsdir/hicolor/*/*/*
%python_sitelibdir/gnomedvb

%if_enabled totem
%files -n totem-plugins-dvb
%_libdir/totem/plugins/dvb-daemon
%endif

%changelog
* Sun May 20 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.9-alt1
- 0.2.9

* Sat Dec 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.7-alt1
- 0.2.7

* Fri Dec 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.6-alt1
- 0.2.6

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.4-alt1.1
- Rebuild with Python-2.7

* Sat Oct 08 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.4-alt1
- 0.2.4

* Mon Sep 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon May 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Mon Jan 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.23-alt1
- 0.1.23

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.22-alt1
- 0.1.22

* Sun Sep 12 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.21-alt1
- 0.1.21

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.19-alt1
- 0.1.19

* Mon May 24 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.18-alt1
- 0.1.18

* Wed Apr 14 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.17-alt1
- 0.1.17

* Thu Mar 18 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.16-alt1
- 0.1.16

* Sun Mar 07 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.15-alt1
- 0.1.15

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt2
- updated buildreqs

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.14-alt1
- first build for Sisyphus

