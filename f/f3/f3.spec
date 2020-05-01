Name:		f3
Version:	7.2
Release:	alt1
Summary:	Fight Flash Fraud / Fight Fake Flash
License:	GPLv3
Group:		System/Configuration/Hardware
Url:		http://oss.digirati.com.br/f3/
Source:		https://github.com/AltraMayor/f3/archive/v7.1.tar.gz#/f3-%version.tar.gz

# Automatically added by buildreq on Sun Mar 06 2016 (-bi)
# optimized out: elfutils python-base
BuildRequires: libparted-devel libudev-devel

%description
This package contains tools for identifying fake flash drives (primarily USB
sticks and memory cards).

A fake flash drive fraudulently inflates its apparent storage capacity (far)
beyond the physical capacity of its flash memory. Not surprisingly, using such
a flash drive will, sooner or later, result in data loss and/or corruption.

The main tools in this package are an open-source implementation of the H2testw
algorithm. Some experimental tools are also provided, among them one for using
the actual storage capacity of fake drives as safely as possible.

%prep
%setup

%build
subst 's|-std=c99 -Wall -Wextra -pedantic -MMD -ggdb|%optflags|g' ./Makefile
subst 's|/usr/local|%prefix|g' ./Makefile
%make_build extra

%install
mkdir -p examples
make DESTDIR=%buildroot install
install -m 0755 f3write.h2w log-f3wr ./examples

mkdir -p %buildroot%prefix/sbin
install -m 0755 f3probe f3brew f3fix %buildroot%prefix/sbin

%files
%doc changelog README.* LICENSE examples
%_bindir/*
%_sbindir/*
%_man1dir/*

%changelog
* Fri May 01 2020 Motsyo Gennadi <drool@altlinux.ru> 7.2-alt1
- 7.2

* Sun Nov 04 2018 Motsyo Gennadi <drool@altlinux.ru> 7.1-alt2
- build with extras

* Sun Nov 04 2018 Motsyo Gennadi <drool@altlinux.ru> 7.1-alt1
- 7.1 (#35573)

* Sun Mar 06 2016 Motsyo Gennadi <drool@altlinux.ru> 6.0-alt1
- initial build for ALT Linux
