%define  oname mando

Name:    python3-module-%oname
Version: 0.6.4
Release: alt1

Summary: Python wrapper around argparse, a tool to create CLI apps

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/mando

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus
