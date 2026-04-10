%define _unpackaged_files_terminate_build 1
%define pypi_name botocore
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.42.87
Release: alt1
Summary: The low-level, core functionality of boto 3
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/botocore/
Vcs: https://github.com/boto/botocore
BuildArch: noarch
Source: %name-%version.tar
Source1: debundler.py.in
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps -- vendored
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# required for test_resource_leaks
BuildRequires: /proc
%pyproject_builddeps_metadata
%pyproject_builddeps -- vendored
%pyproject_builddeps_check
%endif

%description
A low-level interface to a growing number of Amazon Web Services. The
botocore package is the foundation for AWS-CLI.

%prep
%setup
%autopatch -p1

rm %mod_name/cacert.pem

VENDORED_PATH='%mod_name/vendored'
# gen vendored list for upstream (assume package/module name is the same as
# project name)
set -o pipefail
%__python3 - <<-EOF | sort -u > _vendor.txt
import pkgutil
for mod in pkgutil.iter_modules(["$VENDORED_PATH"]):
    if not mod.name.startswith("_"):
        print(mod.name)
EOF
%pyproject_deps_resync vendored pip_reqfile _vendor.txt

UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"%mod_name.vendored"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/{"requests.packages"}/' \
    "$UNVENDORED_PATH"

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
%pyproject_run -- python scripts/ci/run-tests --with-xdist unit/

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Apr 10 2026 Stanislav Levin <slev@altlinux.org> 1.42.87-alt1
- 1.42.68 -> 1.42.87.

* Mon Mar 16 2026 Stanislav Levin <slev@altlinux.org> 1.42.68-alt1
- 1.42.65 -> 1.42.68.

* Wed Mar 11 2026 Stanislav Levin <slev@altlinux.org> 1.42.65-alt1
- 1.40.59 -> 1.42.65.

* Sun Oct 26 2025 Grigory Ustinov <grenka@altlinux.org> 1.40.59-alt1
- Automatically updated to 1.40.59.

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
- 1.37.13 -> 1.37.28.

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 1.37.13-alt1
- New version 1.37.13.

* Wed Mar 05 2025 Stanislav Levin <slev@altlinux.org> 1.37.6-alt1
- 1.36.0 -> 1.37.6.

* Thu Jan 16 2025 Stanislav Levin <slev@altlinux.org> 1.36.0-alt1
- 1.35.37 -> 1.36.0.

* Thu Oct 10 2024 Stanislav Levin <slev@altlinux.org> 1.35.37-alt1
- 1.34.49 -> 1.35.37.

* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 1.34.49-alt1
- 1.31.5 -> 1.34.49.

* Wed Jul 19 2023 Stanislav Levin <slev@altlinux.org> 1.31.5-alt1
- 1.27.90 -> 1.31.5.

* Fri Oct 14 2022 Stanislav Levin <slev@altlinux.org> 1.27.90-alt1
- 1.27.57 -> 1.27.90.

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 1.27.57-alt1
- new version 1.27.57

* Mon Aug 01 2022 Stanislav Levin <slev@altlinux.org> 1.27.42-alt1
- 1.24.15 -> 1.27.42.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 1.24.15-alt1
- 1.20.96 -> 1.24.15.

* Thu Jun 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.20.96-alt1
- new version 1.20.96 (with rpmrb script)

* Wed Jun 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.17.56-alt2
- build python3 module separately

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.17.56-alt1
- Updated to upstream version 1.17.56.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Removed extra dependency on python-tox.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt1
- Updated to upstream version 1.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.7-alt1.git20150806.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.7-alt1.git20150806.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.git20150806
- Version 1.1.7

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150723
- Version 1.1.3

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.104.0-alt1.git20150416
- Version 0.104.0

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.95.0-alt1.git20150312
- Version 0.95.0

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.0-alt1.git20150223
- Version 0.93.0

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.0-alt1.git20150217
- Version 0.91.0

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.88.0-alt1.git20150212
- Version 0.88.0

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.87.0-alt1.git20150210
- Version 0.87.0

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.85.0-alt1.git20150203
- Version 0.85.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.83.0-alt1.git20150119
- Version 0.83.0

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.82.0-alt1.git20150115
- Version 0.82.0

* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.80.0-alt1.git20141217
- Version 0.80.0

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.78.0-alt1.git20141208
- Version 0.78.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.76.0-alt1.git20141126
- New snapshot

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.76.0-alt1.git20141125
- Version 0.76.0

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75.0-alt1.git20141121
- Version 0.75.0

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.74.0-alt1.git20141120
- Version 0.74.0

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.73.0-alt1.git20141112
- Version 0.73.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.71.0-alt1.git20141110
- Initial build for Sisyphus

