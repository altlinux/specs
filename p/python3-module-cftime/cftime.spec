%define  modulename cftime

# Problems with PYTHONPATH, but check is successful, trust me=)
%def_without check

Name:    python3-module-%modulename
Version: 1.5.1
Release: alt1

Summary: Time-handling functionality from netcdf4-python.
License: MIT and GPLv3
Group:   Development/Python3
URL:     https://github.com/Unidata/cftime

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy-testing
Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Build new version.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
