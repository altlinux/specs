%define module Digest-MD4

Name: perl-%module
Version: 1.5
Release: alt1.2

Summary: Perl interface to the MD4 Algorithm
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD4-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libdb4-devel libgdbm-devel perl-devel

%description
The Digest::MD4 module allows you to use the RSA Data Security Inc. MD4
Message Digest algorithm from within Perl programs. The algorithm takes
as input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.5-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt1.1
- rebuilt with perl 5.12

* Wed Oct 10 2007 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- Initial build.
