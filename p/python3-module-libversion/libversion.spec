%define _unpackaged_files_terminate_build 1

%def_with check

%define pkgname libversion

Name: python3-module-%pkgname
Version: 1.2.4
Release: alt2
Group: Development/Python3
License: MIT
Summary: Python wrapper for libversion: an advanced version string comparison algorithm.
URL: https://github.com/repology/py-libversion
VCS: https://github.com/repology/py-libversion.git

Source: python3-module-%pkgname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libversion-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Python bindings for libversion, which provides fast, powerful and correct generic version string comparison algorithm. See libversion for more details.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra --import-mode=append

%files
%doc README.md CHANGELOG.md LICENSE
%python3_sitelibdir/%pkgname
%python3_sitelibdir/%{pyproject_distinfo %pkgname}

%changelog
* Fri Dec 23 2022 Elizaveta Morozova <morozovaes@altlinux.org> 1.2.4-alt2
- Switched to pyproject macros

* Fri Dec 09 2022 Elizaveta Morozova <morozovaes@altlinux.org> 1.2.4-alt1
- Initial build for ALT

