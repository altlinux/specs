Name:		python-module-swiftclient
Version:	1.2.0
Release:	alt1
Summary:	Python API and CLI for OpenStack Swift

License:	ASL 2.0
URL:		https://github.com/openstack/python-swiftclient
BuildArch:	noarch
Group:		Development/Python
Source0:	%{name}-%{version}.tar.gz

#
# patches_base=1.2.0
#

Requires:	python-module-simplejson

BuildRequires:	python-devel
BuildRequires:	python-module-distribute

%description
Client library and command line utility for interacting with Openstack
Swift's API.

%package doc
Summary:	Documentation for OpenStack Swift API Client
Group:		Documentation

BuildRequires:	python-module-sphinx

%description doc
Documentation for the client library for interacting with Openstack
Swift's API.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelibdir}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%{_bindir}/swift
%{python_sitelibdir}/swiftclient
%{python_sitelibdir}/*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 1.2.0-alt1
- Initial release for Sisyphus (based on Fedora)
