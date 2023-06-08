%define _unpackaged_files_terminate_build 1
%define pypi_name requests-mock

%def_with check

Name: python3-module-%pypi_name
Version: 1.11.0
Release: alt1
Summary: Mock out responses from the requests package
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/requests-mock/
Vcs: https://github.com/jamielennox/requests-mock
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter 'requests-futures$'
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The requests-mock library at its core is simply a transport adapter that
can be preloaded with responses that are returned if certain URIs are
requested. This is particularly useful in unit tests where you want to
return known responses from HTTP requests without making actual calls.

As the requests library has very limited options for how to load and use
adapters requests-mock also provides a number of ways to make sure the
mock adapter is used. These are only loading mechanisms, they do not
contain any logic and can be used as a reference to load the adapter in
whatever ways works best for your project.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python -m testtools.run discover
%pyproject_run_pytest -ra -Wignore tests/pytest

%files
%doc *.rst
%python3_sitelibdir/requests_mock/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 08 2023 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1
- 1.10.0 -> 1.11.0.

* Mon Oct 03 2022 Stanislav Levin <slev@altlinux.org> 1.10.0-alt1
- 1.9.3 -> 1.10.0.

* Tue Mar 22 2022 Stanislav Levin <slev@altlinux.org> 1.9.3-alt1
- 1.8.0 -> 1.9.3.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1
- 1.3.0 -> 1.8.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- drop pickle package

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20141216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141216
- Initial build for Sisyphus

