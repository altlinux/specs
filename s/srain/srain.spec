%define _unpackaged_files_terminate_build 1

Name: srain
Version: 1.8.0
Release: alt1

Summary: Modern IRC client written in GTK
License: GPL-2.0
Group: Networking/IRC
Url: https://github.com/SrainApp/srain

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libconfig)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: /usr/bin/sphinx-build
BuildRequires: python3-module-sphinxnotes-mock

%description
Srain is a modern IRC client with a GTK+ GUI that is:
* Fully open source
* RFC 1459, 2812 compatible
* Partial IRCv3 support
* Multi-platform support (Linux, Windows, macOS and BSD)

Capabilities of a modern graphical IRC client:
* Convenient connection panel
* Interactive channel search
* Forward message in one click
* URL preview
* Desktop notification
* Special optimization for bridge/relay bot

Power-user capabilities:
* Anything can be done via commands
* Fine-grained configuration with hot update support
* Regex based message render and filter mechanisms

%prep
%setup

%build
%meson \
       -Ddoc_builders=html,man
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE README.rst
%dir %_sysconfdir/srain
%config(noreplace) %_sysconfdir/srain/builtin.cfg
%_bindir/*
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_datadir/doc/%name
%_datadir/doc/%name/*
%_datadir/applications/*.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*.metainfo.xml

%changelog
* Sun Mar 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
