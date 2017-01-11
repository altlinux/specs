%define _unpackaged_files_terminate_build 1
%define oname isodate

%def_with python3

Name: python-module-%oname
Version: 0.5.4
Release: alt1
Summary: An ISO 8601 date/time/duration parser and formater
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/isodate
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/f4/5b/fe03d46ced80639b7be9285492dc8ce069b841c0cebe5baacdd9b090b164/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
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
%setup -q -n %{oname}-%{version}
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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1
- Version 0.4.9

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.4.8-alt1.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus

