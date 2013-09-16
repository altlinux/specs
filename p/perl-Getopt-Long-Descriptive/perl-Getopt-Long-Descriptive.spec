%define _unpackaged_files_terminate_build 1
%define dist Getopt-Long-Descriptive
Name: perl-%dist
Version: 0.094
Release: alt1

Summary: Getopt::Long, but simpler and more powerful
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Getopt-Long-Descriptive-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Params-Validate perl-Sub-Exporter perl-devel perl(Capture/Tiny.pm)

%description
Getopt::Long::Descriptive is yet another Getopt library.  It's built atop
Getopt::Long, and gets a lot of its features, but tries to avoid making you
think about its huge array of options.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Getopt

%changelog
* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.094-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.093-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.092-alt1
- automated CPAN update

* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.091-alt1
- 0.090 -> 0.091

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.090-alt1
- 0.087 -> 0.090

* Wed Dec 29 2010 Alexey Tourbin <at@altlinux.ru> 0.087-alt1
- 0.085 -> 0.087

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 0.085-alt1
- initial revision, for perl-DBIx-Class
