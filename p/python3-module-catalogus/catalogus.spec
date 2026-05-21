%define oname catalogus

Name:    python3-module-%oname
Version: 0.1.0
Release: alt1

Summary: Classes to provide name-to-object registry-like support

Group:   Development/Python3
License: GPL-2.0-or-later
URL:     https://github.com/breezy-team/catalogus
Vcs:     https://github.com/breezy-team/catalogus

Source0: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
A Python library providing classes for name-to-object registry-like support.

Catalogus provides a simple and extensible registry system that allows you to:

- Register objects by name
- Retrieve objects by name
- Support lazy loading of objects
- Maintain type safety with generic support

This library was extracted from the Breezy version control system to provide a
reusable registry implementation.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md COPYING
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu May 21 2026 L.A. Kostis <lakostis@altlinux.ru> 0.1.0-alt1
- Initial build for ALTLinux.

