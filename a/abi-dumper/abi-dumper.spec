Name: abi-dumper
Version: 0.99.5
Release: alt1
Group: Development/Other
License: GPLv2
Summary: A tool to dump ABI of an ELF object containing DWARF debug info
Source: %version.tar.gz
URL: https://github.com/lvc/abi-dumper
BuildArch: noarch

%description
ABI Dumper dumps ABI of an ELF object containing DWARF debug info.

The tool is intended to be used with ABI Compliance Checker tool for
tracking ABI changes of a C/C++ library or kernel module.

%prep
%setup

%install
mkdir -p %buildroot%prefix
perl Makefile.pl -install --prefix=%buildroot%prefix

%files
%doc README
%_bindir/*

%changelog
* Mon Sep 16 2013 Fr. Br. George <george@altlinux.ru> 0.99.5-alt1
- Autobuild version bump to 0.99.5

