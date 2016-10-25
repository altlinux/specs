%define sname openstackclient
%def_with python3

Name: python-module-%sname
Version: 3.2.0
Release: alt1
Summary: OpenStack Command-line Client

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-openstackclient
Source: %name-%version.tar

BuildArch: noarch


Requires: python-module-cliff >= 1.15.0
Requires: python-module-keystoneauth1 >= 2.10.0
Requires: python-module-openstacksdk >= 0.9.4
Requires: python-module-osc-lib >= 1.0.2
Requires: python-module-oslo.i18n >= 2.1.0
Requires: python-module-oslo.utils >= 3.16.0
Requires: python-module-glanceclient >= 2.3.0
Requires: python-module-keystoneclient >= 2.0.0
Requires: python-module-novaclient >= 2.29.0
Requires: python-module-cinderclient >= 1.6.0

Requires: python-module-neutronclient >= 2.6.0
Requires: python-module-requests >= 2.10.0
Requires: python-module-stevedore >= 1.16.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-cliff >= 1.15.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-openstacksdk >= 0.9.4
BuildRequires: python-module-osc-lib >= 1.0.2
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.16.0

BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-glanceclient >= 2.3.0
BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-novaclient >= 2.29.0
BuildRequires: python-module-cinderclient >= 1.6.0
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-stevedore >= 1.16.0

# for build doc
BuildRequires: python-module-mock
BuildRequires: python-module-requests-mock
BuildRequires: python-module-fixtures
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno
BuildRequires: python-module-osprofiler >= 1.4.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-cliff-tablib >= 1.0
BuildRequires: python3-module-os-client-config >= 1.4.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-glanceclient >= 0.18.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-novaclient >= 2.28.1
BuildRequires: python3-module-cinderclient >= 1.3.1
BuildRequires: python3-module-neutronclient >= 2.6.0
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-stevedore >= 1.5.0
%endif

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package doc
Summary: Documentation for OpenStack Client
Group: Development/Documentation

%description doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

This package contains auto-generated documentation.

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack Command-line Client
Group: Development/Python3

%description -n python3-module-%sname
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.
%endif


%prep
%setup

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info

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
mv %buildroot%_bindir/openstack %buildroot%_bindir/python3-openstack
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/openstack.1 %buildroot%_mandir/man1/openstack.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/openstack
%python_sitelibdir/*
%_man1dir/openstack.1*

%files doc
%doc html

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-openstack
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1
- add python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package

