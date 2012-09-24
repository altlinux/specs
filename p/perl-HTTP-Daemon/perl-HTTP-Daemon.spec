%define dist HTTP-Daemon
Name: perl-%dist
Version: 6.01
Release: alt1

Summary: a simple http server class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GA/GAAS/HTTP-Daemon-%{version}.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-HTTP-Message perl-devel

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::INET, so you can perform socket operations directly on it
too.

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
* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 6.01-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
