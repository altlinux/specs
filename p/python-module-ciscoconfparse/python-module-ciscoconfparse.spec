%define oname ciscoconfparse
%def_with python3

Name:       python-module-%oname
Version:    1.2.37
Release:    alt1.1
Summary:    Library for parses through Cisco IOS-style configurations
License:    GPLv3
URL:       http://github.com/mpenning/%oname
Source:    %name-%version.tar
Patch0:    ciscoconfparse-1.2.37-setuptools_hg-alt.patch
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
Requires: python-module-ipaddr

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

%description
ciscoconfparse is a Python library, which parses through Cisco IOS-style (and other vendor) configurations.
It can:
* Audit existing router / switch / firewall / wlc configurations
* Retrieve portions of the configuration
* Modify existing configurations
* Build new configurations

%if_with python3
%package -n python3-module-%oname
Summary: Library for parses through Cisco IOS-style configurations
Group: Development/Python3

%description -n python3-module-%oname
ciscoconfparse is a Python library, which parses through Cisco IOS-style (and other vendor) configurations.
It can:
* Audit existing router / switch / firewall / wlc configurations
* Retrieve portions of the configuration
* Modify existing configurations
* Build new configurations
%endif

%prep
%setup
%patch0 -p2

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

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/version_info
popd
%endif

%python_install
rm -rf %buildroot%python_sitelibdir/version_info

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/*test*
rm -fr %buildroot%python3_sitelibdir/*/*test*

%files
%doc LICENSE README.rst TODO CHANGES
%python_sitelibdir/*
# skip Flask:
%exclude %python_sitelibdir/%oname/ccp_flask.py*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
# skip Flask:
%exclude %python3_sitelibdir/%oname/ccp_flask.py*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.37-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.37-alt1
- 1.2.37

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.14-alt1
- Initial release for Sisyphus

