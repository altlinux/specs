%define dist Devel-Cover
Name: perl-%dist
Version: 0.79
Release: alt1

Summary: Code coverage metrics for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Oct 12 2011 (-bi)
BuildRequires: perl-B-Debug perl-JSON-PP perl-PPI-HTML perl-Parallel-Iterator perl-Perl-Tidy perl-Pod-Coverage perl-Template perl-Test-Differences perl-Test-Warn rpm-build-ruby

%description
This module provides code coverage metrics for Perl. Code coverage
metrics describe how thoroughly tests exercise code. By using
Devel::Cover you can discover areas of code not exercised by your tests
and determine which tests to create to increase coverage. Code coverage
can be considered as an indirect measure of quality.

%prep
%setup -q -n %dist-%version

# fix expected output for test suite
sed -i 's@!/bin/perl@!/usr/bin/perl@' test_output/cover/inc_sub.*

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

# Undefined subroutine &Devel::Cover::set_first_init_and_end called
echo 'sub Devel::Cover::set_first_init_and_end{}1' >%buildroot/hack.pm
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot -mhack'

%files
%_bindir/cover
%_bindir/cpancover
%_bindir/gcov2perl
%_man1dir/*
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel
%exclude /hack.pm

%changelog
* Wed Oct 12 2011 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- 0.72 -> 0.79
- built for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.67-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- automated CPAN update

* Tue Jan 19 2010 Vitaly Lipatov <lav@altlinux.ru> 0.65-alt1
- initial build for ALT Linux Sisyphus
