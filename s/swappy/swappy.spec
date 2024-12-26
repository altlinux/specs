Name: swappy
Version: 1.5.1
Release: alt1
License: MIT

Summary: A Wayland native snapshot editing tool, inspired by Snappy on macOS

Group: Graphical desktop/Other

Url: https://github.com/jtheoof/swappy
Vcs: https://github.com/jtheoof/swappy.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gtk+-3.0)

BuildRequires: scdoc

%description
A Wayland native snapshot and editor tool, inspired by Snappy on macOS.
Works great with grim, slurp and sway. But can easily work with other
screen copy tools that can output a final image to stdout.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/*.1.*

%changelog
* Thu Dec 26 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.5.1-alt1
- Initial build
