%define _unpackaged_files_terminate_build 1
%define pypi_name soco
%define mod_name SoCo

%def_with check

Name: python3-module-%pypi_name
Version: 0.30.11
Release: alt1
Summary: SoCo (Sonos Controller) is a Python project that allows you to programmatically control Sonos speakers.
License: MIT
Group: Development/Python3
Url: https://github.com/SoCo/SoCo
Vcs: https://pypi.org/project/soco/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(requests)
BuildRequires: python3(xmltodict)
BuildRequires: python3(ifaddr)
BuildRequires: python3(appdirs)
BuildRequires: python3(lxml)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(sphinx)
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3(graphviz)
BuildRequires: python3(flake8)
BuildRequires: python3(pylint)
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-requests-mock
BuildRequires: python3(twine)
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3(build)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest 


%files
%doc README.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Aug 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.30.11-alt1
- Initial build for Sisyphus.