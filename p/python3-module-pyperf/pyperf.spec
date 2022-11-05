%define oname pyperf

Name: python3-module-%oname
Version: 2.5.0
Release: alt1

Summary: Python module to run and analyze benchmarks

Url: https://github.com/vstinner/pyperf
License: MIT
Group: Development/Python3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
The Python pyperf module is a toolkit to write, run and analyze benchmarks.

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -rfv %buildroot%python3_sitelibdir/pyperf/_win_memory.py
rm -rfv %buildroot%python3_sitelibdir/pyperf/tests/

%files
%_bindir/pyperf
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
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
