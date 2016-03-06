Name:		f3
Version:	6.0
Release:	alt1
Summary:	Fight Flash Fraud / Fight Fake Flash
License:	GPLv3
Group:		System/Configuration/Hardware
Url:		http://oss.digirati.com.br/f3/
Source:		https://github.com/AltraMayor/f3/archive/v6.0.tar.gz#/f3-6.0.tar.gz
Patch:		man-www-ref.patch

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
%patch -p1

%build
subst 's|-std=c99 -Wall -Wextra -pedantic -MMD -ggdb|%optflags|g' ./Makefile
%make_build all experimental

mkdir examples
mv log-f3wr f3write.h2w examples
chmod a-x examples/*

%install
mkdir -p %buildroot%prefix/bin
install f3read f3write %buildroot%prefix/bin

mkdir -p %buildroot%prefix/sbin
install f3probe f3brew f3fix %buildroot%prefix/sbin

mkdir -p %buildroot%_man1dir/
install -m 0644 f3read.1 %buildroot%_man1dir/
ln -sf f3read.1 %buildroot%_man1dir/f3write.1

%files
%doc changelog README.md LICENSE examples
%_bindir/f3read
%_bindir/f3write
%_sbindir/f3probe
%_sbindir/f3brew
%_sbindir/f3fix
%_man1dir/f3read.1.*
%_man1dir/f3write.1.*

%changelog
* Sun Mar 06 2016 Motsyo Gennadi <drool@altlinux.ru> 6.0-alt1
- initial build for ALT Linux
