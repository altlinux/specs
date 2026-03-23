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

Name: dbus-sensors
Version: 0.1
Release: alt2.gitd7be555.1

Summary: D-Bus configurable sensor scanning applications
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/dbus-sensors
Vcs: https://github.com/openbmc/dbus-sensors.git

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

Patch: fix-dbus-sensors-ALT-libgpiod-1.6.3-linker.patch
Patch1: Add_support_for_W83795G_sensor.patch
Patch2: Set_LED_if_fan_is_not_present.patch
Patch3: Add_possibility_to_set_ScaleFactor_for_Tachs.patch
Patch4: Set_Fan_LED_group_on_service_start.patch

BuildRequires(Pre): rpm-macros-meson

BuildRequires: gcc-c++
BuildRequires: libi2c-devel
BuildRequires: libpeci-devel
BuildRequires: liburing-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: nlohmann-json-devel
BuildRequires: meson

%description
dbus-sensors is a collection of sensor applications that provide the
xyz.openbmc_project.Sensor collection of interfaces. They read sensor values
from hwmon, d-bus, or direct driver access to provide readings. Some advance
non-sensor features such as fan presence, pwm control, and automatic cpu
detection (x86) are also supported.

%prep
%setup
%autopatch -p1
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
%_bindir/adcsensor
%_bindir/exitairtempsensor
%_bindir/externalsensor
%_bindir/fansensor
%_bindir/hwmontempsensor
%_bindir/intelcpusensor
%_bindir/intrusionsensor
%_bindir/ipmbsensor
%_bindir/mcutempsensor
%_bindir/nvmesensor
%_bindir/psusensor
%_unitdir/xyz.openbmc_project.adcsensor.service
%_unitdir/xyz.openbmc_project.exitairsensor.service
%_unitdir/xyz.openbmc_project.externalsensor.service
%_unitdir/xyz.openbmc_project.fansensor.service
%_unitdir/xyz.openbmc_project.hwmontempsensor.service
%_unitdir/xyz.openbmc_project.intelcpusensor.service
%_unitdir/xyz.openbmc_project.intrusionsensor.service
%_unitdir/xyz.openbmc_project.ipmbsensor.service
%_unitdir/xyz.openbmc_project.mcutempsensor.service
%_unitdir/xyz.openbmc_project.nvmesensor.service
%_unitdir/xyz.openbmc_project.psusensor.service

%changelog
* Fri Mar 6  2026 Anatoly Mukosey <mukav@altlinux.org> 0.1-alt2.gitd7be555.1
- Set led if fan is not present.
- Set fan led group on service start.
- Add support for W83795G sensor.
- Add possibility to set ScaleFactor for Tachs.

* Wed Dec 10 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.gitd7be555
- Initial build for Sisyphus.
