%def_with python3
%define sname zaqarclient

Name: python-module-%sname
Version: 0.2.0
Release: alt1
Summary: Client Library for OpenStack Zaqar Queueing API

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-%sname
Source: %name-%version.tar


BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-jsonschema >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-requests >= 2.5.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python3-module-jsonschema >= 2.0.0
%endif

%description
Python client to Zaqar messaging service API v1.

%if_with python3
%package -n python3-module-%sname
Summary: Client Library for OpenStack Zaqar Queueing API
Group: Development/Python3

%description -n python3-module-%sname
Python client to Zaqar messaging service API v1.
%endif

%package doc
Summary: Documentation for OpenStack Zaqar Queueing API Client
Group: Development/Documentation

%description doc
Python client to Zaqar messaging service API v1.

This package contains auto-generated documentation.

%prep
%setup

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

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
#mv %buildroot%_bindir/zaqar %buildroot%_bindir/python3-zaqar
%endif

%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%doc LICENSE
#%_bindir/zaqar
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
#%_bindir/python3-zaqar
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial build.


