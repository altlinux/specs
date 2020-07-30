%define oname os-api-ref

Name: python3-module-%oname
Version: 1.6.0
Release: alt2
Summary: Sphinx Extensions to support API reference sites in OpenStack
Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-six >= 1.10.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1


%description
This project is a collection of sphinx stanzas that assist in building
an API Reference site for an OpenStack project in RST. RST is great
for unstructured English, but displaying semi structured (and
repetitive) data in tables is not its strength. This provides tooling
to insert semi-structured data describing request and response
parameters and status or error messages, and turn those into nice tables.

The project also includes a set of styling (and javascript) that is
expected to layer on top of a Sphinx theme base. This addition
provides a nice set of collapsing sections for REST methods and
javascript controls to expand / collapse all sections.


%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack os-api-ref library
Group: Development/Documentation

%description doc
Documentation for the os-api-ref library.

%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

#%check
#python3 setup.py test

%files
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Thu Jul 30 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Transfer on python3.
- Fix license.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial packaging
