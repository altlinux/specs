%define  oname sphinxcontrib-qthelp

%def_with check

Name:    python3-module-%oname
Version: 1.0.3
Release: alt2

Summary: A sphinx extension which outputs QtHelp document
License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sphinxcontrib-qthelp

# https://github.com/sphinx-doc/sphinxcontrib-qthelp
Source:  %name-%version.tar

Patch: 42ca78b178c640cd024f16bfa291ae5093ce4920.patch

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
%endif

BuildArch: noarch

%description
%summary

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
py.test3 -vv

%files
%doc README.rst
%python3_sitelibdir/sphinxcontrib
%python3_sitelibdir/*.pth
%python3_sitelibdir/*.egg-info

%changelog
* Thu Aug 04 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt2
- Fixed FTBFS.

* Mon Mar 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt1
- Build new version.
- Correct license.
- Build with check.

* Fri Apr 26 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
