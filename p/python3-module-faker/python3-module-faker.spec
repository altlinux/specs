%define  modulename faker

Name:    python3-module-%modulename
Version: 7.0.1
Release: alt1

Summary: Faker is a Python package that generates fake data for you.
License: MIT
Group:   Development/Python3
URL:     https://github.com/joke2k/faker

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

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
%_bindir/%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 7.0.1-alt1
- Initial build for Sisyphus.
