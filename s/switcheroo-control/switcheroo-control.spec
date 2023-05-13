Name: switcheroo-control
Version: 2.6
Release: alt1

Summary: D-Bus service to check the availability of dual-GPU
License: GPLv3
Group: System/Configuration/Hardware
Url: https://gitlab.freedesktop.org/hadess/switcheroo-control

Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-meson
BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: pkgconfig
BuildRequires: rpm-build-python3
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(udev)

%description
switcheroo-control is a D-Bus service to check the availability of dual-GPU.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch

%description doc
This package contains the documentation for %name.

%prep
%setup

%build
%meson \
   -Dsystemdsystemunitdir=%_unitdir \
   -Dhwdbdir=%_udevhwdbdir \
   -Dgtk_doc=true

%meson_build

%install
%meson_install

%check
%meson_test

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun_with_restart %name.service

%files
%doc COPYING
%doc NEWS README.md
%_bindir/switcherooctl
%_libexecdir/%name
%_mandir/man1/switcherooctl.1*
%_unitdir/%name.service
%_udevhwdbdir/30-pci-intel-gpu.hwdb
%_datadir/dbus-1/system.d/net.hadess.SwitcherooControl.conf

%files doc
%doc %_datadir/gtk-doc/html/%name/

%changelog
* Fri May 12 2023 Roman Alifanov <ximper@altlinux.org> 2.6-alt1
- Initial build for Sisyphus
