Name:           power-profiles-daemon
Version:        0.12
Release:        alt1

Summary:        Makes power profiles handling available over D-Bus
Group: System/Configuration/Hardware
License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/power-profiles-daemon

Source:        %name-%version.tar

BuildRequires:  meson
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  systemd
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  python3(dbusmock)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires(pre):  rpm-macros-systemd
BuildRequires(pre):  rpm-macros-meson
BuildRequires:   rpm-build-python3

%description
%summary

%package docs
Summary:        Documentation for %name
BuildArch:      noarch
Group: Documentation

%description docs
This package contains the documentation for %name

%prep
%setup -q

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
%_datadir/dbus-1/system.d/net.hadess.PowerProfiles.conf
%_datadir/dbus-1/system-services/net.hadess.PowerProfiles.service
%_datadir/polkit-1/actions/net.hadess.PowerProfiles.policy
%_localstatedir/power-profiles-daemon

%files docs
%dir %_datadir/gtk-doc/
%dir %_datadir/gtk-doc/html/
%_datadir/gtk-doc/html/%name/

%changelog
* Fri Nov 18 2022 Roman Alifanov <ximper@altlinux.org> 0.12-alt1
- Initial build for Sisyphus (based on spec for OpenSUSE)
