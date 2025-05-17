%define _unpackaged_files_terminate_build 1
%define mname system-seed-wheels

Name: python3-module-%mname
Version: 0.0.2
Release: alt1

Summary: Seed wheels for setuptools and pip
License: MIT
Group: Development/Python3

BuildRequires(pre): rpm-build-python3

%description
Base package for providing seed wheels for setuptools and pip.
Used in virtualenv instead of the bundled wheels.

%package wheels
Summary: %summary
Group: Development/Python3

Requires: python3-module-%mname
Requires: python3-module-setuptools-wheel
Requires: python3-module-pip-wheel

%description wheels
Contains system seed wheels for setuptools and pip.
Used in virtualenv instead of the bundled wheels.

%prep

%build

%install
mkdir -p %buildroot%python3_sitelibdir/system_seed_wheels
touch %buildroot%python3_sitelibdir/system_seed_wheels/__init__.py

%check

%files
%python3_sitelibdir/system_seed_wheels/

%files wheels

%changelog
* Thu May 15 2025 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1
- stopped shipping a wheel for wheel package

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
