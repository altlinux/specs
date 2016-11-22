%def_with python3
%define sname aodhclient

Name:       python-module-%sname
Version:    0.7.0
Release:    alt1
Summary:    Python API and CLI for OpenStack Aodh
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/python-%sname
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-argparse
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-cliff >= 1.14.0
BuildRequires: python-module-osc-lib >= 1.0.1
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 1.0.0
BuildRequires: python-module-debtcollector

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-osc-lib >= 1.0.1
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 1.0.0
BuildRequires: python3-module-debtcollector
%endif

%description
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

%if_with python3
%package -n python3-module-%sname
Summary:    Python API and CLI for OpenStack Aodh
Group: Development/Python3

%description -n python3-module-%sname
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.
%endif

%package doc

Summary: Documentation for OpenStack Aodh API Client
Group:  Development/Documentation

%description doc
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool
(aodh).

%prep
%setup

# Let RPM handle the dependencies
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
mv %buildroot%_bindir/aodh %buildroot%_bindir/python3-aodh
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/aodh
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-aodh
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE html

%changelog
* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- Initial release for Sisyphus
