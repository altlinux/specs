%define _unpackaged_files_terminate_build 1

Name:    phosphor-logging
Version: 1.0.0
Release: alt2.git383e9c1.1

Summary: Libraries for common event and logging creation.
License: Apache-2.0
Group:   System/Libraries
Url:     https://github.com/openbmc/phosphor-logging

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: libsdbusplus-devel
BuildRequires: libsdeventplus-devel
BuildRequires: sdbusplus-tools
BuildRequires: cereal-devel
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: phosphor-dbus-interfaces-data
BuildRequires: cli11-devel
BuildRequires: libdbus-devel
BuildRequires: stdexec-devel

%description
The phosphor logging provides mechanisms for event and journal logging.

%package -n lib%name
Summary: Libraries for %name
Group:   System/Libraries

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: Development files for %name
Group:   Development/C++

%description -n lib%name-devel
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%preun
%preun_service xyz.openbmc_project.Logging
%preun_service xyz.openbmc_project.Syslog.Config

%post
%post_service xyz.openbmc_project.Logging
%post_service xyz.openbmc_project.Syslog.Config

%files
%doc *.md
%_bindir/*
%_unitdir/*.service
%_datadir/dbus-1/system-services/*.service
%_datadir/dbus-1/system.d/*.conf

%files -n lib%name
%_libdir/libphosphor_logging.so.*

%files -n lib%name-devel
%_includedir/%name
%_includedir/xyz/openbmc_project/Logging
%_libdir/libphosphor_logging.so
%_libdir/pkgconfig/%name.pc

%changelog
* Wed Jun 24 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt2.git383e9c1.1
- New snapshot.
- Enable tests.

* Mon Aug 11 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.gitfc14867
- Initial build for Sisyphus.
