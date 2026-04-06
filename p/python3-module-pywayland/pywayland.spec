%define pypi_name pywayland

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.18
Release: alt2

Summary: Python bindings for the libwayland library
License: Apache-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/pywayland
VCS:     https://github.com/flacjacket/pywayland

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cffi
BuildRequires: python3-devel
BuildRequires: wayland-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: wayland-protocols

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build
python3 pywayland/ffi_build.py

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
mkdir tmp
export XDG_RUNTIME_DIR="$PWD/tmp"
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%_bindir/pywayland-scanner
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Apr 06 2026 Grigory Ustinov <grenka@altlinux.org> 0.4.18-alt2
- Initial build for Sisyphus.
