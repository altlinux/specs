%define oname robotframework

%def_with python3

Name: python-module-%oname
Version: 3.0.2
Release: alt1.1
Summary: A generic test automation framework
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/robotframework/

# https://github.com/robotframework/robotframework.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_provides %oname
%py_provides robot
%add_python_req_skip java javax org System
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/libraries/dialogs_ipy.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/libraries/dialogs_jy.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/running/timeouts/ironpython.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/running/timeouts/jython.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/htmldata/jartemplate.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/jarrunner.py

%description
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.

%if_with python3
%package -n python3-module-%oname
Summary: A generic test automation framework
Group: Development/Python3
%py3_provides %oname
%py3_provides robot
%add_python3_req_skip java javax java.lang org System UserDict

%description -n python3-module-%oname
Robot Framework is a generic test automation framework for acceptance
testing and acceptance test-driven development (ATDD). It has
easy-to-use tabular test data syntax and it utilizes the keyword-driven
testing approach. Its testing capabilities can be extended by test
libraries implemented either with Python or Java, and users can create
new higher-level keywords from existing ones using the same syntax that
is used for creating test cases.
%endif

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
%exclude %_bindir/*.py3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.2-alt1
- Updated to upstream version 3.0.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.9-alt1.dev20150202.1
- NMU: Use buildreq for BR.

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1.dev20150202
- Version 2.9.dev20150202
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.7-alt1.dev20141007
- Initial build for Sisyphus

