%define _unpackaged_files_terminate_build 1
%define pypi_name jq

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.0
Release: alt1

Summary: Python bindings for jq
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/jq/
Vcs: https://github.com/mwilliamson/jq.py

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: python3-module-cython
BuildRequires: libjq-devel
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
export JQPY_USE_SYSTEM_LIBS=1
%pyproject_build

%install
export JQPY_USE_SYSTEM_LIBS=1
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc *.rst LICENSE
%python3_sitelibdir/%pypi_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 24 2024 Anton Zhukharev <ancieg@altlinux.org> 1.8.0-alt1
- Updated to 1.8.0.

* Mon Mar 25 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.0-alt1
- Updated to 1.7.0.

* Tue Jan 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt3
- Built with check (fixed the test for libjq 1.7.1).

* Sun Jan 07 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Fixed FTBFS, building without check.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Thu Aug 31 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Thu Mar 16 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- 1.4.0 -> 1.4.0.

* Thu Jan 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt2
- remove unused liboniguruma-devel build requirement

* Thu Jan 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- 1.4.0
- update whole package building
- use modern pyproject macros
- actualize Summary, License and Url tags

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt2
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1
- Updated to upstream version 0.1.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150118.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150118
- Initial build for Sisyphus

