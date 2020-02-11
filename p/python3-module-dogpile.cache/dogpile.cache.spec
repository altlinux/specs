%define mname dogpile
%define oname %mname.cache

%def_without docs
%def_disable check

Name: python3-module-%oname
Version: 0.7.1
Release: alt2

Summary: A caching front-end based on the Dogpile lock
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/dogpile.cache/

# https://bitbucket.org/zzzeek/dogpile.cache.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage python3-module-nose
BuildRequires: python3-module-mock python3-module-mako
BuildRequires: python3-module-decorator python-tools-2to3

Provides: python3-module-dogpile-cache = %EVR
Obsoletes: python3-module-dogpile-cache < %EVR
Provides: python3-module-dogpile-core = %EVR
Obsoletes: python3-module-dogpile-core < %EVR

%py3_provides %oname
%py3_provides %mname.core


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

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/build/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%if_with docs
%make -C docs/build pickle
%make -C docs/build html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/build/output/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/output/html/*
%endif


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt2
- Build for python2 disabled.

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 0.7.1-alt1
- 0.7.1

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

