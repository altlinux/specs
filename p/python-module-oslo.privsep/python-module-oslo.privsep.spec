%define oname oslo.privsep

%def_with python3

Name: python-module-%oname
Version: 1.16.0
Release: alt1.1
Summary: OpenStack library for privilege separation
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-eventlet >= 0.18.3
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-msgpack >= 0.4.0
BuildRequires: python-module-enum34
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-cffi
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-eventlet >= 0.18.3
BuildRequires: python3-module-greenlet >= 0.3.2
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-cffi
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
This library helps applications perform actions which require more or less privileges
than they were started with in a safe, easy to code and easy to use manner.
For more information on why this is generally a good idea please read over
the principle of least privilege and the specification which created this library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack library for privilege separation
Group: Development/Python3

%description -n python3-module-%oname
This library helps applications perform actions which require more or less privileges
than they were started with in a safe, easy to code and easy to use manner.
For more information on why this is generally a good idea please read over
the principle of least privilege and the specification which created this library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%package doc
Summary: Oslo service documentation
Group: Development/Documentation

%description doc
Documentation for %oname


%prep
%setup -n %oname-%version
# Remove bundled egg-info
rm -rf %oname.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/privsep-helper %buildroot%_bindir/python3-privsep-helper
popd
%endif
%python_install

%files
%doc README.rst
%python_sitelibdir/*
%_bindir/privsep-helper
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%_bindir/python3-privsep-helper
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.13.1-alt1
- 1.13.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.13.0-alt1
- Initial package.
