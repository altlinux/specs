Name:    phosphor-time-manager
Version: 0.1
Release: alt0.1.g719e2234

Summary: Local time policy and emulated host RTC manager
License: Apache-2.0
Group:   System/Libraries
Url:     https://www.openbmc.org
Vcs:     https://github.com/openbmc/phosphor-time-manager.git

Source: %name-%version.tar
Patch0: %name-%version-alt-fix-meson.patch
Patch1: %name-%version-alt-cast-system_clock-duration-max.patch

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(sdbusplus)
BuildRequires: pkgconfig(phosphor-dbus-interfaces)
BuildRequires: pkgconfig(phosphor-logging)

%description
phosphor-time-manager is the time manager service that implements
D-Bus interface xyz/openbmc_project/Time/EpochTime.interface.yaml.
The user can get or set the BMC's time via this interface.

%prep
%setup
%patch0
%ifarch %ix86
%patch1
%endif

%build
%meson -Dtests=disabled -Ddefault_time_mode=Mode::NTP
%meson_build

%install
%meson_install

%files
%doc *.md
%_bindir/%name
%_unitdir/xyz.openbmc_project.Time.Manager.service

%changelog
* Wed Aug 13 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.1-alt0.1.g719e2234
- Initial build for Sisyphus.
