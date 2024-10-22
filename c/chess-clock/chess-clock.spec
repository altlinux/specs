%define APP_ID eu.fortysixandtwo.chessclock
%def_enable check

Name: chess-clock
Version: 0.6.1
Release: alt1

Summary: Time games of over-the-board chess
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/yakushabb/chess-clock
Vcs: https://gitlab.gnome.org/yakushabb/chess-clock
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson rpm-macros-python3
BuildRequires: rpm-build-gir
BuildRequires: rpm-build-python3
BuildRequires: meson >= 0.59.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.4
BuildRequires: libgsound-devel
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
BuildRequires: %_bindir/glib-compile-schemas
%endif

BuildArch: noarch

%description
Chess Clock is a simple application to provide time control for over-the-board
chess games. Intended for mobile use, players select the time control settings
desired for their game, then the black player taps their clock to start white's
timer. After each player's turn, they tap the clock to start their opponent's,
until the game is finished or one of the clocks reaches zero.

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
%_datadir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_datadir/appdata/%APP_ID.metainfo.xml

%changelog
* Mon Oct 21 2024 Oleg Shchavelev <oleg@altlinux.org> 0.6.1-alt1
- Initial build
