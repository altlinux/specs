%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name appimage-thumbnailer
%define ver_major 5.0

%def_enable check

%def_disable bootstrap

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: AppImage Thumbnailer
Group: Graphical desktop/GNOME
License: MIT
Url: https://github.com/kem-a/appimage-thumbnailer

Vcs: https://github.com/kem-a/appimage-thumbnailer.git

%if_enabled snapshot
Source: %_name-%version.tar
%else
Source: %url/archive/v%version/%_name-%version.tar.gz
%endif
Source1: %name-%version-cargo.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
An in-process thumbnailer that extracts AppImage icons and writes
ready-to-use PNG thumbnails for desktop environments implementing the
freedesktop.org spec.

%prep
%setup %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install
%makeinstall_std PREFIX=%_prefix
%find_lang --output=%name.lang %_name

%check
%rust_test

%files -f %name.lang
%_bindir/%_name
%_datadir/thumbnailers/%_name.thumbnailer
%doc README*

%changelog
* Tue Nov 24 2026 Yuri N. Sedunov <aris@altlinux.org> 5.0.0-alt1
- 5.0.0 (ported to Rust with in-process SquashFS and DwarFS readers)

* Wed Jul 22 2026 Yuri N. Sedunov <aris@altlinux.org> 4.1.1-alt1
- 4.1.1

* Wed Feb 18 2026 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Tue Jan 06 2026 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Wed Dec 24 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Dec 15 2025 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus


