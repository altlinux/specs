%define _unpackaged_files_terminate_build 1
%define pypi_name shiftschema
%define mod_name %pypi_name

# doesn't work because of nose usage
%def_without check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1
Summary: Filtering and validation library for arbitrary data structures
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/shiftschema/
Vcs: https://github.com/projectshift/shift-schema
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Filtering and validation library for Python3. Can filter and validate
data in model objects and simple dictionaries with flexible schemas.

Main idea: decouple filtering and validation rules from web forms into
flexible schemas, then reuse those schemas in forms as well as apis and
cli. Model validation and filtering rules should be part of the model
and your domain logic, not your views or forms logic.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# doesn't work because of nose usage
%pyproject_run -- ./cli test

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jun 10 2024 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1.

* Thu Mar 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.0.11 -> 0.3.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 0.0.11-alt2
- Dropped dependency on coveralls.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.11-alt1
- Updated to upstream version 0.0.11.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.9-alt1.git20150218.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150218
- Version 0.0.9

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150211
- Version 0.0.7

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150205
- Initial build for Sisyphus

