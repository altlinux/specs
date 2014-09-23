%define oname emencia-django-socialaggregator

%def_with python3

Name: python-module-%oname
Version: 0.2.8
Release: alt1
Summary: Django app for aggregate some feeds from social networks
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/emencia-django-socialaggregator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-c++ python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
emencia-django-social-aggregator

This app is an aggregator of social network.

A command script will recover data from social network/external site
from Aggregator info that you specified into admin. It will stock them
into database, like Ressource and you could manage them into admin. You
could regroup Ressource by Feed and return them into JSON or HTML view.

%package -n python3-module-%oname
Summary: Django app for aggregate some feeds from social networks
Group: Development/Python3

%description -n python3-module-%oname
emencia-django-social-aggregator

This app is an aggregator of social network.

A command script will recover data from social network/external site
from Aggregator info that you specified into admin. It will stock them
into database, like Ressource and you could manage them into admin. You
could regroup Ressource by Feed and return them into JSON or HTML view.

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
%doc *.txt *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus

