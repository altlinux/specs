%define _unpackaged_files_terminate_build 1

%define mname scikits
%define rname statsmodels
%define oname %mname.%rname

Name: python3-module-%oname
Epoch: 1
Version: 0.11.1
Release: alt1
Summary: Statistical computations and models for use with SciPy
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/statsmodels/

# https://github.com/statsmodels/statsmodels.git
Source: %name-%version.tar

Patch1: %oname-alt-build.patch
Patch2: %oname-alt-check.patch
Patch3: %oname-alt-skipped-tests.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel python3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-scipy
# Test dependencies
BuildRequires: python3-module-tox
BuildRequires: python3(patsy) python3(pandas)
BuildRequires: python3(joblib) python3(pytest-xdist)

%py3_provides %oname
%py3_requires numpy scipy pandas patsy matplotlib cvxopt
%py3_requires statsmodels.stats.multitest
%add_python3_req_skip models

%description
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip rpy
%add_python3_req_skip yapf.yapflib.yapf_api

%description tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: v%version\)\"/" \
	%rname/_version.py

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%ifnarch armh
%check
# quite a few tests fail on armh. disable it for now
export PIP_NO_INDEX=YES
export PIP_NO_BUILD_ISOLATION=no
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v
%endif

%files
%doc LICENSE.txt
%doc *.md *.rst README_l1.txt
%python3_sitelibdir/%rname
%python3_sitelibdir/%rname-%version-*.egg-info
%exclude %python3_sitelibdir/%rname/*/*/*/example*
%exclude %python3_sitelibdir/%rname/*/*/example*
%exclude %python3_sitelibdir/%rname/*/*/*/test*
%exclude %python3_sitelibdir/%rname/*/*/test*
%exclude %python3_sitelibdir/%rname/*/test*

%files tests
%python3_sitelibdir/%rname/*/*/*/example*
%python3_sitelibdir/%rname/*/*/example*
%python3_sitelibdir/%rname/*/*/*/test*
%python3_sitelibdir/%rname/*/*/test*
%python3_sitelibdir/%rname/*/test*

%changelog
* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.11.1-alt1
- Updated to upstream version 0.11.1.
- Re-enabled tests.

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:0.8.0-alt3
- Build for python2 disabled.

* Wed Feb 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.8.0-alt2
- NMU: disable build python2 module

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.8.0-alt1
- Updated to upstream version 0.8.0.
- Disabled docs generation.

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 30 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt4.git20150731
- rm inessential BR: python3-module-pandas{,-tests} (incorrectly detected by buildreq).

* Fri Mar 25 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.7.0-alt3.git20150731
- BRs fixed with buildreq again (cleared off self-dependence and other
  unneeded pkgs with python-module-setuptools-18.1-alt3,
  python-2.7.11-alt2, and python-module-Cython-0.23.4-alt3).

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.7.0-alt2.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus

