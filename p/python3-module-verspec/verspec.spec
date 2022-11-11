%define _unpackaged_files_terminate_build 1

Name: python3-module-verspec
Version: 0.1.0
Release: alt2

Summary: Library for handling software versions and specifiers

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/verspec/

Source: verspec-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
verspec is a Python library for handling software versions and specifiers,
adapted from the packaging package.

%prep
%setup -n verspec-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/verspec/
%python3_sitelibdir/%{pyproject_distinfo verspec}/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.1.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.1.0-alt1
- Initial build for ALT
