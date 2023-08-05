Name: python3-module-matrix-common
Version: 1.3.0
Release: alt1

Summary: Common utilities for Synapse, Sydent and Sygnal

Url: https://github.com/matrix-org/matrix-python-common
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/matrix-python-common/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-base python3-module-setuptools python3-module-wheel

%description
Common utilities for Synapse, Sydent and Sygnal.

%prep
%setup
cat >setup.py <<EOF
import setuptools
setuptools.setup()
EOF

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sat Aug 05 2023 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus

