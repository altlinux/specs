Name: python3-module-subsonic-connector
Version: 0.1.9
Release: alt1

Summary: SubSonic Connector
License: MIT
Group: Development/Python
Url: https://pypi.org/project/subsonic-connector/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/subsonic_connector
%python3_sitelibdir/subsonic_connector-%version.dist-info

%changelog
* Mon Apr 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.9-alt1
- 0.1.9 released

