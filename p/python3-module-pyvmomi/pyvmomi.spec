%define  modulename pyvmomi

Name:    python3-module-%modulename
Version: 8.0.0.1.1
Release: alt1

Summary: VMware vSphere API Python Bindings

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/vmware/pyvmomi

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildPreReq: rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%add_python3_self_prov_path %buildroot%python3_sitelibdir/pyVmomi/

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to
manage ESX, ESXi, and vCenter.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pyV*
%python3_sitelibdir/*.egg-*

%changelog
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
