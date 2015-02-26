%define oname pylabs_pyramid_scaffolds

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Provides some pyramid scaffold templates with useful default settings
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pylabs_pyramid_scaffolds/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%add_findreq_skiplist %python_sitelibdir/pylabs_pyramid_scaffolds/scaffolds/*/*.py_tmpl

%description
This package provides some pyramid scaffold templates with useful
default settings.

%package -n python3-module-%oname
Summary: Provides some pyramid scaffold templates with useful default settings
Group: Development/Python3
%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/pylabs_pyramid_scaffolds/scaffolds/*/*.py_tmpl

%description -n python3-module-%oname
This package provides some pyramid scaffold templates with useful
default settings.

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
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1
- Version 0.0.6

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

