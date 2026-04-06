%define _unpackaged_files_terminate_build 1
%define pypi_name xyzservices

%def_with check

Name: python3-module-%pypi_name
Version: 2026.3.0
Release: alt1
Summary: Source of XYZ tiles providers
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/xyzservices/
VCS: https://github.com/geopandas/xyzservices
BuildArch: noarch
Source: %name-%version.tar

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires:  python3(mercantile)
BuildRequires:  python3(pytest)
BuildRequires:  python3(requests)
%endif

%description
%summary

%prep
%setup
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
     git init
     git config user.email author@example.com
     git config user.name author
     git add .
     git commit -m 'release'
     git tag '%version'
fi

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/%pypi_name/tests

%check
%pyproject_run_pytest -v -m 'not request'

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%_datadir/%pypi_name/providers.json

%changelog
* Sun Apr 05 2026 Nikita Panov <nexxy@altlinux.org> 2026.3.0-alt1
- New version 2026.3.0.

* Sun Feb 01 2026 Nikita Panov <nexxy@altlinux.org> 2025.11.0-alt1
- New version 2025.11.0.

* Fri Oct 03 2025 Nikita Panov <nexxy@altlinux.org> 2025.4.0-alt1
- Initial build for Sisyphus
