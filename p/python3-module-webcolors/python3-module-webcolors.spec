%define  modulename webcolors

Name:    python3-module-%modulename
Version: 1.10
Release: alt1

Summary: Library for working with HTML/CSS color formats in Python

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/ubernostrum/webcolors

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
%python3_sitelibdir/webcolors.py
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Sep 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.10-alt1
- Initial build for Sisyphus.
