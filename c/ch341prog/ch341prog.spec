%define build_static	0

Name: ch341prog
# look at the last non-specfile change, take date and first 8 digits
Version: 20170517ba1a8306
Release: alt2
Summary: 24xx/25xx I2C/SPI IC flashing tool for CH341-based programmers
License: GPLv3+
Group: Development/Other
URL: https://github.com/setarcos/ch341prog
Source0: %name-%version.tar.xz
%if %build_static
BuildRequires: glibc-devel-static
%endif

%description
%name is a %summary

%package doc
Summary: Optional documentation for %name
Group: Development/Other
BuildArch: noarch

%description doc
%summary


%prep
%setup


%build
%__cc	-std=gnu99 -Wall -Ilibusb \
	*.c libusb/*.c -o %name \
	-lpthread -s \
%if %build_static
	-static
%else
	;
%endif


%install
rm -rf %buildroot
umask 022
mkdir -p %buildroot/%_bindir %buildroot/%_man1dir
install -m 755 %name %buildroot/%_bindir/
install -m 644 %name.1 %buildroot/%_man1dir/


%files
%{_bindir}/*
%{_man1dir}/*

%files doc
%doc CH341_chip.txt COPYING README.md

%changelog
* Mon Jan 29 2023 Gremlin from Kremlin <gremlin@altlinux.org> 20170517ba1a8306-alt2
- build without libnetlink
- set license to explicit GPLv3+

* Wed Oct 04 2017 Gremlin from Kremlin <gremlin@altlinux.org> 20170517ba1a8306-alt1
- first build

