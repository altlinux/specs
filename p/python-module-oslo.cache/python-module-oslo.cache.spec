%define pypi_name oslo.cache

%def_with python3

Name: python-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: Cache storage for Openstack projects

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/oslo
Source: %name-%version.tar
BuildArch:      noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-dogpile.cache >= 0.5.4
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.utils >= 2.0.0


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-dogpile.cache >= 0.5.4
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.log >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
%endif

%description
Cache storage for Openstack projects.

%if_with python3
%package -n python3-module-%pypi_name
Summary: Cache storage for Openstack projects.
Group: Development/Python3

%description -n python3-module-%pypi_name
Cache storage for Openstack projects.
%endif

%package doc
Summary: Documentation for Cache storage for Openstack projects
Group: Development/Documentation

%description doc
Documentation for Cache storage for Openstack projects.


%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc html
%doc README.rst LICENSE

%changelog
* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT
