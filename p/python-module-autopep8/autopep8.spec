%define oname autopep8

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.a0.git20141118
Summary: Automatically formats Python code to conform to the PEP 8 style guide
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/autopep8/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hhatto/autopep8.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-coverage python-tools-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-coverage python3-tools-pep8
%endif

%py_provides %oname

%description
autopep8 automatically formats Python code to conform to the PEP 8 style
guide. It uses the pep8 utility to determine what parts of the code
needs to be formatted. autopep8 is capable of fixing most of the
formatting issues that can be reported by pep8.

%package -n python3-module-%oname
Summary: Automatically formats Python code to conform to the PEP 8 style guide
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
autopep8 automatically formats Python code to conform to the PEP 8 style
guide. It uses the pep8 utility to determine what parts of the code
needs to be formatted. autopep8 is capable of fixing most of the
formatting issues that can be reported by pep8.

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
python setup.py test
%make test
%if_with python3
pushd ../python3
python3 setup.py test
%make test PYTHON=python3 PEP8=python3-pep8
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
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.a0.git20141118
- Initial build for Sisyphus

