%define  modulename webcolors

Name:    python-module-%modulename
Version: 1.10
Release: alt1

Summary: Library for working with HTML/CSS color formats in Python

License: BSD-3-Clause
Group:   Development/Python
URL:     https://github.com/ubernostrum/webcolors

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/webcolors.py
%python_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Sep 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.10-alt1
- Initial build for Sisyphus.
