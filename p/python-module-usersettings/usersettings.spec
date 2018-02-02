%define oname usersettings

%def_without python3

Name: python-module-%oname
Version: 1.0.7
Release: alt2.git20130531.1
Summary: Portable Local Settings Storage
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/usersettings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/glvnst/usersettings.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-appdirs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-appdirs
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires appdirs

%description
"usersettings" is a python module for easily managing persistent
settings using an editable format and stored in an OS-appropriate
location (windows/os x/linux are supported).

%if_with python3
%package -n python3-module-%oname
Summary: Portable Local Settings Storage
Group: Development/Python3
%py3_provides %oname
%py3_requires appdirs

%description -n python3-module-%oname
"usersettings" is a python module for easily managing persistent
settings using an editable format and stored in an OS-appropriate
location (windows/os x/linux are supported).
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
export PYTHONPATH=$PWD
python examples/usersettings-example.py
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
python3 examples/usersettings-example.py
popd
%endif

%files
%doc *.md docs/* examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/* examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2.git20130531.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2.git20130531
- Fixed build

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.git20130531
- Initial build for Sisyphus

