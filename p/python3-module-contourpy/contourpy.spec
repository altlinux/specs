%define modulename contourpy

%def_with check

Name:    python3-module-%modulename
Version: 1.0.7
Release: alt2

Summary: Python library for calculating contours in 2D quadrilateral grids

License: BSD-3-Clause
Group:   Development/Python3
Url:     https://pypi.org/project/contourpy
Vcs:     https://github.com/contourpy/contourpy

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pybind11
BuildRequires: gcc-c++

%if_with check
BuildRequires: python3-module-numpy-tests
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-matplotlib
%endif

# Optional dependency, that not ready for sisyphus
%add_python3_req_skip bokeh bokeh.io bokeh.io.export bokeh.layouts bokeh.models.annotations.labels bokeh.palettes bokeh.plotting

%description
ContourPy is a Python library for calculating contours of 2D quadrilateral
grids. It is written in C++11 and wrapped using pybind11.

It contains the 2005 and 2014 algorithms used in Matplotlib as well as a newer
algorithm that includes more features and is available in both serial and
multithreaded versions. It provides an easy way for Python libraries to use
contouring algorithms without having to include Matplotlib as a dependency.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}

%changelog
* Wed Mar 01 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.7-alt2
- Fixed build requires.

* Mon Feb 13 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus.
