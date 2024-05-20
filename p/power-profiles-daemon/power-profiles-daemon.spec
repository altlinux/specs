Name:           power-profiles-daemon
Version:        0.21
Release:        alt1

Summary:        Makes power profiles handling available over D-Bus
Group:          System/Configuration/Hardware
License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon

VCS:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon.git
Source:         %name-%version.tar

BuildRequires(pre):  rpm-macros-systemd
BuildRequires(pre):  rpm-macros-meson
BuildRequires:  meson
BuildRequires:  rpm-build-python3
BuildRequires:  python3(dbusmock)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(umockdev-1.0) gir(UMockdev)
BuildRequires:  pkgconfig(gtk-doc)

%description
%summary.

%package docs
Summary:        Documentation for %name
BuildArch:      noarch
Group:          Documentation

%description docs
This package contains the documentation for %name.

%prep
%setup

%build
%meson -Dgtk_doc=true
%meson_build

%install
%meson_install
mkdir -p %buildroot/%_localstatedir/power-profiles-daemon

%check
%meson_test

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun_with_restart %name.service

%files
%doc README.md
%_bindir/powerprofilesctl
%_libexecdir/%name
%_unitdir/%name.service
%_datadir/dbus-1/*/*PowerProfiles.*
%_datadir/polkit-1/actions/%name.policy
%_localstatedir/%name

%files docs
%dir %_datadir/gtk-doc/
%dir %_datadir/gtk-doc/html/
%_datadir/gtk-doc/html/%name/

%changelog
* Mon May 20 2024 Roman Alifanov <ximper@altlinux.org> 0.21-alt1
- new version 0.21 (with rpmrb script)

* Fri Mar 22 2024 Roman Alifanov <ximper@altlinux.org> 0.20-alt1
- new version 0.20 (with rpmrb script)
- spec cleared

* Sun Apr 30 2023 Roman Alifanov <ximper@altlinux.org> 0.13-alt1
- new version (0.13)

* Fri Nov 18 2022 Roman Alifanov <ximper@altlinux.org> 0.12-alt1
- Initial build for Sisyphus (based on spec for OpenSUSE)
