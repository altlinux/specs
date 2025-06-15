%define _unpackaged_files_terminate_build 1

%define pypi_name gpxpy

%def_without check

Name: python3-module-%pypi_name
Version: 1.6.2
Release: alt1

Summary: GPX file parser, GPS track manipulation library (Python 3) and utility
License: Apache-2.0
Group: Sciences/Geosciences
URL: https://github.com/tkrajina/gpxpy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
gpxpy is a simple Python library for parsing and manipulating GPX files.
GPX is an XML based format for GPS tracks.

The library also contains utility functions that are used in GPX file
handling, but can also be used separately, e.g. simple functions for
calculating geographical coordinates.

gpxinfo extracts basic statistics from a GPX file. It prints meta info
about the file and calculates data about tracks and routes in the file,
among which are times, distances, and uphill and downhill information.

gpxinfo uses the gpxpy library.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md *.txt
%_bindir/gpxinfo
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jun 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus
