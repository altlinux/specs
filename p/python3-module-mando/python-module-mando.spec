%define  oname mando

Name:    python3-module-%oname
Version: 0.7.1
Release: alt1

Summary: Python wrapper around argparse, a tool to create CLI apps

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/mando

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jul 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.7.1-alt1
- Build new version.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Build new version.
- Drop python2 support.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus
