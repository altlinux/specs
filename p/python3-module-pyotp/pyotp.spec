Name: python3-module-pyotp
Version: 2.10.0
Release: alt1

Summary: Python library for generating and verifying one-time passwords.
License: BSD
Group: Development/Python
URL: https://pypi.org/project/pyotp
VCS: https://github.com/pyauth/pyotp

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

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v -s test

%files
%doc LICENSE* README.*
%python3_sitelibdir/pyotp
%python3_sitelibdir/pyotp-%version.dist-info

%changelog
* Wed Jun 24 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.10.0-alt1
- 2.10.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.9.0-alt1
- 2.9.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.8.0-alt1
- 2.8.0 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.7.0-alt1
- 2.7.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- initial
