%define  modulename cftime

%def_with check

Name:    python3-module-%modulename
Version: 1.6.0
Release: alt1

Summary: Time-handling functionality from netcdf4-python.

License: MIT and GPLv3
Group:   Development/Python3
URL:     https://github.com/Unidata/cftime

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy-testing
%endif

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.
- Build with check.

* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Build new version.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
