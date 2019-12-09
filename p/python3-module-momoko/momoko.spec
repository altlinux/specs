%define _unpackaged_files_terminate_build 1
%define oname momoko

%def_disable check

Name: python3-module-%oname
Version: 2.2.5.1
Release: alt2

Summary: Wraps (asynchronous) Psycopg2 for Tornado
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Momoko
BuildArch: noarch

# https://github.com/FSX/momoko.git
Source0: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-cffi python3-module-psycopg2
BuildRequires: python3-module-pycares python3-module-pytest
BuildRequires: python3-module-unittest2 python3-module-zope
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires tornado psycopg2cffi psycopg2


%description
Momoko wraps Psycopg2's functionality for use in Tornado.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Momoko wraps Psycopg2's functionality for use in Tornado.

This package contains pickles for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python3_build_debug

%install
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export MOMOKO_PSYCOPG2_IMPL=psycopg2cffi
python3 setup.py test -v

%files
%doc *.rst THANKS examples docs/_build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.5.1-alt2
- python2 disabled

* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.5.1-alt1
- Build new version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.git20150803.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.git20150803.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150803
- Initial build for Sisyphus

