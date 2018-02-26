%define dist Encode-Locale
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: Determine the locale encoding
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012 (-bi)
BuildRequires: perl-Encode perl-devel

%description
The purpose of this Perl module is try determine what encodings
should be used when interfacing to various external interfaces.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Encode

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.02 -> 1.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt2
- rebuilt as plain src.rpm

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.01 -> 1.02

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision
