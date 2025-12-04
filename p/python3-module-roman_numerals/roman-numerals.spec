Name: python3-module-roman_numerals
Version: 3.1.0
Release: alt2
Source: roman-numerals-%version.tar.gz
Url: https://github.com/AA-Turner/roman-numerals/

Summary: Manipulate well-formed Roman numerals
License: CC0-1.0
Group: Development/Python3

BuildArch: noarch

# Automatically added by buildreq on Thu Feb 27 2025
# optimized out: bash5 libgpg-error openssl-config python3-base sh5
BuildRequires: python3-module-flit-core python3-module-pyproject-installer pytest3 rpm-build-python3

%description
This project provides utilities manipulating well-formed Roman numerals

%prep
%setup -n roman-numerals-%version
ln [^R]*.rst python/
sed -i 's/roman-numerals-py/roman-numerals/' python/pyproject.toml

%build
cd python
%pyproject_build

%install
cd python
%pyproject_install

%files
%doc *.rst
%python3_sitelibdir/*

%check
pytest3

%changelog
* Thu Dec 04 2025 Fr. Br. George <george@altlinux.org> 3.1.0-alt2
- Remove _py suffix from package name

* Thu Feb 27 2025 Fr. Br. George <george@altlinux.org> 3.1.0-alt1
- Autobuild version bump to 3.1.0

* Thu Feb 27 2025 Fr. Br. George <george@altlinux.org> 3.0.0-alt1
- Initial build for ALT
