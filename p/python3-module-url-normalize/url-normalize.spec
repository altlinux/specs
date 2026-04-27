Name: python3-module-url-normalize
Version: 3.0.0
Release: alt1

Summary: URI Normalization function
License: MIT
Group: Development/Python
URL: https://pypi.org/project/url-normalize
VCS: https://github.com/niksite/url-normalize

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev

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

%check
%pyproject_run_pytest -o addopts= tests

%files
%_bindir/url-normalize
%python3_sitelibdir/url_normalize
%python3_sitelibdir/url_normalize-%version.dist-info

%changelog
* Mon Apr 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.0-alt1
- 3.0.0 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.1-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1.1
- Demodernized packaging.

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.1-alt1
- 2.2.1 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- 1.4.3 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.2-alt1
- initial
