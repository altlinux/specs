%define oname chai

Name: python3-module-%oname
Version: 1.1.2
Release: alt2
Summary: Easy to use mocking, stubbing and spying framework
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/chai

# https://github.com/agoragames/chai.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%add_findreq_skiplist %python3_sitelibdir/%oname/python2.py

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-pytest python3-module-sphinx

%description
Chai provides a very easy to use api for mocking, stubbing and spying
your python objects, patterned after the Mocha library for Ruby.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Chai provides a very easy to use api for mocking, stubbing and spying
your python objects, patterned after the Mocha library for Ruby.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Chai provides a very easy to use api for mocking, stubbing and spying
your python objects, patterned after the Mocha library for Ruby.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc CHANGELOG *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt2
- Drop python2 support.

* Wed Jan 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.git20141014.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20141014.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.git20141014.1
- NMU: Use buildreq for BR.

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141014
- Initial build for Sisyphus

