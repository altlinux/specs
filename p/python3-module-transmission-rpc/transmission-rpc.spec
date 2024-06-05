Name: python3-module-transmission-rpc
Version: 7.0.8
Release: alt1

Summary: Transmission JSON RPC wrapper
License: MIT
Group: Development/Python
Url: https://pypi.org/project/transmission-rpc

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup
%pyproject_deps_resync_build

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/transmission_rpc
%python3_sitelibdir/transmission_rpc-%version.dist-info

%changelog
* Wed Jun 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 7.0.8-alt1
- 7.0.8 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.0.3-alt1
- 7.0.3 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.1.5-alt1
- 4.1.5 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- 3.4.0 released
