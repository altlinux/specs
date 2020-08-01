%define oname pamqp

%def_disable check

Name: python3-module-%oname
Version: 1.6.1
Release: alt2
Summary: RabbitMQ Focused AMQP low-level library
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pamqp/

# https://github.com/gmr/pamqp.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-pbr python3-module-unittest2
BuildRequires: pylint-py3 python3-tools-pep8
BuildRequires: python3-module-z4r-coveralls
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-sphinx

%py3_provides %oname

%description
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pamqp is a pure-python AMQP 0-9-1 frame encoder and decoder. The aim is
to create a client agnostic python encoder and decoder for general
purpose use.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

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
* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.1-alt1
- Updated to upstream version 1.6.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.git20141212.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.git20141212.1
- NMU: Use buildreq for BR.

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.git20141212
- Version 1.6.0

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.git20141105
- Version 1.5.0

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20140505
- Initial build for Sisyphus

