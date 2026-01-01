%define _unpackaged_files_terminate_build 1

%def_with check

Name: photocollage
Version: 1.5.0
Release: alt1

Summary: Graphical tool to make photo collage posters
License: GPL-2.0-or-later
Group: Graphics
URL: https://github.com/adrienverge/PhotoCollage

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(PIL)
BuildRequires: python3(cairo)
%endif

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
PhotoCollage allows you to create photo collage posters. It assembles
the input photographs it is given to generate a big poster. Photos are
automatically arranged to fill the whole poster, then you can change the
final layout, dimensions, border or swap photos in the generated grid.
Eventually the final poster image can be saved in any size.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.rst screenshots
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_bindir/photocollage
%_desktopdir/photocollage.desktop
%_datadir/metainfo/photocollage.appdata.xml
%_iconsdir/hicolor/*/apps/photocollage.png
%_iconsdir/hicolor/*/apps/photocollage.svg

%changelog
* Thu Jan 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
