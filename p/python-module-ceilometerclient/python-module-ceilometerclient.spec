%def_with python3

Name: python-module-ceilometerclient
Version: 1.5.0
Release: alt1
Summary: Python API and CLI for OpenStack Ceilometer

Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%name
Source: %name-%version.tar


BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-stevedore >= 1.5.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-stevedore >= 1.5.0
%endif


%description
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

%if_with python3
%package -n python3-module-ceilometerclient
Summary:  Python API and CLI for OpenStack Ceilometer
Group: Development/Python3

%description -n python3-module-ceilometerclient
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).
%endif

%package doc
Summary: Documentation for OpenStack Ceilometer API Client
Group: Development/Documentation

%description doc
This is a client library for Ceilometer built on the Ceilometer API. It
provides a Python API (the ceilometerclient module) and a command-line tool
(ceilometer).

This package contains auto-generated documentation.

%prep
%setup

# Remove bundled egg-info
rm -rf python_ceilometerclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

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
popd
mv %buildroot%_bindir/ceilometer %buildroot%_bindir/python3-ceilometer
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%_bindir/ceilometer
%python_sitelibdir/*

%if_with python3
%files -n python3-module-ceilometerclient
%_bindir/python3-ceilometer
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.13-alt1
- 1.0.13
- add puthon3 package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.10-alt1
- First build for ALT (based on Fedora 1.0.10-2.fc21.src)

