%define oname schematics-wtf

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.alpha.git20141211
Summary: Schematics Model to WTForm converter
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/schematics-wtf/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Garito/schematics-wtf.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-schematics python-module-wtforms
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-schematics python3-module-wtforms
%endif

%py_provides schematics_wtf
%py_requires schematics wtforms

%description
Convert Schematics Models to WTForms.

%package -n python3-module-%oname
Summary: Schematics Model to WTForm converter
Group: Development/Python3
%py3_provides schematics_wtf
%py3_requires schematics wtforms

%description -n python3-module-%oname
Convert Schematics Models to WTForms.

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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.alpha.git20141211
- Initial build for Sisyphus

