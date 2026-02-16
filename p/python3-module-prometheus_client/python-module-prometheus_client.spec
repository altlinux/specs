%define oname prometheus_client

%def_with check

Name: python3-module-%oname
Version: 0.24.1
Release: alt1

Summary: The Python client for Prometheus

Url: https://github.com/prometheus/client_python
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/prometheus/client_python/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildArch: noarch

Provides: python3-module-%{pep503_name %oname} = %EVR

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
The Python client for Prometheus.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md MAINTAINERS.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Feb 12 2026 Aleksandr A. Voyt <sobue@altlinux.org> 0.24.1-alt1
- New version.
- rpm-build-pyproject is used for dependency management.

* Mon Jul 29 2024 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version.
- Built using pyproject macros.
- Fix license name according to SPDX.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.0-alt2
- (NMU) Provided PEP503-normalized project name.

* Tue Oct 13 2020 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Thu Apr 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- Build for python2 disabled.

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus

