Name: entity-manager
Version: 0.1
Release: alt1.git48e44b7

Summary: Run-time JSON driven system configuration manager
License: Apache-2.0
Group: Other
Url: https://github.com/openbmc/entity-manager
Vcs: https://github.com/openbmc/entity-manager.git

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-meson

BuildRequires: boost-filesystem-devel
BuildRequires: gcc-c++
BuildRequires: libdbus-devel
BuildRequires: libi2c-devel
BuildRequires: libphosphor-dbus-interfaces-devel
BuildRequires: libphosphor-logging-devel
BuildRequires: libsdbusplus-devel
BuildRequires: meson
BuildRequires: python3-module-jsonschema
BuildRequires: valijson-devel

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

%build
%meson
%meson_build

%install
%meson_install

%files
%_libexecdir/%name
%_unitdir/devicetree-vpd-parser.service
%_unitdir/xyz.openbmc_project.EntityManager.service
%_unitdir/xyz.openbmc_project.FruDevice.service
%_datadir/dbus-1/system-services/xyz.openbmc_project.EntityManager.service
%_datadir/%name
%_datadir/%name/configurations

%changelog
* Thu Dec 11 2025 Ulysses Apokin <ulysses@altlinux.org> 0.1-alt1.git48e44b7
- Initial build for Sisyphus.
