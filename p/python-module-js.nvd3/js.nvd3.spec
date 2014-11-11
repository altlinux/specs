%define oname js.nvd3

%def_with python3

Name: python-module-%oname
Version: 1.1.15
Release: alt1.beta
Summary: Fanstatic packaging of NVD3
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.nvd3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-js.d3 python-module-fanstatic
BuildPreReq: python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-js.d3 python3-module-fanstatic
BuildPreReq: python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js js.d3

%description
This library packages NVD3 for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of NVD3
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.d3

%description -n python3-module-%oname
This library packages NVD3 for fanstatic.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.15-alt1.beta
- Initial build for Sisyphus

