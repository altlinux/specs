Name: python3-module-matrix-common
Version: 1.1.0
Release: alt1

Summary: Common utilities for Synapse, Sydent and Sygnal

Url: https://github.com/matrix-org/matrix-python-common
License: ASL 2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/matrix-org/matrix-python-common/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-base python3-module-setuptools

%description
Common utilities for Synapse, Sydent and Sygnal.

%prep
%setup
cat >setup.py <<EOF
import setuptools
setuptools.setup()
EOF

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/*

%changelog
* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build for ALT Sisyphus

