%define oname keystoneauth1

Name: python-module-%oname
Version: 3.10.0
Release: alt1
Summary: OpenStack authenticating tools
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-positional >= 1.1.1
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-os-service-types >= 1.2.0
BuildRequires: python-module-requests-kerberos >= 0.8.0
BuildRequires: python-module-lxml >= 3.4.1
BuildRequires: python-module-oauthlib >= 0.6.2
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-mock >= 2.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslotest >= 3.2.0
BuildRequires: python-module-betamax >= 0.7.0
BuildRequires: python-module-pycrypto >= 2.6
BuildRequires: python-module-requests-mock >= 1.1
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-tools-pep8

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-positional >= 1.1.1
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-requests-kerberos >= 0.8.0
BuildRequires: python3-module-lxml >= 2.4.1
BuildRequires: python3-module-oauthlib >= 0.6.2
BuildRequires: python3-module-fixtures >= 3.0.0

%add_python_req_skip betamax
%add_python3_req_skip betamax

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack authenticating tools
Group: Development/Python3

%description -n python3-module-%oname
OpenStack authenticating tools.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack authenticating tools
Group: Development/Documentation

%description doc
Documentation for OpenStack authenticating tools.

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

# generate html docs
#python setup.py build_sphinx
# remove the sphinx-build leftovers
#rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc AUTHORS ChangeLog README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

#%files doc
#%doc doc/build/html

%changelog
* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.18.0-alt1
- 2.18.0
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- Initial package.
