%define _unpackaged_files_terminate_build 1
%define oname ujson

Name: python3-module-%oname
Version: 5.7.0
Release: alt1

Summary: Ultra fast JSON encoder and decoder for Python

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/ujson

# https://github.com/esnme/ultrajson.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++ libdouble-conversion-devel

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C with
bindings for Python.

%prep
%setup
# Remove bundled double-conversion
rm -vrf deps

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export UJSON_BUILD_NO_STRIP=1
export UJSON_BUILD_DC_INCLUDES='%{_includedir}/double-conversion'
export UJSON_BUILD_DC_LIBS='-ldouble-conversion'
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%oname.cpython-*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Jan 07 2023 Grigory Ustinov <grenka@altlinux.org> 5.7.0-alt1
- Automatically updated to 5.7.0.

* Fri Dec 02 2022 Grigory Ustinov <grenka@altlinux.org> 5.6.0-alt1
- Automatically updated to 5.6.0.

* Mon Oct 03 2022 Grigory Ustinov <grenka@altlinux.org> 5.5.0-alt1
- Build new version (Closes: #43920).
- Build with check.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.35-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.35-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.34-alt1.git20140416.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.34-alt1.git20140416
- Initial build for Sisyphus

