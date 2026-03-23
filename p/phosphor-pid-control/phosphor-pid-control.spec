%set_verify_elf_method unresolved=relaxed

Name: phosphor-pid-control
Version: 1.0.0
Release: alt2.git3bfece8.1

Summary: OpenBMC PID-based Thermal Control Daemon
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-pid-control
Vcs: https://github.com/openbmc/phosphor-pid-control.git

Source: %name-%version.tar

Patch: Change_defualt_for_handle-missing-object-paths_option.patch
Patch1: Fix_build_with_our_old_sdbusplus.patch
Patch2: Print_fail_reason_why_zone_enters_failsafe_mode.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: cli11-devel
BuildRequires: cmake
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: phosphor-host-ipmid-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsystemd-devel
BuildRequires: nlohmann-json-devel
BuildRequires: pkg-config

%description
This is a daemon running within the OpenBMC environment. It uses a
well-defined configuration file to control the temperature of the tray
components to keep them within operating conditions. It may require
coordination with host-side tooling and OpenBMC.

%package tools
Summary: Tools for %name
Group: Other
Requires: libmanualcmds = %EVR

%description tools
%summary.

%package -n libmanualcmds
Summary: Library from %name
Group: System/Libraries

%description -n libmanualcmds
%summary.

%package -n libmanualcmds-devel
Summary: Development files for library from %name
Group: Development/C++
Requires: libmanualcmds = %EVR

%description -n libmanualcmds-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%files tools
%_bindir/setsensor
%_bindir/swampd
%_unitdir/%name.service

%files -n libmanualcmds
%_libdir/ipmid-providers/libmanualcmds.so.*

%files -n libmanualcmds-devel
%_libdir/ipmid-providers/libmanualcmds.so

%changelog
* Tue Mar 10 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt2.git3bfece8.1
- Update to the 3bfece8 upstream stage.
- Change defualt for handle-missing-object-paths option.
- Fix build with our old sdbusplus.
- Print fail reason why zone enters failsafe mode.

* Wed Aug 27 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.git951aff4
- Initial build for Sisyphus.
