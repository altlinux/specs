%define _unpackaged_files_terminate_build 1

Name: badwolf
Version: 1.4.0
Release: alt1

Summary: minimalist and privacy-oriented WebKitGTK+ browser
License: BSD-3-Clause
Group: Networking/WWW

Url: https://hacktivis.me/projects/badwolf

Source: %name-%version.tar

BuildRequires: ninja-build rpm-macros-ninja-build
BuildRequires: pkgconfig(libxml-2.0) libwebkit2gtk-devel libgtk+3-devel

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
* Thu Oct 15 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
