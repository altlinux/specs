%define oname yamlsettings

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150210.1.1
Summary: Yaml Settings Configuration Module
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/yamlsettings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KyleJamesWalker/yamlsettings.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-yaml python-module-nose
BuildPreReq: python-module-mock python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-yaml python3-module-nose
BuildPreReq: python3-module-mock
%endif

%py_provides %oname
%py_requires yaml

%description
A library to help manage project settings, without having to worry about
accidentally checking non-public information, like api keys. Along with
simple environment variable support.

%package -n python3-module-%oname
Summary: Yaml Settings Configuration Module
Group: Development/Python3
%py3_provides %oname
%py3_requires yaml

%description -n python3-module-%oname
A library to help manage project settings, without having to worry about
accidentally checking non-public information, like api keys. Along with
simple environment variable support.

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150210.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150210
- Initial build for Sisyphus

