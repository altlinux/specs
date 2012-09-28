Name: perl-Protocol-WebSocket
Version: 0.11
Release: alt1

Summary: Protocol::WebSocket - WebSocket protocol
Group: Development/Perl
License: Perl

Url: %CPAN Protocol-WebSocket
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Module-Install perl-Digest-SHA1

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Protocol/WebSocket*
%exclude %perl_vendor_privlib/Protocol/README.pod
%doc Changes README.pod

%changelog
* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
