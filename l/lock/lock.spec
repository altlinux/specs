%define APP_ID com.konstantintutsch.Lock
%def_enable check

Name: lock
Version: 1.0.1
Release: alt1

Summary: Process data with GnuPG
License: MIT
Group: Graphical desktop/GNOME

Url: https://konstantintutsch.com/Lock
Vcs: https://github.com/konstantintutsch/Lock
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 1.3
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(glib-2.0) >= 2.80
BuildRequires: pkgconfig(gio-2.0) >= 2.80
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.42
BuildRequires: pkgconfig(gtk4) >= 4.14
BuildRequires: pkgconfig(libadwaita-1) >= 1.6
BuildRequires: pkgconfig(gpgme) >= 1.23
%if_enabled check
BuildRequires: %_bindir/desktop-file-validate
BuildRequires: %_bindir/appstreamcli
%endif

%description
Lock is a graphical front-end for GnuPG (GPG) making use of a beautiful
LibAdwaita GUI.

Process text and files:

* Encryption
* Decryption
* Signing
* Verification

Manage your GnuPG keyring:

* Generate new keypairs
* Import keys
* Export public keys
* View expiry dates

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
%_datadir/%APP_ID.gresource
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Wed Oct 30 2024 Oleg Shchavelev <oleg@altlinux.org> 1.0.1-alt1
- Initial build
