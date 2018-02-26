%define dist HTTP-Tiny
Name: perl-%dist
Version: 0.013
Release: alt1

Summary: A small, simple, correct HTTP/1.1 client
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/HTTP-Tiny-0.013.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-devel

%description
This is a very simple HTTP/1.1 client, designed primarily for doing
simple GET requests without the overhead of a large framework like
LWP::UserAgent.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.012-alt1
- initial revision
