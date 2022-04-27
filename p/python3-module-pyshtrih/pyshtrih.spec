%define  oname pyshtrih

Name:    python3-module-%oname
Version: 2.0.6
Release: alt1

Summary: Implementation of the barcode driver

License: MIT
Group:   Development/Python3
URL:     https://github.com/oleg-golovanov/pyshtrih

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Wed Apr 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.6-alt1
- Automatically updated to 2.0.6.

* Fri Jun 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus (Closes: #24269).
