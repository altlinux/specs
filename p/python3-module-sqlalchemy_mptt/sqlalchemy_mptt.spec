%define oname sqlalchemy_mptt
%def_without pickles
%def_without docs

Name: python3-module-%oname
Version: 0.2.5
Release: alt2

Summary: SQLAlchemy MPTT mixins (Nested Sets)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlalchemy_mptt/
BuildArch: noarch

# https://github.com/ITCase/sqlalchemy_mptt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-SQLAlchemy
%if_with docs
BuildRequires: python3-module-sphinx
%endif
BuildRequires: python3-module-nose python3-module-coverage python3-module-flake8

%py3_provides %oname
%py3_requires sqlite3


%description
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Library for implementing Modified Preorder Tree Traversal with your
SQLAlchemy Models and working with trees of Model instances, like
django-mptt.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8

%python3_install

%if_with docs
%make -C docs html
%endif
%if_with pickles
%make -C docs pickle
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%if_with pickles
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle
%endif

%if_with docs
%files docs
%doc docs/_build/html/*
%endif


%changelog
* Tue Apr 27 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt2
- build without docs and pickles (due obsoleted sphinx.ext.mathbase require)

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt1
- Version updated to 0.2.5
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt1.dev1.git20150722.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.7-alt1.dev1.git20150722.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1.dev1.git20150722.1
- NMU: Use buildreq for BR.

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.dev1.git20150722
- Version 0.1.7.dev1

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141118
- Version 0.1.0

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20141031
- Initial build for Sisyphus

