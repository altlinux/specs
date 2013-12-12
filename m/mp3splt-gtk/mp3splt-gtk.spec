%define gst_api_ver 0.10
%def_disable audacious
%def_enable gstreamer
# not ready for 3.10
%def_disable gtk3

Name: mp3splt-gtk
Version: 0.9
Release: alt1

Summary: GTK3 GUI for libmp3splt
License: GPLv2+
Group: Sound
Url: http://mp3splt.sourceforge.net/mp3splt_page/home.php
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar.gz

Requires: gst-plugins-base gst-plugins-good gst-plugins-ugly
BuildRequires: libmp3splt-devel >= 0.9 libltdl-devel
%if_enabled gtk3
BuildRequires: libgtk+3-devel
%else
BuildRequires: libgtk+2-devel
%endif
%{?_enable_gstreamer:BuildRequires:  gst-plugins-devel}
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
* Thu Dec 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9-alt1
- first build for sisyphus

