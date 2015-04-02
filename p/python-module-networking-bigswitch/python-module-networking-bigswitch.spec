%define sname networking-bigswitch

%def_without python3

Name: python-module-%sname
Version: 2015.1.26
Release: alt1
Summary: Big Switch Networks Plugins for OpenStack Networking
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
BuildRequires: python-module-oslo.log >= 0.4.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
%endif

%description
This library contains the components required to integrate an
OpenStack deployment with a Big Switch Networks fabric.

%if_with python3
%package -n python3-module-%sname
Summary: Big Switch Networks Plugins for OpenStack Networking
Group: Development/Python3

%description -n python3-module-%sname
This library contains the components required to integrate an
OpenStack deployment with a Big Switch Networks fabric.
%endif


%package doc
Summary: Documentation for Openstack bigswitch driver
Group: Development/Documentation

%description doc
Documentation for Openstack bigswitch drivers.

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
mkdir -p %buildroot%_sysconfdir/neutron/plugins/bigswitch

mv %buildroot/usr/etc/neutron/plugins/ml2/* %buildroot%_sysconfdir/neutron/plugins/ml2/
mv %buildroot/usr/etc/neutron/plugins/bigswitch/* %buildroot%_sysconfdir/neutron/plugins/bigswitch/

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/test*
rm -fr %buildroot%python_sitelibdir/*/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/test*
rm -fr %buildroot%python3_sitelibdir/*/*/tests
%endif

%files
%doc README.rst
%_bindir/*
%config(noreplace) %_sysconfdir/neutron/plugins/ml2/*
%config(noreplace) %_sysconfdir/neutron/plugins/bigswitch/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2015.1.26-alt1
- Initial release
