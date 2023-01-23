Name: python3-module-janus
Version: 1.0.0
Release: alt1

Summary: Mixed sync-async queue
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/janus/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
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
%python3_sitelibdir/janus
%python3_sitelibdir/janus-%version.dist-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
