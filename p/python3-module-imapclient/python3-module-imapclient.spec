%define pypi_name imapclient

%def_without check

Name:    python3-module-%pypi_name
Version: 2.3.1
Release: alt1

Summary: An easy-to-use, Pythonic and complete IMAP client library
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/mjs/imapclient

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/IMAPClient-%version.dist-info/

%changelog
* Tue Sep 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus.
