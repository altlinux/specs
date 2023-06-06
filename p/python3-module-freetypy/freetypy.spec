%define oname freetypy

%def_disable check
%def_without docs

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Fast and modern Python wrappers for freetype, written in Python/C API 
License: BSD
Group: Development/Python3
Url: https://github.com/matplotlib/freetypy

# https://github.com/matplotlib/freetypy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libfreetype-devel
%if_with docs
BuildRequires: python3-module-sphinx python3-module-numpydoc
%endif

%py3_provides %oname


%description
Fast and modern Python wrappers for freetype, written in Python/C API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains documentation for %oname.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
%endif

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v --processes=-1 freetypy.tests

%files
%doc *.md examples
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with odcs
%files docs
%doc doc/build/html/*
%files pickles
%python3_sitelibdir/*/pickle
%endif


%changelog
* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.git20150408.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20150408.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20150408.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150408
- Initial build for Sisyphus

