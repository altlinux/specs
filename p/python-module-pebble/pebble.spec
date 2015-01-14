%define oname pebble

%def_with python3

Name: python-module-%oname
Version: 3.1.8
Release: alt1.git20140910
Summary: Threading and multiprocessing eye-candy
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/Pebble/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/noxdafox/pebble.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires multiprocessing

%description
Pebble provides a neat API to manage threads and processes within an
application.

%package -n python3-module-%oname
Summary: Threading and multiprocessing eye-candy
Group: Development/Python3
%py3_provides %oname
%py3_requires multiprocessing

%description -n python3-module-%oname
Pebble provides a neat API to manage threads and processes within an
application.

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
%doc *.txt doc/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt doc/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.8-alt1.git20140910
- Initial build for Sisyphus

