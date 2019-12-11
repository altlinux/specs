%define oname datarray

%def_disable check

Name: python3-module-%oname
Version: 0.1.0
Release: alt1

Summary: NumPy arrays with named axes and named indices
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/datarray/
BuildArch: noarch

# https://github.com/fperez/datarray.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy-testing python3-module-sphinx
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires numpy matplotlib


%description
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Scientists, engineers, mathematicians and statisticians don't just work
with matrices; they often work with structured data, just like you'd
find in a table. However, functionality for this is missing from Numpy,
and there are efforts to create something to fill the void. This is one
of those efforts.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-apidoc|sphinx-apidoc-3|' doc/Makefile
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/test*

%files tests
%python3_sitelibdir/*/test*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*


%changelog
* Wed Dec 11 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.0-alt1
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.7-alt1.git20111119.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.git20111119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.7-alt1.git20111119.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20111119
- Initial build for Sisyphus

