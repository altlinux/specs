%define module Test-Base

Name: perl-%module
Version: 0.60
Release: alt1

Summary: Data driven testing framework for perl
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 10 2011
BuildRequires: perl-Module-Install perl-Spiffy perl-Test-Deep perl-Test-Tester perl-Text-Diff

%description
Perl gives you a standard way to run tests with Test::Harness, and basic
testing primitives with Test::More. After that you are pretty much on your own
to develop a testing framework and philosophy. Test::More encourages you to
make your own framework by subclassing Test::Builder, but that is not trivial.
Test::Base gives you a way to write your own test framework base class that is
trivial.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/
%perl_vendor_privlib/Module/Install/*

%changelog
* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 0.60-alt1
- 0.60

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Jan 25 2010 Victor Forsyuk <force@altlinux.org> 0.59-alt1
- 0.59

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.55-alt1
- 0.55

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.54-alt1
- Initial build.
