%define _unpackaged_files_terminate_build 1

Name: badwolf
Version: 1.4.0
Release: alt2

Summary: minimalist and privacy-oriented WebKitGTK+ browser
License: BSD-3-Clause AND CC-BY-SA-4.0 AND MPL-2.0
Group: Networking/WWW

Url: https://hacktivis.me/projects/badwolf

Source: %name-%version.tar

BuildRequires: ninja-build rpm-macros-ninja-build
BuildRequires: pkgconfig(libxml-2.0) libwebkit2gtk4.1-devel libgtk+3-devel

%description
%summary.

%prep
%setup

%build
./configure \
    PREFIX=%_prefix \
    CFLAGS="%optflags"

%ninja_build

%install
%ninja_install

%find_lang --with-man --output=%name.lang %name

%files -f %name.lang
%doc README.md
%_bindir/badwolf
%_man1dir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*

%changelog
* Mon Oct 19 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.0-alt2
- Fix specified license
- Update BR to libwebkit2gtk.

* Thu Oct 15 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
