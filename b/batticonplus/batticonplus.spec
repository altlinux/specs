%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: batticonplus
Version: 2.0.1
Release: alt1

Summary: Lightweight battery status icon for the system tray and notifier (based on cbatticon)
License: GPL-2.0-only
Group: Graphical desktop/Other
Url: https://github.com/artist4xlibre/batticonplus

Source: %name-%version.tar

BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)

%description
%summary.

%prep
%setup
sed -i "s|Categories=.*|Categories=GTK;System;Monitor;|" batticonplus.desktop

%build
export CFLAGS="%optflags"
%make_build \
            WITH_NOTIFY=1 \
            WITH_GTK3=1 \
            WITH_APPINDICATOR=1

%install
%makeinstall_std

%find_lang %name

%files -f %{name}.lang
%doc Changelog COPYING README.md
%_bindir/batticonplus
%_desktopdir/batticonplus.desktop
%exclude %_datadir/doc/batticonplus-2.0/Changelog
%exclude %_datadir/doc/batticonplus-2.0/README.md
%_iconsdir/hicolor/scalable/apps/batticonplus.svg
%exclude %_datadir/licenses/batticonplus-2.0/COPYING
%_man1dir/batticonplus.1.*

%changelog
* Sun Feb 08 2026 Nikolay Strelkov <snk@altlinux.org> 2.0.1-alt1
- Initial build for Sisyphus
