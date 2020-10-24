%define _unpackaged_files_terminate_build 1
%define dist Tie-RefHash
Name: perl-%dist
Version: 1.40
Release: alt1

Summary: Use references as hash keys
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 20 2010
BuildRequires: perl-Storable perl-devel perl-threads

%description
This module provides the ability to use references as hash keys if you
first tie the hash variable to this module.  Normally, only the keys
of the tied hash itself are preserved as references; to use references
as keys in hashes-of-hashes, use Tie::RefHash::Nestable, included as
part of Tie::RefHash.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING README
%perl_vendor_privlib/Tie*

%changelog
* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- initial revision
