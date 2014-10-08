%define oname velruse

%def_with python3

Name: python-module-%oname
Version: 1.1.1
Release: alt1
Summary: Simplifying third-party authentication for web applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/velruse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-pyramid-tests
BuildPreReq: python-module-zope.deprecation python-module-anykeystore
BuildPreReq: python-module-zope.component python-module-requests
BuildPreReq: python-module-openid python-module-requests-oauthlib
BuildPreReq: python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Velruse is a set of authentication routines that provide a unified way
to have a website user authenticate to a variety of different identity
providers and/or a variety of different authentication schemes.

It is similar in some ways to RPXnow with the exception of being
open-source, locally installable, and easily pluggable for custom
identity providers and authentication schemes.

You can run Velruse as a stand-alone service for use with your websites
regardless of the language they're written in. While Velruse itself is
written in Python, since it can interact with your website purely via
HTTP POST's.

%package -n python3-module-%oname
Summary: Simplifying third-party authentication for web applications
Group: Development/Python3

%description -n python3-module-%oname
Velruse is a set of authentication routines that provide a unified way
to have a website user authenticate to a variety of different identity
providers and/or a variety of different authentication schemes.

It is similar in some ways to RPXnow with the exception of being
open-source, locally installable, and easily pluggable for custom
identity providers and authentication schemes.

You can run Velruse as a stand-alone service for use with your websites
regardless of the language they're written in. While Velruse itself is
written in Python, since it can interact with your website purely via
HTTP POST's.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Velruse is a set of authentication routines that provide a unified way
to have a website user authenticate to a variety of different identity
providers and/or a variety of different authentication schemes.

It is similar in some ways to RPXnow with the exception of being
open-source, locally installable, and easily pluggable for custom
identity providers and authentication schemes.

You can run Velruse as a stand-alone service for use with your websites
regardless of the language they're written in. While Velruse itself is
written in Python, since it can interact with your website purely via
HTTP POST's.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Velruse is a set of authentication routines that provide a unified way
to have a website user authenticate to a variety of different identity
providers and/or a variety of different authentication schemes.

It is similar in some ways to RPXnow with the exception of being
open-source, locally installable, and easily pluggable for custom
identity providers and authentication schemes.

You can run Velruse as a stand-alone service for use with your websites
regardless of the language they're written in. While Velruse itself is
written in Python, since it can interact with your website purely via
HTTP POST's.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus

