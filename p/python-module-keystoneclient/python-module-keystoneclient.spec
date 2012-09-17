Name:		python-module-keystoneclient
Version:	0.1.2
Release:	alt1
Summary:	Python API and CLI for OpenStack Keystone

Group:		Development/Python
License:	ASL 2.0
URL:		https://github.com/openstack/python-keystoneclient
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

# https://review.openstack.org/5353
Patch1:		python-module-keystoneclient-avoid-no-handlers.patch

Requires:	python-module-httplib2
Requires:	python-module-prettytable
Requires:	python-module-distribute
Requires:	python-module-simplejson

BuildRequires:	python-devel
BuildRequires:	python-module-distribute

%description
Client library and command line utility for interacting with Openstack
Keystone's API.

%package doc
Summary:	Documentation for OpenStack Keystone API Client
Group:		Documentation

BuildRequires:	python-module-sphinx
BUildRequires:	python-module-objects.inv

%description doc
Documentation for the client library for interacting with Openstack
Keystone's API.

%prep
%setup -q
%patch1 -p1
# Remove bundled egg-info
#rm -rf python_keystoneclient.egg-info

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
%doc README.rst
%{_bindir}/keystone
%{python_sitelibdir}/keystoneclient
%{python_sitelibdir}/*.egg-info

%files doc
%doc LICENSE doc/build/html

%changelog
* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.2-alt1
- Initial release for Sisyphus (based on Fedora)
