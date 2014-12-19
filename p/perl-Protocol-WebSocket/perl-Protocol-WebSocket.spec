BuildRequires: perl(Module/Build.pm)
Name: perl-Protocol-WebSocket
Version: 0.18
Release: alt1

Summary: Protocol::WebSocket - WebSocket protocol
Group: Development/Perl
License: Perl

Url: %CPAN Protocol-WebSocket
Source: http://www.cpan.org/authors/id/V/VT/VTI/Protocol-WebSocket-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-Module-Install perl-Digest-SHA1 perl(Digest/SHA.pm)

%description
%summary

%prep
%setup -q -n Protocol-WebSocket-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Protocol/WebSocket*
%doc Changes

%changelog
* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
