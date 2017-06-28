%define  modulename secretstorage

Name:    python3-module-%modulename
Version: 2.3.1
Release: alt2

Summary: Python bindings to Freedesktop.org Secret Service API
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mitya57/secretstorage

Packager: Gordeev Mikhail <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Wed Jun 28 2017
# optimized out: python-base python-modules python3 python3-base python3-module-setuptools
BuildRequires: python3-dev

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
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/%modulename/
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Wed Jun 28 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.3.1-alt2
- Add rpm-build-python3 to BuildRequires(pre)

* Wed Jun 28 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
