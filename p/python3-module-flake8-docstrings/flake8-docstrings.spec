%define  modulename flake8-docstrings

Name:    python3-module-%modulename
Version: 1.7.0
Release: alt1

Summary: Integration of pydocstyle and flake8 for combined linting and reporting

License: MIT
Group:   Development/Python3
URL:     https://github.com/PyCQA/flake8-docstrings

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/flake8_docstrings.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Fri Jan 27 2023 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Automatically updated to 1.7.0.

* Thu Apr 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus.
