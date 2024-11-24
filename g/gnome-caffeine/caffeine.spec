%define APP_ID com.konstantintutsch.Caffeine
%def_enable check

Name: gnome-caffeine
Version: 1.0.5+3
Release: alt1

Summary: Calculate your coffee
License: MIT
Group: Graphical desktop/GNOME

Url: https://konstantintutsch.com/Caffeine
Vcs: https://github.com/konstantintutsch/Caffeine
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 1.3
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) >= 1.4
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
%endif

%description
Caffeine is a utility for coffee enthusiasts. It's sole purpose is to calculate
the extraction ratio of a coffee.

For example, an espresso brewed from 10g of coffee ground weighing 18g would
have an extraction ratio of 1 : 1.8.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%check
%meson_test

%files -f %APP_ID.lang
%_bindir/%APP_ID
%_desktopdir/%APP_ID.desktop
%_datadir/com.konstantintutsch.Caffeine.gresource
%_iconsdir//hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Sun Nov 24 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.5+3-alt1
- Initial build
