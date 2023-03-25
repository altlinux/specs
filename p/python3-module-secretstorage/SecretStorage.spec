Name: python3-module-secretstorage
Version: 3.3.3
Release: alt1

Summary: Python bindings to Freedesktop.org Secret Service API
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/mitya57/secretstorage

Packager: Gordeev Mikhail <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Wed Jun 28 2017
# optimized out: python-base python-modules python3 python3-base python3-module-setuptools
BuildRequires: python3-dev

BuildArch: noarch

Source: SecretStorage-%version.tar.gz

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
%setup -n SecretStorage-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir_noarch/secretstorage/
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Fri Mar 24 2023 Fr. Br. George <george@altlinux.org> 3.3.3-alt1
- Autobuild version bump to 3.3.3

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 3.3.2-alt1
- Autobuild version bump to 3.3.2

* Thu Feb 11 2021 Fr. Br. George <george@altlinux.ru> 3.3.1-alt1
- Autobuild version bump to 3.3.1

* Wed Jun 28 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.3.1-alt2
- Add rpm-build-python3 to BuildRequires(pre)

* Wed Jun 28 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus
