%def_enable snapshot

%define _name GstPipelineStudio
%define ver_major 0.3
%define rdn_name org.freedesktop.dabrain34.%_name

%def_disable bootstrap

Name: gst-pipeline-studio
Version: %ver_major.5
Release: alt1

Summary: Draw your own GStreamer pipeline
License: GPL-3.0
Group: Video
Url: https://gitlab.freedesktop.org/dabrain34/GstPipelineStudio

%if_disabled snapshot
Source: %url/-/archive/%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.freedesktop.org/dabrain34/GstPipelineStudio.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%define glib_ver 2.66
%define gtk_ver 4.0
%define gst_ver 1.20

Requires: gstreamer1.0-utils gst-devtools
Requires: gst-plugins-base1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
GstPipelineStudio aims to provide a graphical user interface to the
GStreamer framework. From a first step in the framework with a simple
pipeline to a complex pipeline debugging, the tool provides a friendly
interface to add elements to a pipeline and debug it.

%prep
%setup -n %{?_enable_snapshot:%name}%{?_disable_snapshot:%_name}-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.appdata.xml
%doc README*

%changelog
* Fri Jan 12 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.5-alt1
- first build for Sisyphus (0.3.5-1-g7a70fee)


