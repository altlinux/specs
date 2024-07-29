%define  modulename pyperclip

# https://github.com/asweigart/pyperclip/issues/263
%def_without check

Name:    python3-module-%modulename
Version: 1.9.0
Release: alt1

Summary: Python module for cross-platform clipboard functions

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pyperclip
# Upstream dont make github tags =(
# VCS:     https://github.com/asweigart/pyperclip

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-sphinx

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%package doc
Summary: Documentation for %modulename
Group: Development/Documentation

%description doc
Documentation for %modulename.

%prep
%setup -n %modulename-%version

# Fix ends of line encoding
sed -i 's/\r$//' README.md docs/*

%build
%pyproject_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run py.test-3

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc *.md

%files doc
%doc html

%changelog
* Mon Jul 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Build new version.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- Build new version.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Build new version.

* Sun Jun 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Build new version.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2
- Build with docs.

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
