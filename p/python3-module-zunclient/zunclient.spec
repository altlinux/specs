%define oname zunclient

Name:       python3-module-%oname
Version:    4.0.1
Release:    alt2

Summary:    Client Library for Zun

Group:      Development/Python3
License:    Apache-2.0
Url:        http://docs.openstack.org/developer/%oname

Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-openstackclient >= 3.12.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-websocket-client >= 0.44.0
BuildRequires: python3-module-docker >= 2.4.2
BuildRequires: python3-module-yaml >= 3.12

# doc
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Octavia client
Group: Development/Documentation

%description doc
This is a client library for Zun built on the Zun API.
It provides a Python API (the zunclient module)
and a command-line tool (zun).

This package contains documentation for %oname.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/python-zunclient.1 %buildroot%_man1dir/zunclient.1

# install bash completion
install -p -D -m 644 tools/zun.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/zun.bash_completion

%files
%doc *.rst LICENSE
%_bindir/zun
%_man1dir/zunclient*
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d/zun*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt2
- Remove doc knob for unifying.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.
- Build without python2.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- Initial build.
