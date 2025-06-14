%define _unpackaged_files_terminate_build 1

%global import_path github.com/nwg-piotr/nwg-menu

Name: nwg-menu
Version: 0.1.9
Release: alt1

Summary: MenuStart plugin to nwg-panel, also capable of working standalone
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/nwg-piotr/nwg-menu

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

BuildRequires: pkgconfig(gtk-layer-shell-0)

%description
The nwg-menu command displays the system menu with simplified freedesktop
main categories (8 instead of 13). It also provides the search entry, to
look for installed application on the basis of .desktop files, and for
files in XDG user directories.

You may pin applications by right-clicking them. Pinned items will appear
above the categories list. Right-click a pinned item to unpin it. The
pinned items cache is shared with the nwggrid command, which is a part
of nwg-launchers.

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
* Sat Jun 14 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.9-alt1
- New version 0.1.9.

* Sun May 11 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus
