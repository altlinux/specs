%define _unpackaged_files_terminate_build 1
%define oname sphinxtesters

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt2
Summary: Utilities for testing Sphinx extensions
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sphinxtesters

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(docutils) python2.7(nose.tools) python2.7(sphinx.application)
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(docutils) python3(nose.tools) python3(sphinx.application)
BuildRequires: python3-module-pytest
%endif

%description
Sphinxtesters - utilities for testing Sphinx extensions.

%package tests
Summary: Utilities for testing Sphinx extensions
Group: Development/Python

%description tests
Sphinxtesters - utilities for testing Sphinx extensions.

This package contains tests.

%if_with python3
%package -n python3-module-%oname
Summary: Utilities for testing Sphinx extensions
Group: Development/Python3

%description -n python3-module-%oname
Sphinxtesters - utilities for testing Sphinx extensions.

%package -n python3-module-%oname-tests
Summary: Utilities for testing Sphinx extensions
Group: Development/Python3

%description -n python3-module-%oname-tests
Sphinxtesters - utilities for testing Sphinx extensions.

This package contains tests.
%endif

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test -vv

%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2
- Updated build dependencies.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt1
- Initial build for ALT.
