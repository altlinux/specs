%define src_name include

Name: openwince-%src_name
Version: 0.4.2
Release: alt1

Group: Development/C
Summary: Openwince includes
License: BSD-style license
URL: http://openwince.sourceforge.net/include/

Source: %src_name-%version.tar.bz2

Buildarch: noarch

%description
Openwince includes
include package is a collection of the useful independent include files for
C/Assembler developers.

%prep
%setup -n %src_name-%version -q

%build
%configure
%make

%install
%makeinstall

%files
%doc README COPYING AUTHORS NEWS ChangeLog
%dir %_includedir/*
%_includedir/*

%changelog
* Sat Aug 02 2008 Grigory Milev <week@altlinux.ru> 0.4.2-alt1
- Initial build for ALT Linux
