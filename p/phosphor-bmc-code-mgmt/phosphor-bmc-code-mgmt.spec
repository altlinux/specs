Name: phosphor-bmc-code-mgmt
Version: 1.0.0
Release: alt1.git46f2a39

Summary: Manage the BMC's code versions
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-bmc-code-mgmt
Vcs: https://github.com/openbmc/phosphor-bmc-code-mgmt.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: boost-asio-devel
BuildRequires: boost-context-devel
BuildRequires: boost-coroutine-devel
BuildRequires: boost-devel-headers
BuildRequires: boost-filesystem-devel
BuildRequires: boost-interprocess-devel
BuildRequires: cereal-devel
BuildRequires: cli11-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: libi2c-devel
BuildRequires: libpam0-devel
BuildRequires: libpldm-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: libsdeventplus-devel
BuildRequires: libssl-devel
BuildRequires: libstdplus-devel
BuildRequires: libsystemd-devel
BuildRequires: libudev-devel
BuildRequires: pkg-config
BuildRequires: sdbusplus-tools

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%config(noreplace) %_sysconfdir/synclist
%_bindir/detect-slot-aspeed
%_bindir/obmc-flash-bmc
%_bindir/phosphor-bmc-side-switch
%_bindir/phosphor-download-manager
%_bindir/phosphor-image-updater
%_bindir/phosphor-software-manager
%_bindir/phosphor-sync-software-manager
%_bindir/phosphor-usb-code-update
%_bindir/phosphor-version-software-manager
%_bindir/reset-cs0-aspeed
%_bindir/sync-once.sh
%_tmpfilesdir/software.conf
%_udevrulesdir/70-bmc-usb.rules
%_unitdir/force-reboot.service
%_unitdir/obmc-flash-bmc-alt@.service
%_unitdir/obmc-flash-bmc-prepare-for-sync.service
%_unitdir/obmc-flash-bmc-setenv@.service
%_unitdir/obmc-flash-bmc-static-mount-alt.service
%_unitdir/obmc-flash-host-bios@.service
%_unitdir/phosphor-bmc-side-switch.service
%_unitdir/reboot-guard-disable.service
%_unitdir/reboot-guard-enable.service
%_unitdir/usb-code-update@.service
%_unitdir/usr-local.mount
%_unitdir/xyz.openbmc_project.Software.BMC.Updater.service
%_unitdir/xyz.openbmc_project.Software.Download.service
%_unitdir/xyz.openbmc_project.Software.Manager.service
%_unitdir/xyz.openbmc_project.Software.Sync.service
%_unitdir/xyz.openbmc_project.Software.Version.service

%changelog
* Wed Aug 27 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.git46f2a39
- Initial build for Sisyphus.
