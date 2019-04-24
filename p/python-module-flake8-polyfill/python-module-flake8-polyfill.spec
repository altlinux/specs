%define  oname flake8-polyfill

Name:    python-module-%oname
Version: 1.0.2
Release: alt1

Summary: Polyfill package for Flake8 plugins

License: MIT
Group:   Development/Python
URL:     https://pypi.org/project/flake8-polyfill

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
flake8-polyfill is a package that provides some compatibility helpers for
Flake8 plugins that intend to support Flake8 2.x and 3.x simultaneously.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS.rst CHANGELOG.rst README.rst
%python_sitelibdir/flake8_polyfill/
%python_sitelibdir/*.egg-info/

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
