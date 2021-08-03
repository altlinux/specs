%define oname robotframework

Name: python3-module-%oname
Version: 3.0.2
Release: alt2
Summary: A generic test automation framework
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/robotframework/

# https://github.com/robotframework/robotframework.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_provides robot
%add_python3_req_skip java javax java.lang org System UserDict
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/libraries/dialogs_ipy.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/libraries/dialogs_jy.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/running/timeouts/ironpython.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/running/timeouts/jython.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/htmldata/jartemplate.py
%add_findreq_skiplist /usr/lib*/python*/site-packages/robot/jarrunner.py

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
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

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/*

%files docs
%doc doc/*

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt2
- Drop python2 support.

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

