Name: python3-module-charset-normalizer
Version: 3.4.7
Release: alt1

Summary: The Real First Universal Charset Detector
License: MIT
Group: Development/Python
URL: https://pypi.org/project/charset-normalizer
VCS: https://github.com/jawah/charset_normalizer

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
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
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/normalizer
%python3_sitelibdir/charset_normalizer
%python3_sitelibdir/charset_normalizer-%version.dist-info

%check
%pyproject_run_pytest -o addopts= tests

%changelog
* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.7-alt1
- 3.4.7 released

* Tue Mar 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.6-alt1
- 3.4.6 released

* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.4-alt1
- 3.4.4 released

* Fri May 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Fri Dec 02 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.6-alt1
- initial
