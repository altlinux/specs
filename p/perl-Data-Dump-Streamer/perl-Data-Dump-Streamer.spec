%define dist Data-Dump-Streamer
Name: perl-%dist
Version: 2.32
Release: alt2

Summary: Accurately serialize a data structure as Perl code
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Algorithm-Diff perl-B-Utils perl-IO-Compress perl-Module-Build perl-PadWalker perl-Text-Balanced

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects.  The contents of each
variable is output using the least number of Perl statements as convenient,
usually only one.  Self-referential structures, closures, and objects are
output correctly.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 2.32-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 2.08.40-alt1
- initial build for ALT Linux Sisyphus

