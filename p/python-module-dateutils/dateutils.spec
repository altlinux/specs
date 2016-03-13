%define oname dateutils

%def_with python3

Name: python-module-%oname
Version: 0.6.5
Release: alt1.git20150225.1
Summary: Various utilities for working with date and datetime objects
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dateutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jmcantrell/python-dateutils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-future python-module-dateutil
BuildPreReq: python-module-pytz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-future python3-module-dateutil
BuildPreReq: python3-module-pytz
%endif

%py_provides %oname
%py_requires future dateutil pytz

%description
The main purpose of this package is to provide more complex arithmetic
operations on dates/times. Heavy use is made of the relativedelta type
from Labix's dateutil library. Much of this package is just a light
wrapper on top of this with some added features such as range generation
and business day calculation.

%if_with python3
%package -n python3-module-%oname
Summary: Various utilities for working with date and datetime objects
Group: Development/Python3
%py3_provides %oname
%py3_requires future dateutil pytz

%description -n python3-module-%oname
The main purpose of this package is to provide more complex arithmetic
operations on dates/times. Heavy use is made of the relativedelta type
from Labix's dateutil library. Much of this package is just a light
wrapper on top of this with some added features such as range generation
and business day calculation.
%endif

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

%check
python setup.py test
py.test -vv %oname/*.py
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv %oname/*.py
popd
%endif

%files
%doc *.mkd
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.mkd
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.5-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20150225
- Initial build for Sisyphus

