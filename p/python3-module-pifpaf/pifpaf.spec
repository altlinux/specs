%define oname pifpaf

%def_without check

Name: python3-module-%oname
Version: 3.2.3
Release: alt1

Summary: Suite of tools and fixtures to manage daemons for testing

Group: Development/Python3
License: Apache-2.0
URL: https://pypi.org/project/pifpaf
VCS: https://github.com/jd/pifpaf

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-daiquiri
BuildRequires: python3-module-psutil
BuildRequires: python3-module-pyxattr
BuildRequires: python3-module-requests
BuildRequires: memcached
%endif

%add_python3_req_skip swift.common

%description
Pifpaf is a suite of fixtures and a command-line tool that allows to start
and stop daemons for a quick throw-away usage. This is typically useful when
needing these daemons to run integration testing. It originaly evolved from
its precussor overtest.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

cp -av %oname/drivers %buildroot%python3_sitelibdir/%oname

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Jan 31 2025 Grigory Ustinov <grenka@altlinux.org> 3.2.3-alt1
- Build new version.

* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt2
- Drop dependency on distutils.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.5-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Build new version.
- Fix license.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt2
- Build without python2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- initial build
