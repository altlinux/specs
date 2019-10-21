%define  modulename pyperclip

Name:    python3-module-%modulename
Version: 1.7.0
Release: alt1

Summary: Python module for cross-platform clipboard functions.

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/asweigart/pyperclip

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
