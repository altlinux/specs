Name: python3-module-jsonrpc-async
Version: 2.1.2
Release: alt1

Summary: JSON-RPC client implementation for asyncio python code
License: BSD
Group: Development/Python
Url: https://pypi.org/project/jsonrpc-async/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
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
%doc LICENSE.* README.*
%python3_sitelibdir/jsonrpc_async
%python3_sitelibdir/jsonrpc_async-%version.dist-info

%changelog
* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.2-alt1
- 2.1.2 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Mon Jan 13 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.1-alt1
- initial
