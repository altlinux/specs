%define oname rpyc

%def_disable check

Name: python3-module-%oname
Version: 4.1.2
Release: alt1

Summary: Remote Python Call (RPyC), a transparent and symmetric RPC library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/rpyc/
BuildArch: noarch

# https://github.com/tomerfiliba/rpyc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinx

%py3_provides %oname


%description
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
RPyC (pronounced like are-pie-see), or Remote Python Call, is a
transparent library for symmetrical remote procedure calls, clustering,
and distributed-computing. RPyC makes use of object-proxying, a
technique that employs python's dynamic nature, to overcome the physical
boundaries between processes and computers, so that remote objects can
be manipulated as if they were local.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
%__python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html demos


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.1.2-alt1
- python2 disabled

* Mon May 06 2019 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.3.0-alt1.git20141023.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.git20141023.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.3.0-alt1.git20141023.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.git20141023
- Initial build for Sisyphus

