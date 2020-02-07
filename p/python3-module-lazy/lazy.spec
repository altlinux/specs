%define oname lazy

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: Lazy attributes for Python objects
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/lazy/
BuildArch: noarch

# https://github.com/stefanholek/lazy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20140420.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20140420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140420
- Initial build for Sisyphus

