%define  modulename cbor

Name:    python3-module-%modulename
Version: 1.0.0
Release: alt2

Summary: CBOR rfc7049 for Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/brianolson/cbor

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3

Source:  %modulename-%version.tar

%description
Concise Binary Object Representation (CBOR) is a superset of JSON's
schema that's faster and more compact.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt2
- Drop python2 support.

* Tue Aug 21 2018 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
