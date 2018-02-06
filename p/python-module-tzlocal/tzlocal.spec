%define _unpackaged_files_terminate_build 1
%define oname tzlocal

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.1
Summary: tzinfo object for the local timezone
License: CC0 1.0 Universal
Group: Development/Python
Url: https://pypi.python.org/pypi/tzlocal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/regebro/tzlocal.git
Source0: https://pypi.python.org/packages/d3/64/e4b18738496213f82b88b31c431a0e4ece143801fb6771dddd1c2bf0101b/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytz
%endif

%py_provides %oname

%description
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This module attempts to fix a glaring hole in pytz, that there is no way
to get the local timezone information, unless you know the zoneinfo
name, and under several Linux distros that's hard or impossible to
figure out.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: tzinfo object for the local timezone
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This module attempts to fix a glaring hole in pytz, that there is no way
to get the local timezone information, unless you know the zoneinfo
name, and under several Linux distros that's hard or impossible to
figure out.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
sed -i 's|@PYVER@|%_python3_version|' ../python3/tzlocal/unix.py
%endif

sed -i 's|@PYVER@|%_python_version|' tzlocal/unix.py

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2.dev0.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2.dev0.git20141018
- tzlocal.unix: added path to localtime in pytz

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141018
- Initial build for Sisyphus

