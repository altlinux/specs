%define sname networking-cisco

%def_without python3

Name: python-module-%sname
Version: 2015.1.0
Release: alt1
Summary: Networking Cisco contains the Cisco vendor code for Openstack Neutron
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
Networking Cisco contains the Cisco vendor code for Openstack Neutron.

%if_with python3
%package -n python3-module-%sname
Summary: Networking Cisco contains the Cisco vendor code for Openstack Neutron
Group: Development/Python3

%description -n python3-module-%sname
Networking Cisco contains the Cisco vendor code for Openstack Neutron.
%endif


%package doc
Summary: Documentation for Openstack cisco driver
Group: Development/Documentation

%description doc
Documentation for Openstack cisco drivers.

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

mkdir -p %buildroot%_sysconfdir/neutron/plugins/ml2
mkdir -p %buildroot%_sysconfdir/neutron/plugins/cisco
#mkdir -p %buildroot%_sysconfdir/neutron/rootwrap.d
mv %buildroot/usr/etc/neutron/ml2_* %buildroot%_sysconfdir/neutron/plugins/ml2/
mv %buildroot/usr/etc/neutron/cisco_* %buildroot%_sysconfdir/neutron/plugins/cisco/
#mv %buildroot/usr/etc/neutron/rootwrap.d/* %buildroot%_sysconfdir/neutron/rootwrap.d/

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
%endif

%files
%doc README.rst
#%_bindir/*
#%config(noreplace) %_sysconfdir/neutron/plugins/ml2/*
#%config(noreplace) %_sysconfdir/neutron/plugins/cisco/*
#%config(noreplace) %_sysconfdir/neutron/rootwrap.d/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Fri May 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.0-alt1
- 2015.1.0

* Fri Apr 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt2
- don't package config

* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial release
