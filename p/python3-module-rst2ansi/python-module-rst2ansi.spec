%define  oname rst2ansi

Name:    python3-module-%oname
Version: 0.1.5
Release: alt2

Summary: A rst converter to ansi-decorated console output

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/rst2ansi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar
Patch0: python-module-rst2ansi-0.1.5-remove-unsused-imports.patch

%description
A python module dedicated to rendering RST (reStructuredText) documents to
ansi-escaped strings suitable for display in a terminal.

%prep
%setup -n %oname-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info/

%changelog
* Mon Dec 01 2025 Anton Farygin <rider@altlinux.com> 0.1.5-alt2
- Added patch from Debian to fix build with docutils 0.22

* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
