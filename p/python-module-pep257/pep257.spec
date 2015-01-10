%define oname pep257

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150109
Summary: Python docstring style checker
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pep257/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/GreenSteam/pep257.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

%package -n python3-module-%oname
Summary: Python docstring style checker
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pep257 is a static analysis tool for checking compliance with Python PEP
257.

The framework for checking docstring style is flexible, and custom
checks can be easily added, for example to cover NumPy docstring
conventions.

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
export LC_ALL=en_US.UTF-8
py.test -vv
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150109
- Initial build for Sisyphus

