%define pypi_name donfig

%def_with check

Name:    python3-module-%pypi_name
Version: 0.8.1
Release: alt1

Summary: Python library for configuring a package including defaults, env variable loading, and yaml loading

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/donfig
VCS:     https://github.com/pytroll/donfig

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-yaml
BuildRequires: python3-module-cloudpickle
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Donfig is a python library meant to make configuration easier for other
python packages. Donfig can be configured programmatically, by environment
variables, or from YAML files in standard locations.

%prep
%setup

# do not use versioneer
sed -i 's/^dynamic = \["version"\]$/version = "%version"/' pyproject.toml
sed -i '/import versioneer/d' setup.py
sed -i 's/version=versioneer.get_version(),/version="%version",/' setup.py
sed -i '/cmdclass=versioneer.get_cmdclass(),/d' setup.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
