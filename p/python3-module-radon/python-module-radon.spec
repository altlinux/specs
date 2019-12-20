%define  oname radon

Name:    python3-module-%oname
Version: 4.0.0
Release: alt2

Summary: Various code metrics for Python code

License: MIT
Group:   Development/Python3
URL:     https://github.com/rubik/radon

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
Radon is a Python tool that computes various metrics from the source code.
Radon can compute:

* McCabe's complexity**, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%prep
%setup -n %oname-%version

%build
%python3_build
rm -r */lib/radon/tests

%install
%python3_install

%files
%doc CHANGELOG README.rst
%_bindir/radon
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/

%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0.0-alt2
- build for python2 disabled

* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Build new version.

* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.3-alt1
- Build new version.

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus.
