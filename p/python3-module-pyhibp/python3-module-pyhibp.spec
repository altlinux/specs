%define pypi_name pyhibp

# flake8 tests failed
%def_disable check

Name: python3-module-%pypi_name
Version: 4.2.0
Release: alt1

Summary: A Python interface to HIBP public API
Group: Development/Python3
License: AGPL-3.0-only
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://gitlab.com/kitsunix/pyHIBP/pyHIBP.git

Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz
#Source: https://gitlab.com/kitsunix/pyHIBP/pyHIBP/archive/v%version/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(tox)
BuildRequires: python3(pytest_cov) python3(flake8)
BuildRequires: python3(requests) /usr/bin/check-manifest}

%description
A Python interface to Troy Hunt's 'Have I Been Pwned?' (HIBP) public
API. A full reference to the API specification can be found at the [HIBP
API Reference](https://haveibeenpwned.com/API/v3).

%prep
%setup -n %pypi_name-%version
# we are not in git repo
sed -i '/check-manifest/d' tox.ini

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check

%files
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Tue Sep 16 2025 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- first build for Sisyphus


