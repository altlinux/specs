%define oname PythonPi

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20150227
Summary: Get the Value of Pi upto as many decimal places as needed
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PythonPi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/geekpradd/PythonPi.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pypandoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Get the Value of Pi upto n decimal digits using this Python Script. Uses
the chudnovsky algorithm implemented using the Python Decimal Data Type.

%package -n python3-module-%oname
Summary: Get the Value of Pi upto as many decimal places as needed
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Get the Value of Pi upto n decimal digits using this Python Script. Uses
the chudnovsky algorithm implemented using the Python Decimal Data Type.

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

python -c "import pypandoc; print pypandoc.convert('README.md','rst')" \
	>README.rst

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150227
- Initial build for Sisyphus

