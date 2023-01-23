Name: python3-module-transmission-rpc
Version: 3.4.0
Release: alt1

Summary: Transmission JSON RPC wrapper
License: MIT
Group: Development/Python
Url: https://pypi.org/project/transmission-rpc

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/transmission_rpc
%python3_sitelibdir/transmission_rpc-%version.dist-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- 3.4.0 released
