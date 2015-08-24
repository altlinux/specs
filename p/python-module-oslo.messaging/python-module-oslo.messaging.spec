%global sname oslo.messaging

%def_with python3

Name:       python-module-%sname
Epoch:      1
Version:    1.8.3
Release:    alt1
Summary:    OpenStack common messaging library

Group:      Development/Python
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    %name-%version.tar

Provides:  python-module-oslo-messaging = %EVR
Obsoletes: python-module-oslo-messaging < %EVR
BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-iso8601
BuildRequires: python-module-oslo.config >= 1.9.3
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.middleware >= 1.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-stevedore >= 1.3.0
BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-kombu >= 2.5.0
#BuildRequires: python-module-qpid-proton
BuildRequires: python-module-eventlet >= 0.16.1
BuildRequires: python-module-fixtures
BuildRequires: python-module-babel
BuildRequires: python-module-futures >= 2.1.6
BuildRequires: python-module-aioeventlet >= 0.4
BuildRequires: python-module-trollius >= 1.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-iso8601
BuildRequires: python3-module-oslo.config >= 1.9.3
BuildRequires: python3-module-oslo.utils >= 1.4.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.middleware >= 1.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.3.0
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-kombu >= 2.5.0
# BuildRequires: python3-module-qpid-proton
BuildRequires: python3-module-eventlet >= 0.16.1
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-babel
BuildRequires: python3-module-aioeventlet >= 0.4
BuildRequires: python3-module-trollius >= 1.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%if_with python3
%package -n python3-module-oslo.messaging
Summary: OpenStack oslo.messaging library
Group: Development/Python3
Provides: python3-module-oslo-messaging = %EVR
%add_python3_req_skip proton
%add_python3_req_skip pyngus

%description -n python3-module-oslo.messaging
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.
%endif

%package doc
Summary:    Documentation for OpenStack common messaging library
Group:     Development/Documentation
Provides:  python-module-oslo-messaging-doc = %EVR
Obsoletes: python-module-oslo-messaging-doc < %EVR

%description doc
Documentation for the oslo.messaging library.

%prep
%setup


# Remove bundled egg-info
#rm -rf %sname.egg-info
# let RPM handle deps
#sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
#rm -rf {test-,}requirements.txt

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/*

%if_with python3
%files -n python3-module-oslo.messaging
%python3_sitelibdir/*
%endif

%files doc
%doc html LICENSE

%changelog
* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.8.3-alt1
- 1.8.3

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0
- add python3 package

* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.3.0.2-alt1
- First build for ALT (based on Fedora 1.3.0.2-4.fc21.src)
