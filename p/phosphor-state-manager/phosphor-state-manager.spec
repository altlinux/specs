# Replace the hash of the archive containing the source code or patches from
# Meson WrapDB packages with the hash of our archives generated in hasher.
# This is necessary for dependency vendoring.
# For more details, see:
# https://mesonbuild.com/Wrapdb-projects.html
# https://mesonbuild.com/Wrap-dependency-system-manual.html
#
# 1-st param is the name of the wrap dependency being vendored. Without
# subdirectories and file extensions.
# 2-nd param is the type of hash to replace. Either "source_hash" or
# "patch_hash".
# 3-rd param is name of the archive that is generated in the hasher for
# vendoring.
%define replace_meson_wrapdb_hash() \
	(grep %2 subprojects/%1.wrap | cut -d' ' -f3 && sha256sum %3) | xargs -n2 sh -c 'sed -i "s|$0|$1|g" subprojects/%1.wrap'

Name: phosphor-state-manager
Version: 0.1
Release: alt1.git39e0cbe

Summary: Tracking and controlling the state of different objects
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-state-manager
Vcs: https://github.com/openbmc/phosphor-state-manager.git

Source0: %name-%version.tar
#
# We do use dependency vendoring here.
#
# See subprojects/libgpiod.wrap file, line "source_url"
# https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-1.6.3.tar.gz
Source1: libgpiod-1.6.3.tar.gz
# See subprojects/libgpiod.wrap file, line "patch_url"
# https://wrapdb.mesonbuild.com/v2/libgpiod_1.6.3-1/get_patch
Source2: libgpiod_1.6.3-1_patch.zip

Patch: fix-phosphor-state-manager-ALT-libgpiod-1.6.3-linker.patch

BuildRequires(Pre): rpm-macros-meson

BuildRequires: cereal-devel
BuildRequires: cli11-devel
BuildRequires: gcc-c++
BuildRequires: libgpioplus-devel
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsdeventplus-devel
BuildRequires: meson
BuildRequires: nlohmann-json-devel

ExcludeArch: %ix86

%filter_from_requires /chassiskill/d
%filter_from_requires /host-reboot/d

%description
Software responsible for tracking and controlling the state of different
objects within OpenBMC. This currently includes the BMC, Chassis, Host,
and Hypervisor. The most critical feature of phosphor-state-manager (PSM)
software is its support for requests to power on and off the system by
the user.

This software also enforces any restore policy (i.e. auto power on system
after a system power event or bmc reset) and ensures its states are updated
correctly in situations where the BMC is rebooted and the chassis or host
are in on/running states.

%prep
%setup
%autopatch

# Meson downloads source code from the internet and places it in a directory
# subprojects/packagecache.
# See https://mesonbuild.com/Wrap-dependency-system-manual.html
mkdir -p subprojects/packagecache

# Since the hash of our sources is different from what meson expects, we need
# to correct them.
%{replace_meson_wrapdb_hash libgpiod source_hash %SOURCE1}

# Since we didn't have internet access during the build, we downloaded the
# necessary files ahead of time. Now we'll place them where meson expects them.
install -Dpm 0644 %SOURCE1 subprojects/packagecache

# We do the same for the archives with patches for wrapdb.
# See https://mesonbuild.com/Wrapdb-projects.html
%{replace_meson_wrapdb_hash libgpiod patch_hash %SOURCE2}

install -Dpm 0644 %SOURCE2 subprojects/packagecache

%build
%meson
%meson_build

%install
# We don't want to install vendored libgpio in the system.
%__meson_install --skip-subprojects libgpiod

%files
%_sysconfdir/phosphor-systemd-target-monitor
%_bindir/obmcutil
%_bindir/phosphor-bmc-state-manager
%_bindir/phosphor-chassis-check-power-status
%_bindir/phosphor-chassis-state-manager
%_bindir/phosphor-discover-system-state
%_bindir/phosphor-host-condition-gpio
%_bindir/phosphor-host-reset-recovery
%_bindir/phosphor-host-state-manager
%_bindir/phosphor-hypervisor-state-manager
%_bindir/phosphor-scheduled-host-transition
%_bindir/phosphor-secure-boot-check
%_bindir/phosphor-systemd-target-monitor
%_libexecdir/%name
%_unitdir/obmc-bmc-service-quiesce@.target
%_unitdir/obmc-chassis-blackout@.target
%_unitdir/obmc-chassis-hard-poweroff@.target
%_unitdir/obmc-chassis-powercycle@.target
%_unitdir/obmc-chassis-powered-off@.target
%_unitdir/obmc-chassis-poweroff@.target
%_unitdir/obmc-chassis-poweron@.target
%_unitdir/obmc-chassis-powerreset@.target
%_unitdir/obmc-fan-control-ready@.target
%_unitdir/obmc-fan-control.target
%_unitdir/obmc-fan-watchdog-takeover.target
%_unitdir/obmc-fans-ready.target
%_unitdir/obmc-host-crash@.target
%_unitdir/obmc-host-diagnostic-mode@.target
%_unitdir/obmc-host-force-warm-reboot@.target
%_unitdir/obmc-host-graceful-quiesce@.target
%_unitdir/obmc-host-quiesce@.target
%_unitdir/obmc-host-reboot@.target
%_unitdir/obmc-host-reset-running@.target
%_unitdir/obmc-host-reset@.target
%_unitdir/obmc-host-shutdown@.target
%_unitdir/obmc-host-start-pre@.target
%_unitdir/obmc-host-start@.target
%_unitdir/obmc-host-started@.target
%_unitdir/obmc-host-starting@.target
%_unitdir/obmc-host-startmin@.target
%_unitdir/obmc-host-stop-pre@.target
%_unitdir/obmc-host-stop@.target
%_unitdir/obmc-host-stopped@.target
%_unitdir/obmc-host-stopping@.target
%_unitdir/obmc-host-timeout@.target
%_unitdir/obmc-host-warm-reboot@.target
%_unitdir/obmc-power-off@.target
%_unitdir/obmc-power-on@.target
%_unitdir/obmc-power-reset-on@.target
%_unitdir/obmc-power-start-pre@.target
%_unitdir/obmc-power-start@.service
%_unitdir/obmc-power-start@.target
%_unitdir/obmc-power-stop-pre@.target
%_unitdir/obmc-power-stop@.service
%_unitdir/obmc-power-stop@.target
%_unitdir/obmc-powered-off@.service
%_unitdir/phosphor-bmc-security-check.service
%_unitdir/phosphor-chassis-check-power-status@.service
%_unitdir/phosphor-clear-one-time@.service
%_unitdir/phosphor-create-chassis-poweron-log@.service
%_unitdir/phosphor-discover-system-state@.service
%_unitdir/phosphor-host-condition-gpio@.service
%_unitdir/phosphor-reboot-host@.service
%_unitdir/phosphor-reset-chassis-on@.service
%_unitdir/phosphor-reset-chassis-running@.service
%_unitdir/phosphor-reset-host-reboot-attempts@.service
%_unitdir/phosphor-reset-host-recovery@.service
%_unitdir/phosphor-reset-host-running@.service
%_unitdir/phosphor-reset-sensor-states@.service
%_unitdir/phosphor-set-chassis-transition-to-off@.service
%_unitdir/phosphor-set-chassis-transition-to-on@.service
%_unitdir/phosphor-set-host-transition-to-off@.service
%_unitdir/phosphor-set-host-transition-to-running@.service
%_unitdir/phosphor-systemd-target-monitor.service
%_unitdir/xyz.openbmc_project.State.BMC.service
%_unitdir/xyz.openbmc_project.State.Chassis@.service
%_unitdir/xyz.openbmc_project.State.Host@.service
%_unitdir/xyz.openbmc_project.State.Hypervisor.service
%_unitdir/xyz.openbmc_project.State.ScheduledHostTransition@.service

%changelog
* Wed Dec 10 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git39e0cbe
- Initial build for Sisyphus.
