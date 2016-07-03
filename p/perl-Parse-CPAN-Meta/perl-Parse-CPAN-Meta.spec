%define _unpackaged_files_terminate_build 1
%define dist Parse-CPAN-Meta
Name: perl-%dist
Version: 1.4422
Release: alt1

Summary: Base class for image manipulation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/Parse-CPAN-Meta-%{version}.tar.gz

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
* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.4422-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.4417-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.4414-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.4409-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.4407-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.4405-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.4404-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.4401-alt2
- added dependency on perl-JSON-PP

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.4401-alt1
- 1.40 -> 1.4401

* Fri Mar 12 2010 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- initial revision (required for recent Module-Install)
