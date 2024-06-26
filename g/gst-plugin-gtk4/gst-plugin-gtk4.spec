%def_disable snapshot
%define ver_major 0.12

%def_disable bootstrap
%def_disable check

Name: gst-plugin-gtk4
Version: %ver_major.7
Release: alt1

Summary: GStreamer GTK4 Sink element and Paintable widget
License: MPL-2.0
Group: System/Libraries
Url: https://crates.io/crates/gst-plugin-gtk4

%if_disabled snapshot
Source: https://static.crates.io/crates/%name/%name-%version.crate
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo-c
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gstreamer-video-1.0)

%description
This GStreamer plugin provides `gtk::Video` & `gtk::Picture` for
rendering media such as videos. As the default `gtk::Video` widget
doesn't offer the possibility to use a custom `gst::Pipeline`. The
plugin provides a `gst_video::VideoSink` along with a `gdk::Paintable`
that's capable of rendering the sink's frames.

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%define opts --offline --prefix=%_prefix --libdir=%_libdir --all-features --frozen --library-type=cdylib

cargo cbuild %opts

%install
cargo cinstall %opts --destdir=%buildroot

%check
%rust_test

%files
%_libdir/gstreamer-1.0/libgstgtk4.so
%exclude %_pkgconfigdir/gstgtk4.pc
%doc README*

%changelog
* Wed Jun 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Fri May 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- first build for Sisyphus


