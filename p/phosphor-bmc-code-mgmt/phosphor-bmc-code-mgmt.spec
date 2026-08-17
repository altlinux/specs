# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

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

# Since we didn't have internet access during the build, we downloaded the
# necessary files ahead of time. Now we'll place them where meson expects them.
#
# 1-st param is name of the archive that is generated in the hasher for
# vendoring.
%define install_meson_subproject() \
    install -Dpm 0644 %1 subprojects/packagecache

Name: phosphor-bmc-code-mgmt
Version: 1.0.0
Release: alt2.git14a40be.1

Summary: Manage the BMC's code versions
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/phosphor-bmc-code-mgmt
Vcs: https://github.com/openbmc/phosphor-bmc-code-mgmt.git

Source: %name-%version.tar
# See subprojects/libgpiod.wrap file, line "source_url"
# https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-1.6.3.tar.gz
Source1: libgpiod-1.6.3.tar.gz
# See subprojects/libgpiod.wrap file, line "patch_url"
# https://wrapdb.mesonbuild.com/v2/libgpiod_1.6.3-1/get_patch
Source2: libgpiod_1.6.3-1_patch.zip

Patch: fix-phosphor-state-manager-ALT-libgpiod-1.6.3-linker.patch

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
BuildRequires: stdexec-devel

%description
%summary.

%prep
%setup
%autopatch -p1

mkdir -p subprojects/packagecache
%{replace_meson_wrapdb_hash libgpiod source_hash %SOURCE1}
%{install_meson_subproject %SOURCE1}
%{replace_meson_wrapdb_hash libgpiod patch_hash %SOURCE2}
%{install_meson_subproject %SOURCE2}

# Restore path to binary in unit files
find . -type f \( -name "*service" -o -name "*service.in" \) \
    -exec sed -i "s|ExecStart=/usr/libexec/|ExecStart=%_libexecdir/|g" {} +

%build
%meson
%meson_build

%install
%__meson_install --skip-subprojects libgpiod

%files
%config(noreplace) %_sysconfdir/synclist
%_bindir/detect-slot-aspeed
%_bindir/obmc-flash-bmc
%_bindir/reset-cs0-aspeed
%_bindir/sync-once.sh
%_libexecdir/phosphor-code-mgmt

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
%_unitdir/xyz.openbmc_project.Software.BIOS.service
%_unitdir/xyz.openbmc_project.Software.CPLD.service
%_unitdir/xyz.openbmc_project.Software.Download.service
%_unitdir/xyz.openbmc_project.Software.EEPROMDevice.service
%_unitdir/xyz.openbmc_project.Software.I2CVR.service
%_unitdir/xyz.openbmc_project.Software.Manager.service
%_unitdir/xyz.openbmc_project.Software.Sync.service
%_unitdir/xyz.openbmc_project.Software.TPM.service

%changelog
* Thu Jul 23 2026 Anatoly Mukosey <mukav@altlinux.org> 1.0.0-alt2.git14a40be.1
- New snapshot.
- Restore path to binary in unit files.

* Wed Aug 27 2025 Ulysses Apokin <ulysses@altlinux.org> 1.0.0-alt1.git46f2a39
- Initial build for Sisyphus.
