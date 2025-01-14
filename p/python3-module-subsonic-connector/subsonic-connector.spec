Name: python3-module-subsonic-connector
Version: 0.1.17
Release: alt2

Summary: SubSonic Connector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/subsonic-connector/

Source0: %name-%version-%release.tar
# https://github.com/GioF71/subsonic-connector/issues/95
Patch0: subsonic-connector-0.1.17-metadata-sync-project-s-names.patch

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/subsonic_connector
%python3_sitelibdir/subsonic_connector-%version.dist-info

%changelog
* Tue Jan 14 2025 Stanislav Levin <slev@altlinux.org> 0.1.17-alt2
- Fixed FTBFS (poetry-core 2.0).

* Wed Jul 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.17-alt1
- 0.1.17 released

* Tue Jun 20 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.16-alt1
- 0.1.16 released

* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.9-alt1
- 0.1.9 released

