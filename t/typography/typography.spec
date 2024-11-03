%define APP_ID org.gnome.design.Typography
%def_enable check

Name: typography
Version: 0.3.0
Release: alt1.1

Summary: Look up text styles
License: GPL-3.0-only
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/World/design/typography
Vcs: https://gitlab.gnome.org/World/design/typography
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.59.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.5
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

%description
Tool for working with the GNOME typography design guidelines.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%__meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/dbus-1/services/%APP_ID.service
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Thu Oct 31 2024 Oleg Shchavelev <oleg@altlinux.org> 0.3.0-alt1.1
- Rebuild improved spec (ALT #51799)
- Replaced license GPL-3.0-or-later with GPL-3.0-only
- Drop require cmake dependency in BuildRequires
- Add version require libadwaita in BuildRequires
- Turn keys URL and VCS order

* Mon Oct 14 2024 Oleg Shchavelev <oleg@altlinux.org> 0.3.0-alt1
- Initial build
