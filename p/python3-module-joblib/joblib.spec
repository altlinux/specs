%define _unpackaged_files_terminate_build 1
%define pypi_name joblib

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.0
Release: alt2

Summary: Lightweight pipelining: using Python functions as pipeline jobs
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/joblib/

BuildArch: noarch

# https://github.com/joblib/joblib.git
Source: %name-%version.tar
Source1: debundler.py.in
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# unvendored deps
BuildRequires: python3(loky)
BuildRequires: python3(cloudpickle)

BuildRequires: /proc
BuildRequires: python3(numpy)
BuildRequires: python3(numpy.testing)
BuildRequires: python3(threadpoolctl)
BuildRequires: python3(pytest)
%endif

# `distributed` is not packaged yet
%filter_from_requires /python[3]\(\.[[:digit:]]\)\?(distributed\()\|\..*)\)/d

# debundler
## filter no longer provided self-dependencies
%filter_from_requires /python3(joblib\.externals\..*)/d

## dependencies on debundled packages
%py3_requires loky
%py3_requires cloudpickle

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

VENDORED_PATH='joblib/externals'
UNVENDORED_PATH="$VENDORED_PATH/__init__.py"
rm -r "$VENDORED_PATH"
mkdir "$VENDORED_PATH"
cp "%SOURCE1" "$UNVENDORED_PATH"
sed -i \
    -e 's/@VENDORED_ROOT@/"joblib.externals"/' \
    -e 's/@VENDORED_FAKE_PACKAGES@/None/' \
    "$UNVENDORED_PATH"

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/joblib/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/joblib/test*
%exclude %python3_sitelibdir/joblib/__pycache__/test*

%changelog
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

