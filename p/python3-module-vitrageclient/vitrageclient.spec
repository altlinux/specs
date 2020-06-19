%define oname vitrageclient

Name:       python3-module-%oname
Version:    4.1.0
Release:    alt1

Summary:    Python client for Vitrage REST API

Group:      Development/Python3
License:    Apache-2.0
Url:        http://docs.openstack.org/developer/%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0

%description
This is a client library for Vitrage built to interface with the Vitrage API.
It provides a Python API (the vitrageclient module) and a command-line tool
(vitrage).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Python client for Vitrage REST API
Group: Development/Documentation

%description doc
This is a client library for Vitrage built to interface with the Vitrage API.
It provides a Python API (the vitrageclient module) and a command-line tool
(vitrage).

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install bash completion
mkdir -p %buildroot%_sysconfdir/bash_completion.d
mv %buildroot%_datadir/vitrage.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/vitrage.bash_completion

%files
%doc *.rst LICENSE
%_bindir/vitrage
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d/vitrage*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Initial build for Sisyphus.
