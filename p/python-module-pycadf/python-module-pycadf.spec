%global pypi_name pycadf

%def_with python3

Name: python-module-%pypi_name
Version: 1.1.0
Release: alt1
Summary: DMTF Cloud Audit (CADF) data model

Group: Development/Python
License: ASL 2.0
URL: https://launchpad.net/pycadf
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-sphinx >= 1.1.2
BuildRequires: python-module-oslosphinx >= 2.5.0
BuildRequires: python-module-oslo.config >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-pytz
BuildRequires: python-module-six >= 1.9.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx >= 1.1.2
BuildRequires: python3-module-oslosphinx >= 2.5.0
BuildRequires: python3-module-oslo.config >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-pytz
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
DMTF Cloud Audit (CADF) data model

%if_with python3
%package -n python3-module-%pypi_name
Summary: DMTF Cloud Audit (CADF) data model
Group: Development/Python3

%description -n python3-module-%pypi_name
DMTF Cloud Audit (CADF) data model
%endif

%package doc
Summary: Documentation for DMTF Cloud Audit (CADF) data model
Group: Development/Documentation

%description doc
Documentation for the DMTF Cloud Audit (CADF) data model.

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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
mkdir -p %buildroot%_sysconfdir
mv %buildroot/usr/etc/%pypi_name %buildroot%_sysconfdir
rm -rf %buildroot/%python_sitelibdir/%pypi_name/tests
rm -rf %buildroot/%python3_sitelibdir/%pypi_name/tests

%files
%doc README.rst LICENSE
%dir %_sysconfdir/%pypi_name
%config(noreplace) %_sysconfdir/%pypi_name/*.conf
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add python3 module

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-1.fc21.src)

