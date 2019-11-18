%define oname universal-analytics-python

Name: python3-module-%oname
Version: 0.2.4
Release: alt2

Summary: Universal Analytics Python Module
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/universal-analytics-python/
# https://github.com/analytics-pros/universal-analytics-python.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-to-python3.patch

BuildRequires(pre): rpm-build-python3

%py3_provides UniversalAnalytics


%description
This library provides a Python interface to Google Analytics, supporting
the Universal Analytics Measurement Protocol, with an interface modeled
(loosely) after Google's analytics.js.

%prep
%setup
%patch0 -p1

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

echo %version > commit-version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
sed -i 's|python|python3|' Makefile

%files
%doc *.rst *.md
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt2
- python2 disabled
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.git20141205.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20141205.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141205
- Initial build for Sisyphus

