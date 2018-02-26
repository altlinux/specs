
%define module POE-Component-Client-Ident

Name: perl-POE-Component-Client-Ident
Version: 1.16
Release: alt2

Summary: A component that provides non-blocking ident lookups to your sessions

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Alexey Shabalin <shaba@altlinux.ru>

BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: perl-Test-POE-Server-TCP perl-Test-Pod perl-Test-Pod-Coverage

%description
POE::Component::Client::Ident is a POE component that provides non-blocking Ident lookup services to other components and sessions. The Ident protocol is described in RFC 1413 http://www.faqs.org/rfcs/rfc1413.html.

The component takes requests in the form of events, spawns POE::Component::Client::Ident::Agent sessions to perform the Ident queries and returns the appropriate responses to the requesting session.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/Component/Client/*
%perl_vendor_privlib/POE/Filter/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.16-alt2
- drop %%perl_vendor_man3dir

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.16-alt1
- 1.16

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 1.14-alt1
- initial build for ALT Linux Sisyphus

