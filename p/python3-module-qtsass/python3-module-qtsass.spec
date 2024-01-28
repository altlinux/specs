%define _unpackaged_files_terminate_build 1
%define pypi_name qtsass

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt3

License: MIT
Group: Development/Python
Url: https://github.com/spyder-ide/qtsass

Summary: QtSASS: Compile SCSS files to Qt stylesheets

# Source-url: https://github.com/spyder-ide/qtsass/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Patch0: qtsass-0.3.0-Add-check-for-deprecated-api-between-2-and-3-version.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(sass)

BuildRequires: python3(pytest)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
SASS brings countless amazing features to CSS.
Besides being used in web development,
CSS is also the way to stylize Qt-based desktop applications.
However, Qt's CSS has a few variations that prevent the direct use of SASS compiler.

The purpose of this tool is to fill the gap between SASS and Qt-CSS by handling those variations.

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
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt3
- Moved on modern pyproject macros.

* Fri Apr 01 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- Fixed FTBFS (Python 3.10).

* Thu Mar 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Sun Feb 02 2020 Vitaly Lipatov <lav@altlinux.ru> 0.0.1-alt1.git132651a
- initial build for ALT Sisyphus
