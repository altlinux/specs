%define module POE-Test-Loops
%define m_distro POE-Test-Loops
%define m_name POE::Test::Loops
%define m_author_id CPAN
%define _enable_test 1

%add_findreq_skiplist */POE/Test/Loops/wheel_curses.pm 

Name: perl-POE-Test-Loops
Version: 1.312
Release: alt1

Summary: POE::Loop test suite

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/POE-Test-Loops/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/R/RC/RCAPUTO/%m_distro-%version.tar.gz

# Automatically added by buildreq on Thu Oct 15 2009 (-bi)
BuildRequires: perl-POE perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
POE::Test::Loops contains one function, generate(), which will
generate all the loop tests for one or more POE::Loop subclasses.

The "SYNOPSIS" example is a version of poe-gen-tests, which is a
stand-alone utility to generate the actual tests.  poe-gen-tests
also documents the POE::Test::Loops system in more detail.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/*
%_man1dir/*
%_bindir/*
%doc CHANGES README

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.312-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.035-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.035-alt1
- automated CPAN update

* Thu Oct 15 2009 Michael Bochkaryov <misha@altlinux.ru> 1.030-alt1
- initial build for ALT Linux Sisyphus

