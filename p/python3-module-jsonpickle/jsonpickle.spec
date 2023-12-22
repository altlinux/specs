%define _unpackaged_files_terminate_build 1
%define pypi_name jsonpickle

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.2
Release: alt1.1
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jsonpickle/
VCS: https://github.com/jsonpickle/jsonpickle.git

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pytest-black-multipy
# scikit-learn is broken with current numpy
%add_pyproject_deps_check_filter scikit-learn
%pyproject_builddeps_metadata_extra testing
BuildRequires: python3-module-pandas-tests
%endif

%description
jsonpickle converts complex Python objects to and from JSON.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# test_multindex_dataframe_roundtrip fail on armh and i586
%pyproject_run_pytest -ra -k 'not test_multindex_dataframe_roundtrip'

%files
%doc CHANGES.rst README.rst
%python3_sitelibdir/jsonpickle/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 22 2023 Anton Vyatkin <toni@altlinux.org> 3.0.2-alt1.1
- NMU: fix ftbfs (added BR pandas-tests).

* Mon Aug 14 2023 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1
- 3.0.0 -> 3.0.2.

* Fri Dec 02 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.1.0 -> 3.0.0.

* Mon Feb 07 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Tue Oct 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2
- Updated build and runtime dependencies.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.
- Enabled tests.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.
- Disabled build for python-2.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.5-alt1
- Updated to upstream version 0.9.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

