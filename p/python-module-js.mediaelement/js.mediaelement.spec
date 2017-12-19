%define mname js
%define oname %mname.mediaelement

%def_with python3

Name: python-module-%oname
Version: 2.13.1
Release: alt2
Summary: Fanstatic packaging of MediaElement.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.mediaelement/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-fanstatic python-module-js.jquery
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-fanstatic python3-module-js.jquery
%endif

%py_provides %oname
%py_requires %mname fanstatic js.jquery

%description
This library packages MediaElement.js for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.mediaelement) are published to some URL.

%if_with python3
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
%endif

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

%if "%_lib" == "lib64"
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
py.test3 -vv
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%endif

%changelog
* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.1-alt2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13.1-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus

