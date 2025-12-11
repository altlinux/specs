%global _unpackaged_files_terminate_build 1

Name: gnvim
Version: 0.3.1
Release: alt1
License: MIT
Summary: GNvim - GTK4 Neovim GUI
Group: Editors
Url: https://github.com/vhakulinen/gnvim
Vcs: https://github.com/vhakulinen/gnvim.git
Source: %name-%version.tar
#Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(gtk4) >= 4.10
BuildRequires: pkgconfig(glib-2.0) >= 2.56 pkgconfig(gobject-2.0) >= 2.56 pkgconfig(gio-2.0) >= 2.56
BuildRequires: pkgconfig(graphene-gobject-1.0) >= 1.10
BuildRequires: pkgconfig(libadwaita-1) >= 1.5

Requires: %name-runtime = %EVR

%description
Gnvim, opinionated Neovim GUI.

%package runtime
Summary: Runtime files for Gnvim
Group: Editors
Requires: neovim

%description runtime
Runtime files for Gnvim.

%prep
%setup
#%%patch -p1
%rust_prep
sed -e 's|/usr/local/share/gnvim/runtime|%_datadir/%name/runtime|' \
    -i ui/src/app.rs

%build
%make_build PROFILE=release PREFIX=%_prefix

%install
%makeinstall_std PROFILE=release PREFIX=%_prefix
rm -f %buildroot%_datadir/glib-2.0/schemas/gschemas.compiled

%files
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/glib-2.0/schemas/*

%files runtime
%doc %_datadir/%name/runtime/doc
%_datadir/%name/runtime/lua/%name

%changelog
* Wed Dec 10 2025 Alexey Shabalin <shaba@altlinux.org> 0.3.1-alt1
- Initial build.

