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

Name: x86-power-control
Version: 0.1
Release: alt1.git05e8ea8

Summary: Implementation of power control for x86 servers
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/x86-power-control
Vcs: https://github.com/openbmc/x86-power-control.git

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

Patch: fix-x86-power-control-ALT-libgpiod-1.6.3-linker.patch

BuildRequires(Pre): rpm-macros-meson

BuildRequires: gcc-c++
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: nlohmann-json-devel
BuildRequires: meson

ExclusiveArch: %ix86 x86_64

%description
The OpenBMC compliant implementation of power control for x86 servers.
It relies on a number of features to do its job. It has several
intentional design goals.

1. The BMC should maintain the Host state machine internally, and be able to
   track state changes.
2. The implementation should either give the requested power control result,
   or should log an error on the failure it detected.
3. The BMC should support all the common operations, hard power on/off/cycle,
   soft power on/off/cycle.

This daemon has been successfully used on a variety of server platforms; it
should be able to support platforms with power control GPIOs similar to those
in its config file.

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
%_bindir/power-control
%_unitdir/chassis-system-reset.service
%_unitdir/chassis-system-reset.target
%_unitdir/xyz.openbmc_project.Chassis.Control.Power@.service
%_datadir/%name

%changelog
* Thu Dec 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git05e8ea8
- Initial build for Sisyphus.
