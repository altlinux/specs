Name: satty
Version: 0.20.0
Release: alt1
License: MPL-2.0

Summary: Satty - Modern Screenshot Annotation

Group: Graphical desktop/Other

Url: https://github.com/gabm/Satty
Vcs: https://github.com/gabm/Satty.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(epoxy)

BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)

%description
Satty is a screenshot annotation tool inspired by Swappy and Flameshot.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install
install -D satty.desktop %buildroot%_desktopdir/satty.desktop
install -D assets/satty.svg %buildroot%_iconsdir/hicolor/scalable/apps/satty.svg

%files
%_bindir/%name
%_desktopdir/satty.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Thu Oct 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.20.0-alt1
- new version 0.20.0 (with rpmrb script)

* Wed Jun 18 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.19.0-alt1
- Initial build
