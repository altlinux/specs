Name: python3-module-spidev
Version: 3.8
Release: alt1

Summary: Python SPI devices Extension
License: MIT
Group: Development/Python
Url: https://pypi.org/project/spidev
VCS: https://github.com/doceme/py-spidev

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/spidev.*.so
%python3_sitelibdir/spidev-%version.dist-info

%changelog
* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.8-alt1
- 3.8 released

* Wed Dec 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.6-alt1
- initial
