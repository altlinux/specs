%define xdg_name io.github.zefr0x.ianny

Name: ianny
Version: 2.1.1
Release: alt1
License: GPL-3.0

Summary: Break reminder app to prevent strain injuries

Group: Monitoring

Url: https://github.com/zefr0x/ianny
Vcs: https://github.com/zefr0x/ianny.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-meson

BuildRequires: rpm-build-rust
BuildRequires: meson
BuildRequires: /proc

BuildRequires: pkgconfig(dbus-1)

%description
Desktop utility that helps preventing repetitive strain injuries by keeping
track of usage patterns and periodically informing the user to take breaks.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson -Dbuildtype=release
%meson_build

%install
%meson_install
%find_lang %xdg_name

%files -f %xdg_name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_sysconfdir/xdg/autostart/%xdg_name.desktop

%changelog
* Wed Jun 18 2025 Kirill Unitsaev <fiersik@altlinux.org> 2.1.1-alt1
- Initial build
