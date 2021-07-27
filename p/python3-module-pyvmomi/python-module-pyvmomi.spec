%define  modulename pyvmomi

Name:    python3-module-%modulename
Version: 7.0.2
Release: alt2

Summary: VMware vSphere API Python Bindings
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/vmware/pyvmomi

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildPreReq: rpm-build-python3 python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to
manage ESX, ESXi, and vCenter.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/pyV*
%python3_sitelibdir/*.egg-*

%changelog
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
