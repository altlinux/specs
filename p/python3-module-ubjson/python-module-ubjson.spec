# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define  modulename ubjson
%define  srcname py-ubjson

Name:    python3-module-%modulename
Version: 0.12.0
Release: alt2

Summary: Universal Binary JSON draft-12 serializer for Python
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/Iotic-Labs/py-ubjson

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

Source:  %srcname-%version.tar

%description
This is a Python Universal Binary JSON encoder/decoder based on the
draft-12 specification.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/_ubjson*.so
%python3_sitelibdir/*.egg-info

%changelog
* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt2
- Drop python2 support

* Sat Oct 20 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt1.1
- Fix unpackages files

* Wed Aug 22 2018 Anton Midyukov <antohami@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
