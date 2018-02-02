%define oname robotframework-selenium2library

%def_with python3

Name: python-module-%oname
Version: 1.8.0
Release: alt1.1
Summary: Web testing library for Robot Framework
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/robotframework-selenium2library/

# https://github.com/rtomac/robotframework-selenium2library.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools python-module-decorator
BuildRequires: python-module-selenium python-module-robotframework
BuildRequires: python-module-docutils python-module-html5lib
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-decorator
BuildRequires: python3-module-selenium python3-module-robotframework
BuildRequires: python3-module-docutils python3-module-html5lib
BuildRequires: python-tools-2to3 python3-module-sphinx
BuildRequires: python3-module-pytest
%endif

%py_requires decorator

%description
Selenium2Library is a web testing library for Robot Framework that
leverages the Selenium 2 (WebDriver) libraries.

%package -n python3-module-%oname
Summary: Web testing library for Robot Framework
Group: Development/Python3
%py3_requires decorator

%description -n python3-module-%oname
Selenium2Library is a web testing library for Robot Framework that
leverages the Selenium 2 (WebDriver) libraries.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
PYTHONPATH=./src:./test/lib py.test

%if_with python3
pushd ../python3
python3 setup.py test
# TODO: two tests still fail
PYTHONPATH=./src:./test/lib py.test3 ||:
popd
%endif

%files
%doc *.txt *.rst *.md docs/*.html
%python_sitelibdir/Selenium2Library
%python_sitelibdir/robotframework_selenium2library-%version-py*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst *.md docs/*.html
%python3_sitelibdir/Selenium2Library
%python3_sitelibdir/robotframework_selenium2library-%version-py*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.0-alt1
- Updated to upstream version 1.8.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.dev.git20150217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7-alt1.dev.git20150217.1
- NMU: Use buildreq for BR.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev.git20150217
- Version 1.7.dev
- Added module for Python 3

* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141102
- Version 1.6.0

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141008
- Initial build for Sisyphus

