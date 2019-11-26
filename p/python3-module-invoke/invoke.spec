%define oname invoke

%def_disable check

Name: python3-module-%oname
Version: 0.21.0
Release: alt2

Summary: Simple Python task execution
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/invoke/
# https://github.com/pyinvoke/invoke.git
BuildArch: noarch

Source: %name-%version.tar
Patch1: %oname-%version-alt-reqs.patch
Patch2: %oname-%version-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8
BuildRequires: python3-module-html5lib python3-module-pbr
BuildRequires: python3-module-spec python3-module-unittest2
BuildRequires: python3-module-yaml python3-module-six

%py3_provides %oname


%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

# remove some vendored stuff
rm -rf invoke/vendor/yaml{2,3}
rm -rf invoke/vendor/six.*

sed -i \
	-e 's|from \.vendor import yaml3 as yaml # noqa|import yaml # noqa|g' \
	-e 's|from \.vendor import yaml2 as yaml # noqa|import yaml # noqa|g' \
	-e 's|from \.vendor import six|import six|g' \
	-e 's|from \.vendor\.six\.moves import reduce # noqa|from six.moves import reduce # noqa|g' \
	invoke/util.py

find . -name '*.py' | xargs sed -i \
	-e 's|from invoke\.vendor\.six import |from six import |g'

%build
%python3_build_debug

%install
%python3_install

pushd sites/docs
sphinx-build-3 -b pickle -d build/doctrees . build/pickle
sphinx-build-3 -b html -d build/doctrees . build/html
popd

cp -fR sites/docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test
PYTHONPATH=$(pwd) spec.py3 ||:

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc sites/docs/build/html/*


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.21.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt1
- Updated to upstream version 0.21.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt2.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.1-alt2.git20150730
- cleanup buildreq

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150730
- Version 0.10.1

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20141113
- Initial build for Sisyphus

