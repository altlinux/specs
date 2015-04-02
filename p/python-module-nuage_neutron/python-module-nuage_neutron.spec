%define sname nuage_neutron

%def_without python3

Name: python-module-%sname
Version: 0.0.0
Release: alt1.post4
Summary: Openstack Neutron Plugin for Nuage Networks
Group: Development/Python
License: ASL 2.0
Url: https://github.com/nuage-networks/nuage-openstack-neutron
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
Openstack Neutron Plugin for Nuage Networks

%if_with python3
%package -n python3-module-%sname
Summary: Openstack Neutron Plugin for Nuage Networks
Group: Development/Python3

%description -n python3-module-%sname
Openstack Neutron Plugin for Nuage Networks
%endif


%package doc
Summary: Documentation for Openstack nuage driver
Group: Development/Documentation

%description doc
Documentation for Openstack nuage drivers.

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
rm -fr %buildroot%python_sitelibdir/*/test*
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/test*
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
* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.0.0-alt1.post4
- Initial release
