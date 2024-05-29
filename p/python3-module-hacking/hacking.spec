%define _unpackaged_files_terminate_build 1
%define pypi_name hacking

%def_with check

Name: python3-module-%pypi_name
Version: 6.1.0
Release: alt1

Summary: OpenStack Hacking Guideline Enforcement
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
URL: https://pypi.org/project/hacking
VCS: https://github.com/openstack/hacking

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pbr)

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(flake8)

BuildRequires: python3(stestr)
BuildRequires: python3(ddt)
%endif

%py3_requires flake8

%description
hacking is a set of flake8 plugins that test and enforce the OpenStack
Style Guidlines.

%prep
%setup
%autopatch -p1
sed -i -e '/flake8/d' requirements.txt

%build
# https://docs.openstack.org/pbr/latest/user/packagers.html#versioning
export PBR_VERSION=%version
%pyproject_build

%install
export PBR_VERSION=%version
%pyproject_install

# don't ship tests
rm -rv %buildroot%python3_sitelibdir/hacking/tests/

%check
export PBR_VERSION=%version
%tox_check_pyproject

%files
%doc *.rst doc/source/*.rst
%python3_sitelibdir/hacking
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 27 2024 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt1
- Automatically updated to 6.1.0.

* Fri Jul 28 2023 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- Automatically updated to 6.0.1.

* Mon Oct 03 2022 Stanislav Levin <slev@altlinux.org> 4.1.0-alt2
- Fixed FTBFS (Flake8 5.0).
- Modernized packaging.

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

