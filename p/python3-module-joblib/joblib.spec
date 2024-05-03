%define _unpackaged_files_terminate_build 1
%define pypi_name joblib

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Lightweight pipelining: using Python functions as pipeline jobs
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/joblib/
Vcs: https://github.com/joblib/joblib
BuildArch: noarch
Source: %name-%version.tar
Source1: debundler.py.in
Source2: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps -- vendored
# manually manage dependencies with metadata
AutoReq: yes, nopython3
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps -- vendored
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-timeout
%endif

%description
Joblib is a set of tools to provide lightweight pipelining in Python. In
particular, joblib offers:

  1. transparent disk-caching of the output values and lazy
     re-evaluation (memoize pattern)
  2. easy simple parallel computing
  3. logging and tracing of the execution

Joblib is optimized to be fast and robust in particular on large data
and has specific optimizations for numpy arrays.

%prep
%setup
%autopatch -p1
# gen vendored list for upstream
set -o pipefail
%__python3 - <<-'EOF' | sort -u > _vendor.txt
import pkgutil
for mod in pkgutil.iter_modules(["joblib/externals"]):
    print(mod.name)
EOF
%pyproject_deps_resync vendored pip_reqfile _vendor.txt

VENDORED_PATH='joblib/externals'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"joblib.externals"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc CHANGES.rst README.rst
%python3_sitelibdir/joblib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/joblib/test*
%exclude %python3_sitelibdir/joblib/__pycache__/test*

%changelog
* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1
- 1.4.0 -> 1.4.2.

* Tue Apr 09 2024 Stanislav Levin <slev@altlinux.org> 1.4.0-alt1
- 1.3.2 -> 1.4.0.

* Thu Mar 21 2024 Stanislav Levin <slev@altlinux.org> 1.3.2-alt2
- Fixed FTBFS (Python 3.12).

* Thu Aug 10 2023 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1
- 1.2.0 -> 1.3.2.

* Thu Oct 13 2022 Stanislav Levin <slev@altlinux.org> 1.2.0-alt2
- Fixed build without check.

* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0.

* Tue Mar 01 2022 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1
- 0.14.1 -> 1.1.0.

* Tue Mar 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.14.1-alt1
- Version updated to 0.14.1
- build for python2 disabled.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.13.2-alt2
- Added missing dep on `numpy.testing`.

* Wed May 08 2019 Stanislav Levin <slev@altlinux.org> 0.13.2-alt1
- Update to upstream version 0.13.2.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt2
- Applied patch to tests.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11-alt1
- Update to upstream version 0.11.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.b3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.b3.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.b3
- Version 0.9.0b3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1
- Version 0.8.2

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Version 0.7.1

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0d-alt1
- Version 0.7.0d

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6.4-alt1.1
- Rebuild with Python-3.3

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Version 0.6.4
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.dev
- Version 0.5.6.dev

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev
- Version 0.5.5.dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus

