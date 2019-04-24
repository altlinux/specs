%define  oname mando

Name:    python-module-%oname
Version: 0.6.4
Release: alt1

Summary: Python wrapper around argparse, a tool to create CLI apps

License: MIT
Group:   Development/Python
URL:     https://pypi.org/project/mando

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
Mando is a wrapper around argparse, and allows writing CLI
applications.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info/

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus
