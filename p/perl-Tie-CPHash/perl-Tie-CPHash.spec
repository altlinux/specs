%define module Tie-CPHash
%define intmodule Tie-CPHash
%define m_name Tie::CPHash

Name: perl-%module
Version: 1.05
Release: alt1

Summary: Tie::CPHash - Case preserving but case insensitive hash table
License: GPL or Artistic
Group: Development/Perl
BuildArch: noarch
Url: %CPAN %module
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/C/CJ/CJM/%{intmodule}-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 06 2003
BuildRequires: perl-devel perl-Module-Build perl-Test-Pod >= 1.14 perl-Test-Pod-Coverage >= 1.04

%description
The Tie::CPHash module provides a hash table that is case preserving
but case insensitive. This means that

    $cphash{KEY}    $cphash{key}
    $cphash{Key}    $cphash{keY}

all refer to the same entry. Also, the hash remembers which form of
the key was last used to store the entry. The keys and each functions
will return the key that was used to set the value.

%prep
%setup -q -n %intmodule-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Tie/CPHash.pm

%changelog
* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 1.05-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 1.04-alt1
- New version

* Sat Jul 21 2007 Sergei Epiphanov <serpiph@altlinux.ru> 1.03-alt1
- New version
- Fix build dependencies

* Thu Dec 21 2006 Sergei Epiphanov <serpiph@altlinux.ru> 1.02-alt1
- Built for Sisyphus
