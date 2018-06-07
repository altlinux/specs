%define _unpackaged_files_terminate_build 1

%define oname zodburi

%def_with python3

Name:           python-module-%oname
Version:        2.3.0
Release:        alt1
Summary:        Construct ZODB storage instances from URIs.
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/zodburi
BuildArch:      noarch

# https://github.com/Pylons/zodburi.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(ZODB) python2.7(ZConfig) python2.7(ZEO)
BuildRequires: python2.7(nose) python2.7(coverage) python2.7(mock)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(ZODB) python3(ZConfig) python3(ZEO)
BuildRequires: python3(nose) python3(coverage) python3(mock)
%endif

%description
A library which parses URIs and converts them to ZODB storage objects and database arguments.

See the documentation at http://docs.pylonsproject.org/projects/zodburi/en/latest/ for more information.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library which parses URIs and converts them to ZODB storage objects and database arguments.

See the documentation at http://docs.pylonsproject.org/projects/zodburi/en/latest/ for more information.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Construct ZODB storage instances from URIs.

%description -n python3-module-%oname
A library which parses URIs and converts them to ZODB storage objects and database arguments.

See the documentation at http://docs.pylonsproject.org/projects/zodburi/en/latest/ for more information.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A library which parses URIs and converts them to ZODB storage objects and database arguments.

See the documentation at http://docs.pylonsproject.org/projects/zodburi/en/latest/ for more information.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

python setup.py test

%files
%doc README.rst LICENSE.txt
%python_sitelibdir/%oname/
%python_sitelibdir/%{oname}-%{version}*.egg-info
%exclude %python_sitelibdir/%oname/tests

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}-%{version}*.egg-info
%exclude %python3_sitelibdir/%oname/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.0-alt1
- Updated to upstream version 2.3.0.

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.2-alt1
- Initial build for ALT.
