Name:       mako
Version:    1.8.0
Release:    alt1
Summary:    Lightweight Wayland notification daemon
Group:      Graphical desktop/Other
License:    MIT

URL:        https://github.com/emersion/mako
Source0:    %name-%version.tar

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(basu)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)

Provides: desktop-notification-daemon

Requires: basu
Requires: dbus

%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.

%prep
%setup

%build
%meson -Dwerror=false
%meson_build

%install
%meson_install

%files
%doc LICENSE README.md
%_bindir/mako
%_bindir/makoctl
%_datadir/dbus-1/services/fr.emersion.mako.service
%_man1dir/mako.*
%_man1dir/makoctl.*
%_man5dir/mako.*

%changelog
* Sun Jun 11 2023 Alexey Gladkov <legion@altlinux.ru> 1.8.0-alt1
- New version (1.8).

* Wed Jul 06 2022 Alexey Gladkov <legion@altlinux.ru> 1.7.1-alt1
- New version (1.7.1).

* Wed Jul 06 2022 Alexey Gladkov <legion@altlinux.ru> 1.7-alt1
- New version (1.7).

* Sat Jul 17 2021 Alexey Gladkov <legion@altlinux.ru> 1.6-alt1
- New version (1.6).

* Tue May 04 2021 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- New version (1.5).

* Tue Apr 27 2021 Alexey Gladkov <legion@altlinux.ru> 1.4.1.64.ge5b5d56-alt1
- New snapshot (1.4.1-64-ge5b5d56)
- Rebase to upstream git history.
- Add makoctl.

* Wed Nov 06 2019 Alexey Gladkov <legion@altlinux.ru> 1.4-alt2
- Drop makoctl to avoid logind dependency.

* Wed Aug 07 2019 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Jeff Peeler <jpeeler@redhat.com> - 1.3-1
- Upstream 1.3 release

* Thu Apr 04 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-2
- Fix location of systemd service file

* Sun Mar 17 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-1
- Let there be package
