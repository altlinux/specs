%define dist Parse-CPAN-Meta
Name: perl-%dist
Version: 1.4401
Release: alt2

Summary: Base class for image manipulation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# loaded with _can_load
Requires: perl-JSON-PP

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-CPAN-Meta-YAML perl-JSON perl-JSON-PP perl-devel

%description
Image::Base is a base class for loading, manipulating and saving images.
This class should not be used directly. Known inheritors are Image::Xbm
and Image::Xpm.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Parse

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.4401-alt2
- added dependency on perl-JSON-PP

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.4401-alt1
- 1.40 -> 1.4401

* Fri Mar 12 2010 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- initial revision (required for recent Module-Install)
