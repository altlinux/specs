%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname gettext

%def_with python3

Name: python-module-%oname
Version: 3.0
Release: alt1.1
Summary: Python Gettext po to mo file compiler
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-gettext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hannosch/python-gettext.git
Source0: https://pypi.python.org/packages/80/a7/a4a5cf3aa9500dbb09b48dae6d4d9581883dd90ae7a84cbb2d3448410114/python-%{oname}-%{version}.zip
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-unittest2
%endif

%py_provides pythongettext

%description
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python Gettext po to mo file compiler
Group: Development/Python3
%py3_provides pythongettext

%description -n python3-module-%oname
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

This package contains tests for %oname.

%prep
%setup -q -n python-%{oname}-%{version}

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst PKG-INFO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt1.dev.git20130210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev.git20130210
- Initial build for Sisyphus

