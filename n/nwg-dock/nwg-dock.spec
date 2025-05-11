%define _unpackaged_files_terminate_build 1

%global import_path github.com/nwg-piotr/nwg-dock

Name: nwg-dock
Version: 0.4.3
Release: alt1

Summary: GTK3-based dock for sway
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-dock

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

BuildRequires: pkgconfig(gtk-layer-shell-0)

%description
Fully configurable (w/ command line arguments and css) dock, written in
Go, aimed exclusively at sway Wayland compositor. It features pinned
buttons, task buttons, the workspace switcher and the launcher button.
The latter by default starts nwg-drawer or nwggrid (application grid) -
if found. In the picture(s) below the dock has been shown together with
nwg-panel.

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
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus
