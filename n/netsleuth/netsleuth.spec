%define APP_ID io.github.vmkspv.netsleuth
%def_enable check

Name: netsleuth
Version: 1.1.0
Release: alt1

Summary: Calculate IP subnets
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/vmkspv/netsleuth
Vcs: https://github.com/vmkspv/netsleuth
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rpm-build-python3
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

BuildArch: noarch

%description
A simple utility for the calculation and analysis of IP subnet values, designed
to simplify network configuration tasks.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_bindir/netsleuth_search_provider
%_desktopdir/%APP_ID.desktop
%_desktopdir/%APP_ID.SearchProvider.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/dbus-1/services/%APP_ID.SearchProvider.service
%_datadir/gnome-shell/search-providers/%APP_ID.search-provider.ini
%_datadir/%name

%changelog
* Sun Jan 12 2025 Oleg Shchavelev <oleg@altlinux.org> 1.1.0-alt1
- New version 1.1.0 (ALT #52672)
- Update build dependencies for check

* Fri Nov 15 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.5-alt1
- New version 1.0.5

* Tue Nov 12 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.4-alt2
- Rebuild improved spec (ALT #51818)
- Add macro %%meson_build
- Update BuildRequires

* Mon Oct 21 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.4-alt1
- New version 1.0.4

* Fri Oct 11 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.3-alt1
- Initial build
