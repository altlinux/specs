%define oname contexts

Name: python3-module-%oname
Version: 0.10.1
Release: alt2

Summary: Descriptive testing for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Contexts/
BuildArch: noarch

# https://github.com/benjamin-hodgson/Contexts.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires colorama


%description
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Dead simple descriptive testing for Python. No custom decorators, no
context managers, no '.feature' files, no fuss.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

%build
%python3_build_debug

%install
%python3_install

%make -C doc pickle
%make -C doc html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.md RELEASING
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.10.1-alt2
- remove python2 support

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1.git20141112.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.git20141112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.git20141112.1
- NMU: Use buildreq for BR.

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20141112
- Initial build for Sisyphus

