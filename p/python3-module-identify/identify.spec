%define  modulename identify

Name:    python3-module-%modulename
Version: 1.5.10
Release: alt1

Summary: File identification library for Python

License: MIT
Group:   Development/Python3
URL:     https://github.com/pre-commit/identify

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
%_bindir/identify-cli
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.10-alt1
- Automatically updated to 1.5.10.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.9-alt1
- Initial build for Sisyphus.
