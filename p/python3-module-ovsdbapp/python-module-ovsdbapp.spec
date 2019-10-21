%global oname ovsdbapp

Name: python3-module-%oname
Version: 0.17.0
Release: alt1
Summary: A library for creating OVSDB applications

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-openvswitch >= 2.8.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
A library for creating OVSDB applications

The ovdsbapp library is useful for creating applications that communicate
via Open_vSwitch's OVSDB protocol (https://tools.ietf.org/html/rfc7047). It
wraps the Python 'ovs' and adds an event loop and friendly transactions.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for %oname.

%prep
%setup -n %oname-%version
# Remove bundled egg-info
rm -rf %oname.egg-info

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc README.rst LICENSE ChangeLog
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.17.0-alt1
- Automatically updated to 0.17.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.15.0-alt1
- Automatically updated to 0.15.0

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.12.2-alt1
- Initial build.
