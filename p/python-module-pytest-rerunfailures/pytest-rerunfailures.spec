%define  modulename pytest-rerunfailures

Name:    python-module-%modulename
Version: 7.0
Release: alt1

Summary: a pytest plugin that re-runs failed tests up to -n times to eliminate flakey failures

License: MPLv2
Group:   Development/Python
URL:     https://github.com/pytest-dev/pytest-rerunfailures

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/pytest_rerunfailures.py
%python_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- Initial build for Sisyphus.
