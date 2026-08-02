Name:    lan-mouse
Version: 0.11.0
Release: alt1

Summary: mouse & keyboard sharing via LAN
License: GPL-3.0-only
Group:   Accessibility
URL:     https://github.com/feschber/lan-mouse

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: glib2-devel libcairo-devel libgio-devel libpango-devel
BuildRequires: libgdk-pixbuf-devel libcairo-gobject-devel libgraphene-devel
BuildRequires: libgtk4-devel libXtst-devel libadwaita-devel

ExcludeArch: i586

%description
Lan Mouse is a cross-platform mouse and keyboard sharing software similar to
universal-control on Apple devices. It allows for using multiple PCs via a
single set of mouse and keyboard. This is also known as a Software KVM switch.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

install -Dm0644 de.feschber.LanMouse.desktop \
    %buildroot%_desktopdir/de.feschber.LanMouse.desktop

install -Dm0644 lan-mouse-gtk/resources/de.feschber.LanMouse.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/de.feschber.LanMouse.svg

%files
%doc LICENSE README.md
%_bindir/lan-mouse
%_desktopdir/de.feschber.LanMouse.desktop
%_iconsdir/hicolor/scalable/apps/de.feschber.LanMouse.svg

%changelog
* Sun Aug 02 2026 Sergey Palcheh <minergenon@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus
