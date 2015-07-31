%define oname hitchselenium

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20150704
Summary: Plugin to run Selenium with firefox using the Hitch testing framework
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchselenium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchselenium.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hitch python-module-hitchserve
BuildPreReq: python-module-selenium
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitch python3-module-hitchserve
BuildPreReq: python3-module-selenium
%endif

%py_provides %oname
%py_requires hitch hitchserve selenium

%description
HitchSelenium is a plugin for the Hitch testing framework that wraps
selenium and starts firefox, optionally with XVFB.

%if_with python3
%package -n python3-module-%oname
Summary: Plugin to run Selenium with firefox using the Hitch testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires hitch hitchserve selenium

%description -n python3-module-%oname
HitchSelenium is a plugin for the Hitch testing framework that wraps
selenium and starts firefox, optionally with XVFB.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150704
- Initial build for Sisyphus

