%define oname convertdate

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0.3.1
Release: alt2.git20141125.1.1
Summary: Utils for converting between date formats and calculating holidays
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/convertdate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fitnr/convertdate.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ephem python-module-pytz
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ephem python3-module-pytz
%endif

%py_provides %oname
%py_requires ephem pytz

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%package -n python3-module-%oname
Summary: Utils for converting between date formats and calculating holidays
Group: Development/Python3
%py3_provides %oname
%py3_requires ephem pytz

%description -n python3-module-%oname
Converts between Gregorian dates and other calendar systems. Calendars
included: Baha'i, French Republican, Hebrew, Indian Civil, Islamic,
Julian, Mayan and Persian.

%prep
%setup

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
py.test tests/*.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version tests/*.py
popd
%endif

%files
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.3.1-alt2.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.3.1-alt2.git20141125.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.3.1-alt2.git20141125
- Rebuild with "def_disable check"

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3.1-alt1.git20141125
- Initial build for Sisyphus

