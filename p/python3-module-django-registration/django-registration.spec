%define oname django-registration

%def_with bootstrap

Name: python3-module-%oname
Version: 3.0.1
Release: alt1

Summary: An extensible user-registration application for Django
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-registration/
BuildArch: noarch

# hg clone https://bitbucket.org/ubernostrum/django-registration
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme


%description
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3
%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults
%add_python3_req_skip django.utils.hashcompat
%add_python3_req_skip django.views.generic.simple
%endif

%description pickles
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

mv tests/ %buildroot%python3_sitelibdir/%oname

%files
%doc README.rst AUTHORS LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.0.1-alt1
- version updated to 3.0.1
- build for python2 disabled

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.hg20130617.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.hg20130617.1
- NMU: Use buildreq for BR.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20130617
- Initial build for Sisyphus

