%define oname js.momentjs

%def_with python3

Name: python-module-%oname
Version: 2.8.3
Release: alt1
Summary: Fanstatic packaging of Moment.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.momentjs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-shutilwhich
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-shutilwhich
%endif

%py_provides %oname
%py_requires js

%description
This library packages Moment.js for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of Moment.js
Group: Development/Python3
%py3_provides %oname
%py3_requires js

%description -n python3-module-%oname
This library packages Moment.js for fanstatic.

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
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
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
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus

