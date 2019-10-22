%define  modulename pytest-rerunfailures

Name:    python3-module-%modulename
Version: 7.0
Release: alt1

Summary: a pytest plugin that re-runs failed tests up to -n times to eliminate flakey failures

License: MPLv2
Group:   Development/Python3
URL:     https://github.com/pytest-dev/pytest-rerunfailures

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pytest_rerunfailures.py
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 7.0-alt1
- Initial build for Sisyphus.
