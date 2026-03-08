Name: python3-module-setuptools-reproducible
Version: 0.1
Release: alt1

License: MIT
Group: Development/Python
Url: https://github.com/wimglenn/setuptools-reproducible

Summary: Extension of setuptools to support reproducible dists

# Source-url: %__pypi_url setuptools-reproducible
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Extension of setuptools to support reproducible dists.

setuptools-reproducible is a PEP 517 build backend that wraps setuptools
to enable reproducible builds by controlling timestamps, file permissions,
and archive metadata.

%prep
%setup
# Use standard setuptools backend instead of self-referencing one
sed -i 's/build-backend = "setuptools_reproducible"/build-backend = "setuptools.build_meta"/' pyproject.toml
sed -i '/backend-path/d' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/setuptools_reproducible.py
%python3_sitelibdir/__pycache__/setuptools_reproducible.*
%python3_sitelibdir/%{pyproject_distinfo setuptools_reproducible}

%changelog
* Sat Mar 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus

