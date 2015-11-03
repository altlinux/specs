%define pypi_name os-brick

%def_with python3

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%pypi_name
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel
BuildRequires: python-module-eventlet >= 0.17.4
BuildRequires: python-module-oslo.concurrency >= 2.3.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.service >= 0.7.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-retrying >= 1.2.3
BuildRequires: python-module-six >= 1.9.0


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-eventlet >= 0.17.4
BuildRequires: python3-module-oslo.concurrency >= 2.3.0
BuildRequires: python3-module-oslo.log >= 1.8.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.service >= 0.7.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-retrying >= 1.2.3
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
OpenStack Cinder brick library for managing local volume attaches

%package doc
Summary: Documentation for OpenStack os-brick library
Group: Development/Documentation

%description doc
Documentation for OpenStack os-brick library

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Cinder brick library for managing local volume attaches
Group: Development/Python3

%description -n python3-module-%pypi_name
OpenStack Cinder brick library for managing local volume attaches

%endif

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%pypi_name/rootwrap.d
mv %buildroot/usr/etc/os-brick/rootwrap.d/*.filters %buildroot%_sysconfdir/%pypi_name/rootwrap.d/

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%python_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*

%files doc
%doc html README.rst

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%dir %_sysconfdir/%pypi_name
%dir %_sysconfdir/%pypi_name/rootwrap.d
%config(noreplace) %_sysconfdir/%pypi_name/rootwrap.d/*
%endif

%changelog
* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial packaging
