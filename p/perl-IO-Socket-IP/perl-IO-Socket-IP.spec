Name: perl-IO-Socket-IP
Version: 0.17
Release: alt1

Summary: IO::Socket::IP - A drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
Group: Development/Perl
License: Perl

Url: %CPAN IO-Socket-IP
Source: %name-%version.tar

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
# cannot listen on PF_INET6 on buildhost
mv t/16v6only.t t/16v6only.t.orig
# no internet connection on buildhost
mv t/21nonblocking-connect-internet.t t/21nonblocking-connect-internet.t.orig

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IO/Socket/IP*
%doc LICENSE Changes README 

%changelog
* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- initial build
