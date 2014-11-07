%define oname tmdb3

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20140128
Summary: TheMovieDB.org APIv3 interface
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tmdb3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wagnerrp/pytmdb3.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python-tools-2to3
%endif

%py_provides %oname

%description
This Python module implements the v3 API for TheMovieDb.org, allowing
access to movie and cast information, as well as related artwork.

%package -n python3-module-%oname
Summary: TheMovieDB.org APIv3 interface
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This Python module implements the v3 API for TheMovieDb.org, allowing
access to movie and cast information, as well as related artwork.

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
%doc LICENSE README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140128
- Initial build for Sisyphus

