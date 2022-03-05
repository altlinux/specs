%define _unpackaged_files_terminate_build 1
%define oname isodate

%def_with check

Name: python3-module-%oname
Version: 0.6.1
Release: alt1
Summary: An ISO 8601 date/time/duration parser and formater
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/isodate/

Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
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

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# override upstream's tox config
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    python -m unittest discover -v src
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/*/tests

%changelog
* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 0.6.1-alt1
- 0.6.0 -> 0.6.1.

* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.4 -> 0.6.0.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt2
- Drop python2 support.

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

