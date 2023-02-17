%define _unpackaged_files_terminate_build 1
%define pypi_name aiohttp-jinja2
%define mod_name aiohttp_jinja2

%def_with check

Name: python3-module-%mod_name
Epoch: 1
Version: 1.5.1
Release: alt1
Summary: jinja2 template renderer for aiohttp.web
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aiohttp-jinja2/
VCS: https://github.com/aio-libs/aiohttp_jinja2.git
Source0: aiohttp-%version.tar
Patch0: aiohttp_jinja2-1.5-tests-Drop-dependency-on-coverage.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# dependencies=
BuildRequires: python3(aiohttp)
BuildRequires: python3(jinja2)

BuildRequires: python3(aiohttp.test_utils)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_aiohttp)
BuildRequires: python3(yarl)
%endif

# well-known PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

%description
jinja2 template renderer for aiohttp.web.

%prep
%setup -n aiohttp-%version
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 17 2023 Stanislav Levin <slev@altlinux.org> 1:1.5.1-alt1
- 1.5 -> 1.5.1.

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 1:1.5-alt1
- 0.13.0 -> 1.5.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1:0.13.0-alt3
- Drop python2 support.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.13.0-alt2
- drop excessive python3-module-jinja2-tests BR

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.13.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.13.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.4.1-alt1.git20150418.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.4.1-alt1.git20150418.1
- NMU: Use buildreq for BR.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.1-alt1.git20150418
- Version 0.4.1

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2.1-alt1.git20150215
- Version 0.2.1

* Mon Jan 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.0.1-alt1.git20150108
- Version 0.0.1

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a.git20141227
- Initial build for Sisyphus

