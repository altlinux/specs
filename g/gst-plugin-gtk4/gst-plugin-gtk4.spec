%def_disable snapshot
%define ver_major 0.15

%def_disable bootstrap
%def_disable check

Name: gst-plugin-gtk4
Version: %ver_major.2
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
%{?_disable_bootstrap:Source1: %name-%version-cargo.tar}

%define gtk_ver 4.19

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo-c
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
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
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
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
* Tue Jun 23 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Fri Mar 20 2026 Yuri N. Sedunov <aris@altlinux.org> 0.15.0-alt1
- 0.15.0

* Mon Dec 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.4-alt1
- 0.14.4

* Wed Nov 05 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.3-alt1
- 0.14.3

* Wed Oct 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Sun Aug 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Jul 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.7-alt1
- 0.13.7

* Fri May 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.6-alt1
- 0.13.6

* Thu Mar 13 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.5-alt1
- 0.13.5

* Tue Jan 07 2025 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4

* Wed Dec 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Thu Sep 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

* Mon Aug 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Wed Jun 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Fri May 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Fri Sep 29 2023 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- first build for Sisyphus


