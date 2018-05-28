%define _unpackaged_files_terminate_build 1

%define oname rubber

%def_with python3

Name: python-module-%oname
Version: 0.1.8
Release: alt3
Summary: Elasticsearch client with Django support
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/rubber

Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%description
rubber is a Python client for Elasticsearch.

Its main features are:
  - rubber is easy to use
  - rubber does not try to hide or wrap Elasticsearch syntax.
  - rubber integrates nicely with Django:
  - automatically saves your models to Elasticsearch
  - provides a Manager-style object on your django models
    for querying
  - rubber is unit-testing friendly: you don't need an elasticsearch
    instance to run your tests

%if_with python3
%package -n python3-module-%oname
Summary: Elasticsearch client with Django support
Group: Development/Python3

%description -n python3-module-%oname
rubber is a Python client for Elasticsearch.

Its main features are:
  - rubber is easy to use
  - rubber does not try to hide or wrap Elasticsearch syntax.
  - rubber integrates nicely with Django:
  - automatically saves your models to Elasticsearch
  - provides a Manager-style object on your django models
    for querying
  - rubber is unit-testing friendly: you don't need an elasticsearch
    instance to run your tests
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
rm -rf %buildroot%python_sitelibdir/tests

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/tests
popd
%endif

%files
%doc README.md
%python_sitelibdir/%{oname}*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/%{oname}*
%endif

%changelog
* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.8-alt3
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.8-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt2
- Added module for Python 3

* Tue Jun 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1
- Initial build for Sisyphus

