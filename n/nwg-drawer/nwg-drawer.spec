%define _unpackaged_files_terminate_build 1

%global import_path github.com/nwg-piotr/nwg-drawer

%global __find_debuginfo_files %nil

Name: nwg-drawer
Version: 0.7.5
Release: alt1

Summary: Application drawer for wlroots-based Wayland compositors
License: AGPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-drawer

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)

%description
Nwg-drawer is an application launcher. It's being developed with sway
and Hyprland in mind, but should also work with other wlroots-based
Wayland compositors.

The nwg-drawer command displays the application grid. The search entry
allows to look for installed applications, and for files in XDG user
directories. The grid view may also be filtered by categories.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name
make install DESTDIR=%buildroot

%files
%doc LICENSE README.md
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.7.5-alt1
- New version 0.7.5.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.4-alt1
- New version 0.7.4.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.3-alt1
- New version 0.7.3.

* Sat Jun 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.1-alt1
- New version 0.7.1.

* Wed May 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.7.0-alt1
- New version 0.7.0.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.6.5-alt1
- Initial build for Sisyphus
