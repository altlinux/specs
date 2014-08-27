%define modulename icalendar

Name: python3-module-%modulename
Version: 3.8.3
Release: alt1
Summary: iCalendar parser/generator
License: GPLv2.1
Group: Development/Python3
BuildArch: noarch
Source: %modulename-%version.tar.gz
Url: http://pypi.python.org/pypi/icalendar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-jinja2-tests

%description
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

%package tests
Summary: Tests for %modulename
Group: Development/Python3
Requires: %name = %EVR

%description tests
iCalendar is a parser/generator of iCalendar files
(RFC 2445) for use with Python.

This package contains tests for %modulename.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/%modulename
%exclude %python3_sitelibdir/%modulename/tests
%python3_sitelibdir/%modulename-*

%files tests
%python3_sitelibdir/%modulename/tests

%changelog
* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Initial build for Sisyphus

