%define  modulename secretstorage

Name:    python-module-%modulename
Version: 2.3.1
Release: alt1

Summary: Python bindings to Freedesktop.org Secret Service API
License: BSD-3-Clause
Group:   Development/Python
URL:     https://github.com/mitya57/secretstorage

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev

BuildArch: noarch

Source:  %modulename-%version.tar

%description
This module provides a way for securely storing passwords and other secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring (since
version 2.30) and KSecretsService.

The main classes provided are secretstorage.Item, representing a secret item
(that has a label, a secret and some attributes) and secretstorage.Collection,
a place items are stored in.

SecretStorage supports most of the functions provided by Secret Service,
including creating and deleting items and collections, editing items, locking
and unlocking collections (asynchronous unlocking is also supported).

The documentation can be found on secretstorage.readthedocs.io.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir_noarch/%modulename/
%python_sitelibdir_noarch/*.egg-info

%changelog
* Thu Dec 13 2018 Evgeniy Korneechev <ekorneechev@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
