%define _unpackaged_files_terminate_build 1
%define oname nosepipe

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt1.1
Summary: Plugin for the nose testing framework for running tests in a subprocess
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nosepipe/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dmccombs/nosepipe.git
Source0: https://pypi.python.org/packages/57/61/95306f40c9b61cfc06cef1c83e983db039298056cc3da50fcfad4a9baf37/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-django-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-django-nose
%endif

%py_provides %oname

%description
Plugin for the nose testing framework for running tests in a subprocess.

Use nosetests --with-process-isolation to enable the plugin. When
enabled, each test is run in a separate process.

%package -n python3-module-%oname
Summary: Plugin for the nose testing framework for running tests in a subprocess
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Plugin for the nose testing framework for running tests in a subprocess.

Use nosetests --with-process-isolation to enable the plugin. When
enabled, each test is run in a separate process.

%prep
%setup -q -n %{oname}-%{version}

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150720
- Version 0.7

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20150224
- Version 0.6

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20141114
- Initial build for Sisyphus

