%define modname backports.entry-points-selectable
%define pypi_name backports.entry_points_selectable

%def_disable check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Compatibility shim providing selectable entry points for older implementations
Group: Development/Python3
License: MIT
Url: https://pypi.org/project/backports.entry-points-selectable

Vcs: https://github.com/jaraco/backports.entry_points_selectable.git

Source: https://pypi.io/packages/source/b/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools) python3(setuptools_scm)
%{?_enable_check:BuildRequires: python3(tox) python3(pytest) python3(diff_cover)
BuildRequires: python3(twine) python3(jaraco.develop}

%description
Compatibility shim to ease adoption of importlib_metadata 3.6. Supplies
forward-compatibility of "selectable" entry points even on older
versions of importlib_metadata and importlib.metadata, and avoids usage
that triggers deprecation warnings.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/backports/*.py
%python3_sitelibdir_noarch/backports/__pycache__/*
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info
%doc README* NEWS*

%changelog
* Wed Oct 09 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus

