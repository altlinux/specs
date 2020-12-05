%define gst_api_ver 1.0
%def_disable audacious
%def_enable gstreamer
%def_enable gtk3

Name: mp3splt-gtk
Version: 0.9.2
Release: alt2

Summary: GTK3 GUI for libmp3splt
License: GPLv2+
Group: Sound
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php

Source: http://prdownloads.sourceforge.net/mp3splt/%name-%version.tar.gz
Patch: %name-0.9.2-fno-common.patch

Requires: gst-plugins-base%gst_api_ver gst-plugins-good%gst_api_ver gst-plugins-ugly%gst_api_ver
BuildRequires: libmp3splt-devel >= 0.9.2 libltdl-devel
%if_enabled gtk3
BuildRequires: libgtk+3-devel
%else
BuildRequires: libgtk+2-devel
%endif
%{?_enable_gstreamer:BuildRequires: gst-plugins%gst_api_ver-devel}
%{?_enable_audacious:BuildRequires: libaudacious-devel libdbus-glib-devel}
BuildRequires: gnome-doc-utils doxygen graphviz

%description
Mp3splt-gtk is a GTK3 GUI that uses libmp3splt.

mp3splt-gtk features :
- integrated player using gstreamer
- support for snackamp and audacious control
- advanced zoom progress bar with amplitude wave and splitpoints

%prep
%setup
%patch -p1 -b .gcc10

%build
%configure %{subst_enable audacious} \
	%{subst_enable gtk3}
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%_pixmapsdir/%{name}*
%_man1dir/%name.1*

%changelog
* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt2
- fixed build with gcc10/-fno-common

* Sat Jul 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- 0.9.2

* Thu Oct 30 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.1b-alt1
- 0.9.1b

* Thu Dec 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- first build for sisyphus

