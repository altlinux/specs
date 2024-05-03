%define oname pefile

Name: python3-module-%oname
Version: 2023.2.7
Release: alt1
Group: Development/Python3
Summary: Python module for working with Portable Executable files
License: MIT
Url: https://github.com/erocarrera/pefile
Vcs: https://github.com/erocarrera/pefile.git
Source0: https://github.com/erocarrera/%oname/releases/download/v%version/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
pefile is a multi-platform Python module to read and work with Portable
Executable (aka PE) files. Most of the information in the PE Header is
accessible, as well as all the sections, section's information and data.
pefile requires some basic understanding of the layout of a PE file. Armed
with it it's possible to explore nearly every single feature of the file.
Some of the tasks that pefile makes possible are:
* Modifying and writing back to the PE image
* Header Inspection
* Sections analysis
* Retrieving data
* Warnings for suspicious and malformed values
* Packer detection with PEiD's signatures
* PEiD signature generation

%prep
%setup -n %oname-%version
sed -i -e '/^#!\//, 1d' pefile.py

%build
%python3_build

%install
%python3_install

%files
%doc README*
%python3_sitelibdir/*

%changelog
* Fri May 03 2024 Alexey Shabalin <shaba@altlinux.org> 2023.2.7-alt1
- 2023.2.7

* Wed Aug 10 2022 Alexey Shabalin <shaba@altlinux.org> 2022.5.30-alt1
- Initial packaging.
