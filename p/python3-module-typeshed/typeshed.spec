%define _unpackaged_files_terminate_build 1

%define oname typeshed

Name: python3-module-%oname
Version: 0
# https://github.com/python/mypy/pull/11600
Release: alt3.git2445eddb

Summary: External type annotations for the Python packages
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/python/typeshed

BuildRequires: rpm-build-python3

BuildArch: noarch

Source: %name-%version.tar

%description
Typeshed contains external type annotations for the Python standard library and
Python builtins, as well as third party packages as contributed by people
external to those projects.

This data can e.g. be used for static analysis, type checking or type
inference.

%prep
%setup

%build

%install
mkdir -p %buildroot%python3_sitelibdir/%oname
cp -a stdlib %buildroot%python3_sitelibdir/%oname/

%files
%doc README.md
%python3_sitelibdir/%oname/

%changelog
* Thu Jan 27 2022 Stanislav Levin <slev@altlinux.org> 0-alt3.git2445eddb
- 17bc1d83 -> 2445eddb.

* Wed Jun 23 2021 Stanislav Levin <slev@altlinux.org> 0-alt2.git17bc1d83
- add4d92f -> 17bc1d83.

* Wed Mar 24 2021 Stanislav Levin <slev@altlinux.org> 0-alt1.gitadd4d92f
- Updated to add4d92f.

* Tue Sep 15 2020 Stanislav Levin <slev@altlinux.org> 0-alt1.git81d06761
- Initial build for Sisyphus.

