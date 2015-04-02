%define sname vmware-nsx


%def_without python3

Name: python-module-%sname
Version: 0.0.1
Release: alt1.post183
Summary: VMware NSX library for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://git.openstack.org/cgit/stackforge/%sname
Source: %name-%version.tar

%py_provides vmware_nsx

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-six >= 1.7.0
BuildRequires: python-module-oslo.concurrency >= 0.3.0
BuildRequires: python-module-oslo.config >= 1.6.0
BuildRequires: python-module-oslo.db >= 1.3.0
BuildRequires: python-module-oslo.serialization >= 1.2.0
BuildRequires: python-module-oslo.utils >= 1.2.0
BuildRequires: python-module-oslo.vmware >= 0.9.0
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-eventlet >= 0.15.2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-babel >= 1.3
%endif

%description
VMware NSX library for OpenStack projects

%if_with python3
%package -n python3-module-%sname
Summary: VMware NSX library for OpenStack projects
Group: Development/Python3

%py3_provides vmware_nsx

%description -n python3-module-%sname
VMware NSX library for OpenStack projects
%endif


%package doc
Summary: Documentation for Openstack vmware-nsx driver
Group: Development/Documentation

%description doc
Documentation for Openstack vmware-nsx drivers.

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
rm -fr %buildroot%python_sitelibdir/*/*/tests
%if_with python3
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/*/tests
%endif

%files
%doc README.rst
%_bindir/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Apr 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1.post183
- Initial release
