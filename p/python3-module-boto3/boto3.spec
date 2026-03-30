%define _unpackaged_files_terminate_build 1
%define pypi_name boto3
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.42.68
Release: alt1.1
Summary: The AWS SDK for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/boto3/
Vcs: https://github.com/boto/boto3
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# this version includes debundler
Requires: python3-module-botocore >= 1.27.42-alt1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-atomicwrites
BuildRequires: python3-module-colorama
BuildRequires: python3-module-coverage
BuildRequires: python3-module-packaging
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-wheel

BuildRequires: python3-module-botocore
BuildRequires: python3-module-jmespath
BuildRequires: python3-module-s3transfer
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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python scripts/ci/run-tests unit/

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.42.68-alt1.1
- Demodernized packaging.

* Mon Mar 16 2026 Stanislav Levin <slev@altlinux.org> 1.42.68-alt1
- 1.42.65 -> 1.42.68.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 1.42.65-alt1
- 1.40.25 -> 1.42.65.

* Mon Sep 08 2025 Stanislav Levin <slev@altlinux.org> 1.40.25-alt1
- 1.40.22 -> 1.40.25.

* Wed Sep 03 2025 Stanislav Levin <slev@altlinux.org> 1.40.22-alt1
- 1.40.7 -> 1.40.22.

* Tue Aug 12 2025 Stanislav Levin <slev@altlinux.org> 1.40.7-alt1
- 1.40.6 -> 1.40.7.

* Mon Aug 11 2025 Stanislav Levin <slev@altlinux.org> 1.40.6-alt1
- 1.40.2 -> 1.40.6.

* Tue Aug 05 2025 Stanislav Levin <slev@altlinux.org> 1.40.2-alt1
- 1.39.15 -> 1.40.2.

* Tue Jul 29 2025 Stanislav Levin <slev@altlinux.org> 1.39.15-alt1
- 1.39.14 -> 1.39.15.

* Mon Jul 28 2025 Stanislav Levin <slev@altlinux.org> 1.39.14-alt1
- 1.39.9 -> 1.39.14.

* Mon Jul 21 2025 Stanislav Levin <slev@altlinux.org> 1.39.9-alt1
- 1.39.8 -> 1.39.9.

* Fri Jul 18 2025 Stanislav Levin <slev@altlinux.org> 1.39.8-alt1
- 1.39.0 -> 1.39.8.

* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 1.39.0-alt1
- 1.38.41 -> 1.39.0.

* Mon Jun 23 2025 Stanislav Levin <slev@altlinux.org> 1.38.41-alt1
- 1.38.36 -> 1.38.41.

* Mon Jun 16 2025 Stanislav Levin <slev@altlinux.org> 1.38.36-alt1
- 1.38.34 -> 1.38.36.

* Wed Jun 11 2025 Stanislav Levin <slev@altlinux.org> 1.38.34-alt1
- 1.38.32 -> 1.38.34.

* Mon Jun 09 2025 Stanislav Levin <slev@altlinux.org> 1.38.32-alt1
- 1.38.31 -> 1.38.32.

* Fri Jun 06 2025 Stanislav Levin <slev@altlinux.org> 1.38.31-alt1
- 1.38.22 -> 1.38.31.

* Fri May 23 2025 Stanislav Levin <slev@altlinux.org> 1.38.22-alt1
- 1.37.37 -> 1.38.22.

* Mon Apr 21 2025 Stanislav Levin <slev@altlinux.org> 1.37.37-alt1
- 1.37.28 -> 1.37.37.

* Mon Apr 07 2025 Stanislav Levin <slev@altlinux.org> 1.37.28-alt1
- 1.37.6 -> 1.37.28.

* Wed Mar 05 2025 Stanislav Levin <slev@altlinux.org> 1.37.6-alt1
- 1.36.0 -> 1.37.6.

* Thu Jan 16 2025 Stanislav Levin <slev@altlinux.org> 1.36.0-alt1
- 1.35.37 -> 1.36.0.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 1.35.37-alt1
- 1.34.49 -> 1.35.37.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 1.34.49-alt1
- 1.28.5 -> 1.34.49.

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

