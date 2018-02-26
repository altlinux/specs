%define dist Bloom-Filter
Name: perl-%dist
Version: 1.0
Release: alt1

Summary: Sample Perl Bloom filter implementation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Digest-SHA1 perl-devel

%description
A Bloom filter is a probabilistic algorithm for doing existence tests in
less memory than a full list of keys would require.  The tradeoff to
using Bloom filters is a certain configurable risk of false positives.
This module implements a simple Bloom filter with configurable capacity
and false positive rate. Bloom filters were first described in a 1970
paper by Burton Bloom, see
http://portal.acm.org/citation.cfm?id=362692&dl=ACM&coll=portal

See also: Using Bloom Filters,
http://www.perl.com/pub/a/2004/04/08/bloom_filters.html

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Bloom*

%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt1
- 0.03 -> 1.0

* Sun Sep 18 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision
