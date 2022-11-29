%define  modulename flake8-import-order

%def_with check

Name:    python3-module-%modulename
Version: 0.18.2
Release: alt1

Summary: Flake8 plugin that checks import order against various Python Style Guides

License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/PyCQA/flake8-import-order

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pylama
BuildRequires: python3-module-pycodestyle
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
A flake8 and Pylama plugin that checks the ordering of your imports.
It does not check anything else about the imports. Merely that they are grouped
and ordered correctly.
In general stdlib comes first, then 3rd party, then local packages, and that
each group is individually alphabetized, however this depends on the style used.
Flake8-Import-Order supports a number of styles and is extensible allowing for
custom styles.
This plugin was originally developed to match the style preferences of the
cryptography project, with this style remaining the default.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 -m pytest -v

%files
%python3_sitelibdir/flake8_import_order
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 0.18.2-alt1
- Automatically updated to 0.18.2.

* Thu Apr 28 2022 Grigory Ustinov <grenka@altlinux.org> 0.18.1-alt1
- Initial build for Sisyphus.
