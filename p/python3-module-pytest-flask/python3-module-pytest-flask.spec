%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-flask
%define mod_name pytest_flask

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: A set of pytest fixtures to test Flask applications
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-flask/
Vcs: https://github.com/pytest-dev/pytest-flask

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-pep8
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
An extension of pytest test runner which provides a set of useful
tools to simplify testing and development of the Flask extensions
and applications.

%prep
%setup
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Dec 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Mar 04 2022 Danil Shein <dshein@altlinux.org> 1.2.0-alt1
- new version 0.10.0 -> 1.2.0

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141124.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20141124.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141124
- Version 0.6.0

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141103
- Version 0.5.0

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141028
- Initial build for Sisyphus

