Name: abi-dumper
Version: 0.99.19
Release: alt1
Group: Development/Other
License: GPLv2
Summary: A tool to dump ABI of an ELF object containing DWARF debug info
Source: %version.tar.gz
Url: https://github.com/lvc/abi-dumper
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
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.99.19-alt1
- Autobuild version bump to 0.99.19

* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 0.99.16-alt1
- Autobuild version bump to 0.99.16

* Mon Jan 18 2016 Fr. Br. George <george@altlinux.ru> 0.99.13-alt1
- Autobuild version bump to 0.99.13

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.99.12-alt1
- Autobuild version bump to 0.99.12

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.99.8.1-alt1
- Autobuild version bump to 0.99.8.1

* Mon Apr 14 2014 Fr. Br. George <george@altlinux.ru> 0.99.8-alt1
- Autobuild version bump to 0.99.8

* Mon Sep 16 2013 Fr. Br. George <george@altlinux.ru> 0.99.5-alt1
- Autobuild version bump to 0.99.5

