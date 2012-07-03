%define dist RPM-Payload
Name: perl-%dist
Version: 0.10
Release: alt1

Summary: Simple in-memory access to RPM cpio archive
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

Requires: /usr/bin/rpm2cpio

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 03 2009
BuildRequires: perl-devel

%description
RPM::Payload provides in-memory access to RPM cpio archive.
Cpio headers and file data can be read in a simple loop.
RPM::Payload uses rpm2cpio program which comes with RPM.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/RPM*

%changelog
* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- implemented $entry->readlink method
- released under GPLv2+

* Mon Feb 16 2009 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- use rpm2cpio, to handle LZMA payloads

* Sat Mar 18 2006 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial revision
