%define dist Convert-BinHex
Name: perl-%dist
Version: 1.119 
Release: alt2

Summary: Extract data from Macintosh BinHex files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Convert-BinHex-1.119-alt-Checker-ISA.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
BinHex is a format used by Macintosh for transporting Mac files safely
through electronic mail, as short-lined, 7-bit, semi-compressed data
streams.  This module provides a means of converting those data streams
back into into binary data.

%prep
%setup -q -n %dist-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Convert

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.119-alt2
- rebuilt

* Fri May 13 2005 Alexey Tourbin <at@altlinux.ru> 1.119-alt1
- initial revision (required for MIME-tools-5.417)
