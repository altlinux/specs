Name: python3-module-subsonic-connector
Version: 0.3.11
Release: alt1

Summary: SubSonic Connector
License: MIT
Group: Development/Python
URL: https://pypi.org/project/subsonic-connector
VCS: https://github.com/GioF71/subsonic-connector

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

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/subsonic_connector
%python3_sitelibdir/subsonic_connector-%version.dist-info

%changelog
* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.11-alt1
- 0.3.11 released

* Wed Dec 10 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.3.9-alt1
- 0.3.9 released

* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 0.1.17-alt2
- Fixed FTBFS (poetry-core 2.0).

* Wed Jul 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.17-alt1
- 0.1.17 released

* Tue Jun 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.16-alt1
- 0.1.16 released

* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.9-alt1
- 0.1.9 released

