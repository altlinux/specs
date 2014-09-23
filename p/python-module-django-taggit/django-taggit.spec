%define oname django-taggit

%def_with python3

Name: python-module-%oname
Version: 0.12.2
Release: alt1.git20140921
Summary: Simple tagging for django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-taggit
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/alex/django-taggit.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
django-taggit is a reusable Django application for simple tagging.

%package -n python3-module-%oname
Summary: Simple tagging for django
Group: Development/Python3

%description -n python3-module-%oname
django-taggit is a reusable Django application for simple tagging.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%make -C docs html

%files
%doc AUTHORS *.txt* *.rst docs/_build/html
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.txt* *.rst docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140921
- Initial build for Sisyphus

