%define _unpackaged_files_terminate_build 1

%define pypi_name selenium
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 4.20.0
Release: alt1

Summary: Python bindings for Selenium
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/selenium

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: selenium-use-without-bundled-libs.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Python language bindings for Selenium WebDriver.

The selenium package is used automate web browser interaction from
Python.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Apr 25 2024 Stanislav Levin <slev@altlinux.org> 4.20.0-alt1
- 4.19.0 -> 4.20.0.

* Thu Mar 28 2024 Stanislav Levin <slev@altlinux.org> 4.19.0-alt1
- 3.14.1 -> 4.19.0.

* Thu Jan 20 2022 Stanislav Levin <slev@altlinux.org> 3.14.1-alt1
- 3.0.2 -> 3.14.1.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.2-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 19 2017 Lenar Shakirov <snejok@altlinux.ru> 3.0.2-alt2
- selenium-use-without-bundled-libs.patch added

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.47.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.47.0-alt1
- Version 2.47.0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.44.0-alt1
- Version 2.44.0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.43.0-alt1
- Initial build for Sisyphus

