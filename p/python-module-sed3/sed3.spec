%define oname sed3

%def_with python3

Name: python-module-%oname
Version: 1.1.10
Release: alt1
Summary: 3D viewer and editor of color seeds
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sed3
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mjirik/sed3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
BuildPreReq: python-module-matplotlib-qt4 python-module-yaml
BuildPreReq: python-module-scipy python-module-nose
BuildPreReq: python-module-mock python-module-PyQt4
BuildPreReq: python-module-pytz python-module-pygobject3
BuildPreReq: python-module-pycairo python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-matplotlib-qt4 python3-module-yaml
BuildPreReq: python3-module-scipy python3-module-nose
BuildPreReq: python3-module-mock python3-module-PyQt4
BuildPreReq: python3-module-pytz python3-module-pygobject3
BuildPreReq: python3-module-pycairo python3-module-coverage
%endif

%py_provides %oname
%py_requires matplotlib yaml scipy PyQt4
%py_requires matplotlib.backends.backend_qt4agg

%description
3D viewer and editor of color seeds.

%if_with python3
%package -n python3-module-%oname
Summary: 3D viewer and editor of color seeds
Group: Development/Python3
%py3_provides %oname
%py3_requires matplotlib yaml scipy PyQt4
%py3_requires matplotlib.backends.backend_qt4agg

%description -n python3-module-%oname
3D viewer and editor of color seeds.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test -v
xvfb-run nosetests -vv --with-coverage --cover-package=%oname
%if_with python3
pushd ../python3
python3 setup.py test -v
xvfb-run nosetests3 -vv --with-coverage --cover-package=%oname
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
* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.10-alt1
- Initial build for Sisyphus

