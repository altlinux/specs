%define oname incremental
%def_without check
%def_with bootstrap

Name: python3-module-incremental
Version: 24.7.2
Release: alt1

Summary: Incremental is a small library that versions your Python project

License: ASL 2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/incremental

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with bootstrap
%add_python3_req_skip twisted.python.compat twisted.python.filepath twisted.trial.unittest
%endif

%description
Incremental is a small library that versions your Python projects.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/


%changelog
* Mon Mar 09 2026 Vitaly Lipatov <lav@altlinux.ru> 24.7.2-alt1
- new version 24.7.2
- switch to pyproject build

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 22.10.0-alt1
- new version 22.10.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 21.3.0-alt1
- new version 21.3.0 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt4
- build python3 package separately

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 17.5.0-alt3
- Bootstrap for python3.7.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 17.5.0-alt2.qa1
- NMU: applied repocop patch

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt2
- (NMU) Rebuilt without bootstrap.

* Tue Mar 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 17.5.0-alt1
- initial build for ALT Sisyphus

