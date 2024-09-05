Name: python3-module-aiocoap
Version: 0.4.11
Release: alt1

Summary: The Python CoAP library
License: MIT
Group: Development/Python
Url: https://pypi.org/project/aiocoap/

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

# optional
%add_python3_req_skip js
%add_python3_req_skip lakers
%add_python3_req_skip pyodide.ffi.wrappers

%files
%_bindir/aiocoap-*
%python3_sitelibdir/aiocoap
%python3_sitelibdir/aiocoap-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.11-alt1
- 0.4.11 released

* Thu May 11 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.7-alt1
- 0.4.7 released

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.4-alt1
- 0.4.4 released
