%define oname numdifftools

%def_disable check

Name: python3-module-%oname
Version: 0.9.12
Release: alt2.git20150828.1

Summary: Solves automatic numerical differentiation problems in one or more variables
License: BSD
Group: Development/Python3
Url: http://code.google.com/p/numdifftools/

# https://github.com/pbrod/numdifftools.git
Source: Numdifftools-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-scipy git xvfb-run
BuildPreReq: python3-module-numpy-addons python3-module-matplotlib
BuildPreReq: python3-module-coverage python3-module-setuptools
BuildPreReq: python3-module-setuptools_scm python3-module-six
BuildPreReq: python3-module-algopy python3-module-nose
BuildPreReq: python3-module-pytest-runner
BuildPreReq: python3-module-pytest-cov
BuildPreReq: texlive-latex-recommended

%py3_provides %oname
%py3_requires numpy scipy algopy

%description
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

%package test
Summary: Test suite for Numdifftools
Group: Development/Python
Requires: %name = %version-%release

%description test
Numdifftools is a suite of tools to solve automatic numerical
differentiation problems in one or more variables. All of these methods
also produce error estimates on the result.

This package contains test suite for Numdifftools.

%prep
%setup

git config --global user.email "real at atlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
xvfb-run python3 -c "import numdifftools as nd; nd.test(coverage=True)"
popd
xvfb-run py.test-%_python3_version -vv -rsxXf

%files
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/test*

%files test
%python3_sitelibdir/%oname/test*
%python3_sitelibdir/%oname/*/test*

%changelog
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

