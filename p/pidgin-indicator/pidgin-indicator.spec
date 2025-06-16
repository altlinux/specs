%define _unpackaged_files_terminate_build 1

Name: pidgin-indicator
Version: 1.0.2
Release: alt1

Summary: This plugins provides an AppIndicator/KStatusNotifierItem for pidgin
License: LGPL-2.0-only GPL-2.0-or-later GPL-3.0-or-later
Group: Networking/Chat
Url: https://github.com/philipl/pidgin-indicator
Vcs: https://github.com/philipl/pidgin-indicator

Source: %name-%version.tar

Requires: pidgin

BuildRequires: intltool
BuildRequires: libayatana-appindicator3-devel
BuildRequires: pkgconfig(pidgin)

%description
This plugins provides an AppIndicator/KStatusNotifierItem for pidgin. All
the current desktop environments are moving away from XEmbed based systray
icons, and that is the only kind of icon that Pidigin provides out of the
box.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f pidgin-indicator.lang
%_libdir/pidgin/indicator.*
%_datadir/icons/hicolor/*/status/%name-nothing.png
%doc AUTHORS NEWS README.md

%changelog
* Tue Jun 10 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.2-alt1
- Initial build.
