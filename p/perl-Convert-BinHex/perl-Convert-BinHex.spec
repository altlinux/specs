BuildRequires: perl-podlators
%define dist Convert-BinHex
Name: perl-%dist
Version: 1.123
Release: alt1

Summary: Extract data from Macintosh BinHex files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/ST/STEPHEN/Convert-BinHex-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel perl(autodie.pm) perl(Test/Most.pm)

%description
BinHex is a format used by Macintosh for transporting Mac files safely
through electronic mail, as short-lined, 7-bit, semi-compressed data
streams.  This module provides a means of converting those data streams
back into into binary data.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Convert

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.123-alt1
- automated CPAN update

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.119-alt2
- rebuilt

* Fri May 13 2005 Alexey Tourbin <at@altlinux.ru> 1.119-alt1
- initial revision (required for MIME-tools-5.417)
