%define APP_ID com.github.cassidyjames.clairvoyant
%def_enable check

Name: clairvoyant
Version: 3.1.8
Release: alt1

Summary: Ask questions, get psychic answers
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://cassidyjames.com/apps
Vcs: https://github.com/cassidyjames/clairvoyant
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 1.5.1
BuildRequires: vala
BuildRequires: pkgconfig(glib-2.0) >= 2.82.0
BuildRequires: pkgconfig(gtk4) >= 4.16.1
BuildRequires: pkgconfig(libadwaita-1) >= 1.6.0
BuildRequires: pkgconfig(libportal) >= 0.8.1
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

%description
Does he love you? Should you have pizza for dinner? Is there such thing as a
stupid question? Discover the answers to these questions and more with
Clairvoyant, the magic 8-ball inspired fortune teller.

* Ask a question, then open Clairvoyant for an answer.
* Not satisfied? Ask again, then hit "Ask Again" to try again.
* Do what you'd like with the answers-just don't shoot the messenger!

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
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Tue Nov 05 2024 Oleg Shchavelev <oleg@altlinux.org> 3.1.8-alt1
- Initial build
