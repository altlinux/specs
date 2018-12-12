%define oname os-api-ref

Name: python-module-%oname
Version: 1.6.0
Release: alt1
Summary: Sphinx Extensions to support API reference sites in OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-six >= 1.10.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1


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
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack os-api-ref library
Group: Development/Documentation

%description doc
Documentation for the os-api-ref library.

%package -n python3-module-%oname
Summary: Sphinx Extensions to support API reference sites in OpenStack
Group: Development/Python3

%description -n python3-module-%oname
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


%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python_install

pushd ../python3
%python3_install
popd

#%check
#python setup.py test

#%if_with python3
#pushd ../python3
#python3 setup.py test
#popd
#%endif

%files
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

#%files tests
#%python_sitelibdir/*/tests

%files doc
%doc doc/build/html

%files -n python3-module-%oname
%doc ChangeLog CONTRIBUTING.rst PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

# need sphinx_testing module
#%files -n python3-module-%oname-tests
#%python3_sitelibdir/*/tests

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial packaging
