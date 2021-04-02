%define  modulename m2r2

Name:    python3-module-%modulename
Version: 0.2.7
Release: alt1

Summary: Markdown to reStructuredText converter
License: MIT
Group:   Development/Python3
URL:     https://github.com/CrossNox/m2r2

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
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__/%{modulename}*
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Fri Apr 02 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.7-alt1
- Initial build for Sisyphus.
