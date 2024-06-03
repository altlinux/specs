%define oname daiquiri

%def_with check

Name: python3-module-%oname
Version: 3.2.5.1
Release: alt1

Summary: Library to configure Python logging easily

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/daiquiri
VCS: https://github.com/Mergifyio/daiquiri

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-python-json-logger
%endif

%description
The daiquiri library provides an easy way to configure logging.
It also provides some custom formatters and handlers.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 3.2.5.1-alt1
- Build new version.

* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.0-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- initial build
