%global modname cursive

Name: python-module-%modname
Version: 0.2.2
Release: alt1
Summary: Cursive implements OpenStack-specific validation of digital signatures

Group: Development/Python
License: ASL 2.0
Url: http://www.openstack.org/
Source: %modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-castellan >= 0.4.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.17.0
BuildRequires: python-module-reno >= 2.5.0

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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %modname.

%package -n python3-module-%modname
Summary: Cursive implements OpenStack-specific validation of digital signatures
Group: Development/Python3

%description -n python3-module-%modname
Cursive implements OpenStack-specific validation of digital signatures.

As OpenStack continues to mature, robust security controls become increasingly critical.
The cursive project contains code extracted from various OpenStack projects for verifying digital signatures.
Additional capabilities will be added to this project in support of various security features.


%package -n python3-module-%modname-tests
Summary: Tests for %modname
Group: Development/Python3
Requires: python3-module-%modname = %EVR

%description -n python3-module-%modname-tests
This package contains tests for %modname.

%prep
%setup -n %modname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt
# Remove bundled egg info
rm -rf *.egg-info

cp -fR . ../python3

#%prepare_sphinx doc
#ln -s ../objects.inv doc/source/

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

#export PYTHONPATH=$PWD
#%make -C doc html

%files
%doc AUTHORS  README.rst LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%modname
%doc AUTHORS  README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%modname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.2.2-alt1
- 0.2.2
- add tests packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial build
