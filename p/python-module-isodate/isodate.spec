%define oname isodate

%def_with python3

Name: python-module-%oname
Version: 0.4.8
Release: alt1
Summary: An ISO 8601 date/time/duration parser and formater
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/isodate
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not
intended by this module to support 2 digit years. (while it may still be
valid as ISO date, because it is not explicitly forbidden.) Another
example is, when no time zone information is given for a time, then it
should be interpreted as local time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types,
like date, time, datetime and timedelta, it is not possible to convert
all possible ISO 8601 dates/times. For instance, dates before 0001-01-01
are not allowed by the Python date and datetime classes. Additionally
fractional seconds are limited to microseconds. That means if the parser
finds for instance nanoseconds it will round it to microseconds.

%if_with python3
%package -n python3-module-%oname
Summary: An ISO 8601 date/time/duration parser and formater (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

For instance, ISO8601:2004 never mentions 2 digit years. So, it is not
intended by this module to support 2 digit years. (while it may still be
valid as ISO date, because it is not explicitly forbidden.) Another
example is, when no time zone information is given for a time, then it
should be interpreted as local time, and not UTC.

As this module maps ISO 8601 dates/times to standard Python data types,
like date, time, datetime and timedelta, it is not possible to convert
all possible ISO 8601 dates/times. For instance, dates before 0001-01-01
are not allowed by the Python date and datetime classes. Additionally
fractional seconds are limited to microseconds. That means if the parser
finds for instance nanoseconds it will round it to microseconds.

%package -n python3-module-%oname-tests
Summary: Tests for isodate (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

This package contains tests for isodate.
%endif

%package tests
Summary: Tests for isodate
Group: Development/Python
Requires: %name = %version-%release

%description tests
This module implements ISO 8601 date, time and duration parsing. The
implementation follows ISO8601:2004 standard, and implements only
date/time representations mentioned in the standard. If something is not
mentioned there, then it is treated as non existent, and not as an
allowed option.

This package contains tests for isodate.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus

