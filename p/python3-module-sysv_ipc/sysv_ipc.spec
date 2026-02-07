%define oname sysv_ipc

Name: python3-module-%oname
Version: 1.2.0
Release: alt1
Summary: System V IPC for Python - Semaphores, Shared Memory and Message Queues
Group: Development/Python3
License: GPLv3+
URL:    https://pypi.org/project/sysv-ipc
VCS:    https://github.com/osvenskan/sysv_ipc
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
The sysv_ipc module which gives Python access to System V inter-process
semaphores, shared memory and message queues on systems that support them.

%package examples
Summary: Examples for Python sysv_ipc module
Group: Development/Python3
Requires: %name = %version-%release
BuildArch: noarch

%description examples
This module comes with two demonstration apps. The first (in the directory
demo) shows how to use shared memory and semaphores. The second (in the
directory demo2) shows how to use message queues.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc INSTALL LICENSE README.md VERSION
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Feb 07 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Build new version.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt2
- Drop python2 support.

* Mon Feb 24 2020 Nikita Nikiforov <rav263@altlinux.org> 1.0.1-alt1
- (NMU) Update version 1.0.1

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.8-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.8-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.8-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.8-alt1
- Initial build
