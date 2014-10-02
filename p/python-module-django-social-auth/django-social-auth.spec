%define oname django-social-auth

%def_with python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.git20140208
Summary: Django social authentication made simple
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-social-auth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/omab/django-social-auth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Django Social Auth is an easy way to setup social
authentication/authorization mechanism for Django projects.

Crafted using base code from django-twitter-oauth and
django-openid-auth, it implements a common interface to define new
authentication providers from third parties.

%package -n python3-module-%oname
Summary: Django social authentication made simple
Group: Development/Python3

%description -n python3-module-%oname
Django Social Auth is an easy way to setup social
authentication/authorization mechanism for Django projects.

Crafted using base code from django-twitter-oauth and
django-openid-auth, it implements a common interface to define new
authentication providers from third parties.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Django Social Auth is an easy way to setup social
authentication/authorization mechanism for Django projects.

Crafted using base code from django-twitter-oauth and
django-openid-auth, it implements a common interface to define new
authentication providers from third parties.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Django Social Auth is an easy way to setup social
authentication/authorization mechanism for Django projects.

Crafted using base code from django-twitter-oauth and
django-openid-auth, it implements a common interface to define new
authentication providers from third parties.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc ChangeLog *.rst example
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20140208
- Initial build for Sisyphus

