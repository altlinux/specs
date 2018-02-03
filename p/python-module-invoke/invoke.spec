%define oname invoke

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.21.0
Release: alt1.1
Summary: Simple Python task execution
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/invoke/

# https://github.com/pyinvoke/invoke.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-reqs.patch
Patch2: %oname-%version-alt-docs.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-alabaster python-module-docutils python-module-flake8 python-module-html5lib
BuildRequires: python-module-objects.inv python-module-pbr python-module-pytest python-module-spec python-module-unittest2
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-yaml python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-flake8
BuildRequires: python3-module-html5lib python3-module-pbr python3-module-spec python3-module-unittest2
BuildRequires: python3-module-yaml python3-module-six
%endif

%py_provides %oname

%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%if_with python3
%package -n python3-module-%oname
Summary: Simple Python task execution
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

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

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx sites
ln -s ../objects.inv sites/docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

pushd sites/docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

cp -fR sites/docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
# TODO: around 16 tests are failing
PYTHONPATH=$(pwd) spec ||:
%if_with python3
pushd ../python3
python3 setup.py test
PYTHONPATH=$(pwd) spec.py3 ||:
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc sites/docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
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

