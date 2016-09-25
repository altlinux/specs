Name: perl-IO-Socket-IP
Version: 0.38
Release: alt1

Summary: IO::Socket::IP - A drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
Group: Development/Perl
License: Perl

Url: %CPAN IO-Socket-IP
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, as a drop-in replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way. For a
list of known differences, see the IO::Socket::INET INCOMPATIBILITES
section.

It uses the getaddrinfo(3) function to convert hostnames and service
names or port numbers into sets of possible addresses to connect to or
listen on. This allows it to work for IPv6 where the system supports it,
while still falling back to IPv4-only on systems which don't.

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IO/Socket/IP*
%doc LICENSE Changes README 

%changelog
* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Tue Jul 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.22-alt1
- 0.22
- fixed tests 15io-socket.t, 16v6only.t

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- initial build
