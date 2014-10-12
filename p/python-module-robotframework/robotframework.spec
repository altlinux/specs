%define oname robotframework

%def_without python3

Name: python-module-%oname
Version: 2.8.7
Release: alt1.dev20141007
Summary: A generic test automation framework
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/robotframework/robotframework.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_provides robot
%add_python_req_skip java javax org

%description
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.

%package -n python3-module-%oname
Summary: A generic test automation framework
Group: Development/Python3
%py3_provides %oname
%py3_provides robot
%add_python3_req_skip java javax org

%description -n python3-module-%oname
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.

This package contains documentation for %oname.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude%_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc doc/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt1.dev20141007
- Initial build for Sisyphus

