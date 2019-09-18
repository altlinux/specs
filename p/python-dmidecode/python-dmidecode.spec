Name:     python-dmidecode
Version:  3.12.2
Release:  alt1

Summary:  Python DMI-Decode
License:  GPL-2.0
Group:    Other
Url:      https://github.com/nima/python-dmidecode

Source:   %name-%version.tar

BuildRequires: libxml2-devel
BuildRequires: python-module-setuptools python-module-libxml2

%description
python-dmidecode is a python extension module that uses the
code-base of the 'dmidecode' utility, and presents the data
as python data structures or as XML data using libxml2.


%prep
%setup
sed -i 's!setup.py install!\0 --root=%buildroot!' Makefile
sed -i /dmixml_GetContent/s/^inline// src/dmixml.c

%build
%make_build

%install
%makeinstall_std

%check
%make_build unit

%files
%doc README doc/README.upstream doc/LICENSE doc/AUTHORS doc/AUTHORS.upstream
%python_sitelibdir/*
%_datadir/%name

%changelog
* Tue Sep 17 2019 Vitaly Chikunov <vt@altlinux.org> 3.12.2-alt1
- Initial build for Sisyphus using github2spec
