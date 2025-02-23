%define APP_ID org.gnome.gitlab.cheywood.Pulp
%def_enable check

Name: pulp
Version: 0.1.15
Release: alt1

Summary: Skim excessive feeds
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/cheywood/Pulp
Vcs: https://gitlab.gnome.org/cheywood/Pulp
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Note: Today Pulp is in preview as a client for FreshRSS and Nextcloud News.
Direct RSS access is planned for the future.

Pulp provides a workflow focused on reading through an excessive number of RSS
feeds with the goal of regularly marking all read, resting in a state akin
to an empty inbox.

Contributing to quickly parsing excessive articles:

* A large "mash roughly here" button to mark list read and continue
* Marking read while scrolling
* Ensuring full article titles and longer excerpts are visible in the article
  list
* Minimising everything else, in both UI clutter and functionality

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/feed_parsing
%python3_sitelibdir_noarch/backends
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/%name

%changelog
* Sat Feb 22 2025 Oleg Shchavelev <oleg@altlinux.org> 0.1.15-alt1
- Initial build
