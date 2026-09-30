%define _unpackaged_files_terminate_build 1
%define pypi_name telepot

Name:           python3-module-telepot
Version:        12.7
Release:        alt1
Summary:        Python framework for Telegram Bot API
Group:          Development/Python3
License:        MIT
URL:            https://github.com/nickoala/telepot

Source:         %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-setuptools

%description
Telepot is a Python framework for the Telegram Bot API.
It is designed to be simple, stable, and extensible.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE.md
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 30 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 12.7-alt1
- Initial build for ALT.

