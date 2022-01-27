%define _unpackaged_files_terminate_build 1
%define oname hacking

%def_with check

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: OpenStack Hacking Guideline Enforcement
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/hacking/

# https://github.com/openstack-dev/hacking.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pbr)

%if_with check
# install_requires=
BuildRequires: python3(flake8)

BuildRequires: python3(stestr)
BuildRequires: python3(ddt)

BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_requires flake8

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

This package contains tests for %oname.

%prep
%setup
%autopatch -p1

%build
# https://docs.openstack.org/pbr/latest/user/packagers.html#versioning
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
export PBR_VERSION=%version
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc *.rst doc/source/*.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 26 2022 Stanislav Levin <slev@altlinux.org> 4.1.0-alt1
- 3.2.0 -> 4.1.0.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.0-alt2
- drop excessive python3-module-jinja2-tests BR

* Thu Sep 10 2020 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Build new version.
- Build with check.

* Thu Jun 04 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Build new version.
- Fix license.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.
- Disabled tests.

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.0-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.2-alt3.git20150723.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.2-alt3.git20150723.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt3.git20150723
- Added necessary requirements

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt2.git20150723
- Enabled check

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20150723
- Version 0.10.2
- Disabled check (for bootstrap)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20141105
- Initial build for Sisyphus

