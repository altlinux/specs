%define module POE-Component-Jabber

Name: perl-%module
Version: 3.00
Release: alt1

Summary: POE-Component-Jabber - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org


BuildArch: noarch
Source: %module-%version.tar.gz

# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: perl-Authen-SASL perl-Digest-SHA1 perl-Module-Build perl-Net-SSLeay perl-POE-Filter-XML
BuildRequires: perl-POE-Component-SSLify perl-POE-Component-PubSub

%description
PCJ is a communications component that fits within the POE framework and
provides the raw low level footwork of initiating a connection,
negotiatating various protocol layers, and authentication necessary for
the end developer to focus more on the business end of implementing a
client or service.

POE::Component::Jabber - A POE Component for communicating over Jabber

%prep
%setup -q -n %module-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/POE/*

%changelog
* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 3.00-alt1
- 3.00
- drop %%perl_vendor_man3dir

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.03-alt1
- initial build for ALT Linux Sisyphus

