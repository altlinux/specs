%define  modulename cfgv

Name:    python3-module-%modulename
Version: 3.3.1
Release: alt1

Summary: Validate configuration and produce human readable error messages

License: MIT
Group:   Development/Python3
URL:     https://github.com/asottile/cfgv

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
%doc *.md
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/*.egg-info

%changelog
* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.
