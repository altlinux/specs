%define oname pyga

Name: python3-module-%oname
Version: 2.5.0
Release: alt2

Summary: Server side implemenation of Google Analytics in Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyga/
BuildArch: noarch

# https://github.com/kra3/py-ga-mob.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx
BuildRequires: python3-module-html5lib python3-module-pbr
BuildRequires: python3-module-pytest python3-module-unittest2
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

This package contains documentation for %oname.

%prep
%setup

## py2 -> py3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build_debug

%install
%python3_install

%make -C doc pickle
mkdir -p build/docs
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.rst RELEASES
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.git20140809.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.git20140809.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.git20140809.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20140809
- Initial build for Sisyphus

