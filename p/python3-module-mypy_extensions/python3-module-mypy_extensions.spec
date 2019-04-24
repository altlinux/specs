%define  oname mypy_extensions

Name:    python3-module-%oname
Version: 0.4.1
Release: alt1

Summary: Extensions for mypy (separated out from mypy/extensions).

License: MIT
Group:   Development/Python3
URL:     https://github.com/python/mypy_extensions

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
The "mypy_extensions" module defines experimental extensions to the standard
"typing" module that are supported by the mypy typechecker.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/*.egg-info/
%python3_sitelibdir/__pycache__/%oname.*

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus
