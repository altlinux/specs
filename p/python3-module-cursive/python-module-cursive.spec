%global modname cursive

Name: python3-module-%modname
Version: 0.2.2
Release: alt2
Summary: Cursive implements OpenStack-specific validation of digital signatures

Group: Development/Python3
License: ASL 2.0
Url: http://www.openstack.org/
Source: %modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-castellan >= 0.4.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.17.0
BuildRequires: python3-module-reno >= 2.5.0

%description
Cursive implements OpenStack-specific validation of digital signatures.

As OpenStack continues to mature, robust security controls become increasingly critical.
The cursive project contains code extracted from various OpenStack projects for verifying digital signatures.
Additional capabilities will be added to this project in support of various security features.

%package tests
Summary: Tests for %modname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %modname.

%prep
%setup -n %modname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt
# Remove bundled egg info
rm -rf *.egg-info


#%%prepare_sphinx3 doc
#ln -s ../objects.inv doc/source/

%build
%python3_build

%install
%python3_install

#export PYTHONPATH=$PWD
#%%make -C doc html

%files
%doc AUTHORS  README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sun Oct 27 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt2
- Build without python2.

* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.2.2-alt1
- 0.2.2
- add tests packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial build
