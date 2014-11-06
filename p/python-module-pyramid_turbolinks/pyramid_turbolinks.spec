%define oname pyramid_turbolinks

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20141104
Summary: Turbolinks for Pyramid
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_turbolinks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/pyramid_turbolinks.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid
%endif

%py_provides %oname

%description
Turbolinks makes following links in your web application faster. For
more information, visit the original rails repo: turbolinks.js.

%package -n python3-module-%oname
Summary: Turbolinks for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Turbolinks makes following links in your web application faster. For
more information, visit the original rails repo: turbolinks.js.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
pushd src
%python_build_debug
popd

%if_with python3
pushd ../python3/src
%python3_build_debug
popd
%endif

%install
pushd src
%python_install
popd

%if_with python3
pushd ../python3/src
%python3_install
popd
%endif

%check
pushd src
python setup.py test
popd
%if_with python3
pushd ../python3/src
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141104
- Initial build for Sisyphus

