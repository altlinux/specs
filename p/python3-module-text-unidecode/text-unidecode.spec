Name: python3-module-text-unidecode
Version: 1.3
Release: alt3

Summary: Python port of Text::Unidecode Perl library.
License: GPLv2
Group: Development/Python
URL: https://pypi.org/project/text-unidecode
VCS: https://github.com/kmike/text-unidecode

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
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test_unidecode.py

%files
%python3_sitelibdir/text_unidecode
%python3_sitelibdir/text_unidecode-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3-alt3
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.3-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3-alt2
- moved to pyproject

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- initial
