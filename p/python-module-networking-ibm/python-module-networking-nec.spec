%define sname networking-ibm

%def_without python3

Name: python-module-%sname
Version: 0.0.0
Release: alt0.post3
Summary: Openstack Neutron IBM Networking drivers
Group: Development/Python
License: ASL 2.0
Url: http://git.openstack.org/cgit/stackforge/%sname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-babel >= 1.3
%endif

%description
Openstack Neutron IBM Networking drivers

%if_with python3
%package -n python3-module-%sname
Summary: Openstack Neutron IBM Networking drivers
Group: Development/Python3

%description -n python3-module-%sname
Openstack Neutron IBM Networking drivers
%endif


%package doc
Summary: Documentation for Openstack ibm driver
Group: Development/Documentation

%description doc
Documentation for Openstack ibm drivers.

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info

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
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif


# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
%endif

%files
%doc README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.0.0-alt0.post3
- Initial release
