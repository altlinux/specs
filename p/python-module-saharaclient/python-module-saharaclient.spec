%define oname saharaclient
%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Python API and CLI for OpenStack  Sahara

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneauth1 >= 2.18.0
BuildRequires: python-module-osc-lib >= 1.2.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-openstackclient >= 3.3.0
BuildRequires: python-module-requests >= 2.10.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneauth1 >= 2.18.0
BuildRequires: python3-module-osc-lib >= 1.2.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-openstackclient >= 3.3.0
BuildRequires: python3-module-requests >= 2.10.0
%endif

%description
This is a client for the OpenStack Sahara API. There's a Python API (the
saharaclient module), and a command-line script (sahara). Each implements
100 percent of the OpenStack Sahara API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python API and CLI for OpenStack Sahara
Group: Development/Python3

%description -n python3-module-%oname
This is a client for the OpenStack Sahara API. There's a Python API (the
saharaclient module), and a command-line script (sahara). Each implements
100 percent of the OpenStack Sahara API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Sahara API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Sahara API. There's a Python API (the
saharaclient module), and a command-line script (sahara). Each implements
100 percent of the OpenStack Sahara API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

rm -rf *.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

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

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

%files
%doc README.rst
%doc LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.1-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- Initial release for Sisyphus

