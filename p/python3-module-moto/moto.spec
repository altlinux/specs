%define _unpackaged_files_terminate_build 1
%define pypi_name moto

%def_with check
# full testsuite takes too long for now, run it locally
# name                      aarch64   armh   i586  ppc64le  x86_64
# python3-module-moto         20:32  35:22  12:18    25:10   12:09
%def_without full_testsuite

Name: python3-module-%pypi_name
Version: 5.0.9
Release: alt1

Summary: A library that allows your python tests to easily mock out the boto library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/moto/
Vcs: https://github.com/getmoto/moto
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manage deps with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter cfn-lint
%add_pyproject_deps_check_filter py-partiql-parser
%add_pyproject_deps_check_filter joserfc
%add_pyproject_deps_check_filter antlr4-python3-runtime
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_metadata_extra server
%pyproject_builddeps_check
%endif

%description
Moto is a library that allows your python tests to easily mock out the
boto library.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
export TESTS_SKIP_REQUIRES_DOCKER=YES
%if_with full_testsuite
export TESTS=tests
%else
export TESTS=tests/test_core
%endif
%pyproject_run_pytest $TESTS -m 'not network' -ra -Wignore

%files
%doc README.*
%_bindir/moto_server
%_bindir/moto_proxy
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 31 2024 Stanislav Levin <slev@altlinux.org> 5.0.9-alt1
- 5.0.8 -> 5.0.9.

* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 5.0.8-alt1
- 5.0.6 -> 5.0.8.

* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 5.0.6-alt1
- 4.1.13 -> 5.0.6.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 4.1.13-alt1
- 4.0.5 -> 4.1.13.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 4.0.5-alt1
- 3.1.16 -> 4.0.5.

* Mon Aug 01 2022 Stanislav Levin <slev@altlinux.org> 3.1.16-alt1
- 3.0.7 -> 3.1.16.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 3.0.7-alt1
- 3.0.5 -> 3.0.7.

* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 3.0.5-alt1
- 1.3.16 -> 3.0.5.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.3.16-alt1
- 1.3.15 -> 1.3.16.

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.15-alt1
- Updated to upstream version 1.3.15.

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt1.git20150808.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.10-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.10-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.git20150808
- Version 0.4.10

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.git20150722
- Version 0.4.7

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150222
- Version 0.4.1

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git201500203
- Version 0.4.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150117
- Initial build for Sisyphus

