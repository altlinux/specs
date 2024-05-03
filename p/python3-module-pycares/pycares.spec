%define module_name pycares
%def_with docs
%def_without check

Name: python3-module-%module_name
Version: 4.4.0
Release: alt1

Summary: Python interface for c-ares

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pycares
VCS: http://github.com/saghul/pycares

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libcares-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-cffi

%if_with check
BuildRequires: python3-module-pytest
%endif

%if_with docs
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
%endif

%description
pycares is a Python module which provides an interface to c-ares. c-ares
(http://c-ares.haxx.se/) c-ares is a C library that performs DNS
requests and name resolves asynchronously.

%prep
%setup

%build
export PYCARES_USE_SYSTEM_LIB=1
export LANG=en_US.UTF-8
%pyproject_build
%if_with docs
make -C docs html SPHINXBUILD=py3_sphinx-build
%endif

%install
export LANG=en_US.UTF-8
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-%version.dist-info
%doc README.rst LICENSE ChangeLog
%if_with docs
%doc docs/_build/html
%endif

%changelog
* Fri May 03 2024 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1
- Automatically updated to 4.4.0.

* Fri Feb 09 2024 Grigory Ustinov <grenka@altlinux.org> 4.1.2-alt2
- Fixed FTBFS.

* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.2-alt1
- Build new version.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 2.3.0-alt1
- Autobuild version bump to 2.3.0

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0
- Build documentation

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.3-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Vladimir Didenko <cow@altlinux.ru> 0.6.3-alt1
- new version

* Tue Sep 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus

