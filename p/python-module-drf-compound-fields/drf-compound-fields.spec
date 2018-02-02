%define oname drf-compound-fields

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20141012.1.1.1
Summary: Django-REST-framework serializer fields for compound types
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/drf-compound-fields/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/estebistec/drf-compound-fields.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-django-tests python-module-djangorestframework
#BuildPreReq: python-module-coverage
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-django-tests python3-module-djangorestframework
#BuildPreReq: python3-module-coverage
%endif

%py_provides drf_compound_fields

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytest python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-psycopg2 python3-module-pytest python3-module-setuptools python3-module-yaml
BuildRequires: python-module-alabaster python-module-coverage python-module-django python-module-docutils python-module-html5lib python-module-objects.inv python-module-setuptools python3-module-coverage python3-module-django python3-module-setuptools rpm-build-python3 time

%description
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package expands on that and provides fields allowing:

* Lists of simple (non-object) types, described by other serializer
  fields.
* Fields that allow values to be a list or individual item of some type.
* Dictionaries of simple and object types.
* Partial dictionaries which include keys specified in a list.

%package -n python3-module-%oname
Summary: Django-REST-framework serializer fields for compound types
Group: Development/Python3
%py3_provides drf_compound_fields

%description -n python3-module-%oname
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package expands on that and provides fields allowing:

* Lists of simple (non-object) types, described by other serializer
  fields.
* Fields that allow values to be a list or individual item of some type.
* Dictionaries of simple and object types.
* Partial dictionaries which include keys specified in a list.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Python
BuildArch: noarch

%description docs
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains documentation for %oname.

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

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.git20141012.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20141012.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20141012.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141012
- Initial build for Sisyphus

