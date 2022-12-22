%define  oname identify

%def_with check

Name:    python3-module-%oname
Version: 2.5.11
Release: alt1

Summary: File identification library for Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/pre-commit/identify

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-ukkonen
BuildRequires: python3-module-cffi
%endif

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%_bindir/identify-cli
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.11-alt1
- Automatically updated to 2.5.11.

* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.10-alt1
- Automatically updated to 2.5.10.

* Wed Nov 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.9-alt1
- Automatically updated to 2.5.9.
- Build with check.

* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.10-alt1
- Automatically updated to 1.5.10.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.9-alt1
- Initial build for Sisyphus.
