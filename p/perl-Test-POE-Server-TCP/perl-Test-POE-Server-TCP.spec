%define module Test-POE-Server-TCP

Name: perl-%module
Version: 1.16
Release: alt1

Summary: A POE Component providing TCP server services for test cases

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Test-POE-Server-TCP-1.16.tar.gz

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: perl-POE perl-Test-Pod perl-Test-Pod-Coverage

%description
Test::POE::Server::TCP is a POE component that provides a TCP server framework for inclusion in client component test cases, instead of having to roll your own.

Once registered with the component, a session will receive events related to client connects, disconnects, input and flushed output. Each of these events will refer to a unique client ID which may be used in communication with the component when sending data to the client or disconnecting a client connection.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/POE/Server/*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 1.14-alt1
- 1.14
- drop %%perl_vendor_man3dir

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 1.08-alt1
- 1.08

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- initial build for ALT Linux Sisyphus

