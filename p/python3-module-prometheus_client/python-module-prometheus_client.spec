%define oname prometheus_client

Name: python3-module-%oname
Version: 0.20.0
Release: alt1

Summary: The Python client for Prometheus

Url: https://github.com/prometheus/client_python
License: Apache-2.0
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/prometheus/client_python/archive/v%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

Provides: python3-module-%{pep503_name %oname} = %EVR

BuildRequires(pre): rpm-build-python3 rpm-build-intro >= 2.1.4
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-decorator python3-module-pytest

%description
The Python client for Prometheus.

%prep
%setup -n %oname-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
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

