%define oname django-facebook-comments

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.hg20120729.1
Summary: Drop-in facebook comments for django
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-facebook-comments/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/sirpengi/django-facebook-comments
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django-facebook-comments is a reusable Django app to place facebook
comment boxes in your templates.

This app basically provides two templatetags to use in your templates,
one which just places in a facebook comment box, and one which caches
the facebook comment box (using their api) so that content will be in
the rendered html (some people like this for SEO purposes).

%package -n python3-module-%oname
Summary: Drop-in facebook comments for django
Group: Development/Python3

%description -n python3-module-%oname
django-facebook-comments is a reusable Django app to place facebook
comment boxes in your templates.

This app basically provides two templatetags to use in your templates,
one which just places in a facebook comment box, and one which caches
the facebook comment box (using their api) so that content will be in
the rendered html (some people like this for SEO purposes).

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

%files
%doc *.rst dfc_test_app
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst dfc_test_app
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.hg20120729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.hg20120729
- Initial build for Sisyphus

