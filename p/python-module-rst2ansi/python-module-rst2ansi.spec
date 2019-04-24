%define  oname rst2ansi

Name:    python-module-%oname
Version: 0.1.5
Release: alt1

Summary: A rst converter to ansi-decorated console output

License: MIT
Group:   Development/Python
URL:     https://pypi.org/project/rst2ansi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
A python module dedicated to rendering RST (reStructuredText) documents to
ansi-escaped strings suitable for display in a terminal.

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
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
