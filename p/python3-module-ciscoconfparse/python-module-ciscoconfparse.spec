%define oname ciscoconfparse

Name:       python3-module-%oname
Version:    1.2.37
Release:    alt2

Summary:    Library for parses through Cisco IOS-style configurations
License:    GPLv3
Group:      Development/Python3
URL:        http://github.com/mpenning/%oname

BuildArch:  noarch

Source:     %name-%version.tar
Patch0:     ciscoconfparse-1.2.37-setuptools_hg-alt.patch

BuildRequires(pre): rpm-build-python3


%description
ciscoconfparse is a Python library, which parses through Cisco IOS-style (and other vendor) configurations.
It can:
* Audit existing router / switch / firewall / wlc configurations
* Retrieve portions of the configuration
* Modify existing configurations
* Build new configurations

%prep
%setup
%patch0 -p2

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

%build
%python3_build

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/version_info

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/*test*
rm -fr %buildroot%python3_sitelibdir/*/*test*

%files
%python3_sitelibdir/*
# skip Flask:
%exclude %python3_sitelibdir/%oname/ccp_flask.py*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.37-alt2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.37-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.37-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.37-alt1
- 1.2.37

* Mon Mar 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.14-alt1
- Initial release for Sisyphus

