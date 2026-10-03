%define oname exam

%def_with check

Name: python3-module-exam
Version: 0.10.6
Release: alt6
Summary: Helpers for better testing

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%oname
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/c7/bd/c15ce029540bb1b551af83c0df502ba47e019ce7132a65db046ad16b8eda/%oname-%version.tar.gz
Patch0: remove-nose.patch
Patch1: no-mock.patch
Patch2: fix-python314.patch
Patch3: fix-assertion-methods.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides %oname

%description
Exam is a Python toolkit for writing better tests. It aims to remove a lot of
the boiler plate testing code one often writes, while still following Python
conventions and adhering to the unit testing interface.

%prep
%setup -n %oname-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Oct 03 2026 Anton Vyatkin <toni@altlinux.org> 0.10.6-alt6
- Fixed FTBFS.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.10.6-alt5
- Fixed FTBFS.

* Wed Apr 05 2023 Anton Vyatkin <toni@altlinux.org> 0.10.6-alt4
- (NMU) Fix BuildRequires.

* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 0.10.6-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.10.6-alt2
- srpm build

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 0.10.6-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32334).
