%define oname pyperf

%def_with check

Name: python3-module-%oname
Version: 2.8.0
Release: alt1

Summary: Python module to run and analyze benchmarks

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/pyperf
VCS: https://github.com/vstinner/pyperf

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-psutil
BuildRequires: /proc
%endif

%description
The Python pyperf module is a toolkit to write, run and analyze benchmarks.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -v %buildroot%python3_sitelibdir/pyperf/_win_memory.py
rm -rv %buildroot%python3_sitelibdir/pyperf/tests/

%check
%pyproject_run_pytest

%files
%_bindir/pyperf
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 01 2024 Grigory Ustinov <grenka@altlinux.org> 2.8.0-alt1
- Automatically updated to 2.8.0.

* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 2.7.0-alt1
- Automatically updated to 2.7.0.
- Built with check.

* Wed Apr 03 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.3-alt1
- Automatically updated to 2.6.3.

* Mon Jun 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt1
- Automatically updated to 2.6.1.

* Fri Mar 24 2023 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0.

* Sat Nov 05 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Automatically updated to 2.5.0.

* Sun Aug 07 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1
- Automatically updated to 2.4.1.

* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.0-alt1
- Automatically updated to 2.4.0.

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.1-alt1
- Build new version.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2
- Drop python2 support.

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- initial build for ALT Sisyphus
