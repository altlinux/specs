%define oname robotframework-pageobjects

%def_without python3

Name: python-module-%oname
Version: 1.1.7
Release: alt1.git20150122
Summary: Lets you use the page object pattern with Robot Framework and plain python
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-pageobjects/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ncbi/robotframework-pageobjects.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-decorator python-module-mock
BuildPreReq: python-module-requests python-module-uritemplate
BuildPreReq: python-module-robotframework-selenium2library
BuildPreReq: python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-decorator python3-module-mock
BuildPreReq: python3-module-requests python3-module-uritemplate
BuildPreReq: python3-module-robotframework-selenium2library
BuildPreReq: python3-module-docutils
%endif

%py_provides robotpageobjects

%description
This Python package adds support of the Page Object pattern to Robot
Framework & Robot Framework's Selenium2Library.

The main point of using page objects is to factor out page
implementation details (locators, UI details etc.) from the actual test
suites. This makes the tests read more about the services a page offers
and what's being tested instead of the internals of the page. It also
makes your tests much more maintainable. For example, if a developer
changes an element ID, you only need make that change once--in the
appropriate page object.

Each page object is simply a Robot library that inherits from this
package's base Page class. These library classes can work independently
of Robot Framework, even though they ultimately inherit from Robot
Framework's Selenium2Library. This allows you to encapsulate page logic
Robot libraries, but use those libraries in any testing framework,
including Python unittest test cases.

%package -n python3-module-%oname
Summary: Lets you use the page object pattern with Robot Framework and plain python
Group: Development/Python3
%py3_provides robotpageobjects

%description -n python3-module-%oname
This Python package adds support of the Page Object pattern to Robot
Framework & Robot Framework's Selenium2Library.

The main point of using page objects is to factor out page
implementation details (locators, UI details etc.) from the actual test
suites. This makes the tests read more about the services a page offers
and what's being tested instead of the internals of the page. It also
makes your tests much more maintainable. For example, if a developer
changes an element ID, you only need make that change once--in the
appropriate page object.

Each page object is simply a Robot library that inherits from this
package's base Page class. These library classes can work independently
of Robot Framework, even though they ultimately inherit from Robot
Framework's Selenium2Library. This allows you to encapsulate page logic
Robot libraries, but use those libraries in any testing framework,
including Python unittest test cases.

%prep
%setup

echo '%version' >RELEASE-VERSION

%if_with python3
cp -fR . ../python3
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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md demo
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md demo
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.git20150122
- Version 1.1.7

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.git20141208
- Version 1.1.4

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141124
- Version 1.1.3

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141119
- Version 1.1.0

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141112
- New snapshot

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20141110
- Initial build for Sisyphus

