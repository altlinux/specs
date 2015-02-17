%define oname pyramid_aiorest

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20150215
Summary: A lib to build a rest api using the Pyramid framework and asyncio
License: Repoze Public License
Group: Development/Python
Url: https://github.com/mardiros/pyramid_aiorest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardiros/pyramid_aiorest.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-colander
BuildPreReq: python-module-pyramid_asyncio python-module-pyramid
BuildPreReq: python-module-pyramid_yards
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-colander
BuildPreReq: python3-module-pyramid_asyncio python3-module-pyramid
BuildPreReq: python3-module-pyramid_yards
%endif

%py_provides %oname
%py_requires asyncio colander pyramid_asyncio pyramid pyramid_yards

%description
A lib to build a rest api using the Pyramid framework and asyncio.

%package -n python3-module-%oname
Summary: A lib to build a rest api using the Pyramid framework and asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio colander pyramid_asyncio pyramid pyramid_yards

%description -n python3-module-%oname
A lib to build a rest api using the Pyramid framework and asyncio.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst COPYRIGHT LICENSE
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst COPYRIGHT LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150215
- Initial build for Sisyphus

