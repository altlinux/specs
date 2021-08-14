%define oname drf-compound-fields

%def_disable check

Name: python3-module-%oname
Version: 0.2.2
Release: alt3

Summary: Django-REST-framework serializer fields for compound types
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/drf-compound-fields/
# https://github.com/estebistec/drf-compound-fields.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-django
BuildRequires: python3-module-sphinx

%py3_provides drf_compound_fields


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

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Django-REST-framework serializer fields for compound types.
Django-REST-framework provides the ability to deal with multiple objects
using the many=True option on serializers. That allows for lists of
objects and for fields to be lists of objects.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt3
- drop unneeded BR: rpm-macros-sphinx

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.git20141012.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20141012.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20141012.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20141012
- Initial build for Sisyphus

