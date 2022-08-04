%define _unpackaged_files_terminate_build 1
%define oname elasticsearch

%def_disable check

Name: python3-module-%oname
Version: 5.1.0
Release: alt3
Summary: Python client for Elasticsearch
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/elastic/elasticsearch-py

# https://github.com/elasticsearch/elasticsearch-py.git
Source0: https://pypi.python.org/packages/2a/0a/fca7faa8155a1b6fcd3ce86a351640a2593b1ac8ee461f908a190b06e284/%{oname}-%{version}.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires json

BuildRequires(pre): rpm-macros-sphinx3 python3-module-sphinx python3-module-sphinx_rtd_theme
BuildRequires: python3-module-chardet python3-module-coverage python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-urllib3

%description
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Official low-level client for Elasticsearch. Its goal is to provide
common ground for all Elasticsearch-related code in Python; because of
this it tries to be opinion-free and very extendable.

This package contains documentation for %oname.

%prep
%setup -n %{oname}-%{version}

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc AUTHORS *.rst *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt3
- Fixed BuildRequires.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.0-alt1
- automated PyPI update

* Mon May  9 2016 Terechkov Evgenii <evg@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.0-alt1.dev.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.0-alt1.dev.git20150226.1
- NMU: Use buildreq for BR.

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev.git20150226
- New snapshot

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.dev.git20150211
- Version 1.5.0-dev

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141231
- Version 1.3.0

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2.git20141022
- Tuned requirements

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.git20141022
- Initial build for Sisyphus

