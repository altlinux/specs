%define _unpackaged_files_terminate_build 1
%define pypi_name zstd
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.6.4
Release: alt1

Summary: Zstd Bindings for Python

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/zstd/
Vcs: https://github.com/sergey-dryabzhinsky/python-zstd
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

BuildRequires: gcc
BuildRequires: libzstd-devel

%description
Simple Python bindings for the Zstd compression library.

%prep
%setup
%autopatch -p1
# Remove bundled zstd library
rm -r zstd

%build
export ZSTD_EXTERNAL=1
%pyproject_build

%install
%pyproject_install

%check
# there is no option to exclude tests via CLI
# speed tests check nothing but measure and report speed
rm tests/test_speed.py
%pyproject_run_unittest -v

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name.*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 24 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.4-alt1
- 1.5.6.1 -> 1.5.6.4.

* Thu Jan 09 2025 Stanislav Levin <slev@altlinux.org> 1.5.6.1-alt1
- 1.5.5.1 -> 1.5.6.1.

* Fri Oct 18 2024 Stanislav Levin <slev@altlinux.org> 1.5.5.1-alt1
- 1.5.0.4 -> 1.5.5.1.

* Mon Dec 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0.4-alt1
- Build new version.

* Tue Sep 29 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.5.1-alt1
- Initial build for Sisiphus.
