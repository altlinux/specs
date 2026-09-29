%define _unpackaged_files_terminate_build 1

%define oname astor

Name: python3-module-%oname
Version: 0.8.1
Release: alt2
Summary: Python AST read/write
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/berkerpeksag/astor

BuildArch: noarch

# https://github.com/berkerpeksag/astor.git
Source: %name-%version.tar
Patch0: py314.patch
Patch1: lower-huge-int.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
astor is designed to allow easy manipulation of Python source via the AST.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k "not test_convert_stdlib"

%files
%doc LICENSE
%doc AUTHORS README.rst
%python3_sitelibdir/%oname-%version.dist-info
%python3_sitelibdir/%oname

%changelog
* Tue Sep 29 2026 Anton Vyatkin <toni@altlinux.org> 0.8.1-alt2
- Fixed FTBFS.

* Mon Feb 27 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1.1
- Fixed FTBFS.

* Mon Feb 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt1
- Initial build for ALT.
