%define  oname yappi

Name:    python3-module-%oname
Version: 1.3.3
Release: alt1

Summary: Yet Another Python Profiler, but this time support Multithread/CPU time profiling

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/yappi

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:  %oname-%version.tar

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname

%description
%summary.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/yappi*
%python3_sitelibdir/*%{oname}*
%python3_sitelibdir/__pycache__/

%changelog
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
