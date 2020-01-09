%define  oname yappi

Name:    python-module-%oname
Version: 1.2.3
Release: alt1

Summary: Yet Another Python Profiler, but this time support Multithread/CPU time profiling

License: MIT
Group:   Development/Python
URL:     https://pypi.org/project/yappi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

Source:  %oname-%version.tar

%description
%summary.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install
%if ""=="3"
mv %buildroot%_bindir/yappi %buildroot%_bindir/yappi
%endif

%files
%doc README.md
%_bindir/yappi*
%python_sitelibdir/*%{oname}*

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Build new version.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
-  Initial build for Sisphus.
