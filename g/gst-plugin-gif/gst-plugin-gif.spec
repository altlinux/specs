%def_disable snapshot
%define ver_major 0.12

%def_disable bootstrap
%def_disable check

Name: gst-plugin-gif
Version: %ver_major.0
Release: alt1

Summary: GStreamer GIF encoder plugin
License: MIT or Apache-2.0
Group: System/Libraries
Url: https://crates.io/crates/gst-plugin-gif

%if_disabled snapshot
Source: https://static.crates.io/crates/%name/%name-%version.crate
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo-c
BuildRequires: pkgconfig(gstreamer-video-1.0)

%description
This package provides %{summary}.

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
%_libdir/gstreamer-1.0/libgstgif.so
%exclude %_pkgconfigdir/gstgif.pc
#%doc README*

%changelog
* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- first build for Sisyphus


