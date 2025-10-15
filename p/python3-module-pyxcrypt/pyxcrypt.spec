%define _unpackaged_files_terminate_build 1
%define py_name pyxcrypt


Name: python3-module-pyxcrypt
Version: 0.1.1
Release: alt1


Summary: Python3 bindings for libxcrypt
License: GPL-3.0-or-later

Group: Development/Python3

Url: https://github.com/altlinux/pyxcrypt


Source: %name-%version.tar

BuildRequires: rpm-build-python3, python3-module-pyproject-installer
BuildRequires: libcrypt-devel python3-dev
BuildRequires: python3(mesonpy) meson


%description
%summary.


%prep
%setup

%build
%pyproject_build


%install
%pyproject_install

%check
env PYTHONPATH=%buildroot%python3_sitelibdir python3 -m unittest discover -s tests -v

%files
%doc README.md
%python3_sitelibdir/%py_name
%python3_sitelibdir/%py_name-%version.dist-info

%changelog
* Wed Oct 15 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus.
