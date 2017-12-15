%define _unpackaged_files_terminate_build 1
%define dist Compress-Snappy
Name: perl-%dist
Version: 0.24
Release: alt1.1.1.1

Summary: Perl interface to Google's Snappy (de)compressor
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GR/GRAY/Compress-Snappy-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel perl-parent perl(Devel/CheckLib.pm)

%description
The `Compress::Snappy' module provides an interface to Google's Snappy
(de)compressor.

Snappy does not aim for maximum compression, or compatibility with any other
compression library; instead, it aims for very high speeds and reasonable
compression. For instance, compared to the fastest mode of zlib, Snappy is
an order of magnitude faster for most inputs, but the resulting compressed
files are anywhere from 20%% to 100%% bigger.

%prep
%setup -n %dist-%version

# do not override default CCFLAGS
sed -i- '/CCFLAGS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1.1
- rebuild with new perl 5.22.0

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1.1
- rebuild with new perl 5.20.1

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1
- 0.12 -> 0.18
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt for perl-5.14

* Thu Jul 28 2011 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1
- initial build for ALT Linux Sisyphus
