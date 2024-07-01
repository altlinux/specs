%define  modulename pyvmomi

%def_without check

Name:    python3-module-%modulename
Version: 8.0.3.0.1
Release: alt1

Summary: VMware vSphere API Python Bindings

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/vmware/pyvmomi

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-vcrpy
%endif

BuildArch: noarch

Source:  %name-%version.tar

%add_python3_self_prov_path %buildroot%python3_sitelibdir/pyVmomi/

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to
manage ESX, ESXi, and vCenter.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/pyVmomi
%python3_sitelibdir/pyVim
%python3_sitelibdir/vsanapiutils.py
%python3_sitelibdir/vsanmgmtObjects.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/pyvmomi-%version.dist-info

%changelog
* Mon Jul 01 2024 Grigory Ustinov <grenka@altlinux.org> 8.0.3.0.1-alt1
- Automatically updated to 8.0.3.0.1.

* Wed Jan 24 2024 Grigory Ustinov <grenka@altlinux.org> 8.0.2.0.1-alt1
- Automatically updated to 8.0.2.0.1.

* Mon Oct 02 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.2.0-alt1
- Automatically updated to 8.0.2.0.

* Thu Jul 20 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.1.0.2-alt1
- Automatically updated to 8.0.1.0.2.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.1.0.1-alt1
- Automatically updated to 8.0.1.0.1.

* Tue May 16 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.1.0-alt1
- Automatically updated to 8.0.1.0.

* Thu Jan 19 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.0.1.2-alt1
- Automatically updated to 8.0.0.1.2.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 8.0.0.1.1-alt1
- Automatically updated to 8.0.0.1.1.

* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 8.0.0.1-alt1
- Automatically updated to 8.0.0.1.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 7.0.3-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue May 24 2022 Grigory Ustinov <grenka@altlinux.org> 7.0.3-alt1
- Automatically updated to 7.0.3.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 7.0.2-alt2
- Drop python2 support.

* Mon Apr 12 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- New version.

* Sat Oct 31 2020 Andrey Cherepanov <cas@altlinux.org> 7.0.1-alt1
- New version.

* Wed Apr 15 2020 Andrey Cherepanov <cas@altlinux.org> 7.0-alt1
- New version.

* Thu Sep 05 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.3-alt1
- New version.

* Mon Dec 24 2018 Andrey Cherepanov <cas@altlinux.org> 6.7.1.2018.12-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 6.7.1-alt1
- New version.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- New version.

* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 6.5.0.2017.5-alt1
- Initial build for Sisyphus
