Name: cura-fdm-materials
Version: 2.4.0
Release: alt1
Summary: Cura FDM Material database
License: Public Domain
Group: Engineering
Url: https://github.com/Ultimaker/fdm_materials
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Cura material files.

These files are needed to work with printers like Ultimaker 2+ and Ultimaker 3.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%dir %_datadir/cura
%dir %_datadir/cura/resources
%_datadir/cura/resources/materials

%changelog
* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for ALT Sisyphus.
