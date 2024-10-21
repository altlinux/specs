%define APP_ID io.github.vmkspv.netsleuth
%def_enable check

Name: netsleuth
Version: 1.0.4
Release: alt1
BuildArch: noarch

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
BuildRequires: cmake
BuildRequires: rpm-build-python3
BuildRequires: rpm-build-gir
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

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
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/%name

%changelog
* Mon Oct 21 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.4-alt1
- New version 1.0.4

* Fri Oct 11 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.3-alt1
- Initial build
