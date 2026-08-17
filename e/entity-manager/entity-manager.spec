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

Name: entity-manager
Version: 0.1
Release: alt3.gitedc58d0.1

Summary: Run-time JSON driven system configuration manager
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/entity-manager
Vcs: https://github.com/openbmc/entity-manager.git

Source: %name-%version.tar
# See subprojects/libgpiod.wrap file, line "source_url"
# https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/snapshot/libgpiod-1.6.3.tar.gz
Source1: libgpiod-1.6.3.tar.gz
# See subprojects/libgpiod.wrap file, line "patch_url"
# https://wrapdb.mesonbuild.com/v2/libgpiod_1.6.3-1/get_patch
Source2: libgpiod_1.6.3-1_patch.zip

Patch: Fix_path_to_the_binary_inside_unit_files.patch
Patch1: fix-phosphor-state-manager-ALT-libgpiod-1.6.3-linker.patch

BuildRequires(Pre): rpm-macros-meson

BuildRequires: boost-filesystem-devel
BuildRequires: boost-asio-devel
BuildRequires: gcc-c++
BuildRequires: libdbus-devel
BuildRequires: libi2c-devel
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: meson
BuildRequires: python3-module-jsonschema
BuildRequires: valijson-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: stdexec-devel

ExcludeArch: %ix86

%filter_from_requires /devicetree-vpd-parser/d
%filter_from_requires /entity-manager/d
%filter_from_requires /fru-device/d

%description
Entity manager is a design for managing physical system components,
and mapping them to software resources within the BMC. Said resources
are designed to allow the flexible adjustment of the system at runtime,
as well as the reduction in the number of independent system configurations
one needs to create.

%prep
%setup
%autopatch -p1

mkdir -p subprojects/packagecache
%{replace_meson_wrapdb_hash libgpiod source_hash %SOURCE1}
%{install_meson_subproject %SOURCE1}
%{replace_meson_wrapdb_hash libgpiod patch_hash %SOURCE2}
%{install_meson_subproject %SOURCE2}

%build
%meson
%meson_build

%install
%__meson_install --skip-subprojects libgpiod

%files
%_libexecdir/%name
%_unitdir/devicetree-vpd-parser.service
%_unitdir/xyz.openbmc_project.EntityManager.service
%_unitdir/xyz.openbmc_project.FruDevice.service
%_unitdir/xyz.openbmc_project.gpiopresence.service
%_datadir/dbus-1/system-services/xyz.openbmc_project.EntityManager.service
%_datadir/%name

%changelog
* Wed Jun 25 2026 Anatoly Mukosey <mukav@altlinux.org> 0.1-alt3.gitedc58d0.1
- New snapshot.

* Thu Mar 5 2026 Anatoly Mukosey <mukav@altlinux.org> 0.1-alt2.git48e44b7.1
- Fix path to the binary inside unit files.

* Thu Dec 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git48e44b7
- Initial build for Sisyphus.
