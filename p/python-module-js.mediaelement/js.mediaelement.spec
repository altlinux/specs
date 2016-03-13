%define mname js
%define oname %mname.mediaelement

%def_with python3

Name: python-module-%oname
Version: 2.13.1
Release: alt1.1
Summary: Fanstatic packaging of MediaElement.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.mediaelement/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-js.jquery
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-js.jquery
%endif

%py_provides %oname
%py_requires %mname fanstatic js.jquery

%description
This library packages MediaElement.js for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.mediaelement) are published to some URL.

%package -n python3-module-%oname
Summary: Fanstatic packaging of MediaElement.js
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname fanstatic js.jquery

%description -n python3-module-%oname
This library packages MediaElement.js for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.mediaelement) are published to some URL.

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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus

