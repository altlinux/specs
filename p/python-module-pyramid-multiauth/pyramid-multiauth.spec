%define oname pyramid-multiauth

%def_with python3

Name:           python-module-%oname
Version:        0.9.0
Release:        alt1
Summary:        Stacked authentication policies for pyramid
Group:          Development/Python
License:        MPL-2.0
URL:            https://pypi.python.org/pypi/pyramid_multiauth
BuildArch:      noarch

# https://github.com/mozilla-services/pyramid_multiauth.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools python2.7(pyramid)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(pyramid)
%endif

%description
An authentication policy for Pyramid that proxies to a stack of other authentication policies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
An authentication policy for Pyramid that proxies to a stack of other authentication policies.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Stacked authentication policies for pyramid

%description -n python3-module-%oname
An authentication policy for Pyramid that proxies to a stack of other authentication policies.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
An authentication policy for Pyramid that proxies to a stack of other authentication policies.

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
%doc README.rst LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.py*

%files tests
%python_sitelibdir/*/tests.py*

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.py*
%exclude %python3_sitelibdir/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.py*
%exclude %python3_sitelibdir/*/*/tests*
%endif

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Initial build for ALT.
