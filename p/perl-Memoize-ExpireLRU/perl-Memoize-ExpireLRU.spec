%define _unpackaged_files_terminate_build 1
%define dist Memoize-ExpireLRU
Name: perl-%dist
Version: 0.56
Release: alt1

Summary: Expiry plug-in for Memoize that adds LRU cache expiration

License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Memoize-ExpireLRU-%{version}.tar.gz

BuildArch: noarch

# was packaged into perl-Memoize
Requires: perl-Memoize >= 1.01-alt3

# Automatically added by buildreq on Tue Apr 27 2010
BuildRequires: perl-Memoize perl-devel

%description
For the theory of Memoization, please see the Memoize module
documentation. This module implements an expiry policy for Memoize
that follows LRU semantics, that is, the last n results, where n is
specified as the argument to the C<CACHESIZE> parameter, will be
cached.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Memoize*
%perl_vendor_privlib/auto/Memoize*

%changelog
* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.55-alt1
- decoupled from perl-Memoize
