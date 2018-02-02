%define mname routes
%define oname pybald-%mname

%def_with python3

Name: python-module-%oname
Version: 2.11
Release: alt2.git20140308.1.1
Summary: Routing Recognition and Generation Tools
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pybald-routes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mikepk/routes.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-repoze.lru python-module-nose
BuildPreReq: python-module-webtest python-module-webob
BuildPreReq: python-module-coverage
BuildPreReq: python-modules-logging python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-repoze.lru python3-module-nose
BuildPreReq: python3-module-webtest python3-module-webob
BuildPreReq: python3-module-coverage
%endif

%py_provides %mname %oname
Conflicts: python-module-%mname < %EVR
Conflicts: python-module-%mname > %EVR
%py_requires logging repoze.lru webob

%description
This is a fork of Ben Bangert's Routes project that includes some custom
behaviors that are used by the pybald project. The main difference is
that submappers don't automatically concatenate all keyword arguments
together in submappers and only the 'prefix' style arguments are
generative. All other arguments are allowed to be overridden in
submappers (controllers, actions, etc...).

%package -n python3-module-%oname
Summary: Routing Recognition and Generation Tools
Group: Development/Python3
%py3_provides %mname %oname
Conflicts: python3-module-%mname < %EVR
Conflicts: python3-module-%mname > %EVR
%py3_requires logging repoze.lru webob

%description -n python3-module-%oname
This is a fork of Ben Bangert's Routes project that includes some custom
behaviors that are used by the pybald project. The main difference is
that submappers don't automatically concatenate all keyword arguments
together in submappers and only the 'prefix' style arguments are
generative. All other arguments are allowed to be overridden in
submappers (controllers, actions, etc...).

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This is a fork of Ben Bangert's Routes project that includes some custom
behaviors that are used by the pybald project. The main difference is
that submappers don't automatically concatenate all keyword arguments
together in submappers and only the 'prefix' style arguments are
generative. All other arguments are allowed to be overridden in
submappers (controllers, actions, etc...).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a fork of Ben Bangert's Routes project that includes some custom
behaviors that are used by the pybald project. The main difference is
that submappers don't automatically concatenate all keyword arguments
together in submappers and only the 'prefix' style arguments are
generative. All other arguments are allowed to be overridden in
submappers (controllers, actions, etc...).

This package contains documentation for %oname.

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

install -d %buildroot%python_sitelibdir/%oname

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst TODO
%python_sitelibdir/*



%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.11-alt2.git20140308.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.11-alt2.git20140308.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 2.11-alt2.git20140308
- Disabled Docs

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.11-alt1.git20140308
- Version 2.11

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140307
- Initial build for Sisyphus

