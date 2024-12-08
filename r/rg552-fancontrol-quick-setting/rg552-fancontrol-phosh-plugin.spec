Name: rg552-fancontrol-quick-setting
Version: 0.1.1
Release: alt1

Summary: Change the fan mode on the RG552
License: GPL-3.0-or-later
Group: Other

Url: https://github.com/Maks1mS/rg552-fancontrol-phosh-plugin
Vcs: https://github.com/Maks1mS/rg552-fancontrol-phosh-plugin
Source: %name-%version.tar

Requires: rg552-hw-control

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libnm)
BuildRequires: pkgconfig(phosh-plugins)
BuildRequires: pkgconfig(libphosh-0.43)

ExclusiveArch: aarch64

%description
Change the fan mode on the RG552.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_libdir/phosh/plugins/libphosh-plugin-%name.so
%_libdir/phosh/plugins/%name.plugin

%changelog
* Fri Dec 06 2024 Oleg Shchavelev <oleg@altlinux.org> 0.1.1-alt1
- Initial build
