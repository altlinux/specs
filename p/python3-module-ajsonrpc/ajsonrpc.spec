Name: python3-module-ajsonrpc
Version: 1.2.0
Release: alt2.1

Summary: Async JSON-RPC 2.0 protocol
License: MIT
Group: Development/Python
Url: https://pypi.org/project/ajsonrpc
VCS: https://github.com/pavlov99/ajsonrpc

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
%summary

%prep
%setup
# replaced with release tag in GitHub action
sed -i '/^__version__/ s,0\.0\.0,%version,' ajsonrpc/__init__.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest ajsonrpc/tests

%files
%python3_sitelibdir/ajsonrpc
%python3_sitelibdir/ajsonrpc-%version.dist-info

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2.1
- Demodernized packaging.

* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt2
- moved to pyproject

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.2.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.0-alt1
- 1.2.0 released

* Mon Mar 22 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.0-alt1
- initial
