%define _unpackaged_files_terminate_build 1

Name: waynergy
Version: 0.0.17
Release: alt1

Summary: Synergy client for Wayland compositors
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/r-c-f/waynergy

Source: %name-%version.tar

BuildRequires(pre): meson

BuildRequires: cmake
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libtls)
BuildRequires: /usr/bin/desktop-file-install

Requires: wl-clipboard

%description
An implementation of a synergy client for wayland compositors.
Based on the upstream uSynergy library (heavily modified for
more protocol support and a bit of paranoia).

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

desktop-file-install \
                     --dir=%buildroot%_desktopdir \
                     --add-category=Utility \
                     --add-category=Accessibility \
                     %buildroot%_desktopdir/waynergy.desktop

%files
%doc LICENSE README.md
%_bindir/waynergy
%_bindir/waynergy-clip-update
%_bindir/waynergy-mapper
%_desktopdir/waynergy.desktop

%changelog
* Mon Feb 03 2026 Nikolay Strelkov <snk@altlinux.org> 0.0.17-alt1
- Initial build for Sisyphus
