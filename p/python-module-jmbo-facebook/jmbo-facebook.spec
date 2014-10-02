%define oname jmbo-facebook

%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20130514
Summary: Fetch facebook page updates
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-memcached python-module-django-celery

%description
Fetch facebook page updates.

%package -n python3-module-%oname
Summary: Fetch facebook page updates
Group: Development/Python3
Requires: python3-module-memcached python3-module-django-celery

%description -n python3-module-%oname
Fetch facebook page updates.

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

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20130514
- Initial build for Sisyphus

