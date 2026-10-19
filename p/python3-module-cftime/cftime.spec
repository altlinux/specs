%define  oname cftime

%def_with check

Name:    python3-module-%oname
Version: 1.6.6.1
Release: alt1

Summary: Time-handling functionality from netcdf4-python

License: MIT and GPLv3
Group:   Development/Python3
URL:     https://pypi.org/project/cftime
VCS:     https://github.com/Unidata/cftime

Source:  %name-%version.tar
Patch:   cftime-1.6.6.1-alt-fix-can-use-python-datetime.patch

Packager: Grigory Ustinov <grenka@altlinux.org>

# numpy is imported at runtime by the Cython module, autoreq does not see it
Requires: python3(numpy)

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy-testing
%endif

%description
%summary

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest -v \
%ifarch armh
-k 'not test_num2date_precision'
%endif

%files
%doc LICENSE *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.6.6.1-alt1
- New version 1.6.6.1
- Fix FTBFS: rewrite _can_use_python_datetime (miscompiled by Cython 3.3)
- Add missing runtime dependency on numpy

* Tue Oct 14 2025 Grigory Ustinov <grenka@altlinux.org> 1.6.5-alt1
- Automatically updated to 1.6.5.

* Thu Nov 28 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.4.post1-alt1
- Automatically updated to 1.6.4.post1.

* Fri Jun 14 2024 Grigory Ustinov <grenka@altlinux.org> 1.6.4-alt1
- Automatically updated to 1.6.4.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt1
- Automatically updated to 1.6.3.

* Sun Sep 18 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Automatically updated to 1.6.2.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt1
- Automatically updated to 1.6.1.

* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.
- Build with check.

* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Build new version.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Build new version.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Build new version.

* Thu Jan 21 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus.
