%define _unpackaged_files_terminate_build 1

%define pypi_name boto3
%def_with check

Name: python3-module-%pypi_name
Version: 1.28.5
Release: alt1
Summary: The AWS SDK for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/boto3/
Vcs: https://github.com/boto/boto3
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# this version includes debundler
Requires: python3-module-botocore >= 1.27.42-alt1
# botocore.vendored doesn't provide subpackages
%filter_from_requires /python3(botocore\.vendored\..*)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%prep
%setup
%autopatch1 -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python scripts/ci/run-tests

%files
%doc README.*
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 1.28.5-alt1
- 1.24.90 -> 1.28.5.

* Fri Oct 14 2022 Stanislav Levin <slev@altlinux.org> 1.24.90-alt1
- 1.24.42 -> 1.24.90.

* Mon Aug 01 2022 Stanislav Levin <slev@altlinux.org> 1.24.42-alt1
- 1.21.15 -> 1.24.42.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 1.21.15-alt1
- 1.17.96 -> 1.21.15.

* Sat Aug 14 2021 Ivan A. Melnikov <iv@altlinux.org> 1.17.96-alt2
- minor build requirements cleanup
- enable %%check

* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.17.96-alt1
- new version 1.17.96 (with rpmrb script)
- disable check (due internet depends)

* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.14.56-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.14.56-alt1
- Updated to upstream version 1.14.56.

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.7.29-alt1
- Updated to upstream version 1.7.29.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.6-alt1
- Updated to upstream version 1.4.6.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.1-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150807
- New snapshot

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150723
- Version 1.1.1

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150420
- Version 0.0.16

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1.git20150316
- Version 0.0.10

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150219
- Version 0.0.9

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20150210
- Version 0.0.8

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141218
- Version 0.0.6

* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141209
- Version 0.0.5

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141208
- Version 0.0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141126
- Version 0.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141120
- Version 0.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141111
- Initial build for Sisyphus

