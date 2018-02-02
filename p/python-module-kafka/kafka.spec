%define oname kafka

%def_with python3

Name: python-module-%oname
Version: 1.3.3
Release: alt1.1
Summary: Pure Python client for Apache Kafka
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/kafka-python/

# https://github.com/mumrah/kafka-python.git
Source: %name-%version.tar
BuildArch: noarch


BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-tox python-module-mock 
BuildRequires: python-module-six python-module-snappy
BuildRequires: python-module-pytest python-module-mocker python-module-pytest-mock
BuildRequires: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildRequires: python-module-sphinxcontrib-napoleon
BuildRequires: python-modules-json
BuildRequires: python-module-lz4

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tox python3-module-mock
BuildRequires: python3-module-six python3-module-snappy
BuildRequires: python3-module-pytest python3-module-mocker
BuildRequires: python3-module-lz4
%endif

%py_provides %oname
%py_provides kafka.vendor.six.moves
%py_requires six gzip snappy json

%description
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Pure Python client for Apache Kafka
Group: Development/Python3
%py3_provides %oname
%py3_provides kafka.vendor.six.moves
%py3_requires six gzip snappy

%description -n python3-module-%oname
This module provides low-level protocol support for Apache Kafka as well
as high-level consumer and producer classes. Request batching is
supported by the protocol as well as broker-aware request routing. Gzip
and Snappy compression is also supported for message sets.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

#%check
#export PYTHONPATH=$PWD
#py.test
#%if_with python3
#pushd ../python3
#export PYTHONPATH=$PWD
#py.test-%_python3_version
#popd
#%endif

%files
%doc *.md example.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md example.py
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.dev.git20150219.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.dev.git20150219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.dev.git20150219.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.dev.git20150219
- Version 0.9.4-dev
- Added docs

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.dev.git20150102
- Initial build for Sisyphus

