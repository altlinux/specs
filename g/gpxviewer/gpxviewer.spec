%define _unpackaged_files_terminate_build 1

Name: gpxviewer
Version: 1.2.0
Release: alt1

Summary: Viewer for GPS traces collected in the GPX format
License: GPL-3.0
Group: Sciences/Geosciences
URL: https://github.com/andrewgee/gpxviewer

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool

Requires: typelib(OsmGpsMap)

BuildArch: noarch

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
GPX Viewer is a simple app to look through your GPX trace files that you 
have from your journeys. This application processes these GPX files and 
then outputs useful information like Average and Maximum Speeds. You are
also able to see the route on a map overlay.

%prep
%setup -n %name-%version
%patch -p1

%build
#%%python3_build
%pyproject_build

%install
#%%python3_install
%pyproject_install

%find_lang %name

%files -f %name.lang
%doc AUTHORS CHANGELOG COPYING README
%_bindir/*
%_desktopdir/%{name}.desktop
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%dir %_datadir/%name
%_datadir/%name/*
%_pixmapsdir/*

%changelog
* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
