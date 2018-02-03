%define mname dogpile
%define oname %mname.cache

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.2
Release: alt1.1
Summary: A caching front-end based on the Dogpile lock
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dogpile.cache/

# https://bitbucket.org/zzzeek/dogpile.cache.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-coverage
BuildRequires: python-module-nose python-module-mock
BuildRequires: python-module-mako
BuildRequires: python-module-sphinx-devel python-module-changelog
BuildRequires: python-module-sphinx-paramlinks
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-mako
%endif

Provides: python-module-dogpile-cache = %EVR
Obsoletes: python-module-dogpile-cache < %EVR
Provides: python-module-dogpile-core = %EVR
Obsoletes: python-module-dogpile-core < %EVR

%py_provides %oname
%py_provides %mname.core

BuildRequires(pre): rpm-macros-sphinx

%description
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

dogpile.cache builds on the dogpile.core locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract. Overall, dogpile.cache is intended as a replacement to the
Beaker caching system, the internals of which are written by the same
author. All the ideas of Beaker which "work" are re-implemented in
dogpile.cache in a more efficient and succinct manner, and all the cruft
(Beaker's internals were first written in 2005) relegated to the trash
heap.

%package -n python3-module-%oname
Summary: A caching front-end based on the Dogpile lock
Group: Development/Python3
Provides: python3-module-dogpile-cache = %EVR
Obsoletes: python3-module-dogpile-cache < %EVR
Provides: python3-module-dogpile-core = %EVR
Obsoletes: python3-module-dogpile-core < %EVR
%py3_provides %oname
%py3_provides %mname.core

%description -n python3-module-%oname
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

dogpile.cache builds on the dogpile.core locking system, which
implements the idea of "allow one creator to write while others read" in
the abstract. Overall, dogpile.cache is intended as a replacement to the
Beaker caching system, the internals of which are written by the same
author. All the ideas of Beaker which "work" are re-implemented in
dogpile.cache in a more efficient and succinct manner, and all the cruft
(Beaker's internals were first written in 2005) relegated to the trash
heap.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A caching API built around the concept of a "dogpile lock", which allows
continued access to an expiring data value while a single thread
generates a new value.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/build/

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs/build pickle
%make -C docs/build html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/output/pickle %buildroot%python_sitelibdir/%oname/

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
%doc docs/build/output/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- 0.6.2
- The dogpile.core package has been rolled into dogpile.cache directly

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.7-alt1.1
- (AUTO) subst_x86_64.

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.6-alt2.git20150202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.6-alt2.git20150202.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt2.git20150202
- Provides: python-module-dogpile-cache

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.6-alt1.git20150202
- Initial build for Sisyphus

