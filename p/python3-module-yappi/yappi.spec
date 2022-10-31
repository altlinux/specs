%define  oname yappi

%def_without check

Name:    python3-module-%oname
Version: 1.4.0
Release: alt1

Summary: Yet Another Python Profiler, but this time support Multithread/CPU time profiling

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/yappi

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname

%description
%summary.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 run_tests.py

%files
%doc README.md
%_bindir/yappi*
%python3_sitelibdir/*%{oname}*
%python3_sitelibdir/__pycache__/

%changelog
* Mon Oct 31 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.6-alt1
- Automatically updated to 1.3.6.

* Sun May 29 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt1
- Build new version.

* Tue Nov 30 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Build new version.

* Mon Nov 30 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.2-alt1
- Build new version.

* Mon Nov 23 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Build new version.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.5-alt1
- Build new version.

* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.3-alt2
- Porting on Python3.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Build new version.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
-  Initial build for Sisphus.
