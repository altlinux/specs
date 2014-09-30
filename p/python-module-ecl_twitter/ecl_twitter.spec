%define oname ecl_twitter

%def_without python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20120607
Summary: Easy Twitter integration for Django
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ecl_twitter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/elmcitylabs/ECL-Twitter.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-django
%endif

%description
ECL Twitter is an awesome Twitter library for Python 2.7+. It makes the
Twitter API a joy to use, and Django integration is baked in. To find
out more, read on!

%package -n python3-module-%oname
Summary: Easy Twitter integration for Django
Group: Development/Python3

%description -n python3-module-%oname
ECL Twitter is an awesome Twitter library for Python 2.7+. It makes the
Twitter API a joy to use, and Django integration is baked in. To find
out more, read on!

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ECL Twitter is an awesome Twitter library for Python 2.7+. It makes the
Twitter API a joy to use, and Django integration is baked in. To find
out more, read on!

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export DJANGO_SETTINGS_MODULE="project_name.settings"

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export DJANGO_SETTINGS_MODULE="project_name.settings"

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
%doc *.rst docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20120607
- Initial build for Sisyphus

