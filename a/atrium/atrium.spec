Name: atrium
Version: 0.4.0
Release: alt1

Summary: A Wayland display manager for Linux with first-class multiseat support
License: GPL-2.0-or-later
Group: Graphical desktop/Other

URL: https://github.com/kavau/atrium
VCS: https://github.com/kavau/atrium

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

Requires: greetd
Requires: cage

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(pam)

%description
A lightweight display manager, built for Linux multiseat setups. Discovers seats
via logind, shows a greeter on each seat, handles user authentication, and hands
off to an independent user session per seat.

%prep
%setup
%patch0 -p1

%build
%meson -Ddist="altlinux"
%meson_build

%install
%meson_install

%pre
%sysusers_create_package atrium atrium.conf

%files
%_sysconfdir/atrium-greeter.conf
%_sysconfdir/atrium.conf
%_sysconfdir/pam.d/atrium
%_bindir/atrium
%_prefix/lib/atrium-gtk-greeter
%_prefix/lib/atrium-txt-greeter
%_prefix/lib/systemd/system/atrium.service
%_prefix/lib/sysusers.d/atrium.conf
%_prefix/lib/tmpfiles.d/atrium.conf
%_datadir/atrium

%changelog
* Thu Jul 02 2026 Anton Midyukov <antohami@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Sat Jun 13 2026 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1.512f5b5.2
- Add pam config altlinux.
- Add runtime dependencies on greetd and cage.

* Fri Jun 12 2026 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1.512f5b5.1
- Initial build.
