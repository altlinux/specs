%define  oname pyshtrih

Name:    python3-module-%oname
Version: 2.0.4
Release: alt1

Summary: Implementation of the barcode driver

License: MIT
Group:   Development/Python3
URL:     https://github.com/oleg-golovanov/pyshtrih

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Fri Jun 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus (Closes: #24269).
