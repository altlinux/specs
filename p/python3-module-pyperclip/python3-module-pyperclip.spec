%define  modulename pyperclip

Name:    python3-module-%modulename
Version: 1.7.0
Release: alt2

Summary: Python module for cross-platform clipboard functions.

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/asweigart/pyperclip

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx

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
%python3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%files doc
%doc html

%changelog
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt2
- Build with docs.

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
