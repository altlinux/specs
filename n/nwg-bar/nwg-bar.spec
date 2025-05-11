%define _unpackaged_files_terminate_build 1

%global import_path github.com/nwg-piotr/nwg-bar

Name: nwg-bar
Version: 0.1.6
Release: alt1

Summary: GTK3-based button bar for wlroots-based compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-bar

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

BuildRequires: pkgconfig(gtk-layer-shell-0)

%description
nwg-bar is a Golang replacement to the nwgbar command (a part of
nwg-launchers), with some improvements. Originally aimed at sway,
works with wlroots-based compositors only.

The nwg-bar command creates a button bar on the basis of a JSON template
placed in the ~/.config/nwg-bar/ folder. By default the command displays
a horizontal bar in the center of the screen. Use command line arguments
to change the placement.

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
* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.6-alt1
- Initial build for Sisyphus
