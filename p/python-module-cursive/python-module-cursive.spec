%global modname cursive

%def_with python3

Name: python-module-%modname
Version: 0.1.1
Release: alt1
Summary: Cursive implements OpenStack-specific validation of digital signatures

Group: Development/Python
License: ASL 2.0
Url: http://www.openstack.org/
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-netifaces >= 0.10.4
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-castellan >= 0.4.0

BuildPreReq: python-module-sphinx-devel python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-lxml >= 2.3
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-netifaces >= 0.10.4
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-castellan >= 0.4.0
%endif

%description
Cursive implements OpenStack-specific validation of digital signatures.

As OpenStack continues to mature, robust security controls become increasingly critical.
The cursive project contains code extracted from various OpenStack projects for verifying digital signatures.
Additional capabilities will be added to this project in support of various security features.

%package -n python3-module-%modname
Summary: Cursive implements OpenStack-specific validation of digital signatures
Group: Development/Python3

%description -n python3-module-%modname
Cursive implements OpenStack-specific validation of digital signatures.

As OpenStack continues to mature, robust security controls become increasingly critical.
The cursive project contains code extracted from various OpenStack projects for verifying digital signatures.
Additional capabilities will be added to this project in support of various security features.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt
# Remove bundled egg info
rm -rf *.egg-info

%if_with python3
cp -fR . ../python3
%endif

#%prepare_sphinx doc
#ln -s ../objects.inv doc/source/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

#export PYTHONPATH=$PWD
#%make -C doc html

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc AUTHORS  README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modname
%doc AUTHORS  README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial build
