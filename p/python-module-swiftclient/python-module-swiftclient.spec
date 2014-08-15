Name:       python-module-swiftclient
Version:    2.1.0
Release:    alt1
Summary:    Client Library for OpenStack Object Storage API
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/%{name}
Source0:    %{name}-%{version}.tar
Group:      Development/Python

#
# patches_base=2.1.0
#
Patch0001: 0001-Remove-builtin-requirements-handling.patch

BuildArch:  noarch
Requires:   python-module-keystoneclient
Requires:   python-module-requests
# /usr/bin/swift collision with older swift-im rhbz#857900
Conflicts:  swift < 2.0-0.3

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-d2to1
BuildRequires: python-module-pbr
BuildRequires: python-module-requests
BuildRequires: python-module-six

%description
Client library and command line utility for interacting with Openstack
Object Storage API.

%package doc
Summary:    Documentation for OpenStack Object Storage API Client
Group:      Documentation

BuildRequires: python-module-sphinx

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.

%prep
%setup

%patch0001 -p1

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_swiftclient.egg-info

%build
%python_build

%install
%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd

install -p -D -m 644 doc/manpages/swift.1 %{buildroot}%{_mandir}/man1/swift.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%{_bindir}/swift
%{python_sitelibdir}/swiftclient
%{python_sitelibdir}/*.egg-info
%{_mandir}/man1/swift.1*

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- New version (based on Fedora 2.1.0-1.fc21.src)

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
