%define oname numdifftools

%def_with check

Name: python3-module-%oname
Version: 0.9.41
Release: alt2

Summary: Solves automatic numerical differentiation problems in one or more variables

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/numdifftools
VCS: https://github.com/pbrod/numdifftools
BuildArch: noarch
Source: %name-%version.tar
Patch0: nd-0.9.41-alt-fix-pytest-runner.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-algopy
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-matplotlib
BuildRequires: python3-module-statsmodels
BuildRequires: python3-module-pandas-tests
%endif

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-algopy
Requires: python3-module-scikits.statsmodels
Requires: python3-module-pandas-tests

%description tests
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains tests for %oname.

%prep
%setup
%patch0

%build
%pyproject_build

%install
%pyproject_install

%check
# support numpy 1.25.2 https://github.com/pbrod/numdifftools/issues/72
%pyproject_run_pytest -v src/%oname/tests/ -k "\
not test_high_order_derivative \
and not test_low_order_derivative_on_example_functions \
and not test_sinx_div_x \
and not test_complex_hessian_issue_35"

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests
%doc LICENSE.txt *.rst

%changelog
* Wed Sep 13 2023 Anton Vyatkin <toni@altlinux.org> 0.9.41-alt2
- Fix FTBFS.

* Fri Feb 10 2023 Anton Vyatkin <toni@altlinux.org> 0.9.41-alt1
- new version 0.9.41 (Closes: #44635).

* Fri Jul 30 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.39-alt2
- Updated build dependencies.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.39-alt1
- new version 0.9.39 (with rpmrb script)
- disable check (need rewrite)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.12-alt2.git20150828.2
- cleanup spec, update URL, switch to build from tarball, drop tests packing

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.12-alt2.git20150828.1
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.12-alt1.git20150828.1.1.1.qa1
- NMU: applied repocop patch

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.12-alt1.git20150828.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1.git20150828.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.12-alt1.git20150828
- Version 0.9.12

* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20141217
- Version 0.7.3

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt2.svn20140221
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.svn20140221
- Version 0.6.0

* Tue Jul 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Version 0.3.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.4-alt1.1
- Rebuild with Python-2.7

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus

