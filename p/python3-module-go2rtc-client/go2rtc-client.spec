Name: python3-module-go2rtc-client
Version: 0.1.2
Release: alt1

Summary: Asynchronous Python client for go2rtc
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/go2rtc-client/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(hatchling)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/go2rtc_client
%python3_sitelibdir/go2rtc_client-%version.dist-info

%changelog
* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.2-alt1
- 0.1.2 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.0-alt1
- 0.1.0 released

