%define oname pyramid_debugtoolbar_dogpile

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141105
Summary: dogpile support for pyramid_debugtoolbar
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_debugtoolbar_dogpile
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jvanasco/pyramid_debugtoolbar_dogpile.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-nose
BuildPreReq: python-module-pyramid_debugtoolbar python-module-Pygments
BuildPreReq: python-module-pyramid_mako python-module-mako
BuildPreReq: python-module-markupsafe python-module-dogpile-core
BuildPreReq: python-module-dogpile-cache
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-nose
BuildPreReq: python3-module-pyramid_debugtoolbar python3-module-Pygments
BuildPreReq: python3-module-pyramid_mako python3-module-mako
BuildPreReq: python3-module-markupsafe python3-module-dogpile-core
BuildPreReq: python3-module-dogpile-cache python-tools-2to3
%endif

%py_provides %oname
%py_requires dogpile.cache.api
# for tests:
#py_requires pyramid.testing

%description
dogpile caching support for pyramid_debugtoolbar.

%package -n python3-module-%oname
Summary: dogpile support for pyramid_debugtoolbar
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
dogpile caching support for pyramid_debugtoolbar.

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
nosetests
%if_with python3
pushd ../python3
nosetests3
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141105
- Initial build for Sisyphus

