%def_with check

Name: python3-module-helpdev
Version: 0.7.1
Release: alt1.1

License: MIT
Group: Development/Python
Url: https://gitlab.com/dpizetta/helpdev

Summary: Helping users and developers to get information about the environment to report bugs

# Source-url: https://pypi.io/packages/source/h/helpdev/helpdev-%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
# for test

%if_with check
BuildRequires: python3(psutil)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
Helping users and developers to get information about the environment
to report bugs or even test your system without spending a day on it.
It can get information about hardware, OS, paths,
Python distribution and packages, including Qt-things.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%_bindir/helpdev
%python3_sitelibdir/*

%changelog
* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1.1
- NMU: moved on modern pyproject macros.

* Mon Nov 09 2020 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.6.10 -> 0.7.1.

* Sun May 03 2020 Stanislav Levin <slev@altlinux.org> 0.6.10-alt2
- Dropped dependency on importlib_metadata.

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.6.10-alt1
- initial build for ALT Sisyphus
